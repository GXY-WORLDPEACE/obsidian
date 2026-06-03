---
title: "Xavier Initialization"
date: 2026-06-03
tags:
  - #概念 #权重初始化
---

# Xavier Initialization (Glorot 初始化)

## 提出者

Xavier Glorot 和 Yoshua Bengio (2010)

## 公式

从分布 $\mathcal{N}(0, \sigma^2)$ 采样，其中：

$$ \sigma = gain \times \sqrt