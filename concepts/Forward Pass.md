---
title: "Forward Pass"
date: 2026-06-03
tags:
  - #概念 #神经网络
---

# Forward Pass (前向传播)

## 定义

数据从输入层流向输出层的过程，计算预测值。

## 流程

```
输入 X → 线性变换 (X·w) → 激活函数 (σ) → 输出 ŷ → 计算损失 L
```

## 逻辑回归示例

```python
# 线性变换
z = X @ w

# 激活（Sigmoid）
y_pred = sigmoid(z)

# 计算损失
loss = bce_loss(y_pred, y_true)
```

## 目的

1. 计算模型预测值
2. 计算损失函数值
3. 为反向传播准备中间结果

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_04/1_simple_classifier-summary.md]]
