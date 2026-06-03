---
title: "I2DL Exercise 05 - Neural Networks"
date: 2026-06-03
tags:
  - #I2DL #练习 #神经网络 #CIFAR-10
type: exercise
course: I2DL
---

# I2DL Exercise 05: 神经网络与 CIFAR-10 分类

## 概述

从 Exercise 04 的**逻辑回归**（单层）扩展到**多层神经网络**，实现模块化的网络层组件，并使用 CIFAR-10 数据集进行 10 分类。

## 数据集

| 属性 | 值 |
|------|-----|
| **数据集** | CIFAR-10 |
| **图片尺寸** | 32×32×3 (RGB) |
| **类别数** | 10 (plane, car, bird, cat, deer, dog, frog, horse, ship, truck) |
| **训练样本** | 500 (1% 用于过拟合实验) |

## 需要实现的组件

| 组件 | 文件 | 方法 | 说明 |
|------|------|------|------|
| **Sigmoid** | `layer.py` | `forward()`, `backward()` | Sigmoid 激活函数 |
| **ReLU** | `layer.py` | `forward()`, `backward()` | ReLU 激活函数 |
| **Affine Layer** | `layer.py` | `affine_forward()`, `affine_backward()` | 线性层（权重+偏置） |
| **SGD + Momentum** | `optimizer.py` | `_update()` | 动量梯度下降 |

## 核心概念

### 1. 模块化设计

神经网络由可组合的"层"组成，每个层包含：

```
Layer:
├── forward()  → 计算输出 + 保存缓存
└── backward() → 使用缓存计算梯度
```

**链式法则**允许任意组合层：
$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w} $$

### 2. 非线性激活函数

#### Sigmoid

$$ S(x) = \frac{1}{1 + e^{-x}} $$

- 输出范围：(0, 1)
- 特点：S 形曲线，可将线性输出转为概率
- 问题：梯度在两端接近 0（梯度消失）

#### ReLU (Rectified Linear Unit)

$$ ReLU(x) = \max(0, x) $$

- 计算高效
- 解决 sigmoid 梯度消失问题
- 当前最常用的激活函数

### 3. Affine Layer (线性层)

$$ z = X \cdot W + b $$

- $X$: 输入矩阵 (N × D)
- $W$: 权重矩阵 (D × H)
- $b$: 偏置向量 (H,)
- $z$: 输出 (N × H)

### 4. 多分类损失函数

#### Cross-Entropy (Softmax Loss)

$$ CE(\hat{y}, y) = -\frac{1}{N} \sum_{i=1}^{N} \sum_{k=1}^{C} y_{ik} \log(\hat{y}_{ik}) $$

其中 $y_{ik}$ 是 one-hot 编码的真实标签。

#### 数值稳定性优化

$$ softmax(x) = softmax(x - \max(x)) $$

减去最大值避免指数溢出。

## 优化器

### SGD (Stochastic Gradient Descent)

$$ w \leftarrow w - \alpha \nabla L $$

基础优化器，但收敛较慢。

### SGD + Momentum

$$ v^{k+1} = \beta v^{k} - \alpha \nabla_{\theta} L(\theta^{k}) $$
$$ \theta^{k+1} = \theta^{k} + v^{k+1} $$

- 累积历史梯度方向
- 加速收敛，减少震荡

### Adam

- 使用一阶和二阶矩估计
- 自适应学习率
- 目前最常用的优化器

## 完整训练流程

```
数据预处理 (Rescale → Normalize → Flatten)
       ↓
定义网络 (ClassificationNet)
       ↓
前向传播 (forward)
       ↓
计算损失 (CrossEntropy)
       ↓
反向传播 (backward)
       ↓
更新权重 (optimizer)
```

### 网络结构

```python
ClassificationNet(
    input_size=3072,      # 32×32×3 展平
    hidden_size=128,
    activation=Relu(),
    num_layer=2,          # 2层隐藏层
    num_classes=10
)
```

### CIFAR-10 数据预处理

```python
compose_transform = ComposeTransform([
    RescaleTransform(),           # [0, 255] → [0, 1]
    NormalizeTransform(           # 标准化
        mean=cifar_mean,
        std=cifar_std
    ),
    FlattenTransform()            # 展平为 1D 向量
])
```

## 评分标准

| 项目 | 值 |
|------|-----|
| 总测试数 | 10 |
| 每测试分值 | 10 分 |
| 满分 | 100 分 |
| **通过要求** | **100 分（全部通过）** |

## 关键经验

1. **先在小数据集上过拟合** — 验证代码正确性
2. **模块化设计** — 便于组合不同网络结构
3. **内存问题** — 全量梯度下降内存不够，需用随机方法
4. **超参数调优** — 下个 exercise 会讲

## 提取的概念

- [[concepts/Neural Network]] - 神经网络
- [[concepts/ReLU]] - ReLU 激活函数
- [[concepts/Affine Layer]] - 仿射层/线性层
- [[concepts/Softmax]] - Softmax 函数
- [[concepts/Cross-Entropy Loss]] - 交叉熵损失
- [[concepts/SGD with Momentum]] - 动量梯度下降
- [[concepts/Adam Optimizer]] - Adam 优化器

## 相关代码文件

- `exercise_code/networks/layer.py` - 层实现 (Sigmoid, ReLU, Affine)
- `exercise_code/networks/optimizer.py` - 优化器实现
- `exercise_code/networks/classification_net.py` - 分类网络
- `exercise_code/networks/loss.py` - 损失函数
- `exercise_code/solver.py` - 求解器

## 状态

✅ 已完成摘要生成
