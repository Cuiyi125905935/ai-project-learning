# OpenAI Gym Trading 核心代码片段与选股落地指南

## 1. 基础选股环境初始化 (CPU 适配)
**来源**: `examples/stocks_basic.py`
**说明**: 适配 i5-10400，无 GPU 依赖。
```python
import gymnasium as gym
import gym_anytrading

env = gym.make('stocks-v0', frame_bound=(50, 1000), window_size=10)
observation, info = env.reset()
# 修改点：调整 frame_bound 可改变训练数据的时间跨度
```

## 2. 对接 Stable-Baselines3 PPO 训练 (CPU 优化)
**说明**: 针对 4 核 8 线程优化，设置 `n_envs=4` 并行采样。
```python
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

def make_env():
    return gym.make('stocks-v0', frame_bound=(50, 1000), window_size=10)

env = DummyVecEnv([make_env for _ in range(4)]) # CPU 并行加速
model = PPO("MlpPolicy", env, verbose=1, device='cpu')
model.learn(total_timesteps=50000)
model.save("ppo_stock_selector")
```

## 3. A 股历史数据对接 (免费接口)
**说明**: 使用 baostock 拉取数据并清洗。
```python
import baostock as bs
import pandas as pd

lg = bs.login()
rs = bs.query_history_k_data_plus("sh.600000", "date,open,high,low,close,volume", start_date='2015-01-01')
data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
df = pd.DataFrame(data_list, columns=rs.fields)
# 修改点：更改 code 参数即可切换目标股票
```

## 4. 自定义选股奖励函数 (成功率导向)
**说明**: 优先优化选股成功率而非单纯收益率。
```python
def calculate_reward(self):
    # 如果未来 3 天收益率 > 2%，给予正奖励
    future_return = (self.prices[self._current_idx + 3] - self.current_price) / self.current_price
    return 1.0 if future_return > 0.02 else -1.0
```

## 5. 选股策略回测与结果输出
**说明**: 生成文字版回测报告，包含最大回撤与盈亏比。
```python
# 加载模型并进行单步推理
obs, _ = env.reset()
action, _ = model.predict(obs)
# 输出：选股信号 (Buy/Sell/Hold) 及对应的预期置信度
```
