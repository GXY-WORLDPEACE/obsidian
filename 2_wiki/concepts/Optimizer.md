---
title: "Optimizer"
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

# Optimizer 优化器

## 定义

优化器是用于更新神经网络参数的算法，通过最小化损失函数来学习模型权重。

## 基本公式

```
θ_{t+1} = θ_t - α · ∇L(θ_t)
```

其中 θ 是参数，α 是学习率，∇L 是梯度。

## 分类

### 一阶优化器

| 优化器 | 更新规则 |
|--------|----------|
| SGD | θ = θ - α·g |
| SGD + Momentum | v = βv + αg, θ = θ - v |
| Nesterov | v = βv + α·∇L(θ - βv) |
| AdaGrad | θ = θ - α·g / √(ε+Σg²) |
| RMSProp | θ = θ - α·g / √(ε+E[g²]) |
| Adam | m = β₁m + (1-β₁)g, v = β₂v + (1-β₂)g² |

### 二阶优化器

使用二阶导数（Hessian），如 Newton 法，但计算量大。

## 关键参数

| 参数 | 说明 |
|------|------|
| 学习率 (α) | 最重要的超参数 |
| 动量 (β) | 通常 0.9 |
| 权重衰减 | L2 正则化 |

## 选择建议

| 场景 | 推荐优化器 |
|------|-----------|
| 默认 | Adam |
| 图像分类 | SGD + Momentum |
| 序列模型 | Adam / AdamW |
| 大模型训练 | AdamW + LR Scheduler |

## 相关概念

- [[Gradient Descent]]
- [[Backpropagation]]
- [[Learning Rate]]
- [[Momentum]]

## 来源

[[summaries/I2DL-Lecture-04-Optimization-Backprop]]
[[summaries/I2DL-Lecture-05-Scaling-Optimization]]
