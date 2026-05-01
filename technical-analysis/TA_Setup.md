# technical-analysis 江恩适配与本地搭建说明

## 1. Windows 环境本地搭建步骤（适配 G 盘）
*   **第一步：源码拉取**
    将 `technical-analysis` (shahradelahi) 仓库克隆至 `G:\AI_Alchemy_System\lib\technical-analysis`。该库提供了丰富的技术分析指标，我们重点提取其百分比回调计算逻辑。
*   **第二步：核心模块剥离**
    禁用所有涉及买卖信号生成的函数（如 `buy/sell signals`），仅保留 `fibonacci_retracement` 和 `pivot_points` 等几何计算模块。
*   **第三步：接口兼容性验证**
    编写测试脚本，确保从 pmdarima 导出的时间周期和 HQChart 导出的价格点能直接作为参数传入本工具进行共振计算。

## 2. 版本迭代与共振优化
*   **v1.5**: 实现了基础的斐波那契回调位计算，支持手动输入高低点。
*   **v2.0-v2.2**: 引入“多维度共振验证模块”。模型现在可以自动识别并匹配来自不同工具链的信号（如：HQChart 的 1x1 线价格 vs 本工具的 50% 回调位）。同时升级了“自适应波动率算法”，使百分比位能根据个股近期的 ATR 动态微调。
