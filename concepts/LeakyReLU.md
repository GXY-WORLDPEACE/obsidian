---
title: "LeakyReLU"
date: 2026-06-03
tags:
  - #概念 #激活函数
---

# LeakyReLU

## 定义

$$ f(x) = \max(0, x) + \alpha \cdot \min(0, x) = \begin{cases} x & x > 0 \\ \alpha x & x \leq 0 \end{cases} $$

## 参数

- $\alpha$: 负轴斜率，通常设为 0.01

## 与 ReLU 的区别

| 特性 | ReLU | LeakyReLU |
|------|------|-----------|
| 负轴输出 | 0 | $\alpha x$ |
| 死神经元 | 有 | 无 |

## 优势

- 解决 ReLU 的"死神经元"问题
- 允许负值有微弱梯度
- 计算仍然高效

## 导数

$$ f'(x) = \begin{cases} 1 & x > 0 \\ \alpha & x \leq 0 \end{cases} $$

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/1_cifar10_classification-summary.md]]
