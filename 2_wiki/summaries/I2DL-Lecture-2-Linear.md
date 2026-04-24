---
title: "I2DL L02: Linear Regression"
date: 2026-04-16
tags:
  - #I2DL #讲义 #监督学习
course: I2DL
lecture: 2
---

# I2DL Lecture 2: Linear Regression

## 摘要
本讲介绍机器学习基础——线性回归，包括数据拟合、损失函数、最小二乘法，以及从概率视角的理解。

## 核心内容

### 线性回归模型
$$f(x) = w^T x + b = \sum_{i=1}^{D} w_i x_i + b$$

### 损失函数 - 均方误差 (MSE)
$$L = \frac{1}{N} \sum_{n=1}^{N} (y_n - \hat{y}_n)^2 = \frac{1}{N} \|y - Xw\|^2$$

### 解析解
$$w^* = (X^T X)^{-1} X^T y$$

### 关键概念
| 概念 | 说明 |
|------|------|
| **权重向量 w** | 决定输入特征的线性组合 |
| **偏置 b** | 预测的基准偏移 |
| **MSE Loss** | 回归任务常用损失函数 |
| **闭式解** | 矩阵求逆可直接求解 |

## 概念关联
- [[2_wiki/concepts/Machine Learning]] - 上位概念
- [[2_wiki/concepts/Deep Learning]] - 扩展到非线性

## 来源
[[1_raw/articles/I2DL/lectures/2.linear.pdf]]


