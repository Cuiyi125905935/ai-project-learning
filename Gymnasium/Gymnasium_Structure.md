# Gymnasium 项目结构与迭代逻辑

## 1. 核心目录结构解析
*   `gymnasium/envs/`: 环境实现库，按领域划分为 `classic_control/` (CartPole), `atari/`, `mujoco/` 等子目录。
*   `gymnasium/spaces/`: 定义动作与观察空间的数学结构，如 `Discrete` (离散), `Box` (连续), `Dict` (复合空间)。
*   `gymnasium/wrappers/`: 环境包装器，提供 `TimeLimit` (超时截断), `FrameStack` (帧堆叠), `RecordVideo` 等功能。
*   `gymnasium/vector/`: 并行环境实现，支持 `AsyncVectorEnv` 和 `SyncVectorEnv`，大幅提升样本收集效率。

## 2. 模块调用逻辑（以 CartPole-v1 为例）
**交互流程链：**
`env.reset()` → 返回初始 `observation` → `env.step(action)` → 物理引擎计算下一状态 → 返回 `(obs, reward, terminated, truncated, info)` → `env.render()` 可视化。

## 3. 迭代中的架构调整：Terminated vs Truncated
*   **Gym 时代**: 仅返回 `done`。算法无法区分是“杆子倒了”（失败）还是“步数到了”（超时），导致价值函数估计偏差。
*   **Gymnasium 时代**: 
    *   `terminated`: 任务自然终止（如游戏结束、物体碰撞）。
    *   `truncated`: 外部条件截断（如达到最大步数）。
    *   **影响**: 在 DQN 等算法的经验回放中，`truncated` 状态不应被视为终止状态，从而保证了贝尔曼方程更新的连续性。
