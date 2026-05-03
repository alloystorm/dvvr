---
layout: release
title: 图形
locale: zh-CN
nav_links:
  - label: 简介
    url: /zh/dancexr
  - label: 功能
    url: /zh/dancexr/features
  - label: 发布
    url: /zh/dancexr/releases
  - label: 下载
    url: /zh/dancexr/download
---

# 图形设置

控制 DanceXR HDRP（HD 和 RT）版本的所有渲染质量设置。选择预设可以获得平衡的起始点，然后调整各个功能以达到性能和视觉目标。


## 预设

六个预设涵盖了常见的范围：*性能*禁用反射和大多数屏幕空间效果；*中等*添加雾和屏幕空间阴影；*高*启用屏幕空间反射；*室内全局照明*和*室外全局照明*在有或没有天空贡献的情况下激活全局照明；*抖动 + TAA* 将时间反锯齿与抖动透明度配对，以获得清晰的外观。


## 抗锯齿和超采样

**抗锯齿**选择每摄影机的技术——无 AA、SMAA（延迟）或 TAA。**超采样**在支持时解锁 DLSS 或 FSR 放大，这可以牺牲一点清晰度以提升帧率。


## 反射

屏幕空间反射或平面反射探针。使用 *屏幕空间* 模式处理通用表面；切换到 *探针* 模式用于平坦地板或镜子。质量、边缘衰减距离和回退行为可在子节中调整。


## 环境光遮挡和全局照明

**环境光遮挡**在缝隙中添加接触阴影，以增加扎实的深度感。**全局照明**添加间接反弹光——对于室外场景，启用 *回退到天空*，这样朝离光源的表面仍能接收到天空的颜色。


## 后期处理效果

**深度场**模糊追踪到的动画角色的焦点以外的物体。**运动模糊**在快速运动时添加基于速度的模糊。**辉光**使明亮的高光发光。**镜头光晕**在明亮光源周围添加屏幕空间散射——在 VR 中禁用以避免不适。


## 雾

启用体积雾并设置其高度带和最大渲染距离。雾的密度本身由光照面板中的 **雾** 滑块驱动。


## 颜色调整

色调映射、曝光、对比度、色相偏移、饱和度、颜色滤镜、两点色调曲线和白平衡都在此处。**颜色曲线**将输入亮度映射到输出亮度；对于风格化的外观或保护高光非常有用。


## 选项

各种渲染标志：**透明度预渲染通道**隐藏透过透明表面看到的物体；**卡通着色**将角色或舞台切换为扁平的漫画外观；**抖动透明度**强制所有透明材质进行点状混合；**凹凸贴图阴影**为法线贴图添加微阴影；**计算厚度**启用次表面皮肤效果。


## 色调分级

添加一个自定义通道效果，在最终帧上添加轮廓、色调分级照明或半色调网格——对动漫或漫画风格很有用。

# 子组件

## 反射

配置屏幕空间反射或平面反射探针。

*屏幕空间* 模式对深度缓冲区进行光线步进，以找到反射表面——它可用于任何几何体，但不能反射摄影机视野外的物体。切换到 *探针* 模式用于地板或镜子等平坦表面，它使用始终完整的平面捕获，但性能开销更大。


### 算法


在使用 *屏幕空间* 模式时，*近似* 更快，适用于大多数表面；*PBR 累积* 对粗糙材料更物理准确，但需要 TAA 才能干净收敛。

**边缘衰减距离** 衰减屏幕边缘附近的反射以隐藏伪影；**物体厚度** 控制步进算法假定的表面深度。


### 天空反射和回退


**天空反射** 允许摄影机的天空贡献给向上朝向的表面的反射。**回退到天空** 在屏幕空间通道遗漏的区域填充反射探针的覆盖范围，但会牺牲一点准确度。
## 色调分级

应用于最终渲染图像的全屏自定义通道。四个内置预设提供了快速的起点：*轮廓*、*黑白*、*色调分级* 和 *半色调*。


