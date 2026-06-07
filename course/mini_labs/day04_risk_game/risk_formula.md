# Risk Score 공식 (course/mini_labs/day04_risk_game/risk_formula.md)

이 게임은 "High = 항상 1순위" 가 아님을 점수로 보여줍니다.

## 점수식

```
risk_score = severity_weight × kev_weight × (0.5 + epss) × exposure_weight
```

## 가중치 표

### severity_weight (심각도)
| severity | weight |
|---|---|
| Critical | 4.0 |
| High | 3.0 |
| Medium | 2.0 |
| Low | 1.0 |

### kev_weight (Known Exploited Vulnerabilities — 실제 악용 사례)
| kev | weight |
|---|---|
| true | 1.5 |
| false | 1.0 |

### epss (Exploit Prediction Scoring System — 악용 가능성 확률, 0~1)
- 식에 `(0.5 + epss)` 로 직접 반영. EPSS 가 높을수록 가중.

### exposure_weight (control_module — 노출/영향 범위)
| control_module | weight | 설명 |
|---|---|---|
| ecu_command_bus | 2.0 | 차량 제어 버스, 안전 직결 |
| ecu_firmware_update | 1.8 | 펌웨어 변조 위험 |
| public_web | 1.5 | 외부 인터넷 노출 |
| internal_admin | 1.0 | 내부망 한정 |

## 핵심 메시지
- KEV·EPSS·노출 범위가 결합되면, 단일 severity 라벨보다 우선순위가 더 정확해진다.
- 그래서 "Critical 인데 내부망·EPSS 낮음" 카드가 "High 인데 KEV·노출 높음" 카드보다
  뒤로 밀릴 수 있다.

> 연결: 이 점수 기반 우선순위 감각이 Day 4 본 실습의
> CVE/KEV/EPSS 기반 reports/risk_score_table.md 생성으로 이어집니다.
