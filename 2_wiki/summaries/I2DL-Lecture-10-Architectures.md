---
title: "I2DL L10: Modern Architectures"
date: 2026-04-16
tags:
  - #I2DL #讲义 #网络架构
course: I2DL
lecture: 10
---

# I2DL Lecture 10: Modern Architectures

## 摘要
本讲介绍现代 CNN 架构的设计原则和经典模型，包括 ResNet 的残差连接、EfficientNet 的复合缩放，以及注意力机制的基本概念。

## 核心内容

### ResNet - 残差网络
核心创新：跳跃连接 (Skip Connection)
$$y = F(x) + x$$

解决深层网络梯度消失问题，允许训练超深网络（1000+ 层）。

### EfficientNet
复合缩放策略：
$$\text{depth}: d = \alpha^\phi$$
$$\text{width}: w = \beta^\phi$$
$$\text{resolution}: r = \gamma^\phi$$

平衡深度、宽度、分辨率。

### 注意力机制初步
| 类型 | 说明 |
|------|------|
| **Channel Attention** | SE-Net，每个通道加权 |
| **Spatial Attention** | 关注空间位置 |
| **Self-Attention** | Query-Key-Value 交互 |

### 现代 CNN 组件
| 组件 | 作用 |
|------|------|
| **Depthwise Separable Conv** | 减少计算量 |
| **Inverted Residual** | MobileNetV2 核心 |
| **Squeeze-and-Excitation** | 通道注意力 |
| **Attention Gate** | 跳跃连接门控 |

## 关键架构对比
| 架构 | 参数量 | ImageNet Top-1 | 特点 |
|------|--------|----------------|------|
| ResNet-50 | 25M | 76.1% | 残差连接 |
| ResNet-152 | 60M | 78.3% | 更深 |
| EfficientNet-B3 | 12M | 84.1% | 高效 |
| EfficientNet-B7 | 66M | 85.5% | 最佳效率 |

## 关键概念
- Residual Connection
- Skip Connection
- Compound Scaling
- Depthwise Convolution

## 概念关联
- [[2_wiki/summaries/I2DL-Lecture-9-ConvNets]] - CNN 基础
- [[2_wiki/summaries/I2DL-Lecture-11-RNNs-Transformers]] - Transformer

## 来源
[[1_raw/articles/I2DL/lectures/10.architectures.pdf]]
