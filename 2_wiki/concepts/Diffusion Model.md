---
title: "Diffusion Model"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #generative-model
type: concept
related_lectures:
  - 12
---

# Diffusion Model 扩散模型

## 定义

扩散模型是一类基于逐步去噪思想的生成模型，通过学习反向过程（从噪声恢复数据）来生成样本。

## 核心原理

### 两阶段过程

```
数据 x₀ → x₁ → x₂ → ... → x_T (噪声)  [前向过程]
          ↑       ↑           ↑
          …       …           …      [反向过程]
        x₀ ← x₁ ← x₂ ← ... ← x_T
```

### 1. 前向过程 (Forward/Diffusion)

逐步添加高斯噪声：
```
q(x_t | x_{t-1}) = N(x_t; √(1-β_t)x_{t-1}, β_t I)
```

最终 $x_T ≈ N(0, I)$（纯噪声）

### 2. 反向过程 (Reverse)

学习去噪：
```
p_θ(x_{t-1} | x_t) = N(μ_θ(x_t, t), Σ_θ(x_t, t))
```

## 训练目标

最小化变分下界：
```
L = E_q [D_KL(q(x_T|x_0) || p(x_T)) 
        + Σ_t D_KL(q(x_{t-1}|x_t,x_0) || p_θ(x_{t-1}|x_t))]
```

### 简化目标

```python
# 预测噪声 ε
loss = ||ε - ε_θ(x_t, t)||²
```

## 经典模型

| 模型 | 年份 | 特点 |
|------|------|------|
| DDPM | 2020 | 基础扩散模型 |
| Improved DDPM | 2021 | 改进训练 |
| ADM / DALL-E 2 | 2022 | Classifier-free guidance |
| Stable Diffusion | 2022 | 潜在扩散，效率高 |
| SDXL | 2023 | 高分辨率 |

## 潜在扩散 (Latent Diffusion)

```
图像 → Encoder → 潜在空间 z → 扩散/去噪 → Decoder → 图像
```

优势：计算量大降，效率提升

## 与 GAN 对比

| 特性 | GAN | Diffusion |
|------|-----|-----------|
| 训练稳定性 | 差 | 好 |
| 样本质量 | 高 | 高 |
| 推理速度 | 快 | 慢(需多步) |
| 模式覆盖 | 部分 | 全面 |
| 似然计算 | 不可 | 可 |

## 应用

| 应用 | 说明 |
|------|------|
| Text-to-Image | DALL-E 2, Stable Diffusion |
| Image-to-Image | 风格迁移、局部编辑 |
| Inpainting | 图像修复 |
| Text-to-3D | DreamFusion |
| 视频生成 | Video Diffusion |

## 相关概念

- [[Autoencoder]]
- [[VAE]]
- [[GAN]]
- [[Generative Model]]

## 来源

[[summaries/I2DL-Lecture-12-Advanced-Topics]]
