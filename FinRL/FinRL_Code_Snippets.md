# FinRL 核心代码片段与选股落地指南

## 1. A 股全市场数据拉取与因子计算 (CPU 优化)
**来源**: `examples/a_share_data_download.py`
**说明**: 适配 i5-10400，利用 `n_jobs=8` 并行加速。
```python
from finrl.meta.data_processors import DataProcessor

dp = DataProcessor(data_source='baostock', **kwargs)
# 批量计算 MACD, RSI, PE 等 15 个因子
df_with_indicators = dp.add_technical_indicator(df_raw, tech_indicator_list)
```

## 2. 多股票选股环境初始化 (复用 Gym Trading)
**来源**: `finrl/envs/multi_stock_env.py`
**说明**: 扩展了单股票逻辑，支持 100 只股票并行。
```python
env = StockTradingEnv(df=train_df, stock_dim=100, hmax=100, initial_amount=1000000)
# 复用点：观测空间依然由技术指标构成，动作空间为连续仓位控制
```

## 3. 对接 SB3 PPO 训练多因子选股策略 (CPU 适配)
**来源**: `finrl/agents/stablebaselines3/agent.py`
**说明**: 100% 复用 SB3 训练模板，仅修改环境。
```python
from stable_baselines3 import PPO

model = PPO("MlpPolicy", env, verbose=1, device='cpu', n_steps=2048)
model.learn(total_timesteps=100000)
model.save("finrl_ppo_selector")
```

## 4. 选股策略回测与成功率统计
**说明**: 输出选股成功率及盈亏比。
```python
# 自定义奖励函数：未来 3 天收益率 > 2% 算成功
def calculate_reward(self):
    future_return = self.get_future_return(days=3)
    return 1.0 if future_return > 0.02 else -1.0
```

## 5. 单只股票选股信号输出
**说明**: 输入代码，输出每日买卖信号。
```python
obs, _ = env.reset()
action, _ = model.predict(obs)
# 输出：Buy/Sell/Hold 信号及置信度
```
