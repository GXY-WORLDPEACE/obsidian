---
title: "PyTorch"
date: 2026-06-03
tags:
  - #概念 #深度学习框架
---

# PyTorch

## 概述

Facebook 开发的开源深度学习框架，以其灵活性和易用性著称。

## 核心特点

- **动态计算图**: 运行时构建图，便于调试
- **autograd**: 自动微分
- **GPU 加速**: 简单调用 `.to(device)`
- **丰富的生态**: torchvision, torchtext, torchaudio

## 基础组件

| 组件 | 说明 |
|------|------|
| `torch.Tensor` | 张量，类似 NumPy |
| `nn.Module` | 神经网络基类 |
| `torch.optim` | 优化器 |
| `torch.utils.data` | 数据加载 |

## 简单示例

```python
import torch
import torch.nn as nn

# 定义模型
model = nn.Sequential(
    nn.Linear(784