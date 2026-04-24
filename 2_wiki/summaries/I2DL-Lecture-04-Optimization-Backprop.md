---
title: "I2DL Lecture 4 - Optimization and Backpropagation"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #optimization
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/4.optimization_and_backprop.pdf
---

# I2DL Lecture 4: 优化与反向传播

## 摘要

本讲深入讲解反向传播算法的数学原理和实现细节，介绍梯度下降的变种，以及正则化技术防止过拟合。

## 核心内容

### 1. 反向传播（Backpropagation）

**核心思想**: 利用链式法则，从输出层向输入层逐层计算梯度。

**简单示例**:
```
f(x,y,z) = x + y·z

前向: d = y·z, f = x + d
反向: ∂f/∂f = 1
      ∂f/∂z = ∂f/∂d · ∂d/∂z = z
      ∂f/∂y = ∂f/∂d · ∂d/∂y = z
      ∂f/∂x = ∂f/∂d · ∂d/∂x = 1
```

### 2. 链式法则

∂L/∂w = ∂L/∂ŷ · ∂ŷ/∂a · ∂a/∂w

通过计算图中的每条边传播梯度。

### 3. 梯度下降

```
x_{t+1} = x_t - α · ∇f(x_t)
```

- **学习率 α**: 步长，太大震荡，太小慢
- **收敛**: 无保证全局最优（神经网络非凸）

### 4. 优化器对比

| 优化器 | 更新规则 | 特点 |
|--------|----------|------|
| **SGD** | θ_{t+1} = θ_t - α·∇L | 简单，可能震荡 |
| **Momentum** | v_{t+1} = β·v_t - α·∇L | 加速，收敛更稳 |
| **RMSProp** | s_{t+1} = β·s_t + (1-β)·(∇L)² | 自适应学习率 |
| **Adam** | 结合Momentum+RMSProp | 目前最常用 |

### 5. 正则化

**目的**: 防止过拟合，提高泛化能力

**L2正则化**: L = L_data + λ·Σw²
- 惩罚大权重，使权重均匀分布
- 也称权重衰减 (Weight Decay)

**L1正则化**: L = L_data + λ·Σ|w|
- 产生稀疏解（部分权重为0）
- 用于特征选择

### 6. 正则化效果

```
L1: 关注少数关键特征（稀疏解）
L2: 使用所有特征（平滑解）
```

### 7. 神经网络正则化

在计算图中加入正则项：
```
Loss = Σ(ŷ - y)² + λ·(w₁² + w₂²)
```

## 相关概念

- [[concepts/Backpropagation]]
- [[concepts/Chain Rule]]
- [[concepts/Gradient Descent]]
- [[concepts/Momentum]]
- [[concepts/Regularization]]
- [[concepts/L1 Regularization]]
- [[concepts/L2 Regularization]]

## 来源

[[1_raw/articles/I2DL/lectures/4.optimization_and_backprop.pdf]]