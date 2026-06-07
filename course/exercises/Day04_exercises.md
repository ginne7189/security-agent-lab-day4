# Day 4 과제 — 위험도 (DDD · Risk Score · Decision Support)
> PPT 개념: DDD · Risk Score · Decision Support

## 🎬 시나리오
High 발견이 100개다. 뭐부터 하지?
**도메인(위험) 모델**을 정의하고 **점수로 우선순위를 자동 산출**하라.

## 🟢 기본 과제 (5~10분)
1. `course/mini_labs/day04_risk_game/risk_cards.json` 에 KEV=true·EPSS 높은 카드를 추가
   → 1순위가 바뀌는지 확인.
2. `run_risk_sorting_game.py` 의 `EXPOSURE_WEIGHT` 값을 바꿔 순위 변화 관찰.

## 🏗 생성형 과제 — 점수 규칙/도메인 모델 (10~20분)
1. 점수식 `(0.5 + epss)` 항이나 가중치를 바꿔 **의사결정이 달라지는지** 실험.
2. 대시보드 Day4 **🧠 AI 보안책임자(CISO)** 버튼으로 `risk_score` 근거 Top 3 산출
   (키 없으면 점수 기반 Top 3 fallback).
3. (선택) 새 위협 도메인 에이전트 보일러플레이트 생성:
   ```bash
   python scripts/new_agent.py kev --cwe CWE-1395 --title "KEV 의존성" --pattern "pyyaml|jinja2"
   ```

## 🔥 도전 과제
점수식의 EPSS 반영을 **구간별 비선형 가중**(예: 0.7 이상은 ×2)으로 바꿔 우선순위를 재설계.

## ✅ 완료 체크
- [ ] 카드/가중치 변경으로 순위가 바뀌는 걸 확인
- [ ] AI(또는 규칙) Top 3 의사결정 산출
- [ ] `supervisor_graph.py --threat-intel --report final` 로 점수표 생성
