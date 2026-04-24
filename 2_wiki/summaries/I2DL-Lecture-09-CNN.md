---
title: "I2DL Lecture 9 - Convolutional Neural Networks"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #cnn
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/9.convnets.pdf
---

# I2DL Lecture 9: 卷积神经网络

## 摘要

本讲介绍卷积神经网络（CNN），解释为何卷积比全连接层更适合处理图像，通过权重共享显著减少参数数量。涵盖卷积操作、Padding、Stride、Pooling 等核心概念。

## 核心内容

### 1. 全连接层的问题

对于 224×224×3 的图像：
- 第一个 FC 层需要 ~150M 参数
- 无法利用图像的空间结构
- 参数量太大，容易过拟合

### 2. 卷积的优势

**权重共享**: 同一滤波器在整个图像上滑动

| 操作 | 参数数量 |
|------|----------|
| FC (单个神经元) | 75 (5×5×3) |
| Conv (整个层) | 75 × K (K个滤波器) |

### 3. 卷积操作

**二维卷积**: 滤波器在图像上滑动，计算点积

```
Output(i,j) = Σ_m Σ_n Filter(m,n) × Input(i+m, j+n)
```

### 4. 卷积参数

| 参数 | 说明 |
|------|------|
| **Kernel Size** | 滤波器大小 (如 3×3, 5×5) |
| **Stride** | 滑动步长 |
| **Padding** | 边缘填充 |
| **Depth** | 滤波器数量 |

### 5. 输出尺寸公式

```
Output = floor((N + 2P - F) / S + 1)
N: 输入尺寸
P: Padding
F: Kernel size
S: Stride
```

### 6. Padding 类型

- **Valid**: 无填充，尺寸缩小
- **Same**: 填充使输出等于输入

### 7. 多通道卷积

- 输入: W × H × D
- 滤波器: F × F × D
- 输出: W' × H' × K (K个滤波器)

参数数量: (F×F×D + 1) × K

### 8. 经典滤波器

```
边缘检测:     [-1 -1 -1; -1 8 -1; -1 -1 -1]
锐化:         [0 -1 0; -1 5 -1; 0 -1 0]
高斯模糊:     1/16 × [1 2 1; 2 4 2; 1 2 1]
```

### 9. 池化层

| 类型 | 公式 | 特点 |
|------|------|------|
| Max Pool | max(window) | 最常用，提取显著特征 |
| Avg Pool | mean(window) | 保留背景信息 |

常用设置: 2×2 filter, stride 2

### 10. CNN 架构模式

```
Input → [Conv + ReLU] × N → Pool → [Conv + ReLU] × M → Pool → ... → FC → Output
         (特征提取)                       (空间压缩)        (分类)
```

### 11. 感受野

- 输出特征图中一个像素对应输入图像的区域大小
- 逐层堆叠卷积，感受野逐渐增大

## 相关概念

- [[concepts/Convolutional Neural Network]]
- [[concepts/Convolution]]
- [[concepts/Pooling]]
- [[concepts/Receptive Field]]

## 来源

[[1_raw/articles/I2DL/lectures/9.convnets.pdf]]