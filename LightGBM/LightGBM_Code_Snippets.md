# LightGBM 核心代码片段与选股落地指南

## 1. FinRL 特征数据导入与标签生成
**说明**: 100% 对接 FinRL 输出的 CSV 格式，利用 Pandas 快速生成二分类标签。
```python
import pandas as pd
import numpy as np

df = pd.read_csv("finrl_output_features.csv")
# 生成标签：未来3天收盘价涨幅超过2%记为1，否则为0
df['label'] = (df['close'].shift(-3) / df['close'] > 1.02).astype(int)
df.dropna(inplace=True)
X, y = df[['macd', 'rsi', 'pe']], df['label'] # 选取FinRL计算的因子
```

## 2. CPU 优化的 LightGBM 选股模型训练
**说明**: 针对 i5-10400 设置 `num_threads=8`，开启早停防止过拟合。
```python
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LGBMClassifier(
    n_estimators=1000, 
    learning_rate=0.05, 
    num_leaves=31, 
    num_threads=8, # 适配i5-10400的8线程
    device='cpu'
)
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], early_stopping_rounds=50)
```

## 3. 选股预测与成功率统计
**说明**: 通过概率阈值筛选高胜率股票，输出盈亏比。
```python
probs = model.predict_proba(X_test)[:, 1]
selected_mask = probs > 0.6
success_rate = y_test[selected_mask].mean()
print(f"选股成功率: {success_rate:.2%}")
```

## 4. 特征重要性分析
**说明**: 识别对选股成功率影响最大的因子。
```python
import matplotlib.pyplot as plt
plt.barh(df.columns[:-1], model.feature_importances_)
plt.title("Feature Importance for Stock Selection")
plt.show()
```

## 5. 单只股票选股信号输出
**说明**: 输入最新因子，实时输出买卖建议。
```python
latest_features = np.array([[0.5, 60.2, 15.0]]) # MACD, RSI, PE
prob = model.predict_proba(latest_features)[0][1]
signal = "BUY" if prob > 0.6 else "HOLD"
print(f"Signal: {signal}, Probability: {prob:.4f}")
```
