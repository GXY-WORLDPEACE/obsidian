---
title: "Variational Autoencoder (VAE)"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #generative-model
type: concept
related_lectures:
  - 12
---

# Variational Autoencoder (VAE) 变分自编码器

## 定义

VAE是一种基于变分推断的生成模型，通过学习数据的潜在分布实现样本生成。与标准自编码器不同，VAE的潜在空间是概率分布。

## 核心架构

```
Input(x) → Encoder → μ, σ → z ~ N(μ, σ) → Decoder → Output(x')
```

## 损失函数

```
L = L_reconstruction + L_KL

L_reconstruction = -E_{z~q}[log p(x|z)]  # 重构损失
L_KL = D_KL(q(z|x) || p(z))              # KL散度
```

### KL散度项

使学到的分布 $q(z|x) = N(μ, σ²)$ 接近先验 $p(z) = N(0, I)$：

```
D_KL = 0.5 * Σ (σ² + μ² - 1 - log(σ²))
```

## 关键特性

| 特性 | 说明 |
|------|------|
| 连续潜在空间 | 可插值生成新样本 |
| 生成能力 | 从随机向量生成样本 |
| 概率解释 | 显式建模数据分布 |

## 与标准自编码器对比

| 特性 | Autoencoder | VAE |
|------|-------------|-----|
| 潜在空间 | 确定性向量 | 概率分布 |
| 生成能力 | 无 | 有 |
| 插值 | 模糊 | 平滑过渡 |
| 训练 | 重构损失 | 重构 + KL |

## 应用

| 应用 | 说明 |
|------|------|
| 图像生成 | 人脸、场景生成 |
| 图像编辑 | 潜在空间操作 |
| 异常检测 | 重构误差 |
| 可解释性 | 潜在变量语义 |

## PyTorch 示例

```python
class VAE(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(input_dim, 256), nn.ReLU())
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_logvar = nn.Linear(256, latent_dim)
        self.decoder = nn.Sequential(nn.Linear(latent_dim, 256), nn.ReLU(),
                                     nn.Linear(256, input_dim), nn.Sigmoid())
    
    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5*logvar)
        return mu + std * torch.randn_like(std)
    
    def forward(self, x):
        h = self.encoder(x)
        mu, logvar = self.fc_mu(h), self.fc_logvar(h)
        z = self.reparameterize(mu, logvar)
        return self.decoder(z), mu, logvar

def vae_loss(recon_x, x, mu, logvar):
    recon = F.binary_cross_entropy(recon_x, x)
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return recon + kl
```

## 相关概念

- [[Autoencoder]]
- [[Generative Model]]
- [[GAN]]
- [[Diffusion Model]]

## 来源

[[summaries/I2DL-Lecture-12-Advanced-Topics]]
