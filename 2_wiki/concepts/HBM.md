---
title: "HBM (High Bandwidth Memory)"
date: 2026-05-17
tags:
  - #concept
  - #memory
  - #AI-hardware
aliases:
  - "High Bandwidth Memory"
---

# HBM (High Bandwidth Memory)

## 概述

HBM是一种高性能 DRAM，通过 **硅通孔(TSV)** 技术垂直堆叠多层DRAM die，实现超高带宽。是AI GPU/ASIC的关键组件。

## 技术特点

| 特性 | 说明 |
|------|------|
| 堆叠层数 | 8-12层DRAM die |
| 带宽 | 数百GB/s到TB/s级 |
| 功耗 | 比GDDR低30-50% |
| 封装 | 2.5D/3D堆叠 + 硅中介层 |

## HBM vs 传统DRAM

```
HBM3E (8-12层堆叠)
    ↓ Die Size Penalty: 占用面积是DDR5的2-2.5倍
    ↓ Yield Loss: 任何一层良率问题整颗报废
    ↓ 实际产出: 1片HBM = 消耗3-4片DDR5产能

这就是HBM对传统DRAM产能的"挤压效应"
```

## 在AI推理中的角色

```
GPU HBM (热)  → 当前decode核心瓶颈，放hot KV
CPU DRAM (温) → 放warm/cold KV，HBM溢出时缓存
SSD/NAND (冷) → 放prefix cache，持久化层
```

**为什么HBM是AI加速器的性能瓶颈？**
- LLM decoding是memory-bandwidth bound场景
- 每生成一个token需读取模型权重+KV cache
- KV cache在长上下文、多并发、agent workflow中越来越大

## 市场格局

| 厂商 | 产品 | 状态 |
|------|------|------|
| SK海力士 | HBM3E | 主导地位 |
| 三星 | HBM3E | 竞争 |
| 美光 | HBM3E | 已通过英伟达认证 |

美光HBM3E功耗比竞品低30%，已打入H200/B100供应链。

## 关键概念关系

- [[concepts/TSV]] - 硅通孔技术
- [[concepts/CoWoS]] - 台积电封装技术
- [[concepts/DRAM]] - 传统DRAM对比
- [[concepts/Memory-Hierarchy]] - 存储层级