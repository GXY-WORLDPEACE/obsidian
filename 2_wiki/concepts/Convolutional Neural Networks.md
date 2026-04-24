---
title: "Convolutional Neural Networks"
date: 2026-04-16
aliases: ["CNN", "卷积神经网络"]
tags:
  - #概念 #CNN #计算机视觉
  - #I2DL
---

# CNN (卷积神经网络)

## 核心思想

CNN 是一种专门用于处理**网格化数据**（如图像）的神经网络架构，通过**卷积操作**捕捉空间层次结构。

## 核心层类型

| 层类型 | 功能 |
|--------|------|
| **卷积层 (Conv)** | 提取局部特征 |
| **池化层 (Pool)** | 降低维度，增加鲁棒性 |
| **全连接层 (FC)** | 最终分类/回归 |

## 关键操作

### 卷积 (Convolution)
- **卷积核** (Kernel/Filter): 3x3, 5x5 等
- **步长** (Stride): 移动步幅
- **填充** (Padding): 边缘处理 (same/valid)

### 池化 (Pooling)
- Max Pooling - 取最大值
- Average Pooling - 取平均值

## 经典架构

| 模型 | 年份 | 特点 |
|------|------|------|
| LeNet | 1998 | 早期手写数字识别 |
| AlexNet | 2012 | ImageNet 突破，ReLU + GPU |
| VGG | 2014 | 3x3 卷积堆叠 |
| ResNet | 2015 | 残差连接，152 层 |
| EfficientNet | 2019 | 平衡深度/宽度/分辨率 |

## 应用场景

- 图像分类
- 目标检测
- 语义分割
- 人脸识别

## 相关概念

- [[Neural Networks]] - 神经网络基础
- [[Deep Learning]] - 深度学习

## 课程来源

- [[summaries/I2DL-Lecture-1-Introduction]]