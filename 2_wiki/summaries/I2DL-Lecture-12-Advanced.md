---
title: "I2DL L12: Advanced Deep Learning Topics"
date: 2026-04-16
tags:
  - #I2DL #讲义 #高级话题
course: I2DL
lecture: 12
---

# I2DL Lecture 12: Advanced Deep Learning Topics

## 摘要
本讲涵盖深度学习前沿话题，包括生成模型（VAE、GAN）、图神经网络(GNN)、自监督学习和大型语言模型(LLM)基础。

## 生成模型

### VAE (Variational Autoencoder)
变分自编码器，学习隐空间的概率分布：
- 编码器输出均值和方差
- 从隐分布采样
- 解码器重建

### GAN (Generative Adversarial Network)
对抗训练：
- **生成器 G**：生成假样本
- **判别器 D**：区分真假
- 博弈均衡：$G^*$ 使 $D(G(z))$ 接近 0.5

## 图神经网络 (GNN)

### 消息传递框架
$$h_v^{(k+1)} = \text{UPDATE}(h_v^{(k)}, \text{AGG}(\{h_u^{(k)}: u \in N(v)\}))$$

### GNN 类型
| 类型 | 特点 |
|------|------|
| **GCN** | 图卷积，谱方法 |
| **GraphSAGE** | 归纳学习，采样邻居 |
| **GAT** | 图注意力网络 |

## 自监督学习

### 对比学习
通过区分正负样本学习表示：
- **SimCLR**：裁剪增强 + 双塔网络
- **MoCo**：动量编码器

### 掩码语言/图像建模
- **BERT**：掩码词预测
- **MAE**：掩码图像块重建

## 大语言模型 (LLM)

### GPT 系列
- **GPT-1/2/3**：Decoder-only，Next Token Prediction
- **Instruction Tuning**：指令微调
- **RLHF**：人类反馈强化学习

### Scaling Laws
模型性能与参数量、数据量、计算量的幂律关系。

## 关键概念
- Latent Space
- Adversarial Training
- Message Passing
- Contrastive Learning
- Foundation Models

## 概念关联
- [[2_wiki/concepts/Deep Learning]] - 基础概念
- [[2_wiki/concepts/Transformers]] - Transformer 基础

## 来源
[[1_raw/articles/I2DL/lectures/12.advanced_dl_topics.pdf]]
