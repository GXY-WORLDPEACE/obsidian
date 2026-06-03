---
title: "Tanh"
date: 2026-06-03
tags:
  - #概念 #激活函数
---

# Tanh (双曲正切)

## 定义

$$ \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} $$

## 性质

- 输出范围：$[-1, 1]$
- 零中心化（输出均值为 0）
- 奇函数：$\tanh(-x) = -\tanh(x)$

## 与 Sigmoid 的关系

$$ \tanh(x) = 2 \cdot \sigma(2x) - 1 $$

## 特点

| 特性 | Sigmoid | Tanh |
|------|---------|------|
| 输出范围 | (0, 1) | (-1, 1) |
| 零中心化 | 否 | 是 |
| 梯度饱和 | 严重 | 严重 |

## 导数

$$ \tanh'(x) = 1 - \tanh^2(x) $$

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/1_cifar10_classification-summary.md]]
