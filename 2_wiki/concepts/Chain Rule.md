---
title: "Chain Rule"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #math
type: concept
related_lectures:
  - 4
---

# Chain Rule 链式法则

## 定义

链式法则是微积分中计算复合函数导数的基本规则，是反向传播的理论基础。

## 公式

对于复合函数 $f(g(x))$：
```
d/dx · f(g(x)) = f'(g(x)) · g'(x)
```

多变量形式：
```
∂/∂x · f(g(x), h(x)) = ∂f/∂g · ∂g/∂x + ∂f/∂h · ∂h/∂x
```

## 在神经网络中的应用

```
Loss → Layer_L → ... → Layer_1 → Input
```

梯度逐层回传：
```
∂L/∂W₁ = ∂L/∂a₂ · ∂a₂/∂z₂ · ∂z₂/∂W₁
```

## 反向传播中的链式法则

```
∂L/∂W = ∂L/∂ŷ · ∂ŷ/∂z · ∂z/∂W
```

每层只需：
1. 接收上游梯度 ∂L/∂output
2. 乘以本地梯度 ∂output/∂input
3. 传递给下游

## 相关概念

- [[Backpropagation]]
- [[Gradient Descent]]

## 来源

[[summaries/I2DL-Lecture-04-Optimization-Backprop]]
