---
title: "I2DL L03: Introduction to Neural Networks"
date: 2026-04-16
tags:
  - #I2DL #讲义 #神经网络
course: I2DL
lecture: 3
---

# I2DL Lecture 3: Introduction to Neural Networks

## 摘要
本讲从线性模型扩展到神经网络，介绍感知机、多层感知机(MLP)结构，以及非线性激活函数如何赋予网络表达能力。

## 核心内容

### 感知机 (Perceptron)
单个神经元，计算输入的线性组合后通过阶跃函数输出。

### 多层感知机 (MLP)
```
输入层 → 隐藏层 → ... → 隐藏层 → 输出层
```

### 网络结构
| 层类型 | 说明 |
|--------|------|
| **输入层** | D 维特征向量 |
| **隐藏层** | 非线性变换 $h = f(W_1 x + b_1)$ |
| **输出层** | 预测结果 |

### 激活函数
| 函数 | 公式 | 特点 |
|------|------|------|
| **ReLU** | max(0, x) | 最常用，收敛快 |
| **Sigmoid** | 1/(1+e⁻ˣ) | 输出 [0,1]，易梯度消失 |
| **Tanh** | (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | 输出 [-1,1] |

### 通用近似定理
具有一个隐藏层和足够多神经元的神经网络可以近似任意连续函数。

## 关键概念
- 权重矩阵 W, 偏置向量 b
- 前向传播 (Forward Propagation)
- 层次化表示 (Hierarchical Representations)

## 概念关联
- [[2_wiki/concepts/Neural Networks]] - 基础概念
- [[2_wiki/concepts/Deep Learning]] - 上位概念

## 来源
[[1_raw/articles/I2DL/lectures/3.intro2nn.pdf]]
