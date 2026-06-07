# Day 4 — Threat Intelligence · 위험도 점수화

## 오늘의 목표
- "High 라고 항상 1순위가 아니다"를 점수로 이해한다.
- CVE/KEV/EPSS 를 결합해 위험도 점수표를 생성한다.

---

## Mini Lab — Risk Card Sorting Game
- **목적**: 직관 순위 vs 공식 기반 risk_score 순위를 비교해 우선순위 감각을 잡음
- **실행 명령**
  ```bash
  python course/mini_labs/day04_risk_game/run_risk_sorting_game.py
  ```
- **산출물**: `reports/risk_sorting_game.md`
- **확인 포인트**: severity=Critical 카드가 KEV/EPSS/노출 때문에 1순위가 아닌 경우를 확인했는가?
- **본 실습 연결**: 점수 기반 우선순위 감각이 본 실습의 **CVE/KEV/EPSS 기반 risk_score_table.md** 생성으로 이어진다.
- 자세히: `course/experiments/day04_risk_card_game.md`

---

## Main Lab — Threat Intelligence Agent 강화
- **목적**: 의존성 취약점에 CVE/KEV/EPSS 위협 정보를 붙여 위험도 점수화
- **실행 명령**
  ```bash
  python agents/threat_agent.py
  python orchestrator/supervisor_graph.py --target sample_app/ --threat-intel --report final
  ```
- **산출물**: `reports/threat_context.json`, `reports/risk_score_table.md`, `reports/final_report.md`
- **확인 포인트**: KEV 등재/EPSS 가 점수와 순위에 반영됐는가? control/ 모듈 발견의 가중이 반영됐는가?

---

## 선택 보조: Claude/GPT 저토큰 활용
- 전체 코드베이스를 넣지 않는다.
- `python scripts/make_light_context_pack.py --day 4` 로 `reports/context_pack_day4.md` 만 생성해 복사한다.
- "이 risk_score_table.md 에서 설명이 빠진 점수 항목 3개만 짚어줘" 정도로 가볍게 사용한다.

---

## 완료 체크리스트
- [ ] `reports/risk_sorting_game.md` 생성 (순위 변화 확인)
- [ ] `reports/threat_context.json` 생성
- [ ] `reports/risk_score_table.md` 생성
- [ ] KEV/EPSS 가 우선순위를 바꾼다는 개념 이해
