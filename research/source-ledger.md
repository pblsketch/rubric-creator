# Rubric Creator Skill 출처 대장

작성일 2026-09-07. 조사에 사용한 모든 자료의 서지, 로컬 사본 위치, 해시, 확인 범위, 재사용 경계를 기록한다. 로컬 사본은 모두 `research/private/` 아래에 있으며 **연구용**이다. 배포 스킬에는 넣지 않는다.

상태 표기: `읽음(전체)` 본문 전체 확인 / `읽음(부분)` 표시한 범위만 확인 / `서지만` 초록·메타데이터만 확인, 본문 미확보.

---

## A. 사용자 제공 도서

| ID | 서지 | 로컬 사본 | 확인 | 재사용 경계 |
|---|---|---|---|---|
| A-1 | Susan M. Brookhart, *How to Create and Use Rubrics for Formative Assessment and Grading*, ASCD, 2013. 한국어판 『루브릭 어떻게 만들고 사용할까?』, 장은경 외 옮김, 우리학교, 2022. | `루브릭 어떻게 만들고 사용할까_OCR_문서 평면화.pdf` (310,901,655 B, 262쪽, SHA-256 `86e939dd…3e62b5`; 전체 해시는 `private/book-manifest.json`) | 읽음(전체). OCR 텍스트 183,254자, 빈 페이지 6쪽(PDF 17, 161, 163, 231, 247, 262). 표는 `private/book-renders/` 화면 렌더로 재확인 | **원문·표·예시 루브릭·사례 문장은 스킬에 복제하지 않는다.** 이론적 원칙만 독자적 표현으로 재구성한다. OCR 전문(`private/book-text.txt`, `book-pages.json`)과 장별 발췌(`private/book-notes/`)는 연구용으로만 보관하고 배포·공유하지 않는다. |

인용 형식: "인쇄 N쪽". 로컬 PDF 쪽수 = 인쇄 쪽수 + 1.

## B. DOK(Depth of Knowledge) 자료

로컬 사본은 `private/sources/`, 해시 전문은 `private/sources/manifest.json`. 확인일 2026-09-07.

| ID | 서지 | URL | 로컬 파일 (쪽, SHA-256 앞부분) | 확인 | 신뢰·한계 |
|---|---|---|---|---|---|
| B-1 | WebbAlign / Norman L. Webb (2025). *What is Depth of Knowledge (DOK)?* (DOK Primer) | https://www.webbalign.org/dok-primer | `dok-primer.pdf` (2쪽, `e25b7838`) | 읽음(전체) | 개발자 공식 정의. p.2에 DOK는 채점 루브릭·개인 사고 측정·교수 위계가 아님을 명시. 효과 연구 아님 |
| B-2 | Webb, N., Christopherson, S., & Morelan, B. (2023-03-27). *An Inside Look at Webb's Depth of Knowledge.* Edutopia | https://www.edutopia.org/article/how-use-norman-webb-depth-of-knowledge/ | 웹 열람, 로컬 사본 없음 | 읽음(전체) | 개발자 공동 집필 설명문. 동사 휠 부정확, DOK4 조건, 난도–복잡성 구분. 실험연구 아님 |
| B-3 | Webb, N. L. (2007). Issues Related to Judging the Alignment of Curriculum Standards and Assessments. *Applied Measurement in Education*, 20(1), 7–25. doi:10.1080/08957340709336728 | https://www.tandfonline.com/doi/abs/10.1080/08957340709336728 | 없음 (유료, 직접 접근 403) | 서지만 | 학술 원전. 초록으로 정렬 판단의 다기준·주관성 확인. **본문 미확인**이므로 세부 수치·임계값을 인용하지 않는다 |
| B-4 | Hess, K. K., Jones, B. S., Carlock, D., & Walkup, J. R. (2009). *Cognitive Rigor: Blending the Strengths of Bloom's Taxonomy and Webb's Depth of Knowledge to Enhance Classroom-level Processes.* ERIC ED517804 | https://files.eric.ed.gov/fulltext/ED517804.pdf | `hess-2009-cognitive-rigor.pdf` (8쪽, `2bb9707f`) | 읽음(전체) | 기술적 연구보고서(두 주 학교의 과제·학생 작업 분류). 인과 효과 검증 아님. 매트릭스 도표는 복제하지 않고 개념만 참조 |
| B-5 | Christopherson, S. C. (2023). *Differentiating Difficulty from Complexity to Promote Intended Uses of Learning Progressions.* NCME Annual Meeting paper | https://www.webbalign.org/ncme-2023-differentiating-difficulty-from-complexity | `christopherson-2023-complexity.pdf` (18쪽, `62293ae6`) | 읽음(부분: 표지·초록, pp.6–11) | 개발자 기관 연구자 발표문. 문항 제공기관 비공개, 선택 표본, DOK3 소수·DOK4 없음. 난도≠DOK 지지; 학습 향상 효과는 다루지 않음 |
| B-6 | Webb, N., & Christopherson, S. (2019 rev., ©2020). *DOK: Categories of Cognitive Engagement for Science* | https://www.webbalign.org/dok-definitions-for-science | `dok-science.pdf` (8쪽, `ea58c8f7`) | 읽음(전체) | 과학·NGSS 맥락 공식 정의. NGSS 특유 규정은 한국 교육과정에 직접 적용하지 않음 |
| B-7 | Webb, N., & Christopherson, S. *Mathematics DOK Definitions* (2014 rev. 기반, ©2025) | https://www.webbalign.org/dok-definitions-for-math | `dok-math.pdf` (4쪽, `a6986efb`) | 읽음(전체) | 교과 공식 정의 |
| B-8 | Webb, N., & Christopherson, S. *Reading DOK Definitions* (2014 rev. 기반, ©2025) | https://www.webbalign.org/dok-definitions-for-reading | `dok-reading.pdf` (4쪽, `9b5fbb91`) | 읽음(전체) | 교과 공식 정의. 한국어 독서 성취기준에는 재해석 필요 |
| B-9 | Webb, N., & Christopherson, S. *Social Studies DOK Definitions* (2014 rev., ©2015) | https://www.webbalign.org/dok-definitions-for-social-studies | `dok-social-studies.pdf` (2쪽, `1351b00b`) | 읽음(전체) | 교과 공식 정의 |

