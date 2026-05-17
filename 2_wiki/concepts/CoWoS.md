---
title: "CoWoS (Chip on Wafer on Substrate)"
date: 2026-05-17
tags:
  - #concept
  - #packaging
  - #AI-hardware
aliases:
  - "Chip-on-Wafer-on-Substrate"
---

# CoWoS (Chip on Wafer on Substrate)

## 概述

CoWoS是台积电的 **2.5D封装技术**，将多个芯片（GPU + HBM + 逻辑die）集成在硅中介层上。是AI芯片先进封装的核心。

## 技术架构

```
┌─────────────────────────────────────┐
│           封装基板 (Substrate)       │
├─────────────────────────────────────┤
│         硅中介层 (Silicon Interposer) │
│  ┌─────────┐    ┌─────────┐         │
│  │   GPU   │────│  HBM   │         │
│  │  Core   │    │  Memory │         │
│  └─────────┘    └─────────┘         │
└─────────────────────────────────────┘
        ↑ TSV微凸点连接
```

## 为什么重要

| 问题 | CoWoS解决方案 |
|------|--------------|
| 带宽瓶颈 | 超高密度互连 |
| 功耗 | 短距离信号传输 |
| 良率 | 芯片级测试+筛选 |

**供应链关键点**：
- HBM必须通过CoWoS与GPU整合
- 美光HBM产出 → 台积电CoWoS封装 → 英伟达GPU
- 台积电CoWoS产能 = 美光HBM营收的前置条件

## 产能瓶颈

CoWoS是当前AI芯片供给链的最大瓶颈之一：
- 设备投资大
- 良率爬坡慢
- 产能扩张周期长（6-12个月）

## 相关概念

- [[concepts/HBM]] - HBM需CoWoS封装
- [[concepts/TSV]] - TSV是CoWoS的核心技术
- [[concepts/Advanced-Packaging]] - 先进封装技术