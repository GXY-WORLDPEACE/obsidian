---
title: "Learning Rate"
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

# Learning Rate 学习率

## 定义

学习率控制优化器在每次迭代中更新参数的步长大小。

## 影响

| 学习率 | 表现 |
|--------|------|
| 过小 | 收敛慢，容易陷入局部最优 |
| 过大 | 震荡，无法收敛 |
| 适中 | 快速收敛 |

## 学习率调度

| 方法 | 公式 | 特点 |
|------|------|------|
| 固定 | α = const | 简单 |
| 步进衰减 | α = α₀ · γ^{epoch} | 每 N epoch 衰减 |
| 指数衰减 | α = α₀ · γ^{epoch} | 指数下降 |
| 余弦退火 | α = α_min + 0.5(α_max-α_min)(1+cos(π·epoch/epochs)) | 周期性 |
| Warmup | 线性增长到峰值再衰减 | 稳定训练初期 |

## 常用值

| 优化器 | 典型初始学习率 |
|--------|---------------|
| SGD | 0.01 ~ 0.1 |
| Adam | 1e-3 ~ 1e-4 |
| AdamW | 1e-3 ~ 3e-4 |

## 相关概念

- [[Gradient Descent]]
- [[Optimizer]]
- [[Momentum]]

## 来源

[[summaries/I2DL-Lecture-04-Optimization-Backprop]]
[[summaries/I2DL-Lecture-05-Scaling-Optimization]]
