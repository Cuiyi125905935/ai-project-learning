# OpenAI Gym Trading 项目进化历程

## 1. 版本时间线
*   **2018 (v1.0)**: 基于旧版 OpenAI Gym 发布，内置美股 10 年日线数据，定义了基础的买卖动作空间。
*   **2022 (v2.0)**: 全面适配 Gymnasium API，兼容 Gymnasium 0.26+ 接口规范；新增多周期 K 线支持，提升了对不同交易频率的适配性。
*   **2023-2025 (v2.1-v2.3)**: 新增 A 股数据对接接口（支持 baostock 等免费源），完善自定义奖励函数逻辑，并针对 CPU 批量计算进行了深度优化。

## 2. 与 Gymnasium 的兼容对照表
| 接口项 | Gym Trading 实现 | Gymnasium 标准 | 适配说明 |
| :--- | :--- | :--- | :--- |
| **重置环境** | `env.reset()` 返回 `(obs, info)` | `reset(seed=42)` | 需显式传入 `seed` 以确保实验可复现 |
| **执行动作** | `env.step(action)` 返回 5 元组 | `step(action)` 返回 5 元组 | 完全兼容，直接对接 SB3 算法 |
| **观测空间** | `spaces.Box` (技术指标) | `spaces.Box` | 需确保维度与模型输入层匹配 |
| **动作空间** | `spaces.Discrete(3)` (买/卖/持) | `spaces.Discrete(n)` | 适用于离散决策选股策略 |

## 3. 迭代技术路线分析
Gym Trading 的核心演进是从“单一美股演示”向“全球化、可定制化量化平台”转变。通过 v2.0 的 Gymnasium 重构，它成功接入了 Stable-Baselines3 生态，使得利用 PPO、DQN 等先进算法进行自动化选股成为可能。
