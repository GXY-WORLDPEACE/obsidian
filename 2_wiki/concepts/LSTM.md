---
title: "LSTM (Long Short-Term Memory)"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #rnn
type: concept
related_lectures:
  - 11
---

# LSTM (Long Short-Term Memory) 长短期记忆网络

## 定义

LSTM是一种特殊的RNN变体，通过引入门控机制解决标准RNN的长期依赖问题（梯度消失/爆炸）。

## 核心创新

### 细胞状态 (Cell State)

细胞状态作为"信息高速公路"，允许信息在各时间步间流动而不易衰减：
```
C_t = C_{t-1} + candidate values controlled by gates
```

## 门机制

| 门 | 公式 | 作用 |
|-----|------|------|
| **遗忘门** f_t | σ(W_f·[h_{t-1}, x_t] + b_f) | 决定丢弃什么信息 |
| **输入门** i_t | σ(W_i·[h_{t-1}, x_t] + b_i) | 决定更新什么信息 |
| **输出门** o_t | σ(W_o·[h_{t-1}, x_t] + b_o) | 决定输出什么信息 |

### 完整计算

```
候选记忆: g_t = tanh(W_g·[h_{t-1}, x_t] + b_g)

遗忘: C_t = f_t ⊙ C_{t-1}
输入: C_t = C_t + i_t ⊙ g_t
输出: h_t = o_t ⊙ tanh(C_t)
```

## 与标准 RNN 对比

| 特性 | 标准 RNN | LSTM |
|------|----------|------|
| 梯度流动 | 易消失/爆炸 | 通过细胞状态 |
| 长期依赖 | 难以学习 | 可学习 |
| 参数量 | 少 | 多（约4倍） |
| 训练难度 | 一般 | 较难 |

## 变体

### GRU (Gated Recurrent Unit)

简化版本，两个门：
```
z_t = σ(W_z·[h_{t-1}, x_t])      # 更新门
r_t = σ(W_r·[h_{t-1}, x_t])      # 重置门
h_t = (1-z_t)⊙h_{t-1} + z_t⊙tanh(W·[r_t⊙h_{t-1}, x_t])
```

## PyTorch 实现

```python
import torch.nn as nn

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
    
    def forward(self, x):
        # x: (batch, seq_len, input_size)
        output, (h_n, c_n) = self.lstm(x)
        return output, h_n, c_n
```

## 应用

| 应用 | 说明 |
|------|------|
| 机器翻译 | 序列到序列 |
| 语音识别 | 音频到文本 |
| 文本生成 | 字符/词预测 |
| 时间序列 | 预测未来值 |

## 相关概念

- [[Recurrent Neural Network]]
- [[Attention Mechanism]]
- [[Transformer]]
- [[Backpropagation Through Time]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
