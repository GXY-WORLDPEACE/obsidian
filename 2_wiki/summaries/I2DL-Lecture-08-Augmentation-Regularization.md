---
title: "I2DL Lecture 8 - Data Augmentation and Regularization"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #regularization
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/8.augmentation_and_regularization.pdf
---

# I2DL Lecture 8: 数据增强与高级正则化

## 摘要

本讲介绍防止过拟合的技术，包括数据增强、L2正则化、Dropout、Batch Normalization等。数据增强通过人为增加训练样本多样性，Dropout通过随机丢弃神经元实现模型集成，Batch Normalization通过归一化层输入加速训练。

## 核心内容

### 1. 数据预处理

- 减去均值图像（AlexNet）
- 逐通道减去均值（VGG）

### 2. 数据增强

**目的**: 让分类器对各种变换保持不变性

**常见增强方法**:

| 方法 | 说明 |
|------|------|
| 随机裁剪 | 从大图随机采样 224×224 |
| 翻转 | 水平翻转 |
| 亮度/对比度 | 随机调整 |
| 颜色抖动 | 随机颜色变化 |
| Cutout | 随机遮挡部分区域 |

**Advanced Augmentation**:
- RandAugment (CVPR 2020)
- Trivial Augment (ICCV 2021)

### 3. L2 正则化（权重衰减）

L = L_data + λ·Σw²

- 惩罚大权重
- 改进泛化能力
- 在 SGD 中等价于权重衰减，但在 Adam 中不同

### 4. Early Stopping

监控验证集损失，在开始上升时停止训练。

### 5. Dropout

**原理**: 训练时随机丢弃50%的神经元

```
训练:  y = W·dropout(x)
测试:  y = 0.5 · W·x  (或使用所有神经元)
```

**作用**:
- 减少神经元间的共适应
- 相当于训练大量共享参数的子网络
- 模型集成效果

**注意**: 与 BatchNorm 配合使用时效果不佳

### 6. Monte Carlo Dropout

用于不确定性估计：
- 训练时使用低 dropout rate (0.1-0.2)
- 测试时多次运行取平均

### 7. Batch Normalization

**目的**: 减少内部协变量偏移，加速训练

**公式**:
```
μ = mean(x)           # mini-batch mean
σ = std(x)            # mini-batch std
x_norm = (x - μ) / σ  # 标准化
y = γ·x_norm + β      # 缩放平移（可学习）
```

**位置**: 全连接/卷积层之后，激活函数之前

**训练 vs 测试**:
- 训练: 使用 mini-batch 统计量
- 测试: 使用训练时指数加权平均的统计量

### 8. 初始化方法

| 方法 | 公式 | 适用 |
|------|------|------|
| Xavier | Var(w) = 1/n | Sigmoid/Tanh |
| Kaiming | Var(w) = 2/n | ReLU |

## 相关概念

- [[concepts/Data Augmentation]]
- [[concepts/Dropout]]
- [[concepts/Batch Normalization]]
- [[concepts/Weight Initialization]]

## 来源

[[1_raw/articles/I2DL/lectures/8.augmentation_and_regularization.pdf]]