---
title: "Backpropagation"
date: 2026-06-03
tags:
  - #概念 #神经网络
---

# Backpropagation (反向传播)

## 定义

一种高效计算神经网络梯度的算法，基于链式法则。

## 核心思想

从输出层向输入层反向传播损失函数的梯度。

## 链式法则

$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w} $$

## 流程

1. **Forward Pass**: 计算输出和损失
2. **Backward Pass**: 从后向前计算梯度
3. **Update**: 用梯度更新权重

## 示例（逻辑回归）

$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \sigma(z)}{\partial z} \cdot \frac{\partial z}{\partial w} $$

其中 $z = X \cdot w$

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_04/1_simple_classifier-summary.md]]
