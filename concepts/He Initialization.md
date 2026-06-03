---
title: "He Initialization"
date: 2026-06-03
tags:
  - #概念 #权重初始化
---

# He Initialization (Kaiming 初始化)

## 提出者

Kaiming He 等 (2015)，专为 ReLU 设计。

## 公式

从分布 $\mathcal{N}(0, \sigma^2)$ 采样，其中：

$$ \sigma = \frac{gain}{\sqrt{fan_{mode}}} $$

## 与 Xavier 的区别

| 方法 | 分母 | 适用激活函数 |
|------|------|-------------|
| Xavier | $\sqrt{fan_{in} + fan_{out}}$ | Tanh, Sigmoid |
| He | $\sqrt{fan_{in}}$ | ReLU |

## 为什么 ReLU 需要不同初始化？

ReLU 将负值置零，导致一半神经元失活，需要更大的初始方差来补偿。

## PyTorch 实现

```python
import torch.nn as nn

# Kaiming 均匀分布
nn.init.kaiming_uniform_(layer.weight, nonlinearity='relu')

# Kaiming 正态分布
nn.init.kaiming_normal_(layer.weight, nonlinearity='relu')
```

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_07/1_pytorch-summary.md]]
