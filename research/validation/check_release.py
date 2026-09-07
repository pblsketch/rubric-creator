"""Check source links, published score ranges, and the distributable skill ZIP."""

import argparse
import hashlib
import itertools
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "rubric-creator"
ARCHIVE = ROOT / "dist/rubric-creator.zip"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_documents():
    files = [ROOT / "README.md", ROOT / "research/skill-review-2026-09-07.md"]
    files += sorted(path for path in SKILL.rglob("*.md")
                    if not any(part.startswith(".") for part in path.relative_to(SKILL).parts))
    files += sorted((ROOT / "research/validation").glob("*.md"))
    links = 0
    for path in files:
        content = path.read_text(encoding="utf-8")
        require("\ufffd" not in content, f"Invalid text: {path}")
        require(content.count("```") % 2 == 0, f"Unclosed fence: {path}")
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
            if target.startswith(("http://", "https://", "#")):
                continue
            target = target.split("#", 1)[0]
            require((path.parent / target).is_file(), f"Missing link: {path}: {target}")
            links += 1
        if path.is_relative_to(SKILL):
            for target in re.findall(r"`((?:references/)?[\w-]+\.md)`", content):
                require((path.parent / target).is_file(), f"Missing reference: {path}: {target}")
                links += 1
    print(f"DOCUMENTS_PASS files={len(files)} local_references={links}")


def check_score_sets():
    path = ROOT / "research/validation/case-1-korean.md"
    content = path.read_text(encoding="utf-8")
    rows = [line for line in content.splitlines() if re.match(r"\| \*\*[123]\. ", line)]
    require(len(rows) == 3, "Expected three Korean rubric criteria")
    scales = []
    for row in rows:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        values = [re.match(r"(\d+) · ", cell) for cell in cells[1:]]
        require(len(values) == 4 and all(values), "Missing numeric performance level")
        scale = [int(value[1]) for value in values]
        require(scale == sorted(set(scale), reverse=True), "Levels must have ordered scores")
        scales.append(scale)
    combinations = list(itertools.product(*scales))
    totals = sorted({sum(levels) for levels in combinations})
    original = [13, 15, 17, 19, 20]
    require(totals == list(range(11, 21)), f"Unexpected proposed scores: {totals}")
    require(str(totals) in content and str(original) in content, "Published ranges mismatch")
    require(totals != original, "This example is a changed structure, not a preserved range")
    print(f"SCORE_SETS_PASS combinations={len(combinations)} original={original} proposed={totals}")


def manifest():
    result = {}
    for path in sorted(SKILL.rglob("*")):
        if any(part.startswith(".") for part in path.relative_to(SKILL).parts):
            continue
        if not path.is_file():
            continue
        require(not path.is_symlink(), f"Unexpected symlink: {path}")
        require(path.suffix in {".md", ".yaml"}, f"Unexpected package file: {path}")
        result[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    result["rubric-creator/LICENSE"] = (ROOT / "LICENSE").read_bytes()
    return result


def check_archive(expected, build):
    if build:
        temporary = ARCHIVE.with_suffix(".zip.tmp")
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in sorted(expected.items()):
                info = zipfile.ZipInfo(name, date_time=(2026, 9, 7, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        temporary.replace(ARCHIVE)
    with zipfile.ZipFile(ARCHIVE) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)), "Duplicate archive entries")
        require(set(names) == set(expected), "Archive manifest differs from source")
        require(archive.testzip() is None, "Archive CRC failure")
        for name, data in expected.items():
            require(archive.read(name) == data, f"Archive content mismatch: {name}")
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    print(f"ARCHIVE_PASS files={len(expected)} sha256={digest}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="Rebuild ZIP before comparing")
    options = parser.parse_args()
    check_documents()
    check_score_sets()
    check_archive(manifest(), options.build)


if __name__ == "__main__":
    main()
