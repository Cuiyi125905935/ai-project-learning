"""
Universal Boundary Testing Template for AI Alchemy Agent
Adapts to different data types, algorithms, and business scenarios.
"""

import pandas as pd
import numpy as np

def generate_universal_extreme_cases(project_type="quant"):
    """
    Generate boundary scenarios based on project type.
    Types: 'quant' (trading), 'ml' (machine learning), 'data' (analysis)
    """
    dates = pd.date_range("2023-01-01", periods=50, freq="D")
    
    base_cases = {
        "normal_scenario": pd.DataFrame({
            "feature_1": np.random.uniform(0, 1, 50),
            "target": np.random.randint(0, 2, 50)
        }),
        "missing_data": pd.DataFrame({
            "feature_1": [np.nan if i % 5 == 0 else np.random.uniform(0, 1) for i in range(50)],
            "target": np.random.randint(0, 2, 50)
        })
    }

    if project_type == "quant":
        base_cases.update({
            "limit_up_board": pd.DataFrame({"close": [110] * 50, "volume": [0] * 50}),
            "suspension_gap": pd.DataFrame({"close": list(np.random.uniform(100, 110, 25)) + [150]})
        })
    elif project_type == "ml":
        base_cases.update({
            "extreme_overfitting": pd.DataFrame({"feature": [1.0] * 49 + [0.0], "label": [1] * 50}),
            "adversarial_sample": pd.DataFrame({"feature": np.random.uniform(-100, 100, 50)})
        })
    
    return base_cases

if __name__ == "__main__":
    test_data = generate_universal_extreme_cases()
    print(f"Generated {len(test_data)} universal boundary scenarios.")
    for name, df in test_data.items():
        print(f"- {name}: {len(df)} data points, Vol Range: [{df['volume'].min()}, {df['volume'].max()}]")
