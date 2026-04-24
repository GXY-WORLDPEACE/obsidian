---
title: "Reinforcement Learning"
date: 2026-04-24
tags:
  - #I2DL
  - #concept
  - #rl
type: concept
related_lectures:
  - 12
---

# Reinforcement Learning 强化学习

## 定义

强化学习是一种通过与环境交互学习最优策略的机器学习范式，智能体(Agent)通过试错获得最大化累积奖励。

## 核心框架

```
Agent ←→ Environment
  ↓
  State (s) → Agent 观察
  ↓
  Action (a) → Agent 执行
  ↓
  Reward (r) → Environment 反馈
  ↓
  Next State (s') → 新状态
```

## 马尔可夫决策过程 (MDP)

MDP由五元组定义：`(S, A, R, P, γ)`

| 符号 | 含义 |
|------|------|
| S | 状态空间 |
| A | 动作空间 |
| R | 奖励函数 R(s,a) |
| P | 转移概率 P(s'|s,a) |
| γ | 折扣因子 [0,1] |

## 核心概念

### 策略 (Policy)

```
π(a|s) = P(a|s)
```

- **确定性策略**: a = π(s)
- **随机策略**: π(a|s)

### 价值函数 (Value Function)

**状态价值函数**：
```
V^π(s) = E_π[R_t | s_t = s]
       = E_π[Σγᵏ r_{t+k} | s_t = s]
```

**动作价值函数**：
```
Q^π(s,a) = E_π[R_t + γV^π(s_{t+1}) | s_t=s, a_t=a]
```

### 最优性

```
V*(s) = max_π V^π(s)
π*(s) = argmax_a Q*(s,a)
```

## 算法分类

### Model-Free (无模型)

| 算法 | 类型 | 特点 |
|------|------|------|
| Q-Learning | 值函数 | 离散动作 |
| DQN | 值函数 | 深度学习 + Q-Learning |
| Policy Gradient | 策略梯度 | 连续动作 |
| DDPG | Actor-Critic | 连续控制 |
| PPO | Actor-Critic | 稳定训练 |

### Model-Based (基于模型)

学习环境模型，预测下一个状态和奖励。

### 算法对比

| 算法 | 样本效率 | 稳定性 | 动作类型 |
|------|----------|--------|----------|
| DQN | 低 | 一般 | 离散 |
| Policy Gradient | 低 | 差 | 离散/连续 |
| PPO | 中 | 好 | 离散/连续 |
| DDPG | 低 | 一般 | 连续 |

## 经典应用

| 应用 | 模型 |
|------|------|
| Atari游戏 | DQN |
| 围棋 | AlphaGo/AlphaZero |
| 机械臂控制 | PPO/DDPG |
| 自动驾驶 | Model-based RL |

## 挑战

| 挑战 | 说明 |
|------|------|
| 样本效率低 | 需大量环境交互 |
| 奖励设计 | 难以设计合适的奖励函数 |
| 探索-利用权衡 | 平衡探索新动作与利用已知 |
| 训练不稳定 | 需稳定化技术 |

## 相关概念

- [[Graph Neural Network]]
- [[GAN]]
- [[Diffusion Model]]
- [[Neural Network]]

## 来源

[[summaries/I2DL-Lecture-12-Advanced-Topics]]
