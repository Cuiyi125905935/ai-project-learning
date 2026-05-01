# Backtrader 核心结构与多周期策略逻辑拆解

## 1. 目录结构解析
*   `backtrader/feeds/`: **数据加载模块**。负责将 CSV 或 Pandas DataFrame 转换为不同周期的 `LineSeries`。
*   `backtrader/indicators/`: **指标计算模块**。内置了 TA-Lib 的对接接口，可直接调用 MACD、RSI 等因子。
*   `backtrader/strategies/`: **策略执行模块**。定义了 `next()` 方法，用于在每一个时间步处理多周期信号。

## 2. 多周期策略核心逻辑（日线趋势 + 5分钟入场）
**逻辑拆解：**
1.  **数据注入**: 同时加载日线数据 (`data0`) 和 5分钟数据 (`data1`)。
2.  **因子计算**: 
    *   在 `data0` 上计算日线 MACD，判断大趋势是否向上。
    *   在 `data1` 上计算 5分钟 RSI，寻找超卖入场点。
3.  **成交量过滤**: 调用 1小时 OBV 因子，确保上涨有量能配合。
4.  **信号生成**: 当日线 MACD > 0 且 5分钟 RSI < 30 时，触发买入信号。
