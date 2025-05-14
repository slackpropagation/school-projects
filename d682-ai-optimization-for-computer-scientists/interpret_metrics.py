"""
Task 3 – B1: Analyze RMSE & MAE from comparison_results.txt
and explain how they reflect model effectiveness.
"""

import math

# 1. Load the comparison results
with open("comparison_results.txt") as f:
    lines = f.read().splitlines()

results = {}
for line in lines:
    parts = [p.strip() for p in line.split(";")]
    name = parts[0]
    metrics = {}
    for item in parts[1:]:
        if "=" in item:
            k, v = item.split("=")
            metrics[k] = float(v)
    results[name] = metrics

# 2. Print a summary with context
print("\n=== Model Performance Summary ===")
for name, m in results.items():
    rmse = m["RMSE"]
    mae  = m["MAE"]
    print(f"{name}:")
    print(f"  • RMSE = {rmse:.3f} → average error magnitude")
    print(f"  • MAE  = {mae:.3f} → mean absolute deviation")
    if name != "Baseline_GBM":
        base_rmse = results["Baseline_GBM"]["RMSE"]
        delta = (base_rmse - rmse) / base_rmse * 100
        print(f"    → {delta:.1f}% improvement over baseline")
    print()
