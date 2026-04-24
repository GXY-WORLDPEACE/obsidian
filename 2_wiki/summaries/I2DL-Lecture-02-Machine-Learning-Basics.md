---
title: "I2DL Lecture 2 - Machine Learning Basics"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #machine-learning
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/2.linear.pdf
---

# I2DL Lecture 2: 机器学习基础

## 摘要

本讲介绍机器学习的基本概念，涵盖有监督/无监督/强化学习三种范式，重点讲解线性回归的数学推导和最大似然估计（MLE）方法，并引出逻辑回归作为二分类模型。

## 核心内容

### 1. 机器学习范式

| 类型 | 特点 | 例子 |
|------|------|------|
| **有监督学习** | 有标签数据 | 分类、回归 |
| **无监督学习** | 无标签，发现结构 | 聚类、PCA |
| **强化学习** | 通过奖励学习策略 | 游戏、机器人 |

### 2. 数据划分

```
训练集 (60%) → 训练模型参数
验证集 (20%) → 调优超参数
测试集 (20%) → 最终评估（仅用一次）
```

### 3. 线性回归

**模型**: ŷ = Xθ = θ₀ + x₁θ₁ + ... + x_dθ_d

**损失函数**: MSE = (1/n) Σ(y_i - ŷ_i)²

**闭式解**: θ = (XᵀX)⁻¹Xᵀy

### 4. 最大似然估计 (MLE)

假设 y ~ N(Xθ, σ²)，MLE 等价于最小二乘法。

```
θ_ML = arg max_θ p(y|X,θ)
     = arg max_θ ∏ p_model(y_i|x_i,θ)
     = arg min_θ Σ (y_i - x_i·θ)²
```

### 5. 逻辑回归（二分类）

**Sigmoid函数**: σ(s) = 1/(1 + e^(-s))

**损失函数**: BCE = -[y·log(ŷ) + (1-y)·log(1-ŷ)]

特点：
- 输出 ∈ (0,1)，可解释为概率
- 无闭式解，需用梯度下降
- 可视为单层神经网络

### 6. 回归 vs 分类

| 任务 | 输出 | 例子 |
|------|------|------|
| 回归 | 连续值 | 房价、温度 |
| 二分类 | 0/1 | 猫/狗 |
| 多分类 | {1,...,C} | CIFAR-10 |

## 相关概念

- [[concepts/Linear Regression]]
- [[concepts/Maximum Likelihood Estimation]]
- [[concepts/Logistic Regression]]
- [[concepts/Sigmoid]]
- [[concepts/Loss Function]]

## 来源

[[1_raw/articles/I2DL/lectures/2.linear.pdf]]