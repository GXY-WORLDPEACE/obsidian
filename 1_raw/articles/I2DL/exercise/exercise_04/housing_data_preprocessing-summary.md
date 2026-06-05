---
title: "I2DL Exercise 04 - Housing Data Preprocessing"
date: 2026-06-03
tags:
  - #I2DL #练习 #数据预处理
type: exercise
course: I2DL
---

# Housing Data Preprocessing (可选内容)

## 概述

介绍房价数据集的预处理流程，将原始数据转换为可训练的格式。

## 数据集信息

| 属性 | 值 |
|------|-----|
| **来源** | Housing Price Dataset (Kaggle) |
| **样本数** | ~1400房屋 |
| **原始特征** | 81 个 |
| **最终特征** | 1 个 (GrLivArea) |
| **目标** | 二分类（房价高低） |

## 预处理流程

### 1. 数据加载

使用 `CSVDataset` 类加载 `housing_train.csv` 数据集：

```python
train_dataset = CSVDataset(
    target_column='SalePrice',
    root=root_path,
    download_url=download_url,
    mode="train"
)
```

### 2. 特征选择

从 80+ 个特征中选择 **GrLivArea**（居住面积）作为唯一特征：

- 简化问题，便于 2D 可视化
- GrLivArea 与房价相关性高

### 3. 数据归一化

使用 **Min-Max 归一化**将特征缩放到 [0, 1] 范围：

```python
# 计算训练集的统计量
min_val = df.min()
max_val = df.max()
mean_val = df.mean()

# 归一化公式
normalized = (data - min) / (max - min)
```

**注意**：必须使用训练集的统计量应用到所有数据划分！

### 4. 二值化标签

将连续房价转为二分类标签：

```python
# 房价分为三类
thirty_percentile = np.percentile(y_all, 30)   # 30% 分位
seventy_percentile = np.percentile(y_all, 70)  # 70% 分位

# 最低 30% → 0 (low-priced)
# 中间 40% → 删除
# 最高 30% → 1 (expensive)
```

### 5. 最终数据

```python
X_train, y_train  # 训练集
X_val, y_val       # 验证集
X_test, y_test    # 测试集
```

## 为什么要数据预处理？

| 问题 | 处理方式 |
|------|----------|
| 数值范围差异大 | 归一化 |
| 缺失值 | 用均值填充 |
| 连续值无法分类 | 二值化 |
| 特征太多 | 特征选择 |

## 与1_simple_classifier.ipynb 的关系

| Notebook | 性质 | 内容 |
|----------|------|------|
| **housing_data_preprocessing** | 可选 | 解释数据如何预处理 |
| **1_simple_classifier** | 必需 | 训练逻辑回归分类器 |

## 相关概念

- [[concepts/Feature Selection]] - 特征选择
- [[concepts/Normalization]] - 归一化
- [[concepts/Data Binarization]] - 数据二值化

## 状态

✅ 已完成摘要生成