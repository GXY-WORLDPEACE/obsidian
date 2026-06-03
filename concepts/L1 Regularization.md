---
title: "L1 Regularization"
date: 2026-06-03
tags:
  - #概念 #正则化
---

# L1 Regularization

## 定义

$$ R(\theta) = \sum_{i} |w_i| $$

## 特性

- 产生稀疏解（很多权重为 0）
- 可用于特征选择
- 梯度：$\nabla |w| = \text{sign}(w)$

## 直观理解

L1 倾向于将不重要的特征权重压缩为 0，实现自动特征选择。

##