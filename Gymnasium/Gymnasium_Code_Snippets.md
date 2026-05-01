# Gymnasium 核心代码片段与复用指南

## 1. 环境基础交互模板（通用落地代码）
**适用场景**: 任何基于 Gymnasium 的强化学习算法开发与测试。
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    # 随机动作，实际使用时替换为策略网络输出
    action = env.action_space.sample()  
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

## 2. 关键模块复用代码
### A. 动作/观察空间定义
**来源**: `gymnasium/spaces/box.py`
**复用建议**: 在自定义量化交易环境时，直接使用 `Box` 定义价格、成交量等连续特征空间。
```python
from gymnasium.spaces import Box
import numpy as np

# 定义一个3维连续特征空间，范围[-1, 1]
observation_space = Box(low=-1.0, high=1.0, shape=(3,), dtype=np.float32)
```

### B. 环境包装器组合 (Wrapper Chain)
**来源**: `gymnasium/wrappers/frame_stack.py`
**复用建议**: 处理时序图像输入（如 K线图），通过堆叠捕捉动态趋势。
```python
env = gym.make("ALE/Breakout-v5")
env = gym.wrappers.FrameStack(env, num_stack=4) # 将4帧图像堆叠为一个观测
```

### C. 并行环境使用 (VectorEnv)
**来源**: `gymnasium/vector/async_vector_env.py`
**复用建议**: 适配 PPO 等需要大规模并行的算法，加速样本收集。
```python
vec_env = gym.vector.make("CartPole-v1", num_envs=4)
obs, infos = vec_env.reset()
```

## 3. 复用说明与修改点
*   **自定义环境开发**: 继承 `gymnasium.Env` 类，必须实现 `reset()` 和 `step()` 方法，并正确声明 `action_space` 和 `observation_space`。
*   **算法 Benchmark**: 利用 `gymnasium.make_vec` 快速切换不同难度的环境配置，验证算法的泛化能力。
*   **修改提示**: 在金融场景中，可将 `truncated` 逻辑设置为“每日收盘”，而 `terminated` 设置为“触发止损线”。
