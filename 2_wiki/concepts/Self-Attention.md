---
title: "Self-Attention"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #attention
type: concept
related_lectures:
  - 11
---

# Self-Attention 自注意力

## 定义

自注意力是一种注意力机制，Query、Key、Value 都来自同一序列，使序列内部每个元素都能关注到其他所有元素。

## 与普通注意力的区别

| 类型 | Q 来源 | K/V 来源 |
|------|--------|----------|
| 普通注意力 | 一个序列 | 另一个序列 |
| **自注意力** | **同一序列** | **同一序列** |

## 数学表示

```
Self-Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V

其中 Q = XW_Q, K = XW_K, V = XW_V
```

## 核心特性

| 特性 | 说明 |
|------|------|
| 全局依赖 | 每个位置可直接关注任意位置 |
| 并行计算 | 无循环依赖 |
| 位置感知 | 需配合 [[Positional Encoding]] |

## 计算过程

```
输入序列 X = [x₁, x₂, ..., xₙ]
    ↓ 线性投影
Q = XW_Q, K = XW_K, V = XW_V
    ↓
计算注意力权重
    ↓
加权求和得到输出
```

## 与 [[Attention Mechanism]] 的关系

Self-Attention 是 [[Attention Mechanism]] 的一种具体形式，也是 [[Transformer]] 的核心组件。

```
Transformer Encoder = Self-Attention + FFN
```

## 与 [[Multi-Head Attention]] 的关系

Multi-Head Attention 是多个 Self-Attention 的并行组合：
```
MultiHead = Concat(Head₁, Head₂, ..., Headₕ) · W⁰
Headᵢ = SelfAttention(XWᵢQ, XWᵢK, XWᵢV)
```

## 相关概念

- [[Attention Mechanism]]
- [[Multi-Head Attention]]
- [[Transformer]]
- [[Positional Encoding]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
