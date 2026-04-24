---
title: "I2DL Lecture 3 - Introduction to Neural Networks"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #neural-networks
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/3.intro2nn.pdf
---

# I2DL Lecture 3: 神经网络入门

## 摘要

本讲从逻辑回归出发，通过叠加多层线性变换+非线性激活，引入神经网络的概念。讲解神经网络的结构、激活函数、损失函数，以及如何用计算图表示和训练网络。

## 核心内容

### 1. 从线性到非线性

**线性分类器的局限**: 无法处理非线性可分数据（如XOR问题）

**解决方案**: 叠加多层线性变换，每层之间加入非线性激活

```
2层网络: f = W₂ · max(0, W₁·x)
3层网络: f = W₃ · max(0, W₂ · max(0, W₁·x))
```

### 2. 神经网络结构

```
输入层 → 隐藏层₁ → 隐藏层₂ → ... → 输出层
(输入)   (特征提取)  (特征变换)      (预测)
```

- **输入层**: 原始数据 (如 32×32×3 的图像展平为 3072 维)
- **隐藏层**: 通过激活函数引入非线性
- **输出层**: 分类/回归结果

### 3. 激活函数

| 函数 | 公式 | 特点 |
|------|------|------|
| **Sigmoid** | σ(x) = 1/(1+e^(-x)) | 输出(0,1)，易饱和 |
| **Tanh** | tanh(x) | 输出(-1,1)，零中心 |
| **ReLU** | max(0, x) | 计算快，梯度不衰减 |
| **Leaky ReLU** | max(0.1x, x) | 解决"死神经元"问题 |
| **ELU** | x if x>0, α(e^x-1) if x≤0 | 平滑负值 |

### 4. 计算图

神经网络可表示为有向无环图：
- **节点**: 变量或操作（+, -, *, /, log, exp等）
- **边**: 数据流动方向
- **前向传播**: 计算输出
- **反向传播**: 计算梯度

### 5. 损失函数

**回归任务**:
- L1: Σ|y_i - ŷ_i|
- MSE: Σ(y_i - ŷ_i)²

**分类任务**:
- Binary Cross-Entropy: -[y·log(ŷ) + (1-y)·log(1-ŷ)]
- Cross-Entropy: -Σ y_k · log(ŷ_k)

### 6. 梯度下降

```
θ_{t+1} = θ_t - α · ∇_θ L(y, f_θ(x))
```

通过反向传播（链式法则）计算所有参数的梯度。

### 7. 训练流程

1. 初始化参数 θ
2. 前向传播计算预测 ŷ
3. 计算损失 L(y, ŷ)
4. 反向传播计算梯度
5. 更新参数
6. 重复 2-5 直到收敛

## 相关概念

- [[concepts/Neural Networks]]
- [[concepts/Activation Function]]
- [[concepts/ReLU]]
- [[concepts/Computational Graph]]
- [[concepts/Gradient Descent]]
- [[concepts/Backpropagation]]

## 来源

[[1_raw/articles/I2DL/lectures/3.intro2nn.pdf]]