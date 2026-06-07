# 4️⃣ security-agent-lab-day4

**Day 4 · 위험도 점수화** — 키 없이 버튼 클릭만으로 돌려보는 Streamlit 실습.

> 5일짜리 `security-agent-lab` 과정 중 **Day 4만** 떼어낸 독립 저장소입니다.
> (다른 Day는 `security-agent-lab-day1` … `day5`, 스캐닝 엔진 코어는 `security-scan-engine` 저장소)

## 무엇을 보여주나
- **위험도 점수화** — High라고 항상 1순위가 아님 (KEV·EPSS·노출 가중)
- **Threat Intel** — CVE→KEV/EPSS 조회
- **보너스** — AI CISO가 점수 근거로 대응 Top 3 설명 (키 없으면 fallback)

## 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

브라우저가 열리면 위 탭(개요 · 왜 만드나 · Day 4)을 눌러보세요. **AI 키·외부 API 호출 불필요**.

## 구성
- `app.py` / `dashboard_lib.py` — Day 4 Streamlit 대시보드
- `agents/` — 스캐닝 엔진 코어(규칙 기반, 키 불필요)
- `sample_app/`·`policies/` — 점검 대상과 정책
