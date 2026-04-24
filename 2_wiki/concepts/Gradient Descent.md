---
title: "Gradient Descent"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #optimization
type: concept
related_lectures:
  - 4
  - 5
---

# Gradient Descent 梯度下降

## 定义

梯度下降是一种优化算法，通过沿损失函数梯度的负方向迭代更新参数，以找到全局/局部最小值。

## 基本公式

```
θ = θ - α · ∇L(θ)
```

其中：
- θ: 参数
- α: 学习率
- ∇L(θ): 损失函数的梯度

## 变体

### 1. Batch Gradient Descent

```python
θ = θ - α · (1/n) · Σ∇L(xᵢ, yᵢ; θ)
```

| 优点 | 缺点 |
|------|------|
| 稳定收敛 | 每次迭代计算所有样本 |
| 凸函数保证全局最优 | 大数据集计算慢 |

### 2. Stochastic Gradient Descent (SGD)

```python
θ = θ - α · ∇L(xᵢ, yᵢ; θ)
```

| 优点 | 缺点 |
|------|------|
| 快，每次用一个样本 | 收敛震荡 |
| 可跳出局部最优 | 需较小学习率 |

### 3. Mini-batch Gradient Descent

```python
θ = θ - α · (1/b) · Σ∇L(xᵢ:yᵢ+b; θ)
```

- 平衡收敛速度和稳定性
- 常用 batch size: 32, 64, 128

## 学习率调度

| 方法 | 公式 | 特点 |
|------|------|------|
| 固定 | α = const | 简单 |
| 步进衰减 | α = α₀ · 0.1^epoch/30 | 每30 epoch衰减 |
| 指数衰减 | α = α₀ · γ^epoch | 指数下降 |
| 余弦退火 | α = α_min + 0.5(α_max-α_min)(1+cos(π·epoch/epochs)) | 周期变化 |
| Warmup | 从小到大再减小 | 稳定训练初期 |

## 自适应优化器

| 优化器 | 更新规则 | 特点 |
|--------|----------|------|
| **SGD + Momentum** | v = βv + α∇L | 加速收敛 |
| **AdaGrad** | θ = θ - α/√(ε+Σg²) · g | 稀疏数据 |
| **RMSProp** | θ = θ - α/√(E[g²]+ε) · g | 非稳态数据 |
| **Adam** | 组合Momentum+RMSProp | 常用默认 |

### Adam 算法

```python
m = β₁m + (1-β₁)g          # 一阶矩估计
v = β₂v + (1-β₂)g²         # 二阶矩估计
m̂ = m / (1-β₁ᵗ)            # 偏差校正
v̂ = v / (1-β₂ᵗ)
θ = θ - α · m̂ / (√v̂ + ε)   # 参数更新
```

默认参数：β₁=0.9, β₂=0.999, ε=10⁻⁸

## 相关概念

- [[Backpropagation]]
- [[Optimizer]]
- [[Learning Rate]]
- [[Momentum]]

## 来源

[[summaries/I2DL-Lecture-04-Optimization-Backprop]]
[[summaries/I2DL-Lecture-05-Scaling-Optimization]]
