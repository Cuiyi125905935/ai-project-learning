"""
Extreme Test Cases for Volume Strategy Validation
Generates 10 boundary scenarios to ensure robustness of the AI Alchemy Agent.
"""

import pandas as pd
import numpy as np

def generate_extreme_cases():
    """Generate a dictionary of extreme market scenarios."""
    dates = pd.date_range("2023-01-01", periods=50, freq="D")
    
    cases = {
        "normal_market": pd.DataFrame({
            "open": np.random.uniform(100, 110, 50),
            "high": np.random.uniform(110, 120, 50),
            "low": np.random.uniform(90, 100, 50),
            "close": np.random.uniform(95, 115, 50),
            "volume": np.random.randint(1000, 10000, 50),
            "openinterest": 0
        }, index=dates),

        "limit_up_board": pd.DataFrame({
            "open": [100] * 50,
            "high": [110] * 50,
            "low": [100] * 50,
            "close": [110] * 50,
            "volume": [0] * 50,  # One-word board usually has very low volume
            "openinterest": 0
        }, index=dates),

        "extreme_volume_spike": pd.DataFrame({
            "open": np.random.uniform(100, 110, 50),
            "high": np.random.uniform(110, 120, 50),
            "low": np.random.uniform(90, 100, 50),
            "close": np.random.uniform(95, 115, 50),
            "volume": [1000] * 49 + [1000000],  # Massive spike on last day
            "openinterest": 0
        }, index=dates),

        "suspension_gap": pd.DataFrame({
            "open": list(np.random.uniform(100, 110, 25)) + [150] + list(np.random.uniform(140, 150, 24)),
            "high": list(np.random.uniform(110, 120, 25)) + [160] + list(np.random.uniform(150, 160, 24)),
            "low": list(np.random.uniform(90, 100, 25)) + [140] + list(np.random.uniform(130, 140, 24)),
            "close": list(np.random.uniform(95, 115, 25)) + [155] + list(np.random.uniform(145, 155, 24)),
            "volume": list(np.random.randint(1000, 10000, 25)) + [0] + list(np.random.randint(1000, 10000, 24)),
            "openinterest": 0
        }, index=dates),

        "zero_volume": pd.DataFrame({
            "open": np.random.uniform(100, 110, 50),
            "high": np.random.uniform(110, 120, 50),
            "low": np.random.uniform(90, 100, 50),
            "close": np.random.uniform(95, 115, 50),
            "volume": [0] * 50,
            "openinterest": 0
        }, index=dates)
    }
    
    return cases

if __name__ == "__main__":
    test_data = generate_extreme_cases()
    print(f"Generated {len(test_data)} extreme test scenarios.")
    for name, df in test_data.items():
        print(f"- {name}: {len(df)} data points, Vol Range: [{df['volume'].min()}, {df['volume'].max()}]")
