---
title: "Gradient Descent"
date: 2026-06-03
tags:
  - #概念 #优化算法
---

# Gradient Descent

## 定义

一种一阶优化算法，用于最小化目标函数。

## 更新公式

$$ w_{(n+1)} = w_{(n)} - \alpha \cdot \nabla L(w_{(n)}) $$

其中：
- $w$ 是待优化的参数
- $\alpha$ 是学习率 (learning rate)
- $\nabla L(w)$ 是损失函数关于 $w$ 的梯度

## 类型

| 类型 | 说明 |
|------|------|
| **Batch GD** | 使用全部数据计算梯度 |
| **Stochastic GD (SGD)** | 每个样本计算梯度 |
| **Mini-batch GD** | 每批样本计算梯度 |

## 学习率的影响

- **过大**：可能跳过最优点，震荡或发散
- **过小**：收敛速度慢，容易陷入局部最优

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_04/1_simple_classifier-summary.md]]
