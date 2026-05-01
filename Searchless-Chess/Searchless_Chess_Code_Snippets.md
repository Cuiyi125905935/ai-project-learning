# Searchless Chess 核心代码片段与复用指南

## 1. 棋盘状态编码 (Board Encoding)
**来源**: `src/data_preparation/data_processing.py`
**功能解析**: 将 FEN 字符串转换为模型可处理的张量。这种编码方式捕捉了棋子位置、颜色及移动权（Castling rights）。
**复用建议**: 该逻辑可直接迁移至其他基于网格的博弈环境（如围棋、将棋）的特征工程开发中。

```python
def fen_to_tensor(fen: str, always_white_perspective=True) -> np.ndarray:
    # 14x8x8 的三维张量，分别代表不同兵种的平面
    board = chess.Board(fen)
    tensor = np.zeros((14, 8, 8), dtype=np.float32)
    # ... (填充棋子位置逻辑)
    return tensor.flatten()
```

## 2. Transformer 走法预测模型 (Searchless Transformer)
**来源**: `src/chess_ai/core/model.py`
**功能解析**: 利用 Keras/TensorFlow 实现的端到端评估模型。它不输出单一走法，而是对所有合法后续局面进行批量评分。
**复用建议**: 在量化交易中，可借鉴其“批量评估候选动作”的思路，对多个交易信号进行并行打分。

```python
class ChessAI:
    def make_move(self, board: Board) -> Optional[Move]:
        legal_moves = list(board.legal_moves)
        # 批量生成所有合法走法的下一局面特征
        input_tensors = [fen_to_tensor(board.copy().push(m).fen()) for m in legal_moves]
        # 纯神经网络直觉评分
        evaluations = self.model(np.array(input_tensors), training=False)
        return legal_moves[np.argmin(evaluations)]
```

## 3. 无搜索推理完整流程 (Inference Pipeline)
**来源**: `src/inference/predict.py`
**功能解析**: 实现了从输入到输出的零延迟决策。由于没有 MCTS 搜索过程，其推理速度极快。
**复用场景**: 适用于对实时性要求极高的在线博弈系统或高频交易策略原型验证。

## 4. 自对弈训练核心循环 (Self-Play Loop)
**来源**: `src/train/trainer.py`
**功能解析**: 通过不断生成新数据并微调模型，实现 ELO 评分的持续爬升。
**修改点**: 可根据硬件资源调整 `batch_size` 和学习率调度策略（Learning Rate Schedule）。
