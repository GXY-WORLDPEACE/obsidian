---
title: "Feature Learning"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #machine-learning
type: concept
related_lectures:
  - 3
---

# Feature Learning 特征学习

## 定义

特征学习是指模型自动从原始数据中学习有用的表示/特征，而无需人工设计特征工程。

## 与传统特征工程的对比

| 方法 | 特征来源 | 人工工作 |
|------|----------|----------|
| 传统 ML | 人工设计 | 大量 |
| 深度学习 | 自动学习 | 极少 |

## 表示学习

深度学习通过多层神经网络自动学习分层表示：

```
原始数据 → 低层特征 → 中层特征 → 高层语义
  (像素)    (边缘)     (纹理)     (物体)
```

## 自监督学习

无需标签，通过代理任务学习特征：

| 方法 | 代理任务 |
|------|----------|
| Contrastive Learning | 区分相似/不相似样本 |
| Masked Prediction | 预测被遮挡的部分 |
| Autoencoder | 重构输入 |

## 与 [[Neural Network]] 的关系

神经网络是实现特征学习的核心工具，逐层自动提取越来越抽象的特征。

## 相关概念

- [[Neural Network]]
- [[Autoencoder]]
- [[Transfer Learning]]

## 来源

[[summaries/I2DL-Lecture-03-Intro-to-NN]]
