---
title: "I2DL Course Index"
date: 2026-04-24
tags:
  - #I2DL
  - #course
  - #index
type: course_index
---

# I2DL 课程索引

## 课程概述

**Introduction to Deep Learning (I2DL)** - 慕尼黑工业大学深度学习导论课程

| 属性 | 内容 |
|------|------|
| 课程类型 | 大学课程 |
| 难度 | 入门/基础 |
| 前提知识 | Python, 线性代数, 微积分, 概率论 |

## 课程内容

### 基础模块

| 序号 | 讲次 | 主题 | 关键词 |
|------|------|------|--------|
| 1 | [[summaries/I2DL-Lecture-01-Introduction]] | 课程介绍 | 深度学习概述, AI历史 |
| 2 | [[summaries/I2DL-Lecture-02-Machine-Learning-Basics]] | 机器学习基础 | 监督学习, 无监督学习, 线性回归, 逻辑回归 |
| 3 | [[summaries/I2DL-Lecture-03-Intro-to-NN]] | 神经网络入门 | 感知机, 激活函数, 损失函数 |

### 核心模块

| 序号 | 讲次 | 主题 | 关键词 |
|------|------|------|--------|
| 4 | [[summaries/I2DL-Lecture-04-Optimization-Backprop]] | 优化与反向传播 | 梯度下降, 链式法则, SGD |
| 5 | [[summaries/I2DL-Lecture-05-Scaling-Optimization]] | 规模化优化 | Adam, Momentum, RMSProp |
| 6 | [[summaries/I2DL-Lecture-06-Training-NN]] | 神经网络训练 | 超参数调优, 训练流程 |
| 7 | [[summaries/I2DL-Lecture-07-Losses-Activations]] | 损失函数与激活函数 | Cross-Entropy, Softmax, ReLU |

### 计算机视觉

| 序号 | 讲次 | 主题 | 关键词 |
|------|------|------|--------|
| 8 | [[summaries/I2DL-Lecture-08-Augmentation-Regularization]] | 数据增强与正则化 | Dropout, BatchNorm, Data Augmentation |
| 9 | [[summaries/I2DL-Lecture-09-CNN]] | 卷积神经网络 | 卷积, 池化, 感受野 |
| 10 | [[summaries/I2DL-Lecture-10-CNN-Architectures]] | CNN经典架构 | AlexNet, VGGNet, ResNet, GoogLeNet |

### 序列模型与注意力

| 序号 | 讲次 | 主题 | 关键词 |
|------|------|------|--------|
| 11 | [[summaries/I2DL-Lecture-11-RNNs-Transformers]] | RNN与Transformer | LSTM, 自注意力, 位置编码, 迁移学习 |

### 高级主题

| 序号 | 讲次 | 主题 | 关键词 |
|------|------|------|--------|
| 12 | [[summaries/I2DL-Lecture-12-Advanced-Topics]] | 高级深度学习主题 | GNN, 生成模型, 强化学习 |

## 核心概念速查

### 神经网络基础

- [[concepts/Neural Network]]
- [[concepts/Perceptron]]
- [[concepts/Activation Function]]
- [[concepts/Loss Function]]

### 优化算法

- [[concepts/Gradient Descent]]
- [[concepts/Backpropagation]]
- [[concepts/Adam]]
- [[concepts/Momentum]]
- [[concepts/Learning Rate]]

### 计算机视觉

- [[concepts/Convolutional Neural Network]]
- [[concepts/Convolution]]
- [[concepts/Pooling]]
- [[concepts/Receptive Field]]
- [[concepts/AlexNet]]
- [[concepts/VGGNet]]
- [[concepts/ResNet]]
- [[concepts/GoogLeNet]]

### 序列处理

- [[concepts/Recurrent Neural Network]]
- [[concepts/LSTM]]
- [[concepts/Attention Mechanism]]
- [[concepts/Transformer]]
- [[concepts/Positional Encoding]]
- [[concepts/Transfer Learning]]

### 正则化与训练

- [[concepts/Dropout]]
- [[concepts/Batch Normalization]]
- [[concepts/Data Augmentation]]
- [[concepts/Weight Initialization]]

### 生成模型

- [[concepts/Autoencoder]]
- [[concepts/Variational Autoencoder]]
- [[concepts/GAN]]
- [[concepts/Diffusion Model]]

### 图神经网络

- [[concepts/Graph Neural Network]]

### 强化学习

- [[concepts/Reinforcement Learning]]

## 学习路径

```
入门
  └─> 机器学习基础 (L2)
        └─> 神经网络入门 (L3)
              └─> 优化与反向传播 (L4)
                    └─> 规模化优化 (L5)
                          └─> 神经网络训练 (L6)
                                ├─> 损失与激活 (L7)
                                ├─> 数据增强正则化 (L8)
                                │     └─> CNN基础 (L9)
                                │           └─> CNN架构 (L10)
                                └─> RNN与Transformer (L11)
                                      └─> 高级主题 (L12)
```

## 相关资源

### 练习与作业

- [[1_raw/articles/I2DL/exercises/]]

### 工具与框架

- [[concepts/Python]]
- [[concepts/Numpy]]
- [[concepts/Google_Colab]]

### 其他课程

- [[indexes/ML Course Index]]
- [[indexes/CV Course Index]]
