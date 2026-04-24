---
title: "Backpropagation"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #optimization
type: concept
related_lectures:
  - 4
---

# Backpropagation 反向传播

## 定义

反向传播是一种高效计算神经网络梯度的算法，通过链式法则从输出层向输入层逐层传递误差。

## 核心原理

### 1. 链式法则

对于复合函数：
```
∂L/∂x = ∂L/∂y · ∂y/∂x
```

### 2. 计算图

```
Input(x) → Linear(z=Wx+b) → Activation(a=σ(z)) → Loss(L)
           ↓                    ↓
         ∂L/∂W                ∂L/∂a
```

## 算法步骤

### 前向传播 (Forward Pass)
1. 计算每一层的输出 $z_l = W_l · a_{l-1} + b_l$
2. 应用激活函数 $a_l = σ(z_l)$
3. 计算最终损失 $L$

### 反向传播 (Backward Pass)
1. 计算输出层梯度：$\frac{∂L}{∂a_L}$
2. 逐层回传梯度：$\frac{∂L}{∂a_{l-1}} = W_l^T · \frac{∂L}{∂a_l}$
3. 计算权重梯度：$\frac{∂L}{∂W_l} = \frac{∂L}{∂a_l} · a_{l-1}^T$

## 计算示例

对于单层网络：
```
Input: x
Output: y = σ(Wx + b)
Loss: L(y, ŷ)

∂L/∂W = δ · xᵀ
∂L/∂b = δ
其中 δ = ∂L/∂y · σ'(Wx+b)
```

## 核心概念

### 梯度 (Gradient)
损失函数对参数的偏导数，指向函数上升最快的方向。

### 梯度消失 (Vanishing Gradient)
- 原因：sigmoid/tanh 激活函数导数 < 1
- 影响：深层网络早期层梯度接近0
- 解决：ReLU激活、BatchNorm、残差连接

### 梯度爆炸 (Exploding Gradient)
- 原因：权重初始化过大
- 影响：梯度过大，参数更新不稳定
- 解决：梯度裁剪、合适的初始化

## 相关概念

- [[Gradient Descent]]
- [[Optimizer]]
- [[Neural Network]]
- [[Chain Rule]]

## 来源

[[summaries/I2DL-Lecture-04-Optimization-Backprop]]
