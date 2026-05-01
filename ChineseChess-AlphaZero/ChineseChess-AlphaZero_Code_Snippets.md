# ChineseChess-AlphaZero 核心代码片段与复用指南

## 1. 棋盘状态表示 (Board Representation)
**来源**: `cchess_alphazero/environment/chessboard.py`
**功能解析**: 使用 14x10x9 的三维张量表示棋盘。其中 14 个通道分别代表红黑双方的不同兵种（车、马、炮等）及其位置信息。
**复用建议**: 这种多维平面表示法非常适合卷积神经网络（CNN）处理，可直接迁移至其他棋类或网格状博弈环境。

```python
# 简化的状态编码逻辑
def encode_board(board):
    state = np.zeros((14, 10, 9))
    for x in range(9):
        for y in range(10):
            piece = board[y][x]
            if piece:
                # 根据棋子类型和颜色填充对应的通道
                channel = get_channel(piece.type, piece.color)
                state[channel][y][x] = 1
    return state
```

## 2. MCTS 核心实现 (UCT Algorithm)
**来源**: `cchess_alphazero/agent/player.py`
**功能解析**: 实现了 Upper Confidence Bound (UCT) 算法来平衡探索与利用。
**代码片段**:
```python
# UCT 评分公式实现
def select_child(self, node):
    return max(node.children.items(), 
               key=lambda item: item[1].value + self.c_puct * item[1].prior * 
               sqrt(node.visit_count) / (1 + item[1].visit_count))
```
**复用建议**: 该逻辑是通用决策核心，调整 `c_puct` 参数可控制模型在“尝试新走法”与“坚持已知最优”之间的倾向。

## 3. 神经网络模型定义 (ResNet Architecture)
**来源**: `cchess_alphazero/agent/model.py`
**功能解析**: 采用残差网络结构，包含一个输入卷积层、多个残差块以及策略头（Policy Head）和价值头（Value Head）。
**复用建议**: 双头设计是本项目的精髓。策略头输出走法概率分布，价值头输出当前局面的胜率评估，这种多任务学习架构可广泛应用于复杂决策系统。

## 4. 训练流程关键逻辑 (Self-Play Loop)
**来源**: `cchess_alphazero/manager.py`
**功能解析**: 循环执行“自对弈生成数据 -> 采样训练 -> 模型评估 -> 更新最佳模型”的流程。
**复用建议**: 这种闭环训练机制确保了模型能持续从最新的状态中汲取经验，是实现强化学习进化的关键。
