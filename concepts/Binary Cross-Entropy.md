---
title: "Binary Cross-Entropy"
date: 2026-06-03
tags:
  - #概念 #损失函数
---

# Binary Cross-Entropy (BCE)

## 定义

$$ BCE(y, \hat{y}) = -\frac{1}{N} \sum_{i=1}^{N} [y_i \cdot \log(\hat{y}_i) + (1-y_i) \cdot \log(1-\hat{y}_i)] $$

## 说明

- 用于二分类问题的损失函数
- $y_i$ 是真实标签（0 或 1）
- $\hat{y}_i$ 是预测概率 $(0, 1)$
- 当预测与真实标签一致时，损失趋近于 0

## 特性

- 非负性：$BCE \geq 0$
- 当 $\hat{y} = y$ 时，$BCE = 0$
- 当 $\hat{y}$ 远离 $y$ 时，$BCE$ 增大

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_04/1_simple_classifier-summary.md]]
