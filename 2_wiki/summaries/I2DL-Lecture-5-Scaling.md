---
title: "I2DL L05: Scaling Optimization"
date: 2026-04-16
tags:
  - #I2DL #讲义 #优化 #规模化
course: I2DL
lecture: 5
---

# I2DL Lecture 5: Scaling Optimization

## 摘要
本讲聚焦大规模深度学习的优化技术，包括 Mini-batch SGD、学习率调度、Adam 自适应优化器，以及 batch normalization。

## 核心内容

### Mini-batch SGD
将数据分成小批量进行训练，平衡计算效率与梯度估计准确性。

| 配置 | 优点 | 缺点 |
|------|------|------|
| 小 batch (32-128) | 泛化好，更新频繁 | 梯度噪声大 |
| 大 batch (1024+) | 梯度估计准，并行效率高 | 泛化可能下降 |

### 学习率调度
| 方法 | 说明 |
|------|------|
| **Step Decay** | 每 N 个 epoch 降低学习率 |
| **Cosine Annealing** | 余弦曲线衰减 |
| **Warmup** | 初期逐渐增大学习率 |

### Adam 优化器
结合动量与 RMSProp：
- 动量项：加速收敛
- 自适应学习率：各参数独立调整
- 偏差校正：弥补初始化偏差

### Batch Normalization
在每层输入前做标准化：
$$\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}$$

作用：稳定训练、允许更高学习率、轻微正则化效果。

## 关键概念
- Mini-batch
- Learning Rate Schedule
- Adam / AdamW
- Batch Normalization
- Weight Decay

## 概念关联
- [[2_wiki/summaries/I2DL-Lecture-4-Optimization]] - 基础优化
- [[2_wiki/concepts/Deep Learning]] - 训练技术

## 来源
[[1_raw/articles/I2DL/lectures/5.scaling_optimization.pdf]]
