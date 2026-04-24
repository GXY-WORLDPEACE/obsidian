---
title: "Graph Neural Network"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #gnn
type: concept
related_lectures:
  - 12
---

# Graph Neural Network (GNN) 图神经网络

## 定义

GNN是一类专门用于处理图结构数据的神经网络，能够学习节点和边的表示，广泛应用于社交网络、分子分析、推荐系统等。

## 核心挑战

| 挑战 | 说明 |
|------|------|
| 输入大小可变 | 节点和边数量不固定 |
| 节点排列不变性 | 不同的图表示顺序应得到相同结果 |
| 无固定结构 | 无法使用卷积的网格假设 |

## 消息传递框架

```
节点 → 边: 更新边嵌入
边 → 节点: 聚合邻居信息更新节点
```

### 单层消息传递

```
Message: m_{uv} = MSG(h_u, h_v, e_{uv})
Aggregate: a_v = AGG({m_{uv} | u ∈ N(v)})
Update: h_v' = UPDATE(h_v, a_v)
```

## GNN 类型

### 1. Graph Convolutional Network (GCN)

```
H' = σ(D^{-1/2} A D^{-1/2} H W)
```

| 层 | 操作 |
|---|------|
| 消息传递 | 邻居特征加权求和 |
| 聚合 | 归一化（度矩阵） |

### 2. GraphSAGE

```python
# 采样 + 聚合
h_{N(v)} = AGG({h_u, u ∈ N(v)})
h_v' = σ(W · [h_v || h_{N(v)}])
```

聚合方式：
- Mean pooling
- Max pooling
- LSTM

### 3. Graph Attention Network (GAT)

```
α_{uv} = softmax(LeakyReLU(a^T[Wh_u || Wh_v]))
h_v' = σ(Σ α_{uv} · W · h_u)
```

使用注意力机制自动学习邻居权重。

## 应用

| 领域 | 应用 |
|------|------|
| 节点分类 | 欺诈检测、用户画像 |
| 边预测 | 推荐系统、知识图谱 |
| 图分类 | 分子性质预测 |
| 场景图生成 | 图像理解 |
| 3D网格处理 | 点云分析 |
| 交通预测 | 道路网络建模 |

## PyG 示例

```python
import torch.nn as nn
from torch_geometric.nn import GCNConv

class GCN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = GCNConv(16, 32)
        self.conv2 = GCNConv(32, 64)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x
```

## 与传统神经网络的区别

| 特性 | CNN | RNN | GNN |
|------|-----|-----|-----|
| 输入 | 网格结构 | 序列 | 图结构 |
| 权重共享 | 空间位置 | 时间步 | 图邻居 |
| 操作 | 卷积 | 循环 | 消息传递 |

## 相关概念

- [[Convolutional Neural Network]]
- [[Attention Mechanism]]
- [[Reinforcement Learning]]

## 来源

[[summaries/I2DL-Lecture-12-Advanced-Topics]]
