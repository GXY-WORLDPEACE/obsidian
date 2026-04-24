---
title: "Recurrent Neural Network"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #rnn
type: concept
related_lectures:
  - 11
---

# Recurrent Neural Network (RNN) 循环神经网络

## 定义

RNN 是一类专门用于处理序列数据的神经网络，通过隐藏状态的循环连接处理任意长度的序列。

## 基本结构

```
h_t = f(W·x_t + U·h_{t-1} + b)
y_t = V·h_t
```

| 符号 | 说明 |
|------|------|
| x_t | t 时刻输入 |
| h_t | t 时刻隐藏状态 |
| y_t | t 时刻输出 |
| W, U, V | 权重矩阵 |

## 特点

| 特点 | 说明 |
|------|------|
| 权重共享 | 每个时间步用相同参数 |
| 任意长度 | 可处理变长序列 |
| 记忆能力 | 隐藏状态携带历史信息 |

## 问题

### 梯度消失/爆炸

| 问题 | 原因 | 影响 |
|------|------|------|
| 梯度消失 | λ^t → 0 | 难以学习长期依赖 |
| 梯度爆炸 | λ^t → ∞ | 训练不稳定 |

### 解决方案

| 方案 | 说明 |
|------|------|
| LSTM | 门控机制缓解 |
| GRU | 简化的门控机制 |
| Gradient Clipping | 裁剪梯度 |
| 残差连接 | ResNet 风格 |

## 应用

| 应用 | 说明 |
|------|------|
| 机器翻译 | 序列到序列 |
| 文本生成 | 字符/词预测 |
| 语音识别 | 音频到文本 |
| 时间序列 | 预测未来值 |

## 与 [[LSTM]] / [[Transformer]] 的关系

- LSTM 是 RNN 的变体，通过门控解决长期依赖
- Transformer 用注意力机制替代循环结构

## 相关概念

- [[LSTM]]
- [[Attention Mechanism]]
- [[Transformer]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
