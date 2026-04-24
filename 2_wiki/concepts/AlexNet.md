---
title: "AlexNet"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #cnn
type: concept
related_lectures:
  - 10
---

# AlexNet

## 定义

AlexNet 是 2012 年 ImageNet 竞赛冠军网络，由 Alex Krizhevsky 等人提出，奠定了深度学习在计算机视觉领域的基础。

## 架构

```
Input(224×224×3)
→ Conv11×11, 96, stride4 → Norm → ReLU → Pool3×3
→ Conv5×5, 256 → Norm → ReLU → Pool3×3
→ Conv3×3, 384
→ Conv3×3, 384
→ Conv3×3, 256 → Pool3×3
→ FC4096 → FC4096 → FC1000
```

## 关键创新

| 创新 | 说明 |
|------|------|
| ReLU 激活 | 缓解梯度消失，加速训练 |
| Dropout | 防止过拟合 |
| GPU 训练 | 使用 CUDA 并行计算 |
| Data Augmentation | 随机裁剪、翻转 |
| Local Response Norm | 类似侧抑制 |

## 意义

- ImageNet 错误率从 26% 降至 15%
- 标志着深度学习复兴
- 证明 CNN 在大规模图像任务上的有效性

## 与 [[Convolutional Neural Network]] 的关系

AlexNet 是 CNN 的经典代表，其架构启发了后续 VGGNet、GoogLeNet 等网络。

## 相关概念

- [[Convolutional Neural Network]]
- [[VGGNet]]
- [[ResNet]]

## 来源

[[summaries/I2DL-Lecture-10-CNN-Architectures]]
