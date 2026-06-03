---
title: "Hyperparameter Tuning"
date: 2026-06-03
tags:
  - #概念 #机器学习
---

# Hyperparameter Tuning (超参数调优)

## 定义

超参数是在训练前设置的参数，不能从数据中直接学习。

## 常见超参数

| 类别 | 超参数 |
|------|--------|
| 网络结构 | 层数、隐藏层大小、激活函数 |
| 优化 | 学习率、动量、批大小 |
| 正则化 | L1/L2 强度、Dropout |
| 训练 | epochs、early stopping |

## 调优方法

1. **手动调参** — 基于经验调整
2. **网格搜索 (Grid Search)** — 遍历所有组合
3. **随机搜索 (Random Search)** — 随机采样
4. **贝叶斯优化** — 基于概率模型

## 最佳实践

1. 先在小数据集上验证代码
2. 粗略搜索宽范围
3. 精细搜索窄范围
4. 使用验证集评估

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/1_cifar10_classification-summary.md]]
