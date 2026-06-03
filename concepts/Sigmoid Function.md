---
title: "Sigmoid Function"
date: 2026-06-03
tags:
  - #概念 #激活函数
---

# Sigmoid Function

## 定义

$$ \sigma(x) = \frac{1}{1 + e^{-x}} $$

## 性质

- 输出范围：$(0, 1)$
- 单调递增
- S 形曲线

## 导数

$$ \sigma'(x) = \sigma(x) \cdot (1 - \sigma(x)) $$

## 应用

- 逻辑回归的激活函数
- 将线性输出转换为概率
- 二分类问题的输出层

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_04/1_simple_classifier-summary.md]]
