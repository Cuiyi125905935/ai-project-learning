# Stable-Baselines3 核心代码片段与复用指南

## 1. 通用算法训练模板 (PPO)
**来源**: `examples/ppo_cartpole.py`
**功能解析**: 展示了如何快速初始化环境、定义模型并启动训练。
**复用建议**: 这是最基础的落地模板，只需替换 `env_id` 即可适配任何 Gymnasium 环境。

```python
import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("CartPole-v1")
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("ppo_cartpole")
```

## 2. 自定义环境适配标准
**来源**: `docs/source/guide/custom_env.md`
**功能解析**: 定义了继承 `gym.Env` 的标准写法，包括 `observation_space` 和 `action_space` 的声明。
**修改点提示**: 在金融量化场景中，可将 `Box` 空间定义为多维因子向量。

## 3. 回调函数实现 (Callbacks)
**来源**: `stable_baselines3/common/callbacks.py`
**功能解析**: `EvalCallback` 用于周期性评估模型性能，`CheckpointCallback` 用于自动保存中间权重。
**复用场景**: 防止模型过拟合，确保能随时回滚到历史最佳状态。

## 4. 经验回放缓冲区自定义 (Replay Buffer)
**来源**: `stable_baselines3/common/buffers.py`
**功能解析**: 实现了高效的样本存储与采样逻辑。
**修改点提示**: 可通过继承 `ReplayBuffer` 类，增加对优先经验回放（PER）的支持，提升 DQN 等算法的训练效率。
