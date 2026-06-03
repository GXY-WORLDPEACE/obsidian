---
title: "I2DL Exercise 06 - CIFAR-10 Classification"
date: 2026-06-03
tags:
  - #I2DL #练习 #分类器 #超参数调优
type: exercise
course: I2DL
---

# I2DL Exercise 06: CIFAR-10 分类与超参数调优

## 概述

使用 CIFAR-10 数据集训练图像分类器，学习网络调试技巧和超参数搜索方法。

## 数据集

| 属性 | 值 |
|------|-----|
| **数据集** | CIFAR-10 |
| **图片尺寸** | 32×32×3 (RGB) |
| **类别数** | 10 (plane, car, bird, cat, deer, dog, frog, horse, ship, truck) |
| **数据划分** | train (60%) / val (20%) / test (20%) |

## 需要实现的组件

| 组件 | 文件 | 方法 | 说明 |
|------|------|------|------|
| **LeakyReLU** | `layer.py` | `forward()`, `backward()` | 带泄露 ReLU |
| **Tanh** | `layer.py` | `forward()`, `backward()` | 双曲正切激活 |

## 新增内容

### 1. 新激活函数

#### LeakyReLU

解决 ReLU "死神经元"问题：

$$ f(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha x & \text{if } x \leq 0 \end{cases} $$

其中 $\alpha$ 是小常数（通常 0.01）。

#### Tanh

$$ \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} $$

- 输出范围：[-1, 1]
- 零中心化
- $\tanh(x) = 2 \cdot \sigma(2x) - 1$

### 2. 数据增强 (Data Augmentation)

通过对训练图像进行变换来扩充数据集：

| 方法 | 说明 |
|------|------|
| **RandomHorizontalFlip** | 随机水平翻转 |
| **Gaussian Blur** | 高斯模糊（可选） |
| **Rotation** | 旋转（可选） |

**重要**：数据增强只应用于训练集！

### 3. 权重正则化 (Weight Regularization)

$$ L^* = \underbrace{L}_{\text{数据损失}} + \underbrace{\lambda R(\theta)}_{\text{正则化损失}} $$

| 类型 | 公式 | 特点 |
|------|------|------|
| **L1** | $R(\theta) = \sum |w|$ | 产生稀疏权重 |
| **L2** | $R(\theta) = \sum w^2$ | 权重分散 |

## 超参数调优方法

### Grid Search (网格搜索)

- 定义每个超参数的可能值集合
- 遍历所有组合
- 缺点：维度爆炸（组合数 = $n_1 \times n_2 \times ...$）

### Random Search (随机搜索)

- 定义超参数取值范围
- 随机采样
- 更高效，避免冗余组合

### Early Stopping (早停)

- 监控验证集损失
- 损失不下降时等待 `patience` 个 epoch
- 防止过拟合，节省时间

## 调参最佳流程

```
1. 小数据集上过拟合（1张图 → 10张图 → 100张图）
       ↓
2. 粗略随机搜索（宽范围）
       ↓
3. 精细搜索（缩小范围）
       ↓
4. 全量数据 + 长训练 → 最终模型
```

## 关键超参数

| 超参数 | 说明 | 常用范围 |
|--------|------|----------|
| learning_rate | 学习率 | 1e-2 ~ 1e-4 |
| reg | 正则化强度 | 1e-3 ~ 1e-7 |
| num_layer | 网络层数 | 2 ~ 5 |
| hidden_size | 隐藏层大小 | 128 ~ 1024 |
| batch_size | 批大小 | 32 ~ 256 |
| epochs | 训练轮数 | 10 ~ 100 |

## 评分标准

| 项目 | 值 |
|------|-----|
| **通过要求** | 测试集准确率 ≥ 48% |
| **评分方式** | 实际准确率百分比 |
| **提交次数** | 无限（取最佳成绩）|

**注意**：这次没有单元测试，只需要模型达到最低准确率！

## 提取的概念

- [[concepts/LeakyReLU]] - 带泄露 ReLU
- [[concepts/Tanh]] - 双曲正切激活函数
- [[concepts/Data Augmentation]] - 数据增强
- [[concepts/Weight Regularization]] - 权重正则化
- [[concepts/L1 Regularization]] - L1 正则化
- [[concepts/L2 Regularization]] - L2 正则化
- [[concepts/Hyperparameter Tuning]] - 超参数调优
- [[concepts/Grid Search]] - 网格搜索
- [[concepts/Random Search]] - 随机搜索
- [[concepts/Early Stopping]] - 早停

## 相关代码文件

- `exercise_code/networks/layer.py` - 层实现 (LeakyReLU, Tanh)
- `exercise_code/networks/classification_net.py` - 分类网络
- `exercise_code/hyperparameter_tuning.py` - 超参数搜索
- `exercise_code/solver.py` - 求解器（含早停）
- `exercise_code/data/image_folder_dataset.py` - 数据增强

## 状态

✅ 已完成摘要生成
