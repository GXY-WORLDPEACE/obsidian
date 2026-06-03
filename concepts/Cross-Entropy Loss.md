---
title: "Cross-Entropy Loss"
date: 2026-06-03
tags:
  - #概念 #损失函数
---

# Cross-Entropy Loss (交叉熵损失)

## 定义

$$ CE(\hat{y}, y) = -\frac{1}{N} \sum_{i=1}^{N} \sum_{k=1}^{C} y_{ik} \log(\hat{y}_{ik}) $$

## 参数说明

- $N$: 样本数量
- $C$: 类别数量
- $y_{ik}$: 第 i 个样本的第 k 类标签（one-hot 编码）
- $\hat{y}_{ik}$: 模型预测的第 i 个样本属于第 k 类的概率

## 与 Binary Cross-Entropy 的关系

当 $C=2$ 时，Cross-Entropy 退化为 Binary Cross-Entropy。

## 与 Softmax 的关系

通常与 Softmax 一起使用：
1. Softmax 将 logits 转为概率
2. Cross-Entropy 计算概率与真实标签的距离

## 优点

- 梯度在预测正确时较小，错误时较大
- 与 Softmax 结合时梯度计算简洁

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_05/1_NeuralNetworks-summary.md]]
