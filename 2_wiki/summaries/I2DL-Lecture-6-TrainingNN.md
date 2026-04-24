---
title: "I2DL L06: Training Neural Networks"
date: 2026-04-16
tags:
  - #I2DL #讲义 #训练技巧
course: I2DL
lecture: 6
---

# I2DL Lecture 6: Training Neural Networks

## 摘要
本讲系统讲解神经网络训练的最佳实践，包括数据划分、超参数调优、debug 策略和工程技巧。

## 核心内容

### 数据划分
```
训练集 (80%) → 验证集 (10%) → 测试集 (10%)
```
- **训练集**：模型学习
- **验证集**：超参数调优、早停
- **测试集**：最终评估（不可用于调参）

### 超参数调优
| 类型 | 示例 | 重要性 |
|------|------|--------|
| **模型架构** | 层数、宽度、激活函数 | 高 |
| **优化器** | 学习率、batch size、momentum | 高 |
| **正则化** | dropout、weight decay | 中 |
| **初始化** | Xavier、Kaiming | 中 |

### Debug 策略
1. 检查数据预处理和增强
2. 用小数据集验证过拟合能力
3. 监控训练/验证损失差距
4. 梯度检查 (gradient checking)

### 工程技巧
- **权重初始化**：Xavier (tanh)、Kaiming (ReLU)
- **Learning Rate Finder**：寻找最优学习率
- **Gradient Clipping**：防止梯度爆炸

## 关键概念
- Hold-out Validation
- Cross-validation
- Hyperparameter Search
- Learning Rate Range Test

## 概念关联
- [[2_wiki/summaries/I2DL-Lecture-4-Optimization]] - 优化基础
- [[2_wiki/summaries/I2DL-Lecture-5-Scaling]] - 规模化训练

## 来源
[[1_raw/articles/I2DL/lectures/6.trainingnn.pdf]]