미확보: 예술·체육·직업 실무 영역에 대한 DOK 공식 정의 또는 타당화 연구. 이 영역에서는 DOK를 제한적으로만 사용한다.

## C. 2022 개정 교육과정 자료

### C-1. 교육과정 학습맵 MCP 저장소 (GitHub 고정 커밋 스냅샷)

로컬 사본은 `private/curriculum/{elementary,secondary,vocational}/`, 파일별 URL·바이트·SHA-256은 `private/curriculum/snapshot-manifest.json` (67개 파일, 71,072,447 B, 다운로드 실패 0). 계수 결과는 `private/curriculum/coverage-check.json`. 확인일 2026-09-07. **설치·MCP 실행은 하지 않았다.**

| ID | 저장소 | 커밋 | 패키지 버전 | 주요 파일 (SHA-256 앞부분) | 권리 고지 |
|---|---|---|---|---|---|
| C-1a | taehyeonglim/korean-elementary-learning-map-mcp | `e5c2c6b40081ce5c27ddd125a77e3a00574976a1` | 0.5.2 | `data/kr/curriculum-standards.json` (1,913,076 B, `aaaebb93`), `data/kr/standard-texts.json` (155,956 B, `8a8535a0`), `data/kr/manifest.json`, `pipeline/sources.json`, `src/server.mjs`, `src/data-store.mjs`, `README.md`, `NOTICE.md`, `LICENSE` | 코드 MIT. 성취기준 원문은 공공저작물(저작권법 제24조의2) 근거 제시 |
| C-1b | raphysicst-create/korean-secondary-learning-map-mcp | `964bfaef6e02781359288a6c1f55240bfb9c439d` | 0.3.0 | `data/kr/curriculum-standards.json` (3,483,851 B, `8a4e7157`), `data/kr/standard-texts.json` (1,089,581 B, `f185421c`), `data/kr/manifest.json`, `pipeline/sources.json`, `src/server.mjs`, `src/data-store.mjs`, `README.md`, `NOTICE.md`, `RIGHTS.md`, `LICENSE` | 코드 MIT. 고시 원문은 보호대상 제외(제7조제2호) 근거 제시. **2026-1호 별책3·4 일부개정 미반영을 자체 고지** |
| C-1c | raphysicst-create/korean-vocational-learning-map-mcp | `8b82b518a9d005b0ce0cdbf61fd36c219eb4c756` | 0.4.0 | `data/kr/core/{curricula,dependencies,major-fields,manifest,routing-index}.json` (routing-index 5,957,874 B, `c3025dd8`), `data/kr/fields/<18분야>/{curriculum-standards,standard-texts}.json` (36개 파일, 58,027,264 B), `pipeline/sources.json`, `src/server.mjs`, `src/data-store.mjs`, `README.md`, `NOTICE.md`, `RIGHTS.md`, `LICENSE` | 코드 MIT. 고시 원문 보호대상 제외 근거 제시. 요약·파생 항목 비보증 고지 |

