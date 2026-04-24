---
title: "I2DL Lecture 12 - Advanced Deep Learning Topics"
date: 2026-04-24
tags:
  - #I2DL
  - #lecture
  - #advanced
type: lecture_summary
course: I2DL
source: 1_raw/articles/I2DL/lectures/12.advanced_dl_topics.pdf
---

# I2DL Lecture 12: 高级深度学习主题

## 摘要

本讲涵盖图神经网络（GNN）、生成模型（Autoencoder、VAE、GAN、Diffusion）以及强化学习（RL）。GNN 用于处理图结构数据，生成模型用于创建新样本，强化学习通过与环境交互学习策略。

## 核心内容

### 1. 图神经网络 (GNN)

**核心挑战**:
- 输入大小可变（节点和边数量不固定）
- 对节点排列不变性

**消息传递**:
```
节点 → 边: 更新边嵌入
边 → 节点: 聚合邻居信息更新节点
```

**应用**:
- 节点/边分类（欺诈检测、社交网络）
- 场景图生成
- 3D网格分类与生成
- 交通预测

### 2. 生成模型

**分类**:

| 类型 | 代表模型 | 特点 |
|------|----------|------|
| 显式密度 | VAE, Flow | 可计算精确概率 |
| 隐式密度 | GAN, DDPM | 不可精确计算概率 |

### 3. Autoencoder

**结构**: Encoder → 潜在空间 z → Decoder

**应用**:
- 预训练/特征提取
- 像素级预测（分割、超分辨率、深度估计）

### 4. Variational Autoencoder (VAE)

**特点**: 潜在空间是概率分布（高斯）

**训练**: 重构损失 + KL散度（使潜在空间接近标准高斯）

**优势**: 可从随机向量生成新样本

### 5. GAN (Generative Adversarial Networks)

**架构**: Generator (生成器) vs Discriminator (判别器) 对抗训练

**损失函数**:
```
min_G max_D L(G, D) = E[log D(x)] + E[log(1-D(G(z)))]
```

**应用**:
- BigGAN: 高清图像生成
- StyleGAN: 人脸生成
- CycleGAN: 风格迁移
- SPADE: 语义图像合成

### 6. Diffusion Models

**原理**:
- 前向过程: 逐步添加噪声
- 反向过程: 学习去噪

**应用**:
- Text-to-image (DALL-E 2, Stable Diffusion)
- Image inpainting
- Text-to-3D (DreamFusion)

### 7. 强化学习 (RL)

**核心概念**:
- Agent 与 Environment 交互
- 奖励信号指导学习
- MDP 定义: (S, A, R, P, γ)

**算法分类**:
- Model-free: DQN, Policy Gradient, DDPG, PPO
- Model-based: 学习环境模型

**里程碑**:
- DQN (Atari游戏)
- AlphaZero (围棋、星际争霸)

### 8. 课程总结

| 主题 | 关键概念 |
|------|----------|
| ML基础 | 监督/无监督学习、线性/逻辑回归 |
| 神经网络 | 反向传播、激活函数、损失函数 |
| 训练技巧 | 梯度下降/SGD、正则化、超参数调优 |
| CNN | 卷积、池化、经典架构 (AlexNet, VGG, ResNet) |
| RNN/Transformer | LSTM、注意力机制、位置编码 |
| 生成模型 | Autoencoder, VAE, GAN, Diffusion |
| GNN | 消息传递、图卷积 |
| RL | MDP、策略、价值函数 |

## 相关概念

- [[concepts/Graph Neural Network]]
- [[concepts/Autoencoder]]
- [[concepts/Variational Autoencoder]]
- [[concepts/GAN]]
- [[concepts/Diffusion Model]]
- [[concepts/Reinforcement Learning]]

## 来源

[[1_raw/articles/I2DL/lectures/12.advanced_dl_topics.pdf]]