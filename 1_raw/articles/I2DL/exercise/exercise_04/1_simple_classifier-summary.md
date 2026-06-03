---
title: "I2DL Exercise 04 - Simple Classifier"
date: 2026-06-03
tags:
  - #I2DL #练习 #分类器 #逻辑回归
type: exercise
course: I2DL
---

# I2DL Exercise 04: 简单分类器 / 逻辑回归

## 概述

Exercise 04 实现完整的训练流程，包括模型、损失函数、优化器和求解器。使用**逻辑回归**预测房价是 "expensive" 还是 "low-priced"（二分类）。

## 数据集

| 属性 | 值 |
|------|-----|
| **任务** | 二分类（房价高低） |
| **类别** | 0 (low-priced), 1 (expensive) |
| **数据划分** | train / validation / test |

## 完整训练流程

```
数据加载 → 模型前向 → 计算损失 → 反向传播 → 梯度下降更新权重
```

## 需要实现的组件

| 组件 | 文件 | 方法 | 说明 |
|------|------|------|------|
| **BCE Loss** | `networks/loss.py` | `forward()`, `backward()` | 二分类交叉熵损失 |
| **Classifier** | `networks/classifier.py` | `sigmoid()`, `forward()`, `backward()` | 逻辑回归分类器 |
| **Optimizer** | `networks/optimizer.py` | `step()` | 梯度下降更新 |
| **Solver** | `solver.py` | `_step()` | 整合训练步骤 |

## 核心公式

### 模型 (Logistic Regression)

$$ \hat{y} = \sigma(X \cdot w) $$

其中 **sigmoid 函数**：

$$ \sigma(t) = \frac{1}{1+e^{-t}} $$

作用：将线性输出压缩到 [0, 1]，表示预测为 "expensive" 的概率。

### 损失函数 (Binary Cross-Entropy)

$$ BCE(y, \hat{y}) = -\frac{1}{N} \sum_{i=1}^{N} [y_i \cdot \log(\hat{y}_i) + (1-y_i) \cdot \log(1-\hat{y}_i)] $$

### 梯度下降

$$ w_{(n+1)} = w_{(n)} - \alpha \cdot \frac{dL}{dw} $$

其中 $\alpha$ 是学习率 (learning rate)。

## 训练流程代码

```python
for i in range(epochs):
    # 1. 前向传播
    output = model.forward(X_train)
    
    # 2. 计算损失
    loss = loss_func(output, y_train)
    loss_grad = loss_func.backward(output, y_train)
    
    # 3. 反向传播 (链式法则)
    grad = model.backward(loss_grad)
    
    # 4. 更新权重
    optimizer.step(grad)
```

## 反向传播链式法则

$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w} $$

分解为：
1. $\frac{\partial L}{\partial \hat{y}}$ — 来自损失函数的梯度
2. $\frac{\partial \hat{y}}{\partial w} = \frac{\partial \sigma(s)}{\partial s} \cdot \frac{\partial s}{\partial w}$，其中 $s = X \cdot w$

## 关键概念

- **Forward Pass**: 数据从输入流向输出，计算预测值和损失
- **Backward Pass**: 损失梯度反向传播，计算各层参数的梯度
- **梯度下降**: 使用梯度更新权重，最小化损失函数
- **Solver**: 封装训练循环，提供训练接口

## 评分标准

| 项目 | 值 |
|------|-----|
| 总测试数 | 10 |
| 最低通过 | 8 个 (80 分) |
| 每测试分值 | 10 分 |
| 满分 | 100 分 |

## 提取的概念

- [[concepts/Logistic Regression]] - 逻辑回归分类器
- [[concepts/Sigmoid Function]] - Sigmoid 激活函数
- [[concepts/Binary Cross-Entropy]] - 二分类交叉熵损失
- [[concepts/Gradient Descent]] - 梯度下降优化
- [[concepts/Backpropagation]] - 反向传播算法
- [[concepts/Forward Pass]] - 前向传播
- [[concepts/Backward Pass]] - 反向传播

## 相关代码文件

- `exercise_code/networks/classifier.py` - 分类器实现
- `exercise_code/networks/loss.py` - 损失函数实现
- `exercise_code/networks/optimizer.py` - 优化器实现
- `exercise_code/solver.py` - 求解器实现
- `exercise_code/networks/base_networks.py` - 基础网络类

## 状态

✅ 已完成摘要生成
