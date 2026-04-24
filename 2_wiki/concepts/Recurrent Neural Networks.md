---
title: "Recurrent Neural Networks"
date: 2026-04-16
aliases: ["RNN", "循环神经网络"]
tags:
  - #概念 #RNN #序列处理
  - #I2DL
---

# RNN (循环神经网络)

## 设计理念

RNN 专为**序列数据**设计，能够处理任意长度的序列输入，通过**隐藏状态**传递历史信息。

```
x_t ──┐
      ├─→ [隐藏状态 h_t] ──→ 输出 y_t
      │
← ────┘  (循环连接)
```

## 核心问题

| 问题 | 描述 | 解决方案 |
|------|------|----------|
| 梯度消失 | 长序列信息丢失 | LSTM, GRU |
| 梯度爆炸 | 训练不稳定 | 梯度裁剪 |
| 长期依赖 | 难以学习远距离依赖 | Attention |

## 变体架构

### LSTM (Long Short-Term Memory)
- 门控机制：输入门、遗忘门、输出门
- 细胞状态：长期记忆载体

### GRU (Gated Recurrent Unit)
- 更简洁：重置门、更新门
- 计算效率更高

## 应用场景

- NLP (自然语言处理)
- 时间序列预测
- 语音识别
- 音乐生成

## 相关概念

- [[Neural Networks]] - 神经网络基础
- [[Transformers]] - Transformer (解决 RNN 局限性)
- [[Deep Learning]] - 深度学习

## 课程来源

- [[summaries/I2DL-Lecture-1-Introduction]]