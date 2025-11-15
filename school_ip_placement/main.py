# UPP School IP Placement Simulation
# Source: NCES 2024-082 Teacher Staffing Model

import json
import pandas as pd
import numpy as np

# === NCES Formula ===
def calculate_need(enrollment, ell_pct, frl_pct):
    base = enrollment * 0.05
    ell_bonus = ell_pct * enrollment * 0.02
    frl_bonus = frl_pct * enrollment * 0.03
    return base + ell_bonus + frl_bonus

# === Simulate 50 schools ===
np.random.seed(7)
schools = []
for i in range(50):
    school = {
        "id": f"S{i:02d}",
        "enrollment": np.random.randint(300, 1200),
        "ell_pct": np.random.uniform(0.05, 0.40),
        "frl_pct": np.random.uniform(0.30, 0.80)
    }
    school["ip_need"] = calculate_need(
        school["enrollment"],
        school["ell_pct"],
        school["frl_pct"]
    )
    schools.append(school)

# === Budget Forecast ===
total_budget = 5_000_000
cost_per_ip = 85_000
max_hires = total_budget // cost_per_ip
hired = sorted(schools, key=lambda x: x["ip_need"], reverse=True)[:max_hires]

# === Save ===
df = pd.DataFrame(schools)
df.to_csv("simulation_output.json", index=False)
budget = pd.DataFrame(hired)[['id', 'ip_need']]
budget.to_csv("budget_forecast.csv", index=False)

print(f"UPP School Simulation: {len(hired)} hires approved under budget.")
