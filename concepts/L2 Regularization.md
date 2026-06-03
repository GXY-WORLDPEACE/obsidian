---
title: "L2 Regularization"
date: 2026-06-03
tags:
  - #概念 #正则化
---

# L2 Regularization

## 定义

$$ R(\theta) = \sum_{i} w_i^2 $$

也称为 **Weight Decay**。

## 特性

- 权重分散，不过分依赖少数特征
- 惩罚大权重
- 梯度：$\nabla w^2 = 2w$

## 直观理解

L2 让所有权重都变小但不归零，使模型更平滑。

## 与 L1 对比

| 特性 | L1 | L2 |
|------|----|----|
| 稀疏性 | 高 | 低 |
| 特征选择 | 是 | 否 |

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/1_cifar10_classification-summary.md]]
