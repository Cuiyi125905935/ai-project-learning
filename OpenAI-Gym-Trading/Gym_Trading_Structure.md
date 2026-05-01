# OpenAI Gym Trading 项目结构与选股逻辑拆解

## 1. 目录结构逐行解析
*   `gym_anytrading/envs/`: 核心环境实现。`trading_env.py` 定义父类，`stocks_env.py` 实现股票专用逻辑（如 K 线窗口滑动）。
*   `gym_anytrading/datasets/`: 数据集模块。内置美股数据，并提供 A 股外部数据对接接口（如 baostock）。
*   `examples/`: 官方落地示例。包含基础训练、回测及自定义环境代码。

## 2. 选股核心逻辑拆解
*   **观测空间 (Observation Space)**: 由 12 个核心特征构成，包括开盘价、收盘价、成交量、MACD、RSI 等。每个特征均经过归一化处理，确保模型收敛速度。
*   **动作空间 (Action Space)**: 采用 `Discrete(3)`，分别代表：0=持有、1=买入、2=卖出。
*   **奖励函数 (Reward Function)**: 默认基于持仓收益率计算。在选股场景中，建议修改为“成功选中涨停股”的稀疏奖励或基于盈亏比的复合奖励。

## 3. 模块调用逻辑（对接 SB3）
**完整流程链：**
`加载 A 股数据` → `env = gym.make('stocks-v0', ...)` → `model = PPO("MlpPolicy", env, device='cpu')` → `model.learn()` → `输出选股信号`。
