# 冗余模块清理报告

## 1. 清理概述
基于 `dependency_map/redundant_modules.txt` 的分析结果，对全工具链进行了标准化重构。

## 2. 删除的重复功能
*   **technical-analysis**: 移除了基础的 `fibonacci_retracement` 实现，统一改为调用 TA-Lib 或 HQChart 的核心接口。
*   **Stock-Pattern-Analyzer**: 移除了独立的均线计算逻辑，全部对接 TA-Lib 的 `SMA/EMA` 接口。

## 3. 合并的标准化接口
*   **价格位计算**: 统一由 `HQChart` 负责江恩几何点位输出。
*   **基础因子**: 统一由 `TA-Lib` 负责 MACD, RSI, OBV 等指标计算。

## 4. 清理后目录结构
所有核心逻辑已收敛至 `pipeline/volume_price_time_pipeline.py`，确保无垃圾代码残留。
