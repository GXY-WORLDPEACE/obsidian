---
title: "Adam Optimizer"
date: 2026-06-03
tags:
  - #概念 #优化算法
---

# Adam (Adaptive Moment Estimation)

## 核心思想

结合动量法和 RMSProp，自适应调整每个参数的学习率。

## 更新公式

```
# 计算梯度
g_t = ∇θ L(θ_t)

# 更新一阶矩估计（类似动量）
m_t = β₁ · m_{t-1} + (1 - β₁) · g_t

# 更新二阶矩估计（类似 RMSProp）
v_t = β₂ · v_{t-1} + (1 - β₂) · g_t²

# 偏差校正
m̂_t = m_t / (1 - β₁^t)
v̂_t = v_t / (1 - β₂^t)

# 参数更新
θ_t = θ_{t-1} - α · m̂_t / (√v̂_t + ε)
```

## 默认超参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| $\alpha$ | 学习率 | 0.001 |
| $\beta_1$ | 一阶矩衰减 | 0.9 |
| $\beta_2$ | 二阶矩衰减 | 0.999 |
| $\varepsilon$ | 数值稳定 | 10⁻⁸ |

## 优点

- 自适应学习率
- 对超参数选择相对鲁棒
- 适合大多数深度学习任务

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_05/1_NeuralNetworks-summary.md]]
