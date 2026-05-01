# ChineseChess-AlphaZero 项目结构与迭代逻辑

## 1. 当前目录结构与功能说明
*   `cchess_alphazero/agent/`: 核心智能体，包含 `model.py` (ResNet 定义) 和 `player.py` (MCTS 搜索逻辑)。
*   `cchess_alphazero/environment/`: 棋盘环境，负责走法生成、局面合法性校验及胜负判定。
*   `cchess_alphazero/configs/`: 配置中心，定义了网络层数、MCTS 模拟次数等超参数。
*   `cchess_alphazero/lib/`: 辅助工具库，包括数据持久化、ELO 评分计算及 TensorFlow 优化工具。

## 2. 模块调用流程图解
**训练阶段逻辑链：**
`manager.py` (调度) → `self_play.py` (调用 MCTS 生成对局数据) → `data_helper.py` (存储至 Replay Buffer) → `trainer.py` (采样数据进行 SGD 更新) → `model_helper.py` (保存新权重)。

## 3. 迭代中结构调整分析
*   **模块化拆分**: 早期版本将 MCTS 逻辑直接嵌入训练脚本，后期独立为 `agent/player.py`，提高了代码复用性。
*   **环境抽象**: 引入了 `static_env` 和 `light_env`，分别用于高精度模拟和快速自对弈，体现了性能与精度的权衡设计。
