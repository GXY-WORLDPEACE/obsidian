---
title: "TensorBoard"
date: 2026-06-03
tags:
  - #概念 #可视化
---

# TensorBoard

## 概述

TensorFlow 的可视化工具，可用于任何深度学习框架。用于监控训练过程和调试模型。

## 安装与启动

```bash
pip install tensorboard
tensorboard --logdir=./logs
```

## 常用 API

| 方法 | 用途 |
|------|------|
| `add_scalar` | 标量（loss, accuracy） |
| `add_image` | 单张图像 |
| `add_images` | 多张图像网格 |
| `add_figure` | matplotlib 图表 |
| `add_histogram` | 分布（权重、梯度） |
| `add_graph` | 网络结构图 |

## 使用示例

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('logs/run_1')

for step in range(1000):
    writer.add_scalar('train/loss', loss, step)
    writer.add_scalar('train/acc', acc, step)

writer.close()
```

## 可视化内容

1. **SCALARS**: 标量变化曲线
2. **IMAGES**: 输入/输出图像
3. **GRAPHS**: 网络结构图
4. **HISTOGRAMS**: 权重/梯度分布

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_07/1_pytorch-summary.md]]