직업 18분야: agriculture-livestock, beauty, business-finance, chemical-industry, construction-civil, convergence-ip, culture-arts-design-broadcast, electrical-electronics, environment-safety-fire, fisheries-shipping, food-cooking, health-welfare, information-communication, machinery, materials, specialized-common, textile-clothing, tourism-leisure.

재사용 경계: 세 저장소의 권리 판단은 각 저장소의 것이다. 파생 그래프·요약을 재사용하면 원저작자 고지를 보존한다. 스킬에는 조회 절차와 최소 출처 목록만 넣고 전체 데이터는 넣지 않는다(`DESIGN.md` 10절).

### C-2. 공식 고시·교육과정 문서 (NCIC, 교육부)

| ID | 자료 | URL | 로컬 파일 | 확인 | 용도 |
|---|---|---|---|---|---|
| C-2a | 교육부 고시 제2026-1호 [별책 15] 바른 생활·슬기로운 생활·즐거운 생활 교육과정 | https://ncic.re.kr/inv/org/download.do?year=2026&seq=10004214&orgType=ogi4 | `private/sources/ncic-2026-annex15.pdf` (90쪽, 1,449,216 B, `39954a4b`) | 읽음(부분: PDF 45쪽/인쇄 39쪽) | `[2건01-01]` 원문 오염 대조. 렌더 `private/sources/renders/health.png` |
| C-2b | 교육부 고시 제2022-33호 [별책 5] 국어과 교육과정 | https://ncic.re.kr/inv/org/download.do?year=2022&seq=10003553&orgType=ogi4 | `private/sources/ncic-2022-korean.pdf` (222쪽, 2,078,590 B, `5c30ae42`) | 읽음(부분: PDF 19쪽, 48쪽) | `[2국01-01]`, `[9국01-01]` 표본 대조. 렌더 `private/sources/renders/korean.png` |
| C-2c | 교육부 고시 제2022-33호 [별책 8] 수학과 교육과정 | https://ncic.re.kr/inv/org/download.do?year=2022&seq=10003559&orgType=ogi4 | 없음 (하위 에이전트가 원격 확인, 해시는 저장소 기록과 일치) | 읽음(부분: PDF 178쪽/인쇄 172쪽) | `[12경수01-01]` 표본 대조 |
| C-2d | 교육부 고시 2024 정보·통신 전문교과 교육과정 별책 | https://ncic.re.kr/inv/org/download.do?year=2024&seq=10004114&orgType=ogi4 | 없음 (원격 확인) | 읽음(부분: PDF 166쪽) | `[네크 01-01-01]` 표본 대조 |
| C-2e | NCIC 공지: 2026-1호 고시 및 적용 시기 | https://ncic.re.kr/bbs/ncicnotice/view/1859.do | 웹 열람 | 읽음(전체) | 초1·2 적용 2028-03-01 확인 |
| C-2f | 교육부 보도자료: 2022 개정 교육과정 고시 및 학년별 시행 일정 | https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=141&boardSeq=93458&lev=0&search= | 웹 열람 | 읽음(전체) | 중3·고3 적용 2027-03-01 확인 |

## D. 루브릭·형성평가 공개 연구

| ID | 서지 | URL | 확인 | 용도 |
|---|---|---|---|---|
| D-1 | Brookhart, S. M. (2018). Appropriate Criteria: Key to Effective Rubrics. *Frontiers in Education*, 3:22 | https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2018.00022/full | 읽음(부분, 웹 열람; 전체 정독 여부는 원 세션 기록에서 확인되지 않음) | "좋은 표만으로 학습 효과 보장 불가", 적절한 평가요소 개념의 공개 근거(`DESIGN.md` 2절) |

도서(A-1) 안에서 인용된 2차 연구(Goldberg & Roswell 1999/2000; Andrade, Du & Wang 2008; Andrade, Du & Mycek 2010; Ross, Hogaboam-Gray & Rolheiser 2002; Ross & Starling 2008; Hafner & Hafner 2003; Sadler 1989; Chapman & Inman 2009; Moss & Brookhart 2009/2012; Nitko & Brookhart 2011)는 원문을 별도로 확보하지 않았다. 도서의 소개 범위에서만 언급하며, 스킬에서 이 연구들을 직접 인용하려면 원문 확인이 필요하다.

## E. 플랫폼 문서

| ID | 자료 | URL | 확인 | 용도 |
|---|---|---|---|---|
| E-1 | OpenAI Codex — Skills | https://developers.openai.com/codex/skills/ | 읽음(웹) | `SKILL.md` 구조, `agents/openai.yaml` 선택 메타데이터 |
| E-2 | Claude Code — Skills | https://code.claude.com/docs/en/skills | 읽음(웹) | `.claude/skills/` 위치, 참조 파일 분리 |
| E-3 | Claude Help Center — Use skills in Claude | https://support.claude.com/en/articles/12512180-use-skills-in-claude | 읽음(웹) | 웹·데스크톱 사용자 스킬 ZIP 등록 |

