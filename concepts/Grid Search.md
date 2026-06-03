---
title: "Grid Search"
date: 2026-06-03
tags:
  - #概念 #超参数调优
---

# Grid Search (网格搜索)

## 定义

遍历所有超参数组合，找到最佳配置。

## 示例

```python
learning_rates = [0.001, 0.01, 0.1]
regs = [1e-4, 1e-3]

best_acc = 0
best_params = {}

for lr in learning_rates:
    for reg in regs:
        model = train(lr=lr, reg=reg)
        acc = evaluate(model)
        if acc > best_acc:
            best_acc = acc
            best_params = {'lr': lr, 'reg': reg}
```

## 优缺点

| 优点 | 缺点 |
|------|------|
| 简单直观 | 维度爆炸 |
| 可并行化 | 效率低 |
| 覆盖全面 | 冗余搜索 |

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/