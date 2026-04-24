---
title: "Perceptron"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #neural-network
type: concept
related_lectures:
  - 3
---

# Perceptron 感知机

## 定义

感知机是最简单的神经网络模型，由 Frank Rosenblatt 于1957年提出，是神经网络的基础单元。

## 模型

```
y = f(w·x + b)
```

| 组件 | 说明 |
|------|------|
| x | 输入特征 |
| w | 权重 |
| b | 偏置 |
| f | 激活函数（早期为阶跃函数） |

## 训练规则

```
w = w + η·(y - ŷ)·x
b = b + η·(y - ŷ)
```

| 符号 | 说明 |
|------|------|
| η | 学习率 |
| y | 真实标签 |
| ŷ | 预测输出 |

## 局限性

- 只能处理线性可分数据
- 无法解决 XOR 问题
- 需多层感知机（MLP）才能处理非线性

## 与 [[Neural Network]] 的关系

单层感知机是神经网络的基本单元，多个感知机堆叠形成多层感知机（MLP），即全连接神经网络。

## 相关概念

- [[Neural Network]]
- [[Loss Function]]

## 来源

[[summaries/I2DL-Lecture-03-Intro-to-NN]]
