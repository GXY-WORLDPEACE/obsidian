---
title: "Attention Mechanism"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #attention
type: concept
related_lectures:
  - 11
---

# Attention Mechanism 注意力机制

## 定义

注意力机制是一种让模型能够"关注"输入中最相关部分的技术，模仿人类视觉的选择性注意能力。

## 核心思想

```
Query (查询) → 与所有 Key 计算相似度 → softmax → 加权 Value
```

## 数学表示

### Scaled Dot-Product Attention

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

| 组件 | 含义 |
|------|------|
| Q (Query) | 当前要查询的内容 |
| K (Key) | 被查询内容的特征 |
| V (Value) | 被查询的实际内容 |
| d_k | Key 的维度（缩放因子） |

### 注意力权重

```
αᵢ = softmax(score(q, kᵢ)) = exp(score) / Σexp(score)
```

## 注意力类型

### 1. Self-Attention (自注意力)

Query, Key, Value 来自同一序列：
```
Attention(X, X, X)
```

### 2. Cross-Attention (交叉注意力)

Query 来自一个序列，K/V 来自另一个：
```
Attention(Q_decoder, K_encoder, V_encoder)
```

### 3. Multi-Head Attention

并行运行多个注意力：
```
MultiHead(Q, K, V) = Concat(head₁,...,headₕ)W⁰

headᵢ = Attention(QWᵢQ, KWᵢK, VWᵢV)
```

## 应用场景

| 场景 | 应用 |
|------|------|
| NLP | Transformer, BERT, GPT |
| Vision | ViT, DETR |
| Multimodal | CLIP, DALL-E |
| Speech | Whisper |

## 与 RNN 对比

| 特性 | RNN | Attention |
|------|-----|-----------|
| 长距离依赖 | 梯度消失 | 直接连接 |
| 计算复杂度 | O(n) | O(n²) |
| 并行化 | 差 | 好 |
| 可解释性 | 一般 | 好（权重可视化） |

## PyTorch 实现

```python
import torch
import torch.nn.functional as F
import math

def attention(query, key, value, mask=None):
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, value), weights
```

## 相关概念

- [[Transformer]]
- [[Positional Encoding]]
- [[Self-Attention]]
- [[Multi-Head Attention]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
