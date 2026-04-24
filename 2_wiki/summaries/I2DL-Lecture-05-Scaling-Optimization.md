---
title: "I2DL Lecture 5 - Scaling Optimization"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #optimization
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/5.scaling_optimization.pdf
---

# I2DL Lecture 5: 规模化优化

## 摘要

本讲介绍如何在大规模数据集上高效训练神经网络。重点讲解随机梯度下降（SGD）及其变种（Momentum、RMSProp、Adam），以及二阶优化方法的基本思想。

## 核心内容

### 1. 梯度下降的挑战

- **全批量GD**: 计算所有样本梯度，O(n)复杂度，太慢
- **神经网络非凸**: 可能陷入局部最优
- **学习率选择**: 敏感且困难

### 2. 随机梯度下降 (SGD)

**核心思想**: 用小批量（minibatch）的梯度近似全局梯度

```
θ_{k+1} = θ_k - α · ∇_θ L(θ_k, x{1..m}, y{1..m})
```

- **Batch size**: 通常为 2 的幂（8, 16, 32, 64, 128）
- **Epoch**: 完整遍历一次训练集
- **Iteration**: 一次参数更新

### 3. SGD 收敛条件

Robbins-Monro 条件：
1. α_n ≥ 0
2. Σ α_n = ∞
3. Σ α_n² < ∞

学习率通常设为 α_n ∝ 1/n

### 4. 动量法 (Momentum)

```
v_{k+1} = β · v_k - α · ∇L(θ_k)
θ_{k+1} = θ_k + v_{k+1}
```

- 累积历史梯度（类似物理惯性）
- β 通常设为 0.9
- 加速收敛，减少震荡

### 5. Nesterov 动量

```
θ̃_{k+1} = θ_k + β · v_k  (预测位置)
v_{k+1} = β · v_k - α · ∇L(θ̃_{k+1})
θ_{k+1} = θ_k + v_{k+1}
```

### 6. RMSProp

```
s_{k+1} = β · s_k + (1-β) · (∇L)²
θ_{k+1} = θ_k - α · ∇L / (√s_{k+1} + ε)
```

- 自适应学习率
- 大梯度 → 大分母 → 小的有效学习率
- 小梯度 → 小分母 → 大的有效学习率

### 7. Adam

结合 Momentum 和 RMSProp：
```
m_{k+1} = β₁ · m_k + (1-β₁) · ∇L  (一阶矩估计)
v_{k+1} = β₂ · v_k + (1-β₂) · (∇L)²  (二阶矩估计)
m̂ = m / (1-β₁^{k+1})  (偏置校正)
v̂ = v / (1-β₂^{k+1})
θ_{k+1} = θ_k - α · m̂ / (√v̂ + ε)
```

**默认值**: β₁=0.9, β₂=0.999, ε=10⁻⁸

### 8. 二阶方法（了解）

| 方法 | 原理 | 缺点 |
|------|------|------|
| Newton | 使用Hessian矩阵 | O(n²) 内存 |
| L-BFGS | 近似Hessian逆 | 不适合大数据 |
| Gauss-Newton | 近似二阶导 | 需解线性系统 |

### 9. 优化器选择

```
标准选择: Adam
备选: SGD + Momentum
大规模全批量: L-BFGS
```

## 相关概念

- [[concepts/Stochastic Gradient Descent]]
- [[concepts/Momentum]]
- [[concepts/RMSProp]]
- [[concepts/Adam]]
- [[concepts/Minibatch]]

## 来源

[[1_raw/articles/I2DL/lectures/5.scaling_optimization.pdf]]