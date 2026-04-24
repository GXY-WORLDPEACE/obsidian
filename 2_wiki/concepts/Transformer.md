---
title: "Transformer"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #nlp
  - #attention
type: concept
related_lectures:
  - 11
---

# Transformer

## 定义

Transformer是一种基于自注意力机制的神经网络架构，完全摒弃了循环结构，通过并行计算大幅提升了训练效率。

## 核心架构

```
Input → Embedding → Positional Encoding → Encoder/Decoder Blocks → Output
```

### Encoder

```
Input Embedding + Positional Encoding
    ↓
Multi-Head Self-Attention
    ↓
Add & LayerNorm
    ↓
Feed Forward Network
    ↓
Add & LayerNorm
    ↓
... (重复N次)
```

### Decoder

```
Output Embedding + Positional Encoding
    ↓
Masked Multi-Head Self-Attention
    ↓
Add & LayerNorm
    ↓
Cross-Attention (Query from Decoder, Key/Value from Encoder)
    ↓
Add & LayerNorm
    ↓
Feed Forward Network
    ↓
Add & LayerNorm
    ↓
... (重复N次)
```

## 注意力机制

### Scaled Dot-Product Attention

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

其中 $d_k$ 是 key 的维度，用于缩放防止点积过大。

### Multi-Head Attention

```
MultiHead(Q, K, V) = Concat(head₁, ..., headₕ) · W⁰

headᵢ = Attention(QWᵢQ, KWᵢK, VWᵢV)
```

常用配置：h=8 个注意力头，$d_k = d_{model}/h$

## 位置编码 (Positional Encoding)

使用正弦/余弦函数编码位置信息：

```
PE(pos, 2i) = sin(pos / 10000^{2i/d})
PE(pos, 2i+1) = cos(pos / 10000^{2i/d})
```

## 关键创新

| 特性 | 说明 |
|------|------|
| 并行化 | 无循环依赖，可并行训练 |
| 长距离依赖 | 自注意力直接计算任意位置关系 |
| 可解释性 | 注意力权重可视化 |

## 经典模型

| 模型 | 应用 | 特点 |
|------|------|------|
| BERT | NLP理解 | Encoder-only, MLM预训练 |
| GPT | NLP生成 | Decoder-only, Next-token预测 |
| ViT | 图像分类 | 将图像视为token序列 |
| DALL-E | 图生文/文生图 | CLIP + Diffusion |

## 与 RNN/LSTM 对比

| 特性 | RNN/LSTM | Transformer |
|------|----------|-------------|
| 复杂度 | O(n·d) | O(n²·d) |
| 长距离依赖 | 弱（梯度消失） | 强（直接连接） |
| 并行化 | 差 | 好 |
| 内存 | 低 | 高 |

## 相关概念

- [[Attention Mechanism]]
- [[Positional Encoding]]
- [[Recurrent Neural Network]]
- [[LSTM]]
- [[Transfer Learning]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
