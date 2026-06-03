---
title: "I2DL Exercise 07 - PyTorch 与 TensorBoard"
date: 2026-06-03
tags:
  - #I2DL #练习 #PyTorch #TensorBoard
type: exercise
course: I2DL
---

# I2DL Exercise 07: PyTorch 入门与 TensorBoard

## 概述

学习使用 **PyTorch** 框架构建神经网络，并使用 **TensorBoard** 可视化训练过程。从纯 NumPy 实现过渡到工业级深度学习框架。

## Notebook 概览

| Notebook | 内容 |
|----------|------|
| **1_pytorch.ipynb** | PyTorch 基础教程（Tensor、数据加载、网络定义、训练流程） |
| **2_tensorboard.ipynb** | TensorBoard 使用（可视化训练过程、权重初始化实验） |
| **3_Cifar10_Pytorch.ipynb** | 用 PyTorch 训练 CIFAR-10 分类器 |

## 数据集

| 属性 | 值 |
|------|-----|
| **数据集** | CIFAR-10 |
| **图片尺寸** | 32×32×3 (RGB) |
| **类别数** | 10 |

## PyTorch 基础

### Tensor (张量)

类似 NumPy 的 ndarray，但支持 GPU 加速。

```python
import torch

# 从 NumPy 创建
x = torch.from_numpy(np_array)

# GPU 迁移
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x_gpu = x.to(device)
```

### nn.Module (神经网络基类)

只需定义 `forward()`，反向传播自动计算。

```python
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

### autograd (自动微分)

自动计算梯度，无需手动实现。

```python
x = torch.tensor([1.0], requires_grad=True)
y = x ** 2
y.backward()  # 自动计算梯度
print(x.grad)  # tensor([2.])
```

### DataLoader (数据加载)

```python
from torch.utils.data import DataLoader

train_loader = DataLoader(
    dataset=train_dataset,
    batch_size=64,
    shuffle=True,
    num_workers=4  # 多进程加速
)
```

## PyTorch 训练流程

```python
# 1. 定义模型
model = MyPytorchModel(hparams).to(device)

# 2. 定义损失和优化器
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 3. 训练循环
for epoch in range(epochs):
    model.train()  # 训练模式
    for batch in train_loader:
        optimizer.zero_grad()     # 清梯度
        output = model(images)    # 前向传播
        loss = criterion(output, labels)  # 计算损失
        loss.backward()           # 反向传播
        optimizer.step()          # 更新参数
    
    # 验证
    model.eval()  # 评估模式
    with torch.no_grad():
        for batch in val_loader:
            # 验证代码
            pass
```

## TensorBoard 可视化

### 安装与启动

```bash
pip install tensorboard
tensorboard --logdir=./logs
```

### 常用 API

| 方法 | 用途 |
|------|------|
| `add_scalar` | 记录标量（loss、accuracy） |
| `add_image` | 记录图像 |
| `add_figure` | 记录 matplotlib 图表 |
| `add_histogram` | 记录分布（激活值、权重） |
| `add_graph` | 可视化网络结构 |

### 使用示例

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('logs/run_1')

# 记录标量
writer.add_scalar('train/loss', loss.item(), step)

# 记录图像
writer.add_image('input', img_grid, step)

# 记录图表
writer.add_figure('predictions', fig, step)

# 记录分布
writer.add_histogram('weights', layer.weight, step)

writer.close()
```

## 权重初始化

### 常见问题

| 初始化方法 | 问题 |
|-----------|------|
| 常数初始化 | 破坏对称性，所有神经元学相同特征 |
| 过大随机值 | 梯度饱和 / 梯度消失 |
| 过小随机值 | 梯度消失 |

### 初始化方法对比

| 方法 | 公式 | 适用激活函数 |
|------|------|-------------|
| **Xavier (Glorot)** | $\sigma = \sqrt{\frac{2}{fan_{in} + fan_{out}}}$ | Tanh, Sigmoid |
| **He (Kaiming)** | $\sigma = \sqrt{\frac{2}{fan_{in}}}$ | ReLU |
| **Kaiming Uniform** | 均匀分布版本 | ReLU |

### PyTorch 实现

```python
# Xavier
nn.init.xavier_normal_(layer.weight)

# He
nn.init.kaiming_uniform_(layer.weight, nonlinearity='relu')
```

## CIFAR-10 分类器要求

```python
class MyPytorchModel(nn.Module):
    def __init__(self, hparams):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, num_classes)
        )
    
    def forward(self, x):
        return self.model(x)
```

### 超参数示例

```python
hparams = {
    "batch_size": 64,
    "learning_rate": 3e-3,
    "n_hidden": 180,
    "input_size": 3 * 32 * 32,  # 3072
    "num_classes": 10,
}
```

## 评分标准

| 项目 | 值 |
|------|-----|
| **通过要求** | 测试集准确率 ≥ 50% |
| **提交次数** | 无限 |
| **模型大小限制** | < 20 MB (~5M 参数) |
| **注意事项** | 使用全连接层（无卷积） |

## 与之前练习的区别

| 方面 | 之前 (NumPy) | Exercise 07 (PyTorch) |
|------|-------------|----------------------|
| 梯度计算 | 手动实现 | `autograd` 自动 |
| GPU 支持 | 无 | 有 |
| 代码量 | 多 | 少 |
| 调试 | 困难 | 有 TensorBoard |

## 提取的概念

- [[concepts/PyTorch]] - PyTorch 框架
- [[concepts/TensorBoard]] - TensorBoard 可视化工具
- [[concepts/autograd]] - 自动微分
- [[concepts/Weight Initialization]] - 权重初始化
- [[concepts/Xavier Initialization]] - Xavier 初始化
- [[concepts/He Initialization]] - He (Kaiming) 初始化

## 相关代码文件

- `exercise_code/MyPytorchModel.py` - PyTorch 模型实现
- `exercise_code/CIFAR10DataModule.py` - 数据模块
- `exercise_code/lightning_models.py` - Lightning 模型（可选）

## 状态

✅ 已完成摘要生成
