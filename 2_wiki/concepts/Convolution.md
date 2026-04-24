---
title: "Convolution"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #cnn
type: concept
related_lectures:
  - 9
---

# Convolution 卷积

## 定义

卷积是一种数学运算，通过滤波器（卷积核）在输入上滑动并计算加权和，提取空间特征。

## 二维卷积

```
Output(i,j) = Σ_m Σ_n Filter(m,n) × Input(i+m, j+n)
```

## 参数

| 参数 | 说明 |
|------|------|
| Kernel Size | 卷积核大小（如 3×3, 5×5） |
| Stride | 滑动步长 |
| Padding | 边缘填充 |

## 输出尺寸

```
Output = floor((N + 2P - F) / S + 1)
```

| 符号 | 说明 |
|------|------|
| N | 输入尺寸 |
| P | Padding |
| F | Kernel size |
| S | Stride |

## 常见操作

| 类型 | 说明 |
|------|------|
| Valid | 无 Padding |
| Same | 输出 = 输入尺寸（需 Padding） |
| Full | 最大 Padding |

## 与 [[Convolutional Neural Network]] 的关系

卷积是 CNN 的核心操作，通过权重共享大幅减少参数数量。

## 相关概念

- [[Convolutional Neural Network]]
- [[Pooling]]

## 来源

[[summaries/I2DL-Lecture-09-CNN]]
