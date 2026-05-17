---
title: "HBM长期看好与存储板块短期过热分析"
date: 2026-05-17
source: "https://x.com/yiran2037840/status/2055494205892448409"
author: "yiran2037840"
created: 2026-05-17
tags:
  - #article-summary
  - #HBM
  - #memory
  - #investment
type: investment_analysis
---

# HBM长期看好 vs 存储板块短期过热

## 核心观点

**HBM是结构性瓶颈，传统DDR/NAND是周期性紧缺。** 估值方式不能一样。

## 三层存储架构

```
GPU HBM (热)    → 放hot KV，当前decode核心瓶颈
CPU DRAM (温)   → 放warm/cold KV，HBM溢出时缓存
SSD/NAND (冷)   → 放prefix cache，持久化层
```

## HBM的核心逻辑

**为什么长期看好？**

1. **技术壁垒高**：高端DRAM die + TSV + 堆叠 + 先进封装
2. **客户绑定强**：与NVIDIA/AMD/ASIC厂商认证周期长
3. **供给弹性低**：扩产需看封装、测试、良率、客户验证

HBM不是普通商品，而是AI加速器性能的一部分。

### LLM推理的关键瓶颈

| 因素 | 影响 |
|------|------|
| HBM容量 | 决定batch size、上下文长度、并发能力 |
| HBM带宽 | 决定token生成速度 |
| KV cache管理 | 影响GPU利用率 |

## 估值框架对比

| 类型 | 估值逻辑 | 关键指标 |
|------|----------|----------|
| HBM | 成长科技股PE | 利润占比提升 |
| 传统DDR | 周期品PS（高PS） | 供需周期 |
| NAND/SSD | 传统存储PS（低PS） | 长江存储扩产 |

## 当前风险点

**为什么短期过热？**

市场可能混淆了三件事：
1. HBM的非周期化
2. DDR的周期上行  
3. NAND/SSD的AI需求放大

如果把传统DDR/NAND也按HBM逻辑重估，估值就脆弱了。

## 核心矛盾

> 存储股现在的核心矛盾不是"AI需求有没有"，而是**市场给传统DDR和NAND/SSD的利润，究竟用了什么倍数？**

## 两大监控指标

1. **HBM利润占比能否持续提高**（目前官方未披露）
2. **长鑫/长江扩产后周期性能否重现**

---

**相关概念**： [[concepts/HBM]] | [[concepts/DRAM]] | [[concepts/Memory-Hierarchy]]

**原始来源**： [[1_raw/X/为什么我长期坚定看好HBM，但短期觉得存储板块过热.md]]