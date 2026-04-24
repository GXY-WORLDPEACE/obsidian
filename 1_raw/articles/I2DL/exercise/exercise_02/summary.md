---
title: "I2DL Exercise 1 README"
date: 2026-04-19
tags:
  - #I2DL #练习 #环境配置
type: exercise_readme
---

# I2DL Exercise 1: 环境设置与入门

## 摘要
Exercise 1 的 README 文档详细介绍了课程实验环境的配置方法，包括本地 Anaconda 安装和 Google Colab 云端环境两种方案，以及数据集下载和作业提交流程。

## 环境配置

### 方案一：Anaconda 本地环境

1. 下载安装 [Anaconda](https://www.anaconda.com/)
2. 创建环境：`conda create --name i2dl python=3.11 -y`
3. 激活环境：`conda activate i2dl`
4. 安装依赖：`pip install -r requirements.txt`
5. 启动 Jupyter：`jupyter notebook`

### 方案二：Google Colab 云端

- 提供免费 GPU（适合后期大模型训练）
- 前 5 个练习不需要 GPU
- 需要 Google Drive 存储空间

## 目录结构

```
i2dl/
├── datasets/       # 数据集目录
├── exercise_1/    # 练习代码
├── exercise_N/    # 各练习
└── output/        # 提交输出
```

## 作业提交

1. 登录 https://i2dl.cvg.cit.tum.de
2. 训练模型自动保存在 `models` 目录
3. 打包上传至提交系统
4. 可查看排行榜和邮件通知结果

## 注意事项

- PyTorch 不支持 M1/M2 MacBook 的 GPU 加速
- Colab 文件需等待几秒保存后再打包
- 截止日期前可反复重新评估

## 概念

- [[concepts/Anaconda]]
- [[concepts/Google_Colab]]
- [[concepts/PyTorch]]
- [[concepts/Jupyter_Notebook]]
