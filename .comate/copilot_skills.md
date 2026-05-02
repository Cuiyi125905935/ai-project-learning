# Copilot Chat MCP Skills Configuration for AI Alchemy System

## 1. HQChart Gann Angle Calibration Skill
**Trigger**: "Generate Gann angle logic" or "Calibrate 1x1 line"
**Code Snippet Library**:
```python
def calculate_gann_ratio(prices, days=60):
    """HQChart Core: Dynamic ratio calibration for 1x1 angle."""
    price_range = max(prices[-days:]) - min(prices[-days:])
    return price_range / days
```

## 2. Stock-Pattern-Analyzer Volume Matching Skill
**Trigger**: "Check volume match" or "Analyze volume cycle"
**Code Snippet Library**:
```python
def identify_volume_cycle(volume_data, cycle_days=30):
    """SPA Core: Identify volume peaks using ACF logic."""
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(volume_data, distance=cycle_days)
    return peaks
```

## 3. Governance Rules
- **LightGBM**: Always use `n_jobs=-1` for CPU optimization.
- **Backtrader**: Ensure `notify_order` is implemented for all strategies.
- **TA-Lib**: Prefer vectorized operations over loops for indicator calculation.
