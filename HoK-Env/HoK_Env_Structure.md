# HoK Env 项目结构与迭代逻辑

## 1. 当前目录结构与功能说明
*   `aiarena/1v1/actor/`: 智能体执行模块，包含 `model.py` (PyTorch/TensorFlow 算法实现) 和 `server.py` (与游戏核心通信)。
*   `aiarena/1v1/learner/`: 训练器模块，负责从 Replay Buffer 采样数据并执行 PPO 梯度更新。
*   `aiarena/3v3/`: 3v3 多智能体环境，引入了更复杂的团队协作逻辑与通信机制。
*   `docs/`: 官方文档，包含集群训练指南（cluster.md）及环境配置说明。

## 2. 模块调用流程图解
**分布式训练逻辑链：**
`Actor (Gamecore)` → 采集状态特征 → `Server` → `Learner (PPO Update)` → 下发最新权重 → `Actor` 执行动作。

## 3. 迭代中结构调整分析
*   **后端解耦**: 提供了 `algorithm_tf.py` 和 `algorithm_torch.py` 两种后端支持，体现了框架的跨平台兼容性。
*   **配置中心化**: 通过 `config.py` 和 `DimConfig` 统一管理数百维的特征切分点，适应了 MOBA 游戏极度复杂的观测空间。
