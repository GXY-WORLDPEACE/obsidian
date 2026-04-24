---
title: "I2DL L09: Convolutional Neural Networks"
date: 2026-04-16
tags:
  - #I2DL #讲义 #CNN #计算机视觉
course: I2DL
lecture: 9
---

# I2DL Lecture 9: Convolutional Neural Networks

## 摘要
本讲介绍卷积神经网络(CNN)，专为处理网格化数据（图像）设计，通过权重共享大幅减少参数量。

## 核心内容

### 卷积操作
```
Input (H×W×C) * Kernel (K×H'×W'×C) → Output (H''×W''×C')
```

关键参数：
| 参数 | 说明 | 常见值 |
|------|------|--------|
| **Kernel Size** | 卷积核大小 | 3×3, 5×5 |
| **Stride** | 步长 | 1, 2 |
| **Padding** | 边缘填充 | 'same', 'valid' |
| **Channels** | 输出通道数 | 64, 128, 256 |

### CNN 经典架构
```
输入 → [Conv → BN → ReLU] × N → Pool → ... → 输出
```

### 池化层 (Pooling)
| 类型 | 作用 |
|------|------|
| **Max Pool** | 取区域最大值，保留显著特征 |
| **Avg Pool** | 取平均值，平滑特征 |

### 典型 CNN 结构
| 网络 | 特点 |
|------|------|
| **LeNet-5** | 早期手写数字识别 |
| **AlexNet** | 2012 ImageNet 突破，ReLU+GPU |
| **VGG** | 3×3 卷积堆叠，统一结构 |
| **GoogLeNet** | Inception 模块，多尺度并行 |

## 关键概念
- Weight Sharing (权重共享)
- Receptive Field (感受野)
- Feature Map
- Spatial Hierarchy

## 概念关联
- [[2_wiki/concepts/Convolutional Neural Networks]] - 概念笔记
- [[2_wiki/summaries/I2DL-Lecture-10-Architectures]] - 进阶架构

## 来源
[[1_raw/articles/I2DL/lectures/9.convnets.pdf]]