## G. 백워드 설계·GRASPS (2026-09-07 추가)

로컬 사본은 `private/grasps/`, 해시 전문은 `private/grasps/manifest.json`. 학습 기록은 [`grasps-study.md`](grasps-study.md).

| ID | 서지 | URL | 로컬 파일 (쪽, SHA-256 앞부분) | 확인 | 신뢰·한계 |
|---|---|---|---|---|---|
| G-1 | Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (2nd ed.). ASCD. | https://andymatuschak.org/files/papers/Wiggins,%20McTighe%20-%202005%20-%20Understanding%20by%20design.pdf (제3자 게시본) | `ubd-2005-expanded.pdf` (382쪽, `6b2d6059`) | 읽음(부분: 7장 146–171, 8장 172–200 전체) | 1차 원전. **제3자 게시 PDF를 연구용으로만 읽었고 재배포하지 않는다.** 원문·그림·예시 과제는 스킬에 복제하지 않음 |
| G-2 | McTighe, J., & Wiggins, G. (2010). *Developing Performance Tasks* — GRASPS Design Sheets, pp.12–16 | https://jaymctighe.com/downloads/GRASPS-Design-sheets.pdf | `mctighe-grasps-design-sheets.pdf` (5쪽, `71165b0f`) | 읽음(전체) | 저자 공식 사이트 공개 워크시트. 문장 틀·역할/청중/산출물 목록. 저자 저작권 표기 유지 |
| G-3 | North Vancouver School District 44 (2017). *Performance Assessment: GRASPS* (UbD PD Workbook 2004 각색) | https://nvsd44curriculumhub.ca/wp-content/uploads/2017/09/GRASPS-Instructions.pdf | `nvsd44-grasps-instructions.pdf` (3쪽, `ea5fbdd2`) | 읽음(전체) | 교육청 실무 안내. 2차 자료 |
| G-4 | Flores, R. V. (2023). *Challenges in the Preparation of Performance Tasks: Basis for a Proposed GRASPS-based Guide on Performance Tasks in Mathematics.* ERIC ED649916 | https://files.eric.ed.gov/fulltext/ED649916.pdf | `eric-ED649916-performance-task-challenges.pdf` (22쪽, `04a7e83f`) | 읽음(부분: 초록·방법·결과) | 필리핀 중등 수학교사 72명 설문. R·A·S·P·S가 "very challenging". 기술적 조사, 효과 연구 아님 |
| G-5 | Alvarez Llerena, C. L. (2024). Students' Perceptions of Applying the GRASPS Framework from the Backward Design Model in Learning English as a Foreign Language. *Language Teaching Research Quarterly*, 40, 129–146. ERIC EJ1425222 | https://files.eric.ed.gov/fulltext/EJ1425222.pdf | `eric-EJ1425222-grasps-perceptions.pdf` (18쪽, `8bacc1cd`) | 읽음(부분: 초록·서론) | 에콰도르 EFL 학생 인식 조사. 성취 효과 아님 |

미확인: UbD 한국어판(강현석 외 역)의 공식 용어, 한국 교육부·교육청 백워드 설계 안내, GRASPS 학습 효과 인과 연구, UbD 1단계(3–6장)·3단계(9장).

## F. 조사 과정 기록

| 항목 | 위치 |
|---|---|
| 조사 계획·진행 상태 | `research/research-plan.md` |
| 자료별 근거 요약 | `research/report-source.md` |
| GRASPS 학습 기록·반영 제안 | `research/grasps-study.md` |
| 백워드 설계·GRASPS 사본 | `research/private/grasps/` |
| 설계안 | `DESIGN.md` |
| 도서 OCR·쪽별 텍스트·렌더 | `research/private/book-*.{json,txt}`, `research/private/book-renders/`, `research/private/book-notes/` |
| DOK·공식 PDF 사본 | `research/private/sources/` |
| 교육과정 스냅샷 | `research/private/curriculum/` |

원 조사 세션: Codex 에이전트(Paseo ID `3511219f-8f31-4262-9a6c-fc5c939c5569`, 2026-09-07 10:50–11:04 KST). 설계안 작성 직후 사용량 한도로 중단되어, 이 대장과 `report-source.md`는 후속 Claude 세션(2026-09-07)이 원 세션 기록·하위 에이전트 보고·로컬 자료를 재검토해 작성했다.
