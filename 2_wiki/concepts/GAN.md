---
title: "GAN (Generative Adversarial Network)"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #generative-model
type: concept
related_lectures:
  - 12
---

# GAN (Generative Adversarial Network) 生成对抗网络

## 定义

GAN由Ian Goodfellow等人于2014年提出，是一种隐式密度生成模型，通过对抗训练学习数据分布。

## 核心架构

```
        噪声 z
          ↓
    ┌─────────────┐
    │  Generator  │  → 生成样本 G(z)
    └─────────────┘
          ↓
    ┌─────────────┐     真实样本 x
    │Discriminator│ ←────────────────
    └─────────────┘
          ↓
      输出 D(x) / D(G(z))
```

## 训练目标

**极小极大博弈**：

```
min_G max_D L(G, D) = E_x[log D(x)] + E_z[log(1-D(G(z)))]
```

| 解释 | 说明 |
|------|------|
| D 的目标 | 最大化 log D(x) + log(1-D(G(z))) |
| G 的目标 | 最小化 log(1-D(G(z))) |

## 训练过程

1. **训练判别器D**：用真实样本(标签=1)和生成样本(标签=0)训练二分类器
2. **训练生成器G**：固定D，最小化 log(1-D(G(z)))

### 伪代码

```python
for epoch in range(epochs):
    # 训练判别器
    for _ in range(k):
        z = noise(batch_size)
        fake = G(z)
        d_loss = -mean(log(D(real)) + log(1-D(fake)))
        
    # 训练生成器
    z = noise(batch_size)
    g_loss = -mean(log(D(G(z))))
```

## 经典变体

| 模型 | 年份 | 贡献 |
|------|------|------|
| DCGAN | 2015 | CNN + GAN，稳定性改进 |
| WGAN | 2017 | Wasserstein距离，解决模式崩溃 |
| Progressive GAN | 2017 | 渐进式生成高清图像 |
| StyleGAN | 2018 | 风格控制，人脸生成 |
| BigGAN | 2019 | 大规模高清图像生成 |
| CycleGAN | 2020 | 风格迁移，无配对数据 |
| StyleGAN3 | 2021 | 消除aliasing |

## 应用

| 领域 | 应用 |
|------|------|
| 图像生成 | 人脸、风景、艺术创作 |
| 风格迁移 | CycleGAN, StarGAN |
| 图像编辑 | 局部修改，属性编辑 |
| 超分辨率 | SRGAN |
| 数据增强 | 增加训练样本多样性 |

## 训练技巧

| 技巧 | 说明 |
|------|------|
| 标签平滑 | 真实标签用0.9代替1 |
| 谱归一化 | 稳定D的训练 |
| TTUR | 不同的D和G学习率 |
| minibatch discrimination | 避免模式崩溃 |

## 问题与挑战

| 问题 | 解决方案 |
|------|----------|
| 模式崩溃 | WGAN, 小批量 discrimination |
| 训练不稳定 | 谱归一化，标签平滑 |
| 评估困难 | FID, IS指标 |

## 相关概念

- [[Autoencoder]]
- [[Variational Autoencoder]]
- [[Diffusion Model]]
- [[Generative Model]]

## 来源

[[summaries/I2DL-Lecture-12-Advanced-Topics]]
