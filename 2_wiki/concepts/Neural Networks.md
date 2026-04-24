---
title: "Neural Networks"
date: 2026-04-16
tags:
  - #概念 #神经网络
  - #I2DL
---

# Neural Networks (神经网络)

## 基本结构

神经网络由**神经元**（节点）组成，包含：
- **输入层** (Input Layer)
- **隐藏层** (Hidden Layers)
- **输出层** (Output Layer)

```
输入 → 隐藏层1 → 隐藏层2 → ... → 输出
```

## 核心组件

| 组件 | 说明 |
|------|------|
| **权重 (Weights)** | 连接神经元之间的参数 |
| **偏置 (Bias)** | 每个神经元的可学习偏移 |
| **激活函数** | 引入非线性 (ReLU, Sigmoid, Tanh) |
| **损失函数** | 衡量预测与真实值的差距 |

## 学习过程

1. **前向传播** (Forward Propagation)
   - 输入 → 隐藏层 → 输出 → 计算损失

2. **反向传播** (Backpropagation)
   - 计算梯度 → 更新权重
   - 使用链式法则 (Chain Rule)

## 常见问题

| 问题 | 解决方法 |
|------|----------|
| 过拟合 | Dropout, 正则化, 数据增强 |
| 梯度消失/爆炸 | BatchNorm, 残差连接, 合适的学习率 |
| 收敛慢 | 学习率调度, Adam 优化器 |

## 相关概念

- [[Deep Learning]] - 深度学习
- [[Convolutional Neural Networks]] - CNN
- [[Recurrent Neural Networks]] - RNN

## 课程来源

- [[summaries/I2DL-Lecture-1-Introduction]]