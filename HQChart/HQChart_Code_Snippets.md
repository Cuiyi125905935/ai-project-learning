# HQChart 核心代码片段与江恩价格时间点输出指南

## 1. 江恩角度线动态校准代码 (CPU 适配)
**说明**: 自动计算适配个股波动率的 1x1 线参数。
```python
def calculate_gann_ratio(prices, days=60):
    # 计算近 60 天的平均日波幅作为基准比率
    price_range = max(prices[-days:]) - min(prices[-days:])
    ratio = price_range / days
    return ratio # 例如：1天对应 2.5 元

ratio = calculate_gann_ratio(df['close'])
print(f"1x1 Line Ratio: {ratio}")
```

## 2. 轮中轮时间-价格共振点计算代码
**说明**: 对接 pmdarima 周期，输出未来共振点。
```python
import math

def wheel_of_fortune(start_price, cycle_days, current_day):
    # 将时间映射到角度 (360度/周期)
    angle = (current_day % cycle_days) * (360 / cycle_days)
    # 计算理论价格偏移量 (简化模型)
    price_offset = start_price * math.sin(math.radians(angle))
    return {"Day": current_day, "Price_Point": start_price + price_offset, "Direction": "Up" if price_offset > 0 else "Down"}

resonance = wheel_of_fortune(100, 30, 31)
print(resonance)
```

## 3. 四方形关键价格点计算代码
**说明**: 计算江恩四方形的支撑/阻力位。
```python
def square_of_nine_levels(base_price):
    sqrt_price = math.sqrt(base_price)
    levels = []
    for i in range(1, 9): # 计算周围 8 个关键点
        level = (sqrt_price + i * 0.125) ** 2
        levels.append(round(level, 2))
    return levels

print(f"S/R Levels: {square_of_nine_levels(100)}")
```

## 4. 量能因子验证代码 (TA-Lib 对接)
**说明**: 输出价格点的量能配合度得分。
```python
import talib
obv = talib.OBV(df['close'], df['volume'])
# 计算当前价格点位的 OBV 趋势强度
score = obv[-1] - obv[-5] 
print(f"Volume Confirmation Score: {score}")
```
