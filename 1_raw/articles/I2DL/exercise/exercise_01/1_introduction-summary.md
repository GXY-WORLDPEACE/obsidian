---
title: "I2DL Exercise 01 - Introduction"
date: 2026-04-24
tags:
  - #I2DL #练习 #入门
type: exercise_introduction
course: I2DL
---

# I2DL Exercise 01: 课程介绍与提交系统

## 概述

Exercise 01 是 I2DL 课程的入门练习，旨在帮助学生：
1. 配置开发环境（本地/Anaconda/Google Colab）
2. 熟悉 IPython Notebook 工作流
3. 掌握 Numpy 基础操作
4. 了解课程提交系统

## 核心内容

### 1. 环境配置

| 环境 | 说明 |
|------|------|
| **本地 Anaconda** | 使用 Python 3.10+，需安装依赖 |
| **Google Colab** | 云端运行，免费 GPU，可挂载 Google Drive |

### 2. IPython Notebook 基础

- **执行单元**: `Shift + Enter`
- **全局变量**: 单元格之间共享
- **执行顺序**: 从上到下，顺序很重要
- **编辑模式**: 双击编辑单元格

### 3. Numpy 核心操作

| 操作 | 示例 |
|------|------|
| 创建数组 | `np.array([[1,2,3], [4,5,6]])` |
| 切片 | `a[:, :2]` |
| 条件筛选 | `a[a>1]` |
| 数学运算 | `np.add()`, `np.multiply()`, `np.divide()` |
| 特殊函数 | `np.sqrt()`, `np.exp()` |

### 4. 提交系统工作流

```
1. 实现指定函数（如 forward()）
2. 运行测试 → 获得分数（0-100）
3. 保存模型 → 生成 pickle 文件
4. 打包提交 → 创建 zip 文件
5. 上传到课程网站
```

### 5. 关键要点

> **门槛分数**: 60 分
> **提交次数**: 不限，取最高分
> **评分方式**: 自动测试用例

## 提取的概念

- [[concepts/Python]] - Numpy 基础
- [[concepts/IPython Notebook]] - 交互式编程
- [[concepts/Google Colab]] - 云端开发环境
- 模型提交与评分系统

## 状态

✅ 已完成摘要生成
