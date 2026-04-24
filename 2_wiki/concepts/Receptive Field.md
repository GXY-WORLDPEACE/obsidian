---
title: "Receptive Field"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #cnn
type: concept
related_lectures:
  - 9
---

# Receptive Field 感受野

## 定义

感受野是指输出特征图上一个像素对应输入图像的区域大小。

## 直观理解

```
Input (224×224)
    ↓ Conv3×3 (stride1)
Feature Map 1 (224×224) → RF = 3×3
    ↓ Conv3×3 (stride1)
Feature Map 2 (222×222) → RF = 5×5
    ↓ Conv3×3 (stride1)
Feature Map 3 (220×220) → RF = 7×7
```

## 计算公式

```
RF_n = RF_{n-1} + (kernel_n - 1) × stride_prod_{prev}
```

其中 stride_prod 是前面所有层 stride 的乘积。

## 有效感受野

不是所有感受野区域都同等重要，中心区域影响更大（有效感受野 ~ 感受野的平方根区域）。

## 影响因素

| 方法 | 效果 |
|------|------|
| 更深的网络 | 更大的感受野 |
| 更大的 Kernel | 更大的感受野 |
| 空洞卷积 (Dilated Conv) | 指数级增大感受野 |
| 池化层 | 增大感受野 |

## 与 [[Pooling]] 的关系

池化层可以快速增大感受野，但会丢失空间信息。

## 相关概念

- [[Convolutional Neural Network]]
- [[Pooling]]
- [[Convolution]]

## 来源

[[summaries/I2DL-Lecture-09-CNN]]
