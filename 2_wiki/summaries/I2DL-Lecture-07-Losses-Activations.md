---
title: "I2DL Lecture 7 - Loss Functions and Activations"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #loss-functions
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/7.losses_and_activations.pdf
---

# I2DL Lecture 7: 损失函数与激活函数

## 摘要

本讲系统介绍各种损失函数（回归、分类）和激活函数，重点对比交叉熵与Hinge损失，分析不同激活函数的优缺点。

## 核心内容

### 1. 回归损失

**L1 Loss**: L1 = Σ|y_i - f(x_i)|
- 对异常值鲁棒
- 梯度恒定

**L2 Loss (MSE)**: L2 = Σ(y_i - f(x_i))²
- 对异常值敏感
- 优化计算简单

### 2. 二分类损失

**Sigmoid**: σ(s) = 1/(1 + e^(-s))
- 输出 ∈ (0,1)，可解释为概率

**Binary Cross-Entropy**:
L = -[y·log(ŷ) + (1-y)·log(1-ŷ)]

### 3. 多分类损失

**Softmax**: 
p(y=k|x) = e^(s_k) / Σ e^(s_j)

**Cross-Entropy Loss**:
L = -log(e^(s_y) / Σe^(s_k))

数值稳定形式：
L = -s_y + log(Σe^(s_k - s_max))

### 4. Hinge Loss (SVM)

L_i = Σ_{k≠y_i} max(0, s_k - s_{y_i} + 1)

特点：
- 边界感知
- 不像CE那样一直想改进

### 5. Cross-Entropy vs Hinge

| 特性 | Cross-Entropy | Hinge |
|------|---------------|-------|
| 优化 | 持续改进 | 可能饱和 |
| 概率输出 | 天然支持 | 不支持 |
| 泛化 | 通常更好 | 边界清晰 |

### 6. 激活函数详解

**Sigmoid** σ(x) = 1/(1+e^(-x))
- 优点: 平滑，可导，输出概率
- 缺点: 梯度饱和（x→±∞时，梯度→0），非零中心输出

**Tanh** tanh(x)
- 优点: 零中心输出
- 缺点: 仍有梯度饱和问题

**ReLU** max(0, x)
- 优点: 计算快，梯度不衰减，不会饱和
- 缺点: 负区间神经元"死亡"

**Leaky ReLU** max(0.1x, x)
- 解决ReLU死神经元问题
- α=0.01 或可学习

**ELU** f(x) = x if x>0, α(e^x-1) if x≤0
- 平滑负值输出
- 收敛更快

### 7. 激活函数选择建议

```
隐藏层: ReLU (首选)
         Leaky ReLU / ELU (替代)
输出层: Sigmoid (二分类)
         Softmax (多分类)
         恒等 (回归)
```

### 8. 损失函数计算图

```
完整损失 = 数据损失 + 正则损失
         = CE Loss + λ·L2_reg
```

反向传播同时更新所有参数。

## 相关概念

- [[concepts/Loss Function]]
- [[concepts/Cross Entropy]]
- [[concepts/Softmax]]
- [[concepts/Hinge Loss]]
- [[concepts/Activation Function]]
- [[concepts/ReLU]]

## 来源

[[1_raw/articles/I2DL/lectures/7.losses_and_activations.pdf]]