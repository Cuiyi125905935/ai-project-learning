# TA-Lib 核心代码片段与选股落地指南

## 1. 批量计算全市场股票因子 (CPU 多核优化)
**说明**: 适配 i5-10400，利用 `n_jobs=8` 并行加速。
```python
import talib
import pandas as pd
from joblib import Parallel, delayed

def calc_factors(df):
    df['MACD'], _, _ = talib.MACD(df['close'])
    df['RSI'] = talib.RSI(df['close'], timeperiod=14)
    return df

# 假设 stock_list 包含全市场 K 线数据
results = Parallel(n_jobs=8)(delayed(calc_factors)(df) for df in stock_list)
```

## 2. 自定义因子参数修改 (短线适配)
**说明**: 调整 MACD 参数以捕捉 A 股短线机会。
```python
# 使用快线参数 (5, 10, 3)
macd_fast, macd_slow, macd_signal = talib.MACD(df['close'], fastperiod=5, slowperiod=10, signalperiod=3)
```

## 3. 因子有效性检验 (相关性分析)
**说明**: 筛选与未来 3 天收益率相关性最高的因子。
```python
df['future_ret'] = df['close'].shift(-3) / df['close'] - 1
corr_matrix = df[['MACD', 'RSI', 'OBV', 'future_ret']].corr()
print(corr_matrix['future_ret'].sort_values(ascending=False))
```

## 4. 对接 LightGBM 的因子输出
**说明**: 生成标准化的特征数据集。
```python
feature_cols = ['MACD', 'RSI', 'OBV']
X = df[feature_cols].dropna()
y = (df['future_ret'] > 0.02).astype(int).loc[X.index] # 生成二分类标签
# X, y 可直接传入 LightGBM 进行训练
```
