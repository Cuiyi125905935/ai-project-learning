# technical-analysis 核心代码片段与江恩共振输出指南

## 1. 江恩百分比回调位计算代码 (CPU 适配)
**说明**: 自动计算核心支撑/阻力位。
```python
def gann_retracement(high, low):
    diff = high - low
    levels = {
        "50%": low + diff * 0.5,
        "66.7%": low + diff * 0.667,
        "33.3%": low + diff * 0.333
    }
    return levels

print(gann_retracement(100, 80)) # 输出各百分比对应的价格点
```

## 2. 时空共振验证代码 (工具链对接)
**说明**: 整合 pmdarima 时间与 HQChart 价格，输出共振得分。
```python
def calculate_resonance_score(time_match, price_match, level_match):
    score = 0
    if time_match: score += 30 # pmdarima 周期吻合
    if price_match: score += 30 # HQChart 几何点位吻合
    if level_match: score += 30 # 本工具百分比位吻合
    return score

resonance = calculate_resonance_score(True, True, False)
print(f"Resonance Score: {resonance}/100")
```

## 3. 多周期共振批量计算代码 (CPU 多核优化)
**说明**: 适配 i5-10400，批量扫描全市场。
```python
from joblib import Parallel, delayed

def batch_scan(stocks_data):
    results = []
    for stock in stocks_data:
        # 调用上述共振逻辑
        score = calculate_resonance_score(...)
        results.append({"Code": stock['code'], "Score": score})
    return results

# n_jobs=8 充分利用 CPU 线程
Parallel(n_jobs=8)(delayed(batch_scan)(batch) for batch in data_batches)
```

## 4. 量能因子对接代码 (TA-Lib 权重调整)
**说明**: 利用 OBV 提升高分信号的可信度。
```python
import talib
obv = talib.OBV(close, volume)
# 如果共振发生时 OBV 处于上升段，额外加 10 分
volume_bonus = 10 if obv[-1] > obv[-5] else 0
final_score = resonance + volume_bonus
```
