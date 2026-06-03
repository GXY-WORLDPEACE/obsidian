---
title: "SGD with Momentum"
date: 2026-06-03
tags:
  - #概念 #优化算法
---

# SGD with Momentum (动量梯度下降)

## 标准 SGD 的问题

- 在陡峭方向震荡
- 在平缓方向收敛慢

## Momentum 思想

累积历史梯度方向，类似物理中的"惯性"。

## 更新公式

$$ v^{k+1} = \beta v^{k} - \alpha \nabla_{\theta} L(\theta^{k}) $$
$$ \theta^{k+1} = \theta^{k} + v^{k+1} $$

## 参数说明

| 参数 | 说明 | 常用值 |
|------|------|--------|
| $v$ | 速度/动量项 | - |
| $\beta$ | 动量系数 | 0.9 |
| $\alpha$ | 学习率 | 0.01 |
| $\nabla L$ | 损失梯度 | - |

## 直观理解

- 动量累积了之前的更新方向
- 减少震荡，加速收敛
- 类似小球在碗中滚动

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_05/1_NeuralNetworks-summary.md]]
