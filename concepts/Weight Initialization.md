---
title: "Weight Initialization"
date: 2026-06-03
tags:
  - #概念 #深度学习
---

# Weight Initialization (权重初始化)

## 为什么重要？

- 影响梯度传播
- 影响训练稳定性
- 影响收敛速度

## 常见问题

### 常数初始化
所有权重相同 → 破坏对称性 → 所有神经元学相同特征 ❌

### 随机大值
$W \sim N(0, 0.2^2)$ → 激活饱和 → 梯度消失 ❌

### 随机小值
$W \sim N(0, 0.01^2)$ → 梯度消失 ❌

## 初始化方法

| 方法 | 适用激活函数 | 公式 |
|------|-------------|------|
| Xavier (Glorot) | Tanh, Sigmoid | $\sqrt{\frac{2}{fan_{in} + fan_{out}}}$ |
| He (Kaiming) | ReLU | $\sqrt{\frac{2}{fan_{in}}}$ |

## PyTorch 实现

```python
# Xavier
nn.init.xavier_normal_(layer.weight)

# He
nn.init.kaiming_uniform