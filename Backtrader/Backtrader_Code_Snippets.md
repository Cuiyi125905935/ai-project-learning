# Backtrader 核心代码片段与全周期选股落地指南

## 1. 全周期数据加载代码 (CPU 适配)
**说明**: 一行代码切换任意周期，适配 i5-10400。
```python
import backtrader as bt

cerebro = bt.Cerebro()
# 修改 compression 参数即可切换为 5分钟、30分钟或日线
data = bt.feeds.PandasData(dataname=df, timeframe=bt.TimeFrame.Minutes, compression=5)
cerebro.adddata(data)
```

## 2. 多周期因子调用代码 (对接 TA-Lib)
**说明**: 同时调用不同周期的技术指标。
```python
class MultiPeriodStrategy(bt.Strategy):
    def __init__(self):
        # data0 为日线，data1 为5分钟线
        self.macd_daily = bt.indicators.MACD(self.datas[0])
        self.rsi_5min = bt.indicators.RSI(self.datas[1], period=14)
        self.obv_hourly = bt.indicators.OnBalanceVolume(self.datas[2])
```

## 3. 全周期选股策略代码 (参数自定义)
**说明**: 实现“日线金叉 + 5分钟超卖”逻辑。
```python
def next(self):
    if self.macd_daily.macd[0] > self.macd_daily.signal[0] and self.rsi_5min[0] < 30:
        self.buy() # 触发买入信号
```

## 4. 成交量因子过滤代码
**说明**: 利用 OBV 提升信号有效性。
```python
def next(self):
    # 只有当 OBV 处于上升趋势时才执行买入
    if self.obv_hourly[0] > self.obv_hourly[-1] and self.should_buy():
        self.buy()
```
