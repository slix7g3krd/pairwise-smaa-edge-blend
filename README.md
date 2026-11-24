# pairwise-smaa-edge-blend

## 领域

游戏、图形与多媒体

## 主题

SMAA 边缘检测与混合

## 说明

色彩空间阈值、全精度查找表与运动裁剪。

初始状态下 `graphics/smaa_edge_blend.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
