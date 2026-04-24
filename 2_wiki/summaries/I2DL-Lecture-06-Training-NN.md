---
title: "I2DL Lecture 6 - Training Neural Networks"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #training
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/6.trainingnn.pdf
---

# I2DL Lecture 6: 神经网络训练实践

## 摘要

本讲聚焦神经网络训练的实践技巧，包括学习率调度、过拟合诊断、数据划分、调试策略等。

## 核心内容

### 1. 学习率的影响

| 学习率 | 表现 |
|--------|------|
| 太高 | 震荡/发散 |
| 太低 | 收敛慢 |
| 合适 | 稳定下降 |

### 2. 学习率衰减

```
α = α₀ / (1 + decay_rate × epoch)
```

其他策略：
- Step decay: 每N个epoch乘以固定比例
- Exponential decay: α = α₀ · t^epoch
- Cosine annealing

### 3. 数据划分

```
训练集 (60-80%) → 学习参数
验证集 (10-20%) → 调超参数
测试集 (10-20%) → 最终评估（不触碰）
```

### 4. 过拟合与欠拟合

| 状态 | 训练损失 | 验证损失 | 解决方案 |
|------|----------|----------|----------|
| 欠拟合 | 高 | 高 | 增加模型复杂度 |
| 合适 | 低 | 最低 | 保持 |
| 过拟合 | 低 | 高 | 正则化、数据增强 |

### 5. 学习曲线诊断

- **持续下降**: 欠拟合，增加模型容量
- **验证曲线上升**: 过拟合，增加正则化
- **Gap太大**: 泛化差

### 6. 调试策略

1. **从小开始**: 单样本过拟合 → 少量样本 → 全量
2. **单一变量**: 每次只改一个因素
3. **可视化**: 画损失曲线、预测结果
4. **计时**: 检查数据加载、计算瓶颈

### 7. 常见错误

- 未切换 train/eval 模式（dropout等）
- 未 zero_grad()
- Softmax输出传入需要logits的loss
- 测试集混入训练数据

### 8. 超参数调优

| 方法 | 特点 |
|------|------|
| 手动搜索 | 依赖经验，最常用 |
| Grid search | 穷举，结构化 |
| Random search | 更高效，发现意外好配置 |

### 9. 训练流程建议

1. 检查单样本过拟合
2. 少量样本验证流程
3. 粗粒度网格搜索
4. 细化搜索区间
5. 最终长时训练

## 相关概念

- [[concepts/Learning Rate]]
- [[concepts/Learning Rate Decay]]
- [[concepts/Overfitting]]
- [[concepts/Underfitting]]
- [[concepts/Regularization]]
- [[concepts/Cross Validation]]

## 来源

[[1_raw/articles/I2DL/lectures/6.trainingnn.pdf]]