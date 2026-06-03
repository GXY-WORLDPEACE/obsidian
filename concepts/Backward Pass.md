---
title: "Backward Pass"
date: 2026-06-03
tags:
  - #概念 #神经网络
---

# Backward Pass (反向传播)

## 定义

从输出层向输入层反向传播梯度，计算各层参数的梯度。

## 与 Forward Pass 的关系

| 阶段 | 方向 | 作用 |
|------|------|------|
| Forward Pass | 输入 → 输出 | 计算预测值和损失 |
| Backward Pass | 输出 → 输入 | 计算梯度 |

## 逻辑回归中的反向传播

```python
# 1. 损失函数梯度
dL_dy = loss.backward(y_pred, y_true)

# 2. Sigmoid 梯度
dy_dz = sigmoid(z) * (1 - sigmoid(z))

# 3. 线性层梯度
dz_dw = X

# 4. 最终参数梯度
dL_dw = dL_dy * dy_dz * dz_dw
```

## 链式法则应用

$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w} $$

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_04/1_simple_classifier-summary.md]]
