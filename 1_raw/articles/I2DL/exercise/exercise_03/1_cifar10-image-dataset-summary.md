---
title: "I2DL Exercise 03 - CIFAR-10 Image Dataset"
date: 2026-04-24
tags:
  - #I2DL #练习 #数据处理
type: exercise_dataset
course: I2DL
---

# I2DL Exercise 03: CIFAR-10 数据集与数据预处理

## 概述

Exercise 03 聚焦于**数据准备技能**，实现自定义 Dataset 和数据变换管道。

## CIFAR-10 数据集

| 属性 | 值 |
|------|------|
| **图片数量** | 50,000 张训练图 |
| **图片尺寸** | 32×32 像素 |
| **颜色通道** | RGB（3通道） |
| **类别数量** | 10 类 |
| **类别名称** | plane, car, bird, cat, deer, dog, frog, horse, ship, truck |

## 核心任务

### 1. Dataset 类实现

```python
class ImageFolderDataset:
    def __init__(self, root, transform=None):
        self.images, self.labels = make_dataset(root, class_to_idx)
        self.transform = transform

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        image = load_image(self.images[index])
        label = self.labels[index]
        if self.transform:
            image = self.transform(image)
        return {"image": image, "label": label}
```

### 2. 数据变换（Transform）

| Transform | 作用 | 关键参数 |
|-----------|------|----------|
| **RescaleTransform** | 将像素值缩放到指定范围 | `in_range=(0,255)`, `out_range=(0,1)` |
| **NormalizeTransform** | 标准化（减均值、除标准差） | `mean`, `std` |
| **ComposeTransform** | 链式组合多个变换 | `[transform1, transform2]` |

### 3. CIFAR-10 统计量

```python
cifar_mean = [0.4919, 0.4824, 0.4467]
cifar_std = [0.2471, 0.2435, 0.2615]
```

## 两种加载方式对比

| 类型 | 加载时机 | 内存占用 | I/O 速度 |
|------|----------|----------|----------|
| **ImageFolderDataset** | 按需加载 | 低 | 慢 |
| **MemoryImageFolderDataset** | 启动时加载 | ~1.2GB | 快 |

## 关键要点

1. **Dataset 协议**: 必须实现 `__len__` 和 `__getitem__`
2. **Transform 设计**: 可调用对象（Callable），支持链式组合
3. **数据可视化**: 训练前必看样本，了解数据分布
4. **归一化重要性**: 加速收敛，数值稳定

## 提取的概念

- [[concepts/Dataset]] - PyTorch Dataset 协议
- [[concepts/Transform]] - 数据预处理管道
- [[concepts/CIFAR-10]] - 图像分类数据集
- [[concepts/Image Normalization]] - 图像标准化

## 相关代码文件

- `exercise_code/data/image_folder_dataset.py` - Dataset 实现
- `exercise_code/data/transforms.py` - Transform 实现

## 状态

✅ 已完成摘要生成