### 轮廓


根据深度和法线不连续性跟踪边缘。控制 **轮廓厚度** 和 **轮廓强度** 来调整权重。与选项面板中的卡通着色结合使用效果良好，以获得漫画动画外观。


### 量化照明和颜色


**量化照明** 减少图像中的亮度步骤数；较低的值（例如 4–8）会产生大胆的色调分级外观。**量化颜色** 对颜色通道执行相同的操作，但独立进行。将两者都设置为 0 可完全禁用量化，只使用其他效果。


### 抖动和半色调


**抖动** 添加有序噪声，分解平滑渐变中的频带效应。**半色调** 覆盖点阵模式；增加 **半色调大小** 和 **强度** 以获得复古印刷美学。
## 配置

<table>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
性能、中等、<b >高</b>、室内全局照明、室外全局照明、抖动 + TAA，</td></tr>
<tr><td><strong >抗锯齿</strong ></td ><td >选项</td><td >无 AA、延迟 SMAA、延迟 TAA</td><td >延迟 SMAA</td><td></td><td></td></tr>
<tr><td><strong >超采样</strong ></td ><td >选项</td><td >关闭、DLSS 性能、DLSS 平衡、DLSS 质量、DLSS 超性能、FSR 50%、FSR 66%、FSR 75%、FSR 100%</td><td >关闭</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong >反射</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >模式</strong ></td ><td >整数</td><td >0 – 1</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >质量</strong ></td ><td >整数</td><td >0 – 2</td><td >2</td><td></td><td></td></tr>
<tr><td><strong >算法</strong ></td ><td >整数</td><td >0 – 1</td><td >0</td><td></td><td>用于屏幕空间反射的算法。</td></tr>
<tr><td><strong >边缘衰减距离</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.1</td><td></td><td></td></tr>
<tr><td><strong >物体厚度</strong ></td ><td >浮点</td><td >0 – 0.1</td><td >0.01</td><td></td><td></td></tr>
<tr><td><strong >回退到天空</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td>当光线追踪没有命中时，回退到天空颜色。</td></tr>
<tr><td><strong >天空反射</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >雾</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >体积雾</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td></td></tr>
<tr><td><strong >基础高度</strong ></td ><td >浮点</td><td >0 – 10</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >最大高度</strong ></td ><td >浮点</td><td >10 – 100</td><td >25</td><td></td><td></td></tr>
<tr><td><strong >最大距离</strong ></td ><td >浮点</td><td >0 – 10000</td><td >5000</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >环境光遮挡</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >质量</strong ></td ><td >整数</td><td >0 – 2</td><td >2</td><td></td><td></td></tr>
<tr><td><strong >强度</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >全局照明</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >质量</strong ></td ><td >整数</td><td >0 – 2</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >回退到天空</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >深度场</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >质量</strong ></td ><td >整数</td><td >0 – 2</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >强度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.25</td><td></td><td></td></tr>
<tr><td><strong >偏移</strong ></td ><td >浮点</td><td >-1 – 1</td><td >0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >运动模糊</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >质量</strong ></td ><td >整数</td><td >0 – 2</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >强度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.25</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >辉光</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >质量</strong ></td ><td >整数</td><td >0 – 2</td><td >2</td><td></td><td></td></tr>
<tr><td><strong >强度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.25</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong >镜头光晕</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >在 VR 中禁用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td>此效果不推荐用于 VR</td></tr>
<tr><td><strong >强度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.1</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong >颜色</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td>
<b >白色</b>、日落、红色、黄色、蓝色、绿色、</td></tr>
<tr><td><strong >颜色模式</strong ></td ><td >整数</td><td >0 – 1</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >色相</strong ></td ><td >浮点</td><td >0 – 1</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >饱和度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >亮度</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >红</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >绿</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >蓝</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >使用舞台环颜色</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td>使用舞台环的颜色</td></tr>
<tr><td><strong >色温</strong ></td ><td >浮点</td><td >3000 – 8000</td><td >6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong >光斑</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >光带</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.2</td><td></td><td></td></tr>
<tr><td><strong >长度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.5</td><td></td><td></td></tr>
<tr><td><strong >色差</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.5</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong >颜色调整</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >色调映射</strong ></td ><td >整数</td><td >0 – 3</td><td >3</td><td></td><td></td></tr>
<tr><td><strong >调整</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td>启用颜色调整。</td></tr>
<tr><td><strong >后曝光</strong ></td ><td >整数</td><td >-12 – 12</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >对比度</strong ></td ><td >浮点</td><td >-100 – 100</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >色相偏移</strong ></td ><td >浮点</td><td >-180 – 180</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >饱和度</strong ></td ><td >浮点</td><td >-100 – 100</td><td >1</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong >颜色滤镜</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >颜色模式</strong ></td ><td >整数</td><td >0 – 1</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >色相</strong ></td ><td >浮点</td><td >0 – 1</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >饱和度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >亮度</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >红</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >绿</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >蓝</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong >颜色曲线</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td><strong >起始渐变</strong ></td ><td >浮点</td><td >0 – 4</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >起始位置</strong ></td ><td >浮点</td><td >0 – 0.5</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >起始值</strong ></td ><td >浮点</td><td >0 – 0.5</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >结束渐变</strong ></td ><td >浮点</td><td >0 – 4</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >结束位置</strong ></td ><td >浮点</td><td >0.5 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >结束值</strong ></td ><td >浮点</td><td >0.5 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >白平衡</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td>启用白平衡。</td></tr>
<tr><td><strong >温度</strong ></td ><td >浮点</td><td >-100 – 100</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >色偏</strong ></td ><td >浮点</td><td >-100 – 100</td><td >0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong >色调分级</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong >启用</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td>
轮廓、黑白、<b >色调分级</b>、半色调、</td></tr>
<tr><td><strong >轮廓厚度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.1</td><td></td><td></td></tr>
<tr><td><strong >轮廓强度</strong ></td ><td >浮点</td><td >0 – 1</td><td >1</td><td></td><td></td></tr>
<tr><td><strong >量化照明</strong ></td ><td >整数</td><td >0 – 16</td><td >8</td><td></td><td></td></tr>
<tr><td><strong >量化颜色</strong ></td ><td >整数</td><td >0 – 64</td><td >0</td><td></td><td></td></tr>
<tr><td><strong >抖动</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.25</td><td></td><td></td></tr>
<tr><td><strong >半色调大小</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.25</td><td></td><td>半色调大小</td></tr>
<tr><td><strong >半色调强度</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.1</td><td></td><td>半色调强度</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong >选项</strong ></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >透明度预渲染通道</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td>启用透明度预渲染通道。这将使被遮挡的透明材质不可见。</td></tr>
<tr><td><strong >屏幕空间阴影</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
<tr><td><strong >接触阴影</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td>小细节的阴影。</td></tr>
<tr><td><strong >凹凸贴图阴影</strong ></td ><td >浮点</td><td >0 – 1</td><td >0.5</td><td></td><td>启用凹凸贴图和细节贴图的阴影。</td></tr>
<tr><td><strong >阻止 NaN</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td>防止后处理过程中发生错误导致黑屏。</td></tr>
<tr><td><strong >计算厚度</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >打开</td><td></td><td>计算可用于皮肤效果的厚度。</td></tr>
<tr><td><strong >角色模型卡通着色</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td>对所有角色使用卡通着色。</td></tr>
<tr><td><strong >舞台模型卡通着色</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td>对舞台和道具使用卡通着色。</td></tr>
<tr><td><strong >抖动透明度</strong ></td ><td >切换</td><td >打开 / 关闭</td><td >关闭</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>