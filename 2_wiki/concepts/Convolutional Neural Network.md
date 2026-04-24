---
title: "Convolutional Neural Network (CNN)"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #cnn
type: concept
related_lectures:
  - 9
  - 10
---

# Convolutional Neural Network (CNN) 卷积神经网络

## 定义

CNN是一种专门用于处理具有网格结构数据（图像、语音等）的深度神经网络，通过卷积操作自动学习空间层次特征。

## 核心组件

### 1. 卷积层 (Convolutional Layer)

**二维卷积操作**：
```
Output(i,j) = Σₘ Σₙ Filter(m,n) × Input(i+m, j+n)
```

**参数**：
| 参数 | 说明 |
|------|------|
| Kernel/Filters | 卷积核大小（如3×3, 5×5） |
| Stride | 卷积步长 |
| Padding | 边缘填充 |
| Depth | 滤波器数量 |

**输出尺寸公式**：
```
Output = floor((N + 2P - F) / S + 1)
N: 输入尺寸, P: Padding, F: Kernel, S: Stride
```

### 2. 池化层 (Pooling Layer)

| 类型 | 公式 | 特点 |
|------|------|------|
| Max Pool | max(window) | 提取显著特征 |
| Avg Pool | mean(window) | 保留背景信息 |

常用设置：2×2 filter, stride 2

### 3. 全连接层 (Fully Connected Layer)

将特征图展平后进行分类/回归

## 经典架构

| 架构 | 年份 | 创新点 |
|------|------|--------|
| LeNet | 1998 | 首个CNN，用于手写识别 |
| AlexNet | 2012 | ReLU、Dropout、GPU训练 |
| VGGNet | 2014 | 3×3卷积堆叠 |
| GoogLeNet | 2014 | Inception模块 |
| ResNet | 2015 | 残差连接 |

## 核心概念

### 感受野 (Receptive Field)

- 输出特征图中一个像素对应输入图像的区域大小
- 逐层堆叠卷积，感受野逐渐增大

### 权重共享

同一滤波器在整个图像上滑动，大幅减少参数数量

### 特征层次

```
底层特征 → 边缘、纹理、颜色
中层特征 → 纹理组合、局部形状
高层特征 → 物体部件、语义概念
```

## PyTorch 示例

```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc = nn.Linear(64 * 8 * 8, 10)
    
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))  # 32×32→16×16
        x = self.pool(F.relu(self.conv2(x)))   # 16×16→8×8
        x = x.view(-1, 64 * 8 * 8)
        x = self.fc(x)
        return x
```

## 相关概念

- [[Convolution]]
- [[Pooling]]
- [[Receptive Field]]
- [[AlexNet]]
- [[VGGNet]]
- [[ResNet]]

## 来源

[[summaries/I2DL-Lecture-09-CNN]]
[[summaries/I2DL-Lecture-10-CNN-Architectures]]
