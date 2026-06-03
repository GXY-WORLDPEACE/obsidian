---
title: "Early Stopping"
date: 2026-06-03
tags:
  - #概念 #正则化
---

# Early Stopping (早停)

## 定义

当验证集性能不再提升时停止训练，防止过拟合。

## 算法

```
best_loss = infinity
patience = 10
counter = 0

for epoch in epochs:
    train(model)
    val_loss = validate(model)
    
    if val_loss < best_loss:
        best_loss = val_loss
        counter = 0
        save(model)  # 保存最佳模型
    else:
        counter += 1
    
    if counter >= patience:
        break  # 停止训练
```

## 参数说明

| 参数 | 说明 |
|------|------|
| patience | 容忍不提升的 epoch 数 |
| best_loss | 历史最佳验证损失 |

## 优势

- 防止过拟合
- 节省训练时间
- 无需手动设置 epochs

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/1_cifar10_classification-summary.md]]
