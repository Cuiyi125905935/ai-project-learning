# Backtrader 全周期适配说明

## 1. 全周期支持范围与参数定义
Backtrader 通过 `timeframe` 和 `compression` 两个核心参数实现任意周期的灵活切换：
*   **标准周期**: `bt.TimeFrame.Days` (日线), `bt.TimeFrame.Minutes` (分钟线), `bt.TimeFrame.Weeks` (周线)。
*   **自定义周期**: 
    *   **5分钟线**: `timeframe=bt.TimeFrame.Minutes, compression=5`
    *   **2日线**: `timeframe=bt.TimeFrame.Days, compression=2`
    *   **30分钟线**: `timeframe=bt.TimeFrame.Minutes, compression=30`

## 2. 周期参数调用逻辑
在策略类中，可以通过 `self.datas[0]`, `self.datas[1]` 等索引同时访问不同周期的数据。修改周期只需在 `cerebro.adddata()` 阶段调整参数，策略内部的计算逻辑（如 MACD、RSI）会自动适配新的时间粒度，无需重构代码。
