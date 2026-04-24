---
title: "VGGNet"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #cnn
type: concept
related_lectures:
  - 10
---

# VGGNet

## 定义

VGGNet 是 2014 年 ImageNet 竞赛亚军网络，由牛津大学 Visual Geometry Group 提出，以简单统一的架构著称。

## 架构 (VGG-16)

```
Conv3×3×64 (×2) → Pool2×2
Conv3×3×128 (×2) → Pool2×2
Conv3×3×256 (×3) → Pool2×2
Conv3×3×512 (×3) → Pool2×2
Conv3×3×512 (×3) → Pool2×2
→ FC4096 → FC4096 → FC1000
```

## 核心思想

**全部使用 3×3 卷积**：
- 两个 3×3 ≈ 一个 5×5 感受野
- 三个 3×3 ≈ 一个 7×7 感受野
- 更少的参数，更多的非线性

## 参数对比

| 架构 | 感受野 | 参数量 |
|------|--------|--------|
| 单个 7×7 | 7×7 | 49×C² |
| 三个 3×3 | 7×7 | 27×C² |

## 变体

| 变体 | 层数 |
|------|------|
| VGG-11 | 11 层 |
| VGG-13 | 13 层 |
| VGG-16 | 16 层 |
| VGG-19 | 19 层 |

## 相关概念

- [[Convolutional Neural Network]]
- [[AlexNet]]
- [[ResNet]]

## 来源

[[summaries/I2DL-Lecture-10-CNN-Architectures]]
