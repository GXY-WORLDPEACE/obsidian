---
title: "Weight Regularization"
date: 2026-06-03
tags:
  - #概念 #正则化
---

# Weight Regularization (权重正则化)

## 定义

在损失函数中添加正则化项，防止过拟合：

$$ L^* = L + \lambda R(\theta) $$

## L1 正则化

$$ R(\theta) = \sum |w| $$

- 产生稀疏权重
- 可用于特征选择
- 梯度：$\nabla |w| = \text{sign}(w)$

## L2 正则化

$$ R(\theta) = \sum w^2 $$

- 权重分散
- 惩罚大权重
- 梯度：$\nabla w^2 = 2w$

## 对比

| 特性 | L1 | L2 |
|------|----|----|
| 稀疏性 | 高 | 低 |
| 特征选择 | 是 | 否 |
| 解的稳定性 | 较低 | 高 |
| 计算代价 | 低 | 低 |

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/1_cifar10_classification-summary.md]]
