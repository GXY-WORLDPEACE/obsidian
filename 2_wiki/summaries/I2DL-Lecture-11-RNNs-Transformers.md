---
title: "I2DL L11: RNNs and Transformers"
date: 2026-04-16
tags:
  - #I2DL #讲义 #RNN #Transformer #序列模型
course: I2DL
lecture: 11
---

# I2DL Lecture 11: RNNs and Transformers

## 摘要
本讲覆盖序列建模的两大范式：循环神经网络(RNN)及其变体(LSTM/GRU)，以及革命性的 Transformer 架构。

## 循环神经网络 (RNN)

### 标准 RNN
$$h_t = \tanh(W_{hh}h_{t-1} + W_{xh}x_t + b)$$

问题：长期依赖困难、梯度消失/爆炸。

### LSTM (Long Short-Term Memory)
门控机制：
- **遗忘门** $f_t = \sigma(W_f \cdot [h_{t-1}, x_t])$
- **输入门** $i_t = \sigma(W_i \cdot [h_{t-1}, x_t])$
- **输出门** $o_t = \sigma(W_o \cdot [h_{t-1}, x_t])$

解决长期依赖问题。

### GRU (Gated Recurrent Unit)
简化版 LSTM，只有更新门和重置门。

## Transformer

### 核心机制：自注意力 (Self-Attention)
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

并行计算，捕获任意位置依赖。

### Transformer 架构
```
输入 → 位置编码 → [编码器层 × N] → 输出
                           ↓
编码器层: Multi-Head Attention → Add & Norm → Feed Forward → Add & Norm

解码器层: Masked MHA → Cross Attention → FFN
```

### 关键组件
| 组件 | 说明 |
|------|------|
| **Positional Encoding** | 注入位置信息 |
| **Multi-Head Attention** | 多角度关注 |
| **Layer Norm** | 稳定训练 |
| **Feed Forward** | 非线性变换 |

## RNN vs Transformer
| 维度 | RNN | Transformer |
|------|-----|-------------|
| 并行性 | 低（时序依赖） | 高（可并行） |
| 长距离依赖 | 困难 | 容易（O(1) 路径） |
| 计算复杂度 | O(n) | O(n²) 注意力 |
| 内存 | 低 | 高 |

## 关键概念
- Hidden State
- Gated Recurrence
- Self-Attention
- Positional Encoding

## 概念关联
- [[2_wiki/concepts/Recurrent Neural Networks]] - RNN 概念
- [[2_wiki/concepts/Transformers]] - Transformer 概念
- [[2_wiki/summaries/I2DL-Lecture-10-Architectures]] - 注意力机制基础

## 来源
[[1_raw/articles/I2DL/lectures/11.rnns_and_transformers.pdf]]
