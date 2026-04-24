---
title: "Multi-Head Attention"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #attention
type: concept
related_lectures:
  - 11
---

# Multi-Head Attention 多头注意力

## 定义

多头注意力通过并行运行多个独立的注意力机制，使模型能够在不同子空间学习不同类型的依赖关系。

## 数学表示

```
MultiHead(Q, K, V) = Concat(head₁, head₂, ..., headₕ) · W⁰

headᵢ = Attention(QWᵢQ, KWᵢK, VWᵢV)
       = softmax(QWᵢQ · (KWᵢK)ᵀ / √d_k) · VWᵢV
```

| 参数 | 说明 |
|------|------|
| h | 注意力头数量 |
| d_k | 每个头的维度 = d_model / h |
| W⁰ | 输出投影矩阵 |

## 架构图

```
Q ──┬──→ W₁Q ──→ Head₁ ──┐
     ├──→ W₂Q ──→ Head₂ ──┼──→ Concat ──→ W⁰ → Output
K ──┬──→ W₁K ──→ ...    ──┤
     ├──→ W₂K ──→ ...    ──┤
V ──┬──→ W₁V ──→ ...    ──┘
     ├──→ W₂V ──→ ...
```

## 核心优势

| 优势 | 说明 |
|------|------|
| 多子空间 | 每个头学习不同的注意力模式 |
| 稳定训练 | 降低单注意力的方差 |
| 捕获多种关系 | 如语法、语义、位置等 |

## 典型配置

| 模型 | d_model | h | d_k |
|------|---------|---|-----|
| Transformer 原始 | 512 | 8 | 64 |
| BERT-Large | 1024 | 16 | 64 |
| GPT-3 | 12288 | 96 | 128 |

## 与 [[Self-Attention]] 的关系

Multi-Head Attention 是多个 [[Self-Attention]] 的并行组合：

```
Multi-Head = [Self-Attention] × h_heads
```

## 与 [[Attention Mechanism]] 的关系

Multi-Head Attention 是 [[Attention Mechanism]] 的增强版本，通过多头扩展表达能力。

## 应用

| 应用 | 说明 |
|------|------|
| Transformer Encoder | 全部使用 Self-Attention |
| Transformer Decoder | Masked Self-Attention + Cross-Attention |
| Vision Transformer | 图像patch间的自注意力 |
| Perceiver IO | 多模态多头的通用架构 |

## 相关概念

- [[Self-Attention]]
- [[Attention Mechanism]]
- [[Transformer]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
