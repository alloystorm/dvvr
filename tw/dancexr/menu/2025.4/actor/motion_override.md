---
locale: zh-rTW
layout: single
title: 動作覆蓋
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/motion_override) | [繁中](/tw/dancexr/menu/2025.4/actor/motion_override) | [日本語](/jp/dancexr/menu/2025.4/actor/motion_override) | [한국어](/kr/dancexr/menu/2025.4/actor/motion_override) | [简中](/zh/dancexr/menu/2025.4/actor/motion_override)

[專業版](../menu#專業版) > 動作覆蓋

(
# Motion Override

## Overview
The Motion Override feature provides advanced tools to customize and enhance the motion of actors. It integrates seamlessly with the actor's rigging system, enabling precise control over body, head, hand, and leg movements. This feature is ideal for creating dynamic and synchronized animations.

## Key Features
- **Motion Presets**: Choose from a variety of motion styles, including rocking motions, ride models, and body poses.
- **Audio-Driven Motion**: Synchronize animations with audio beats for immersive experiences.
- **Body Pose Adjustments**: Control lean, height, forward/backward position, and rotation.
- **Ride Models**: Integrate ride models like hoverbikes or rocking horses with configurable properties such as acceleration and drag.
- **Rocking Motion Simulation**: Simulate rocking motions with adjustable depth, angle, and feet motion.
- **Symmetric Hand Poses**: Enable or disable symmetric hand movements.
- **Dynamic Leg Motion**: Adjust leg motion dynamically based on presets and configurations.
- **Particle Effects**: Add particle effects to enhance visual feedback during motion.
- **Customizable Configurations**: Fine-tune various parameters to achieve the desired motion effects.

## Example Use Cases
- **Limit Movements of a Dance Motion**: Use the Motion Override feature to restrict certain movements of a dance motion, ensuring that the actor's performance remains within desired limits.
    - Set position and rotation locks to control the actor's movement range.
    - Adjust the lean and height to create a more grounded appearance.
    - Optionally apply arms and legs poses to suit your needs.
- **Create a Rocking Horse Animation**: Utilize the rocking motion simulation to create a rocking horse animation.
    - Select the Rocking Horse preset from the motion presets.
    - Adjust the rocking angle and depth to achieve the desired rocking effect.
    - Choose the appropriate ride model to match the rocking horse theme.
- **Turning dance into vehecle motion**: Transform a dance animation into a vehicle-like motion.
    - Enable the ride model and configure the acceleration and drag settings.
    - Adjust the body pose to create a more dynamic and engaging performance.
    - Use the rocking motion simulation to add depth and realism to the animation.
    - Optionally, add particle effects to enhance the visual impact of the motion.

)

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>身體</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 位置</nobr>| 自由 | 自由, 鎖定水平, 鎖定垂直, 鎖定位置, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 旋轉</nobr>| 自由 | 自由, 鎖定旋轉, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 傾斜</nobr>| [0] (-45 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 彎曲</nobr>| [0] (-150 ~ 150) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 扭轉</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 頭部</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 向前/向後</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 距離</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 目標演員</nobr>|  |  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 檢測範圍</nobr>| [2] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最小距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大距離</nobr>| [1] (0.5 ~ 2) | 
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>搖擺動作</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>速度</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 每拍動作數</nobr>| (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 每組動作數</nobr>| [8] (4 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 相位</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 變量速度</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 模式</nobr>| (Gradual) | (Gradual), 隨機, 音量, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 最小速度</nobr>| (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 最大速度</nobr>| (3/2) | (1), (3/2), (2), (3), (4), 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 搖擺角度</nobr>| [30] (0 ~ 60) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 上下</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 前後</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度變化</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度最大</nobr>| [0.15] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度額外</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳部動作</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>頭部姿勢</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> X 旋轉</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Y 旋轉</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Z 旋轉</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>腿部姿勢</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 相對於地面</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大扭轉</nobr>| [60] (0 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 對稱</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>左</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 打開</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳 X</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳 Y</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳 Z</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳旋轉 X</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳旋轉 Y</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳旋轉 Z</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳趾</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>右</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 打開</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳 X</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳 Y</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳 Z</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳旋轉 X</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳旋轉 Y</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳旋轉 Z</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 腳趾</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Ride)** | (Sit), (Ride), (Kneel), (Stand),  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手部對稱</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>左手</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 手勢</nobr>| **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>手部位置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>手掌旋轉</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 旋轉類型</nobr>| 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 不旋轉, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 肘部方向</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 鏡像左右</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 參考演員</nobr>| **(Self)** | (Self), (Partner), (Closest),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 參考骨骼</nobr>| **無** | 無, 臀部, 胸部, 頭部, 中心, 桿, (Upperarm), (Forearm), 手, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> IK 模式</nobr>| 自動 | 自動, 正常, (Cylinder), 球體, (Align), 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 側面選擇</nobr>| 自動 | 自動, 左, 右, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 混合範圍</nobr>| [0.75] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 對稱偏移</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用配件位置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>運動</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>速度</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 每拍動作數</nobr>| (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 每組動作數</nobr>| [8] (4 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 相位</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 變量速度</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 模式</nobr>| (Gradual) | (Gradual), 隨機, 音量, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 最小速度</nobr>| (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 最大速度</nobr>| (3/2) | (1), (3/2), (2), (3), (4), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度</nobr>| [0] (-60 ~ 60) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>自定義姿勢</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 打開</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拇指軸</nobr>| [90] (-360 ~ 360) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拇指摺疊</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拇指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 食指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 無名指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 小指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 傳播</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 混合</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 姿勢權重</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取距離</nobr>| [0.015] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取位置</nobr>| [-0.05] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Grab Axis)</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Rest)** | (Rest), 背面, 正面, 臀部, 頭部, 桿, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>右手</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 手勢</nobr>| **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), 點, (Middle Finger), (Thumb Up), (Grab),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>手部位置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>手掌旋轉</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 旋轉類型</nobr>| 相對於參考骨骼 | 相對於參考骨骼, 相對於自身, 絕對旋轉, 不旋轉, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 肘部方向</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 鏡像左右</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 參考演員</nobr>| **(Self)** | (Self), (Partner), (Closest),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 參考骨骼</nobr>| **無** | 無, 臀部, 胸部, 頭部, 中心, 桿, (Upperarm), (Forearm), 手, 腿, 膝蓋, 腳, 腹部, 胸部, (Pussy), (Dick),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> IK 模式</nobr>| 自動 | 自動, 正常, (Cylinder), 球體, (Align), 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 側面選擇</nobr>| 自動 | 自動, 左, 右, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 混合範圍</nobr>| [0.75] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 對稱偏移</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用配件位置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>運動</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>速度</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 每拍動作數</nobr>| (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 每組動作數</nobr>| [8] (4 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 相位</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 曲線</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 變量速度</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 模式</nobr>| (Gradual) | (Gradual), 隨機, 音量, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 最小速度</nobr>| (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> 最大速度</nobr>| (3/2) | (1), (3/2), (2), (3), (4), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離</nobr>| [0.1] (0 ~ 0.3) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度</nobr>| [0] (-60 ~ 60) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>自定義姿勢</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 打開</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拇指軸</nobr>| [90] (-360 ~ 360) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拇指摺疊</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拇指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 食指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 無名指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 小指彎曲</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 傳播</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 混合</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 姿勢權重</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取距離</nobr>| [0.015] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 抓取位置</nobr>| [-0.05] (-0.1 ~ 0.1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Grab Axis)</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **(Rest)** | (Rest), 背面, 正面, 臀部, 頭部, 桿, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>騎乘模型</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 模型</nobr>| **([Hoverbike])** | ([Hoverbike]), ([Rocking Horse]),  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 加速度</nobr>| [10] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 拖曳</nobr>| [0.05] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 轉彎時傾斜</nobr>| [0.5] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>位置</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>旋轉</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-90 ~ 90) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 縮放</nobr>| [0] (-5 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 粒子效果</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **自由** | 自由, 搖擺動作, 懸浮摩托車, 搖擺馬, 桿子動作, 桿子混合,  |
