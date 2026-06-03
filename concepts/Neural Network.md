---
title: "Neural Network"
date: 2026-06-03
tags:
  - #概念 #深度学习 #神经网络
---

# Neural Network (神经网络)

## 定义

由多个层组成的计算模型，模拟生物神经网络的结构进行信息处理。

## 基本结构

```
输入层 → 隐藏层1 → 隐藏层2 → ... → 输出层
```

## 前向传播

$$ z^{(l)} = W^{(l)} \cdot a^{(l-1)} + b^{(l)} $$
$$ a^{(l)} = \sigma(z^{(l)}) $$

其中 $\sigma$ 是激活函数。

## 反向传播

使用链式法则计算梯度：
$$ \frac{\partial L}{\partial W^{(l)}} = \frac{\partial L}{\partial a^{(L)}} \cdot \frac{\partial a^{(L)}}{\partial a^{(L-1)}} \cdots \frac{\partial a^{(l+1)}}{\partial a^{(l)}} \cdot \frac{\partial a^{(l)}}{\partial W^{(l)}} $