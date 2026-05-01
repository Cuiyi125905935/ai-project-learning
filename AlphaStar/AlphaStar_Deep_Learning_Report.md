# AlphaStar 深度学习报告

## 1. 版本迭代时间线
*   **2019.01 (Nature Paper)**: DeepMind 正式发布 AlphaStar，首次展示在《星际争霸 II》中达到 Grandmaster 级别。
*   **2019.04 (Open Source)**: DeepMind 开源了 StarCraft II Learning Environment (SC2LE) 及部分核心逻辑。
*   **2020-Present**: 社区衍生出多个分支（如 TStarBot-X），重点优化了多智能体协作和训练效率。

## 2. 模型架构演进路线
AlphaStar 的核心是一个复杂的 **Transformer-based Sequence Model**：
1.  **输入编码 (Input Encoding)**: 将游戏状态（单位位置、资源、科技树）转化为向量序列。
2.  **核心网络 (Core Network)**: 使用多层 Transformer 编码器捕捉长距离依赖关系。
3.  **多头输出 (Multi-Head Output)**: 
    *   **Policy Head**: 预测下一个动作的概率分布。
    *   **Value Head**: 评估当前局面的胜率。
    *   **Baseline Head**: 用于减少强化学习中的方差。

## 3. 关键性能优化 PR 分析
*   **PR #1: Autoregressive Policy Decomposition**: 将复杂的动作空间分解为“选择单位 -> 选择动作 -> 选择目标”的串行过程，显著降低了搜索难度。
*   **PR #2: Feature Engineering for Unit Attributes**: 引入了更精细的单位属性嵌入（Embedding），使模型能更好地区分不同兵种的特性。
*   **PR #3: Distributed Training Framework**: 实现了基于 Actor-Learner 的分布式架构，支持数千个 CPU 核心并行采集数据。

## 4. 训练稳定性解决方案汇总
*   **Entropy Regularization**: 在损失函数中加入熵正则项，防止策略过早收敛到局部最优。
*   **Importance Sampling**: 在处理离线数据时，使用重要性采样修正分布偏差。
*   **Gradient Clipping**: 限制梯度范数，防止 Transformer 深层网络出现梯度爆炸。

## 5. 上影线量化适配点
*   **多特征均衡**: 借鉴其 Input Encoding 思路，为 `SYX0`、`量比` 等特征建立独立的 Embedding 层。
*   **辅助任务**: 引入波动率预测作为辅助头，增强模型对市场情绪的感知。
