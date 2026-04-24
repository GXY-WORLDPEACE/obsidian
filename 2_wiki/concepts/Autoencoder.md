---
title: "Autoencoder"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #generative-model
type: concept
related_lectures:
  - 12
---

# Autoencoder 自编码器

## 定义

自编码器是一种无监督学习模型，通过编码器将数据压缩到低维潜在空间，再通过解码器重构原始数据。

## 核心架构

```
Input(x) → Encoder → Latent Code(z) → Decoder → Output(x')
           (压缩)      (瓶颈)         (重构)
```

### 编码器
```
z = f(W_enc · x + b_enc)
```

### 解码器
```
x' = f(W_dec · z + b_dec)
```

## 损失函数

```
L = ||x - x'||² = ||x - Decoder(Encoder(x))||²
```

最小化重构误差

## 类型

### 1. 标准自编码器 (Vanilla AE)

最简单的编码器-解码器结构

### 2. 去噪自编码器 (Denoising AE)

```
x' = Decoder(Encoder(x + noise))
```

提高鲁棒性

### 3. 稀疏自编码器 (Sparse AE)

添加稀疏惩罚：
```
L = ||x - x'||² + λ · Σ |h_j|
```

### 4. 变分自编码器 (VAE)

潜在空间是概率分布，见 [[Variational Autoencoder]]

## 应用

| 应用 | 说明 |
|------|------|
| 降维 | 可视化高维数据 |
| 特征提取 | 学习有用表示 |
| 预训练 | 初始化网络权重 |
| 异常检测 | 重构误差大的样本 |
| 图像去噪 | 去噪自编码器 |
| 超分辨率 | 像素级预测 |
| 语义分割 | 医学图像分割 |

## 与 PCA 对比

| 特性 | PCA | Autoencoder |
|------|-----|-------------|
| 线性 | 线性 | 非线性 |
| 表达能力 | 有限 | 强 |
| 激活函数 | 无 | 可用非线性 |
| 应用 | 统计 | 深度学习 |

## PyTorch 示例

```python
class Autoencoder(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, input_dim),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)

# 训练
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
```

## 相关概念

- [[Variational Autoencoder]]
- [[Generative Model]]
- [[Neural Network]]
- [[Feature Learning]]

## 来源

[[summaries/I2DL-Lecture-12-Advanced-Topics]]
