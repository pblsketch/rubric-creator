# Rubric Creator Skill — 설치 안내

Claude(웹·데스크톱), Claude Code, Codex에서 같은 폴더를 쓴다. 핵심은 `SKILL.md`이고, `references/`는 필요할 때만 읽히는 참고 자료다. `README.md`는 설치용이며 스킬 동작에 필요하지 않다.

```
rubric-creator/
  SKILL.md                     진입점 (이름·설명·절차)
  references/
    rubric-principles.md       요소·수준·배점 규칙, 점검표 11문항
    revise-rubric.md           기존 표 개선
    curriculum.md              성취기준 조회·검증
    dok.md                     DOK 활용 규칙
    subject-guidance.md        교과·학교급 조정
    learning-use.md            학생 활용, 교사 간 기준 맞추기
    sources.md                 근거 출처·재사용 경계
  agents/openai.yaml           Codex UI 메타데이터(선택)
```

## Claude Code

개인용:
```
~/.claude/skills/rubric-creator/
```
프로젝트용:
```
<프로젝트>/.claude/skills/rubric-creator/
```
폴더를 통째로 복사한다. 자연어("루브릭 만들어 줘")로 발동하거나 `/rubric-creator`로 호출한다.

## Codex

```
~/.codex/skills/rubric-creator/
```
폴더를 통째로 복사한다. `$rubric-creator`로 호출하거나 자연어로 발동한다. `agents/openai.yaml`은 UI 표시용이며 없어도 동작한다.

## Claude 웹·데스크톱

`rubric-creator` 폴더를 ZIP으로 압축해(폴더 자체가 최상위가 되도록) 설정 → 기능(Capabilities) → 스킬에서 업로드한다. 성취기준 MCP는 별도로 연결해야 하며, 연결되지 않으면 스킬이 교사가 제공한 성취기준 원문으로 진행한다.

## 성취기준 MCP (선택)

세 서버 중 필요한 것을 각 환경의 MCP 설정에 등록한다. 설치 방법은 각 저장소 README를 따른다.

- 초등: https://github.com/taehyeonglim/korean-elementary-learning-map-mcp
- 중·고 보통교과: https://github.com/raphysicst-create/korean-secondary-learning-map-mcp
- 특성화고 전문교과: https://github.com/raphysicst-create/korean-vocational-learning-map-mcp

## 범위

이 스킬은 루브릭을 **만들고 고치는** 도구다. 학생이 제출한 과제물을 채점하지 않는다.
