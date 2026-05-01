# pmdarima 核心代码片段与江恩高低点预测落地指南

## 1. 江恩周期自动检测代码 (CPU 适配)
**说明**: 自动识别最显著的循环周期。
```python
import pmdarima as pm
from pmdarima.arima import auto_arima

# stepwise=True 加速 CPU 搜索过程
model = auto_arima(y, seasonal=True, m=30, stepwise=True, n_jobs=1)
print(f"Detected Order: {model.order}, Seasonal Order: {model.seasonal_order}")
```

## 2. 多周期数据 + 成交量因子融合代码
**说明**: 对接 Backtrader 数据与 TA-Lib OBV。
```python
import talib
# X 为外部回归变量，包含成交量因子
obv = talib.OBV(df['close'].values, df['volume'].values)
model.fit(y=df['close'], X=obv.reshape(-1, 1))
```

## 3. 高低点快速预测代码 (未来 5 天)
**说明**: 输出预测值及 95% 置信区间。
```python
n_periods = 5
fc, conf_int = model.predict(n_periods=n_periods, return_conf_int=True, alpha=0.05)
print(f"Predicted High/Low Range: {conf_int}")
```

## 4. 预测结果与江恩周期对比代码
**说明**: 计算理论转折点与实际预测的偏差。
```python
# 假设第 30 天为江恩理论转折点
gann_theory_day = 30
deviation = abs(fc[gann_theory_day % len(fc)] - actual_price[gann_theory_day])
print(f"Gann Cycle Deviation Rate: {deviation / actual_price[gann_theory_day]:.2%}")
```
