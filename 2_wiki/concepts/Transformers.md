---
title: "Transformers"
date: 2026-04-16
aliases: ["Transformer", "注意力机制"]
tags:
  - #概念 #Transformer #NLP
  - #I2DL
---

# Transformers

## 革命性架构

2017年《Attention Is All You Need》论文提出了 Transformer 架构，完全基于**注意力机制**，摒弃了循环结构。

## 核心组件

| 组件 | 功能 |
|------|------|
| **Self-Attention** | 建立序列内部依赖关系 |
| **Multi-Head Attention** | 多角度捕捉特征 |
| **Positional Encoding** | 注入位置信息 |
| **Feed-Forward Network** | 逐位置非线性变换 |

## 关键公式

### Scaled Dot-Product Attention

```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

### Multi-Head Attention

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
where head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
```

## 经典模型

| 模型 | 机构 | 特点 |
|------|------|------|
| BERT | Google | 双向编码器，预训练+微调 |
| GPT | OpenAI | 单向解码器，生成式 |
| T5 | Google | Encoder-Decoder 统一框架 |
| LLaMA | Meta | 开源大语言模型 |

## 优势 vs RNN

| 方面 | Transformer | RNN |
|------|-------------|-----|
| 并行化 | ✅ 完全并行 | ❌ 顺序处理 |
| 长距离依赖 | ✅ 直接连接 | ❌ 逐步传播 |
| 梯度流动 | ✅ 无障碍 | ❌ 可能消失 |

## 应用场景

- 语言模型 / 文本生成
- 机器翻译
- 图像生成 (ViT, Diffusion)
- 多模态模型

## 相关概念

- [[Deep Learning]] - 深度学习
- [[Neural Networks]] - 神经网络
- [[Recurrent Neural Networks]] - RNN (前世)

## 课程来源

- [[summaries/I2DL-Lecture-1-Introduction]]