---
title: "I2DL L07: Losses and Activations"
date: 2026-04-16
tags:
  - #I2DL #讲义 #损失函数 #激活函数
course: I2DL
lecture: 7
---

# I2DL Lecture 7: Losses and Activations

## 摘要
本讲深入讲解输出层的激活函数选择与损失函数设计，根据任务类型（分类/回归）匹配合适的输出层配置。

## 核心内容

### 激活函数对比
| 激活函数 | 输出范围 | 适用场景 | 梯度特点 |
|----------|----------|----------|----------|
| **Sigmoid** | (0,1) | 二分类输出 | 梯度易消失 |
| **Softmax** | (0,1) 多类和=1 | 多分类 | 梯度易消失 |
| **Linear** | (-∞, +∞) | 回归任务 | 恒定梯度 |
| **ReLU** | [0, +∞) | 隐藏层 | 单侧饱和 |

### 损失函数
| 任务 | 损失函数 | 公式 |
|------|----------|------|
| **回归** | MSE | $\frac{1}{N}\sum(y-\hat{y})^2$ |
| **二分类** | Binary Cross-Entropy | $-\sum y\log\hat{y}$ |
| **多分类** | Cross-Entropy | $-\sum y\log\hat{y}$ |
| **稀疏标签** | Sparse CE | 同上，输入为整数标签 |

### Softmax 与 Cross-Entropy 联合
数值稳定的实现：
$$\text{Softmax}(x_i) = \frac{e^{x_i - \max(x)}}{\sum e^{x_j - \max(x)}}$$

## 关键概念
- Softmax Function
- Cross-Entropy Loss
- KL Divergence
- Label Smoothing

## 概念关联
- [[2_wiki/concepts/Neural Networks]] - 网络结构
- [[2_wiki/summaries/I2DL-Lecture-3-Intro2NN]] - 激活函数基础

## 来源
[[1_raw/articles/I2DL/lectures/7.losses_and_activations.pdf]]
