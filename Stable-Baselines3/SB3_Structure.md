# Stable-Baselines3 项目结构与迭代逻辑

## 1. 目录结构与模块功能解析
*   `stable_baselines3/algorithms/`: 核心算法库，包含 PPO、DQN、SAC 等模型的训练循环与损失计算逻辑。
*   `stable_baselines3/common/`: 通用工具中心，涵盖回调系统（Callbacks）、评估函数、经验回放缓冲区（Buffers）及预处理器。
*   `stable_baselines3/wrappers/`: 环境适配层，提供观测归一化、奖励缩放等标准化处理逻辑。

## 2. 模块调用逻辑（以 PPO 为例）
**完整训练流程链：**
`env = gym.make()` → `model = PPO("MlpPolicy", env)` → `model.learn(total_timesteps=10000)` → `RolloutBuffer.collect()` (收集样本) → `PPO.train()` (计算优势函数与损失) → `optimizer.step()` (权重更新)。

## 3. 迭代架构调整：v1.0 vs v2.0
*   **回调系统重构**: v2.0 将监控逻辑从训练循环中剥离，通过 `on_step` 钩子实现解耦，极大提升了扩展性。
*   **分布式支持**: 引入了对多进程采样的原生支持，使得在大规模集群上运行 SB3 变得像单机一样简单。
