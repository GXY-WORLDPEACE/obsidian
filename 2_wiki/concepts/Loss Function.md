---
title: "Loss Function"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #training
type: concept
related_lectures:
  - 3
  - 7
---

# Loss Function 损失函数

## 定义

损失函数衡量模型预测值与真实值之间的差异，是模型优化的目标函数。

## 分类

### 回归损失

| 损失 | 公式 | 特点 |
|------|------|------|
| MSE | (1/n)Σ(y-ŷ)² | 常用，对 outlier 敏感 |
| MAE | (1/n)Σ|y-ŷ| | 对 outlier 鲁棒 |
| Huber | 介于 MSE 和 MAE 之间 | 平滑过渡 |

### 分类损失

| 损失 | 公式 | 特点 |
|------|------|------|
| Cross-Entropy | -Σy·log(ŷ) | 分类首选 |
| Hinge Loss | max(0, 1-y·ŷ) | SVM |
| Focal Loss | -α(1-ŷ)^γ·log(ŷ) | 难样本挖掘 |

## Cross-Entropy 详解

```
L = -Σ y_i · log(ŷ_i)
```

当 y=1 时：L = -log(ŷ)（预测越接近1损失越小）
当 y=0 时：L = -log(1-ŷ)（预测越接近0损失越小）

## 与激活函数的关系

| 任务 | 激活函数 | 损失函数 |
|------|---------|----------|
| 二分类 | Sigmoid | Binary Cross-Entropy |
| 多分类 | Softmax | Cross-Entropy |
| 回归 | 无/Linear | MSE |

## 相关概念

- [[Neural Network]]
- [[Activation Function]]
- [[Optimizer]]

## 来源

[[summaries/I2DL-Lecture-03-Intro-to-NN]]
[[summaries/I2DL-Lecture-07-Losses-Activations]]
