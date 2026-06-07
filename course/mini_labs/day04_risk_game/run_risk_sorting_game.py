#!/usr/bin/env python3
"""
Risk Card Sorting Game (course/mini_labs/day04_risk_game/run_risk_sorting_game.py) — Day 4 Mini Lab

목표: "High 라고 항상 1순위가 아니다" 를 점수로 체감한다.
사람이 직관으로 매긴 human_guess_rank 와 공식 기반 risk_score 순위를 비교한다.

- 외부 API 호출 없음 / LLM 호출 없음 / Python 표준 라이브러리만 사용

실행:  python course/mini_labs/day04_risk_game/run_risk_sorting_game.py
산출물: reports/risk_sorting_game.md
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "risk_cards.json")
OUT = "reports/risk_sorting_game.md"

SEVERITY_WEIGHT = {"Critical": 4.0, "High": 3.0, "Medium": 2.0, "Low": 1.0}
EXPOSURE_WEIGHT = {
    "ecu_command_bus": 2.0,
    "ecu_firmware_update": 1.8,
    "public_web": 1.5,
    "internal_admin": 1.0,
}


def risk_score(card):
    sev = SEVERITY_WEIGHT.get(card["severity"], 1.0)
    kev = 1.5 if card.get("kev") else 1.0
    epss = float(card.get("epss", 0.0))
    exposure = EXPOSURE_WEIGHT.get(card.get("control_module"), 1.0)
    return round(sev * kev * (0.5 + epss) * exposure, 3)


def main():
    with open(CARDS, encoding="utf-8") as f:
        cards = json.load(f)["cards"]

    for c in cards:
        c["risk_score"] = risk_score(c)

    # 계산 기반 순위(점수 내림차순)
    ranked = sorted(cards, key=lambda c: c["risk_score"], reverse=True)
    for rank, c in enumerate(ranked, start=1):
        c["calc_rank"] = rank

    lines = ["# Risk Card Sorting Game (Day 4 Mini Lab)", ""]
    lines.append("> 사람의 직관 순위 vs 공식 기반 점수 순위를 비교합니다.")
    lines.append("")
    lines.append("| 계산순위 | 카드 | severity | KEV | EPSS | 모듈 | risk_score | 사람추측 | 변화 |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for c in ranked:
        diff = c["human_guess_rank"] - c["calc_rank"]
        if diff > 0:
            change = f"▲ {diff} (과소평가)"
        elif diff < 0:
            change = f"▼ {abs(diff)} (과대평가)"
        else:
            change = "= 동일"
        kev = "✔" if c.get("kev") else "-"
        lines.append(
            f"| {c['calc_rank']} | {c['title']} | {c['severity']} | {kev} | "
            f"{c['epss']} | {c['control_module']} | {c['risk_score']} | "
            f"{c['human_guess_rank']} | {change} |"
        )
    lines.append("")

    # 해설: KEV / EPSS / 노출이 순위를 어떻게 바꿨는지
    top = ranked[0]
    crit = next((c for c in cards if c["severity"] == "Critical"), None)
    lines.append("## 해설 — 무엇이 순위를 바꿨나")
    lines.append(f"- 1순위는 **{top['title']}** (risk_score={top['risk_score']}).")
    if crit and crit["calc_rank"] > 1:
        lines.append(
            f"- **{crit['title']}** 는 severity=Critical 이지만 "
            f"KEV 미등재·EPSS={crit['epss']}·모듈={crit['control_module']}(노출 낮음) 때문에 "
            f"계산순위 {crit['calc_rank']}위로 밀렸다."
        )
    lines.append("- **KEV** 가 true 면 가중치 1.5배 → 실제 악용 사례가 우선순위를 끌어올린다.")
    lines.append("- **EPSS** 가 높을수록 (0.5+epss) 항이 커져 점수가 오른다.")
    lines.append("- **control_module(노출)** 이 차량 제어 버스/펌웨어면 영향 범위가 커 가중된다.")
    lines.append("")
    lines.append("> 결론: severity 라벨 하나로 줄세우면 위험하다. KEV·EPSS·노출을 결합해야 한다.")
    lines.append("")
    lines.append("> 연결: 이 감각이 Day 4 본 실습의 CVE/KEV/EPSS 기반")
    lines.append("> reports/risk_score_table.md 생성으로 이어집니다.")
    lines.append("")

    os.makedirs("reports", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("[RiskGame] 계산 순위:")
    for c in ranked:
        print(f"  {c['calc_rank']}. {c['title']:24} score={c['risk_score']:6} "
              f"(사람추측 {c['human_guess_rank']})")
    print(f"[RiskGame] 산출물 저장 → {OUT}")


if __name__ == "__main__":
    main()
