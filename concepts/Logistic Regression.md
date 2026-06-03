---
title: "Logistic Regression"
date: 2026-06-03
tags:
  - #概念 #机器学习 #分类器
---
·
# Logistic Regression (逻辑回归)

## 定义

一种用于二分类问题的线性模型，通过 sigmoid 函数将线性输出转换为概率。

## 模型公式

$$ \hat{y} = \sigma(X \cdot w + b) = \frac{1}{1 + e^{-(X \cdot w + b)}} $$

## 与线性回归的区别

| 特性 | 线性回归 | 逻辑回归 |
|------|---------|---------|
| 任务 | 回归（连续值） | 分类（二元） |
| 输出 | 任意实数 | [0, 1] 概率 |
| 激活 | 无 | Sigmoid |

## 决策边界

- 当 $\hat{y} > 0.5$ 时，预测为类别 1
- 当 $\hat{y} < 0.5$ 时，预测为类别 0
- 阈值通常为 0.5

## 损失函数

使用 Binary Cross-Entropy：

$$ BCE = -\frac{1}{N} \sum [y \cdot \log(\hat{y}) + (1-y) \cdot \log(1-\hat{y})] $$

## 实现代码

```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def logistic_regression(X, w, b):
    z = X @ w + b
    return sigmoid(z)
```

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_04/1_simple_classifier-summary.md]]
