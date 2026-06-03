---
title: "Random Search"
date: 2026-06-03
tags:
  - #概念 #超参数调优
---

# Random Search (随机搜索)

## 定义

从超参数范围内随机采样，找到最佳配置。

## 示例

```python
from scipy.stats import uniform

best_acc = 0
best_params = {}

for _ in range(100):
    lr = uniform(1e-4, 1e-1).rvs()  # [1e-4, 1e-1)
    reg = uniform(1e-6, 1e-2).rvs()  # [1e-6, 1e-2)
    
    model = train(lr=lr, reg=reg)
    acc = evaluate(model)
    
    if acc > best_acc:
        best_acc = acc
        best_params = {'lr': lr, 'reg': reg}
```

## 优缺点

| 优点 | 缺点 |
|------|------|
| 高维友好 | 可能错过最优 |
| 效率高 | 结果不稳定 |
| 简单 | - |

## 为什么比 Grid Search 更好？

当超参数重要性不同时，Random Search 能探索更多值。

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/1_cifar10_classification-summary.md]]
