# LightGBM 项目结构与选股核心逻辑拆解

## 1. 目录结构逐行解析（量化选股视角）
*   `src/`: **C++ 核心实现**。包含 CPU 并行训练、直方图计算及损失函数的底层优化，确保了在 i5-10400 上的极致运行效率。
*   `python-package/`: **Python 接口层**。封装了 `LGBMClassifier` 等高级 API，是衔接 FinRL 特征数据与模型训练的直接入口。
*   `examples/`: **官方示例库**。提供了二分类任务、交叉验证及早停机制的标准代码模板。

## 2. 选股核心逻辑拆解
*   **输入层**: 直接对接 FinRL 输出的 15 个多因子特征（MACD, RSI, PE 等）。标签定义为：`label = 1 if 未来 3 天收益率 > 2% else 0`。
*   **训练层**: 采用 Leaf-wise 策略在 CPU 上快速分裂节点，利用 `early_stopping_rounds` 防止过拟合，确保模型在 A 股震荡市中的稳定性。
*   **输出层**: 输出选股概率（0-1）及特征重要性排名。概率越高代表该股票短期爆发力越强，特征排名则揭示了哪些因子主导了本次选股。

## 3. 模块调用逻辑（CPU 优化版）
**完整流程链：**
`FinRL_CSV_Data` → `Label_Generation` → `LGBMClassifier(num_threads=8)` → `fit(X_train, y_train)` → `predict_proba(X_test)` → `Success_Rate_Stats`。
