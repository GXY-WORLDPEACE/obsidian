---
title: "I2DL Lecture 10 - CNN Architectures"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #architectures
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/10.architectures.pdf
---

# I2DL Lecture 10: CNN 经典架构

## 摘要

本讲介绍经典的 CNN 架构，从 LeNet 到 AlexNet、VGGNet、GoogLeNet、ResNet 等，分析各架构的设计理念和改进点。

## 核心内容

### 1. 经典架构时间线

```
1998: LeNet     → 手写数字识别
2012: AlexNet   → 深度学习复兴
2014: VGGNet    → 简单深网络
2014: GoogLeNet → Inception 模块
2015: ResNet    → 残差连接
```

### 2. LeNet (1998)

```
Input(32×32) → Conv5×5×6 → Pool2×2 → Conv5×5×16 → Pool2×2 → Conv5×5×120 → FC84 → FC10
```

- 约 60k 参数
- 用于 MNIST 数字识别
- 使用 tanh/sigmoid 激活

### 3. AlexNet (2012)

突破性工作，ImageNet 错误率减半：

```
Input(224×224×3)
→ Conv11×11, 96, stride4 → Norm → Pool3×3
→ Conv5×5, 256 → Norm → Pool3×3
→ Conv3×3, 384
→ Conv3×3, 384
→ Conv3×3, 256 → Pool3×3
→ FC4096 → FC4096 → FC1000
```

**创新点**:
- ReLU 激活
- Dropout
- Data Augmentation
- GPU 并行训练

### 4. VGGNet (2014)

**特点**: 简单的 3×3 卷积堆叠

```
VGG-16:
Conv3×3×64 (×2) → Pool2×2
Conv3×3×128 (×2) → Pool2×2
Conv3×3×256 (×3) → Pool2×2
Conv3×3×512 (×3) → Pool2×2
Conv3×3×512 (×3) → Pool2×2
→ FC4096 → FC4096 → FC1000
```

**优势**: 
- 两个 3×3 卷积 ≈ 一个 5×5 感受野
- 三个 3×3 卷积 ≈ 一个 7×7 感受野
- 更少的参数，更多的非线性

### 5. Network in Network / GoogLeNet (2014)

**Inception 模块**: 多尺度并行卷积

```
           → Conv1×1 → Conv3×3 →
Input → Conv1×1 → Conv5×5 → Pool → Concat → Output
           → Conv1×1 → Conv3×3 →
```

**1×1 卷积作用**:
- 减少通道数（降维）
- 增加非线性

### 6. ResNet (2015)

**创新**: 残差连接 (Skip Connection)

```
H(x) = F(x) + x
```

**优势**:
- 缓解梯度消失
- 使极深网络可训练
- 超越人类水平 (ImageNet top-5 < 3.5%)

### 7. 评估指标

| 指标 | 说明 |
|------|------|
| Top-1 | 最高概率预测正确 |
| Top-5 | 前5个预测包含正确类 |

### 8. 架构设计趋势

```
更深的网络 (ResNet 152层)
更宽的网络 (Inception)
残差连接 (ResNet)
分组卷积 (ResNeXt)
深度可分离卷积 (MobileNet)
注意力机制 (SE-Net, CBAM)
```

## 相关概念

- [[concepts/AlexNet]]
- [[concepts/VGGNet]]
- [[concepts/ResNet]]
- [[concepts/GoogLeNet]]

## 来源

[[1_raw/articles/I2DL/lectures/10.architectures.pdf]]