---
title: "Momentum"
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

# Momentum 动量

## 定义

动量模拟物理中的惯性概念，加速收敛并减少震荡。

## 算法

```
v_t = β·v_{t-1} + (1-β)·∇L(θ)
θ_{t+1} = θ_t - α·v_t
```

| 参数 | 说明 |
|------|------|
| v | 速度（累积梯度） |
| β | 动量系数（通常 0.9） |
| α | 学习率 |

## 直观理解

- 累积历史的梯度方向
- 在一致方向上加速
- 在震荡方向上抵消

## 与 SGD 的关系

| 方法 | 公式 |
|------|------|
| SGD | θ = θ - α·g |
| SGD + Momentum | v = βv + αg, θ = θ - v |

## 变体

### Nesterov Accelerated Gradient (NAG)

```
v_t = β·v_{t-1} + α·∇L(θ - β·v_{t-1})
θ_{t+1} = θ_t - v_t
```

先看一步的梯度方向，比标准动量更激进。

## 相关概念

- [[Gradient Descent]]
- [[Optimizer]]
- [[Learning Rate]]

## 来源

[[summaries/I2DL-Lecture-04-Optimization-Backprop]]
[[summaries/I2DL-Lecture-05-Scaling-Optimization]]
