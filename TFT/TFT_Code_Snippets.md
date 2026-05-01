# TFT 核心代码片段与江恩高低点预测落地指南

## 1. 江恩特征构造代码 (CPU 适配)
**说明**: 自动计算循环周期剩余天数及角度线斜率。
```python
import numpy as np

def generate_gann_features(dates, cycle=30):
    # 计算距离下一个转折点的剩余天数
    day_in_cycle = np.arange(len(dates)) % cycle
    remaining_days = cycle - day_in_cycle
    # 模拟江恩角度线斜率（此处以黄金分割为例）
    slope_feature = np.full_like(remaining_days, 1.618) 
    return np.column_stack([remaining_days, slope_feature])
```

## 2. 多周期因子 + 江恩特征融合代码
**说明**: 对接 Backtrader 数据与 TA-Lib 因子。
```python
# 假设 df 包含 Backtrader 导出的全周期数据
df['macd'] = talib.MACD(df['close'])[0]
gann_feats = generate_gann_features(df.index)
# 拼接为 TFT 输入矩阵
features = np.hstack([df[['macd', 'rsi']].values, gann_feats])
```

## 3. 高低点时序预测代码 (CPU 优化)
**说明**: 设置 `batch_size=32` 适配 i5-10400，输出未来 7 天预测。
```python
from tft import TemporalFusionTransformer

model = TemporalFusionTransformer(
    input_size=features.shape[1], 
    output_horizon=7, 
    device='cpu'
)
model.fit(features, epochs=50, batch_size=32)
predictions = model.predict(future_features) # 输出 [高点概率, 低点概率, 价格]
```

## 4. 预测结果可视化代码
**说明**: 叠加实际股价与江恩时间窗预测。
```python
import matplotlib.pyplot as plt
plt.plot(actual_prices, label='Actual')
plt.plot(predictions[:, 2], label='Predicted High/Low')
plt.axvline(x=30, color='r', linestyle='--', label='Gann Cycle Day 30')
plt.legend()
plt.show()
```
