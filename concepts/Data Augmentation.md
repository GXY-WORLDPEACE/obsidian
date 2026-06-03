---
title: "Data Augmentation"
date: 2026-06-03
tags:
  - #概念 #数据处理
---

# Data Augmentation (数据增强)

## 定义

通过对训练数据进行随机变换来扩充数据集，提高模型泛化能力。

## 常用方法

### 图像增强

| 方法 | 说明 |
|------|------|
| **RandomHorizontalFlip** | 随机水平翻转 |
| **RandomVerticalFlip** | 随机垂直翻转 |
| **RandomCrop** | 随机裁剪 |
| **Rotation** | 随机旋转 |
| **ColorJitter** | 颜色抖动 |
| **GaussianBlur** | 高斯模糊 |

## 实现示例

```python
# 水平翻转
if random.random() > 0.5:
    image = np.fliplr(image)

# 随机裁剪
top_left_x = random.randint(0, width - crop_size)
top_left_y = random.randint(0, height - crop_size)
image = image[top_left_y:top_left_y+crop_size, top_left_x:top_left_x+crop_size]
```

## 注意事项

- **只应用于训练集**！
- 验证/测试集保持不变
- 变换应保持标签不变

## 来源

- [[1_raw/articles/I2DL/exercise/exercise_06/