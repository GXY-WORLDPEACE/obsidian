---
title: "Backpropagation Through Time (BPTT)"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #rnn
type: concept
related_lectures:
  - 11
---

# Backpropagation Through Time (BPTT)

## 定义

BPTT 是 RNN 的反向传播算法，通过时间步展开 RNN，然后应用标准反向传播。

## 展开 RNN

```
h_t = f(W·x_t + U·h_{t-1} + b)

展开后：
h_0 → h_1 → h_2 → ... → h_T
x_0   x_1   x_2       x_T
```

## 步骤

1. **前向传播**：按时间步计算所有隐藏状态
2. **计算损失**：在最后一个时间步计算 L
3. **反向传播**：从 T 到 0 逐层回传梯度

## 梯度计算

```
∂L/∂W = Σ_{t=0}^T ∂L/∂h_t · ∂h_t/∂W
```

每层依赖前面的时间步。

## 问题：梯度消失/爆炸

| 问题 | 原因 | 表现 |
|------|------|------|
| 梯度消失 | λ^t (λ<1) | 长期依赖丢失 |
| 梯度爆炸 | λ^t (λ>1) | 数值不稳定 |

## 解决方案

| 方法 | 说明 |
|------|------|
| [[LSTM]] | 门控机制保留长期信息 |
| Gradient Clipping | 限制梯度范围 |
| 截断 BPTT | 只回传固定步数 |

## 与 [[Backpropagation]] 的关系

BPTT 是 [[Backpropagation]] 在时间维度上的扩展，处理序列数据的特殊需求。

## 相关概念

- [[Backpropagation]]
- [[Recurrent Neural Network]]
- [[LSTM]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
