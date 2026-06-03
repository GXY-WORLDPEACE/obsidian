---
title: "autograd"
date: 2026-06-03
tags:
  - #概念 #PyTorch #自动微分
---

# autograd

## 概述

PyTorch 的自动微分引擎，无需手动计算梯度。

## 使用方法

```python
x = torch.tensor([1.0], requires_grad=True)

# 前向传播
y = x ** 2 + 2 * x + 1

# 反向传播
y.backward()

# 查看梯度
print(x.grad)  # tensor([4.])
```

## 手动计算验证

$$ y = x^2 + 2x + 1 $$
$$ \frac{dy}{dx} = 2x + 2 = 2(1) + 2 = 4 $$

## 关键方法

| 方法 | 说明 |
|------|------|
| `requires_grad` | 启用梯度追踪 |
| `backward()` | 反向传播 |
| `grad` | 访问梯度 |
| `no_grad()` | 禁用梯度追踪（推理时） |

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_07/1_pytorch-summary.md]]
