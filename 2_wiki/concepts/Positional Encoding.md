---
title: "Positional Encoding"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #nlp
type: concept
related_lectures:
  - 11
---

# Positional Encoding 位置编码

## 定义

位置编码是一种将序列中元素位置信息注入到模型中的技术，使 Transformer 等并行模型能够感知token的顺序。

## 背景

Transformer 完全基于注意力机制，没有循环结构，无法天然感知位置信息。位置编码解决了这个问题。

## 方法

### 1. 三角函数编码 (Sinusoidal)

Transformer 原始论文使用：

```
PE(pos, 2i) = sin(pos / 10000^{2i/d})
PE(pos, 2i+1) = cos(pos / 10000^{2i/d})
```

| 参数 | 说明 |
|------|------|
| pos | token 位置 (0, 1, 2, ...) |
| i | 维度索引 (0 ~ d-1) |
| d | 模型维度 |

### 2. 可学习位置编码

将位置作为可学习的参数：
```
PE(pos) = Embedding(pos)
```

### 3. 旋转位置编码 (RoPE)

用于 LLaMA 等模型，通过旋转操作编码相对位置。

### 4. ALiBi (Attention with Linear Biases)

不添加位置编码，而是在线性注意力中添加位置偏差。

## 为什么用正弦/余弦？

- **周期性**：不同频率的正弦波捕获不同尺度的位置关系
- **相对位置**：可以容易地计算相对位置
  ```
  sin(a+b) = sin(a)cos(b) + cos(a)sin(b)
  ```

## 与注意力机制的关系

位置编码是 [[Transformer]] 的关键组件：
```
Input Embedding + Positional Encoding → Attention Layers
```

没有位置编码，Transformer 无法区分 "小狗咬人" 和 "人咬小狗"。

## 相关概念

- [[Attention Mechanism]]
- [[Transformer]]
- [[Recurrent Neural Network]]

## 来源

[[summaries/I2DL-Lecture-11-RNNs-Transformers]]
