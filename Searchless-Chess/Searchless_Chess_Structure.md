# Searchless Chess 项目结构与迭代逻辑

## 1. 目录结构与模块功能解析
*   `src/model/`: Transformer 模型定义，包含策略头（走法概率）与价值头（局面评估）的实现。
*   `src/encoding/`: 棋盘状态编码逻辑，负责将 FEN 字符串转换为 144 维的特征序列输入。
*   `src/inference/`: 纯模型推理流程，实现了从特征输入到合法走法过滤的端到端逻辑。
*   `src/train/`: 自对弈训练框架，涵盖数据生成、损失函数计算及权重更新循环。

## 2. 模块调用逻辑（无搜索决策流）
**完整流程链：**
`Board State (FEN)` → `fen_to_tensor()` (特征编码) → `Transformer.forward()` (前向传播) → `Policy Head` (输出所有可能走法评分) → `Legal Filter` (合法性校验) → `Argmax` (选择最优直觉走法)。

## 3. 迭代架构调整：ViT vs ResNet
*   **v1.0 阶段**: 采用 Vision Transformer (ViT) 架构。相比传统 ResNet，ViT 在处理棋盘全局依赖关系时表现出极高的参数效率（10倍以上）。
*   **v2.0 阶段**: 优化了位置编码（Positional Encoding）并增加了注意力头数。这种调整显著提升了模型在残局阶段的“大局观”，使其能更准确地识别长距离的子力配合。
