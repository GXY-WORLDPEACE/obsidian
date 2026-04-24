---
title: "ResNet"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #cnn
type: concept
related_lectures:
  - 10
---

# ResNet

## 定义

ResNet (Residual Network) 是 2015 年 ImageNet 冠军网络，由何恺明等人提出，通过残差连接解决了深层网络训练困难的问题。

## 核心创新：残差连接

```
H(x) = F(x) + x
```

网络学习的是残差 F(x)，而非完整的映射 H(x)。

## 残差块

```
Input x
    ↓
Conv3×3 → ReLU → Conv3×3 → ReLU
    ↓                    ↓
         Add ←────── x (shortcut)
              ↓
           Output
```

## 为什么有效

| 优势 | 说明 |
|------|------|
| 恒等映射 | 即使 F(x)=0，也能保持 x 传递 |
| 梯度流动 | 短路连接直接传递梯度 |
| 极深网络 | 可训练 1000+ 层 |

## 变体

| 变体 | 层数 |
|------|------|
| ResNet-18 | 18 层 |
| ResNet-34 | 34 层 |
| ResNet-50 | 50 层 |
| ResNet-101 | 101 层 |
| ResNet-152 | 152 层 |

## 里程碑

- ImageNet Top-5 错误率 < 3.5%
- 首次超越人类水平
- 深度学习里程碑

## 相关概念

- [[Convolutional Neural Network]]
- [[VGGNet]]
- [[AlexNet]]

## 来源

[[summaries/I2DL-Lecture-10-CNN-Architectures]]
