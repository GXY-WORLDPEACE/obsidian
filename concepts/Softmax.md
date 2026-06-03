---
title: "Softmax"
date: 2026-06-03
tags:
  - #概念 #激活函数 #多分类
---

# Softmax

## 定义

将向量转换为概率分布：

$$ softmax(x)_i = \frac{e^{x_i}}{\sum_{j=1}^{n} e^{x_j}} $$

## 性质

- 输出所有元素和为 1
- 每个元素在 (0, 1) 范围内
- 保持相对大小关系

## 数值稳定性优化

$$ softmax(x) = softmax(x - \max(x)) $$

减去最大值避免指数溢出（数值不稳定）。

## 导数（交叉熵结合时）

当与 Cross-Entropy Loss 一起使用时，梯度计算简化：

$$ \frac{\partial CE}{\partial x_i} = softmax(x)_i - y_i $$

## 来源