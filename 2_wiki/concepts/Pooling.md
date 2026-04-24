---
title: "Pooling"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #cnn
type: concept
related_lectures:
  - 9
---

# Pooling 池化

## 定义

池化是一种下采样操作，通过聚合邻域特征来减少特征图尺寸，同时提供平移不变性。

## 类型

### Max Pooling

取窗口内最大值：
```
MaxPool(x) = max(window)
```

**最常用**，提取显著特征。

### Average Pooling

取窗口内平均值：
```
AvgPool(x) = mean(window)
```

保留背景信息。

### Global Pooling

对整个特征图做池化，输出 1×1：
```
GlobalAvgPool(x) = mean(all pixels)
```

常用于分类网络的最后阶段。

## 参数

| 参数 | 常用值 |
|------|--------|
| Kernel Size | 2×2 |
| Stride | 2 |

## 作用

| 作用 | 说明 |
|------|------|
| 减少尺寸 | H, W 减半 |
| 减少参数 | 降低计算量 |
| 平移不变性 | 对位置变化更鲁棒 |
| 扩大感受野 | 后续层看到更大范围 |

## 与 [[Convolutional Neural Network]] 的关系

池化层通常跟在卷积层之后，是 CNN 架构的重要组成部分。

## 相关概念

- [[Convolutional Neural Network]]
- [[Convolution]]
- [[Receptive Field]]

## 来源

[[summaries/I2DL-Lecture-09-CNN]]
