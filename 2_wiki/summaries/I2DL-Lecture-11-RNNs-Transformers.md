---
title: "I2DL Lecture 11 - RNNs and Transformers"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #rnn
  - #transformer
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/11.rnns_and_transformers.pdf
---

# I2DL Lecture 11: RNN 与 Transformer

## 摘要

本讲介绍处理序列数据的神经网络，从循环神经网络（RNN）开始，分析其梯度消失问题，然后介绍 LSTM 和 Transformer 架构。重点讲解注意力机制和 Transformer 的自注意力机制。

## 核心内容

### 1. 迁移学习

**何时使用**:
- 任务间输入相同（如 RGB 图像）
- 源任务数据量大于目标任务
- 低层特征可迁移

**策略**:
- 小数据集: 冻结特征提取器
- 大数据集: 微调更多层

### 2. RNN 基本结构

```
h_t = f(W·x_t + U·h_{t-1} + b)
y_t = V·h_t
```

**特点**:
- 权重共享（每个时间步用相同参数）
- 可处理任意长度序列

### 3. RNN 应用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 图像描述 | 图像 | 文本序列 |
| 语音识别 | 音频 | 文本序列 |
| 机器翻译 | 源语言文本 | 目标语言文本 |
| 情感分类 | 文本 | 情感标签 |

### 4. 长期依赖问题

**问题**: 简单 RNN 难以学习长距离依赖

**原因**:
- 梯度消失: |λ| < 1 时，λ^t → 0
- 梯度爆炸: |λ| > 1 时，λ^t → ∞

### 5. LSTM (Long Short-Term Memory)

**核心思想**: 引入细胞状态（cell state）作为信息高速公路

**门机制**:
| 门 | 公式 | 作用 |
|-----|------|------|
| 遗忘门 f_t | σ(W_f·[h_{t-1}, x_t]) | 决定丢弃什么 |
| 输入门 i_t | σ(W_i·[h_{t-1}, x_t]) | 决定更新什么 |
| 输出门 o_t | σ(W_o·[h_{t-1}, x_t]) | 决定输出什么 |

**细胞更新**:
```
C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t
h_t = o_t ⊙ tanh(C_t)
```

### 6. 注意力机制

**核心思想**: 允许模型关注输入的任意部分

**架构**:
```
Query (Q) → 与所有 Key 计算相似度 → softmax → 加权 Value
```

### 7. Transformer

**架构**:
- Encoder: 多头自注意力 + 前馈网络
- Decoder: 掩码多头注意力 + 交叉注意力

**公式**:
```
Attention(Q, K, V) = softmax(QK^T / √d_k) · V
```

### 8. 位置编码

使用正弦/余弦函数编码位置信息：

```
PE(pos, 2i) = sin(pos / 10000^{2i/d})
PE(pos, 2i+1) = cos(pos / 10000^{2i/d})
```

### 9. CNN vs Transformer

| 特性 | CNN | Transformer |
|------|-----|-------------|
| 复杂度 | O(n·k·d) | O(n²·d) |
| 适用场景 | 局部特征 | 全局依赖 |
| 位置感知 | 隐式 | 需位置编码 |

## 相关概念

- [[concepts/Recurrent Neural Network]]
- [[concepts/LSTM]]
- [[concepts/Attention Mechanism]]
- [[concepts/Transformer]]
- [[concepts/Transfer Learning]]
- [[concepts/Positional Encoding]]

## 来源

[[1_raw/articles/I2DL/lectures/11.rnns_and_transformers.pdf]]