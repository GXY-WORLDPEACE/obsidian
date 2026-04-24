---
title: "I2DL L08: Augmentation and Regularization"
date: 2026-04-16
tags:
  - #I2DL #讲义 #数据增强 #正则化
course: I2DL
lecture: 8
---

# I2DL Lecture 8: Augmentation and Regularization

## 摘要
本讲讲解防止过拟合的核心技术——数据增强和正则化方法，提高模型泛化能力。

## 核心内容

### 数据增强 (Data Augmentation)
通过变换现有数据增加训练样本多样性：

| 任务 | 增强方法 |
|------|----------|
| **图像** | 翻转、旋转、裁剪、颜色抖动、MixUp、Cutmix |
| **文本** | 同义词替换、回译、随机插入 |
| **音频** | 时间偏移、音调变化、噪声添加 |

### 正则化方法
| 方法 | 原理 | 特点 |
|------|------|------|
| **L2 正则化** | 权重衰减 $\lambda\|w\|^2$ | 最常用 |
| **L1 正则化** | 稀疏权重 $\lambda\|w\|$ | 特征选择 |
| **Dropout** | 随机失活神经元 | 高效实用 |
| **Early Stopping** | 验证集监控 | 简单有效 |

### Dropout
训练时随机置零部分神经元：
```python
output = mask * output  # mask 为 Bernoulli(p) 采样
```
推理时使用完整网络，并等价于 L2 正则化。

### 高级正则化
| 方法 | 说明 |
|------|------|
| **MixUp** | 两样本线性插值混合 |
| **CutMix** | 图像块替换 |
| **Label Smoothing** | 软化标签分布 |
| **Stochastic Depth** | 随机跳过残差块 |

## 关键概念
- Generalization Gap
- Underfitting / Overfitting
- Dropout / DropConnect
- Data Augmentation

## 概念关联
- [[2_wiki/summaries/I2DL-Lecture-6-TrainingNN]] - 训练实践
- [[2_wiki/concepts/Deep Learning]] - 泛化理论

## 来源
[[1_raw/articles/I2DL/lectures/8.augmentation_and_regularization.pdf]]
