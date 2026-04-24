---
title: "Neural Network"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #neural-network
type: concept
related_lectures:
  - 3
  - 4
---

# Neural Network 神经网络

## 定义

神经网络是一种受人脑启发的计算模型，由大量相互连接的"神经元"组成，能够从数据中学习复杂的模式。

## 基本结构

```
Input Layer → Hidden Layers → Output Layer
  (输入层)      (隐藏层)         (输出层)
```

### 神经元 (Neuron)

```
y = f(Σwᵢxᵢ + b) = f(w·x + b)
```

其中：
- $x_i$: 输入特征
- $w_i$: 权重
- $b$: 偏置
- $f$: 激活函数

## 核心概念

### 1. 激活函数 (Activation Function)

| 函数 | 公式 | 特点 |
|------|------|------|
| Sigmoid | σ(x) = 1/(1+e⁻ˣ) | 输出[0,1]，易梯度消失 |
| Tanh | tanh(x) | 输出[-1,1]，零中心 |
| ReLU | max(0,x) | 计算高效，缓解梯度消失 |
| Leaky ReLU | max(0.01x, x) | 避免死亡ReLU问题 |
| Softmax | σ(x)ᵢ = eˣⁱ/Σeˣʲ | 多分类输出概率 |

### 2. 损失函数 (Loss Function)

| 类型 | 函数 | 用途 |
|------|------|------|
| MSE | (1/n)Σ(y-ŷ)² | 回归任务 |
| Cross-Entropy | -Σy·log(ŷ) | 分类任务 |
| Hinge Loss | max(0, 1-y·ŷ) | SVM |

### 3. 前向传播 (Forward Propagation)

```
Input → Linear(W·x+b) → Activation → ... → Output
```

### 4. 反向传播 (Backpropagation)

通过链式法则计算梯度：
```
∂L/∂W = ∂L/∂ŷ · ∂ŷ/∂z · ∂z/∂W
```

## 网络类型

| 类型 | 特点 | 应用 |
|------|------|------|
| FFNN | 全连接前馈 | 简单分类 |
| CNN | 卷积神经网络 | 图像处理 |
| RNN | 循环神经网络 | 序列数据 |
| Transformer | 自注意力 | NLP |

## 相关概念

- [[Neural Network#Activation Function]]
- [[Neural Network#Backpropagation]]
- [[Perceptron]]
- [[Loss Function]]
- [[Optimizer]]

## 来源

[[summaries/I2DL-Lecture-03-Intro-to-NN]]
