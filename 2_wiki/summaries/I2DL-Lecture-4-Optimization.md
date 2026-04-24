---
title: "I2DL L04: Optimization and Backpropagation"
date: 2026-04-16
tags:
  - #I2DL #讲义 #优化 #反向传播
course: I2DL
lecture: 4
---

# I2DL Lecture 4: Optimization and Backpropagation

## 摘要
本讲讲解神经网络的训练核心——反向传播算法，通过链式法则高效计算梯度，以及随机梯度下降(SGD)等优化方法。

## 核心内容

### 反向传播 (Backpropagation)
利用链式法则，从输出层向输入层逐层计算梯度：

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w}$$

### 计算图
将网络分解为基本操作（加法、乘法、激活），逐节点求导并反向传播。

### 梯度下降
$$w := w - \alpha \frac{\partial L}{\partial w}$$

### 优化器比较
| 优化器 | 更新规则 | 特点 |
|--------|----------|------|
| **SGD** | $w := w - \alpha \nabla L$ | 简单，可能震荡 |
| **SGD + Momentum** | 加入动量项 | 加速收敛，减少震荡 |
| **Adam** | 自适应学习率 | 当前主流，默认选择 |

### 梯度问题
| 问题 | 原因 | 解决方案 |
|------|------|----------|
| **梯度消失** | 链式法则连乘，小梯度累乘趋近0 | ReLU、残差连接 |
| **梯度爆炸** | 大梯度累乘 | 梯度裁剪、BatchNorm |

## 关键概念
- 链式法则 (Chain Rule)
- 计算图 (Computation Graph)
- 梯度裁剪 (Gradient Clipping)
- 动量 (Momentum)

## 概念关联
- [[2_wiki/concepts/Neural Networks]] - 网络结构
- [[2_wiki/concepts/Deep Learning]] - 训练过程

## 来源
[[1_raw/articles/I2DL/lectures/4.optimization_and_backprop.pdf]]
