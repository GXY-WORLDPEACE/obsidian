---
title: "Generative Model"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #generative-model
type: concept
related_lectures:
  - 12
---

# Generative Model 生成模型

## 定义

生成模型学习数据的分布，能够生成与训练数据相似的新样本。

## 与判别模型对比

| 类型 | 学习 | 用途 |
|------|------|------|
| 判别模型 | P(y|x) | 分类、回归 |
| **生成模型** | P(x) 或 P(x\|y) | 生成新样本 |

## 分类

### 显式密度模型

可计算精确的概率密度：

| 模型 | 密度函数 | 特点 |
|------|----------|------|
| PixelRNN | p(x) = ∏ p(x_i\|x_{<i}) | 逐像素生成 |
| NVRA | 可逆网络 | 精确似然 |
| VAE | 变分下界 | 近似密度 |
| Flow | 可逆变换 | 精确密度 |

### 隐式密度模型

不可精确计算密度：

| 模型 | 方法 | 特点 |
|------|------|------|
| GAN | 对抗训练 | 样本质量高 |
| Diffusion | 去噪过程 | 训练稳定 |

## 评估指标

| 指标 | 说明 |
|------|------|
| Inception Score (IS) | 衡量多样性和质量 |
| FID | Fréchet Inception Distance，越小越好 |
| Precision/Recall | 精确率和召回率 |

## 代表模型

| 模型 | 类型 | 应用 |
|------|------|------|
| VAE | 显式/变分 | 图像生成、编辑 |
| GAN | 隐式 | 人脸、风格迁移 |
| Diffusion | 隐式 | 文生图、视频 |

## 相关概念

- [[Autoencoder]]
- [[Variational Autoencoder]]
- [[GAN]]
- [[Diffusion Model]]

## 来源

[[summaries/I2DL-Lecture-12-Advanced-Topics]]
