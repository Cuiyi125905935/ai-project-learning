# Stock-Pattern-Analyzer 核心代码片段与江恩量价时空输出指南

## 1. 江恩量能周期自动识别代码 (CPU 适配)
**说明**: 从成交量中提取循环规律。
```python
import numpy as np
from scipy.signal import find_peaks

def identify_volume_cycle(volume_data, cycle_days=30):
    # 寻找成交量峰值对应的时间索引
    peaks, _ = find_peaks(volume_data, distance=cycle_days)
    return peaks # 输出量能峰值出现的时间窗口

peaks = identify_volume_cycle(df['volume'])
print(f"Volume Peak Windows: {peaks}")
```

## 2. 量价时空四方匹配代码 (全工具链对接)
**说明**: 整合时间、价格、百分比及量能，输出综合得分。
```python
def calculate_quad_match(time_score, price_score, level_score, volume_score):
    # 简单的加权平均，可根据实际需求调整权重
    total_score = (time_score * 0.3 + price_score * 0.3 + 
                   level_score * 0.2 + volume_score * 0.2)
    return min(total_score, 100)

match_result = calculate_quad_match(90, 85, 80, 70)
print(f"Quad Match Score: {match_result}/100")
```

## 3. 全市场批量量价时空计算代码 (CPU 多核优化)
**说明**: 适配 i5-10400，批量扫描并输出结果。
```python
from joblib import Parallel, delayed

def batch_analyze(stocks_list):
    results = []
    for stock in stocks_list:
        score = calculate_quad_match(...)
        results.append({
            "Code": stock['code'], 
            "Match_Time": stock['predicted_time'],
            "Match_Price": stock['predicted_price'],
            "Score": score
        })
    return results

Parallel(n_jobs=8)(delayed(batch_analyze)(batch) for batch in data_batches)
```

## 4. 量能有效性验证代码 (TA-Lib 对接)
**说明**: 输出量能健康度得分。
```python
import talib
obv = talib.OBV(df['close'], df['volume'])
vol_sma = talib.SMA(df['volume'], timeperiod=5)
# 量能健康度：OBV 趋势向上且当前成交量高于均量
health_score = 10 if (obv[-1] > obv[-5] and df['volume'][-1] > vol_sma[-1]) else 0
print(f"Volume Health Score: {health_score}")
```
