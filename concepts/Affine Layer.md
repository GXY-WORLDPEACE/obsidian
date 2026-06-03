---
title: "Affine Layer"
date: 2026-06-03
tags:
  - #概念 #神经网络 #层
---

# Affine Layer (仿射层 / 线性层)

## 定义

也称为全连接层 (Fully Connected Layer) 或 Dense Layer。

## 计算公式

$$ \mathbf{z} = \mathbf{X} \cdot \mathbf{W} + \mathbf{b} $$

## 参数说明

| 符号 | 形状 | 说明 |
|------|------|------|
| $\mathbf{X}$ | (N, D) | 输入，N 个样本，D 维特征 |
| $\mathbf{W}$ | (D, H) | 权重矩阵 |
| $\mathbf{b}$ | (H,) | 偏置向量 |
| $\mathbf{z}$ | (N, H) | 输出 |

## 梯度计算

**Forward Pass**:
```python
cache = (x, w, b)
out = x @ w + b
```

**Backward Pass**:
```python
dx = dout @ w.T      # 输入梯度
dw = x.T @ dout      # 权重梯度
db = np.sum(dout, axis=0)  # 偏置梯度
```

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_05/1_NeuralNetworks-summary.md]]
