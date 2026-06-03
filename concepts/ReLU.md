---
title: "ReLU"
date: 2026-06-03
tags:
  - #概念 #激活函数
---

# ReLU (Rectified Linear Unit)

## 定义

$$ ReLU(x) = \max(0, x) = \begin{cases} x & \text{if } x > 0 \\ 0 & \text{if } x \leq 0 \end{cases} $$

## 性质

- 计算高效：只需一次比较操作
- 稀疏激活