---
layout: home
title: 支持 — DanceXR
toc: false
locale: zh-CN
lang_path: /dancexr/support
permalink: /zh/dancexr/support
hero_compact: true
hero_title: 支持
hero_image: /images/hero.png
nav_links:
  - label: 功能
    url: /zh/dancexr/features
  - label: 发布
    url: /zh/dancexr/releases
  - label: 下载
    url: /zh/dancexr/download
  - label: 支持
    url: /zh/dancexr/support
---

<!-- ── Get Help ──────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
文档

## 浏览文档

最快找到答案的方式是查阅文档。功能页面详细介绍了每个选项，故障排除指南则针对最常见的问题提供了解决方案。

[功能文档 →](/zh/dancexr/features){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
社区

## 加入 Discord

DanceXR 社区在 Discord 上非常活跃。在这里可以找到其他用户、分享作品，并快速从有过相同经历的人那里获得解答。

[加入 Discord →](https://discord.gg/xN2MaM7C5q){: .btn-ghost}

</div>
</div>
</section>

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section section-light">
<div class="editions-header" markdown="1">

{:.section-label}
常见问题

## 常见问题解答

</div>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 只显示天空，没有 UI 或相机控制

这通常意味着启动时出现了问题。请按顺序尝试以下步骤：

- 删除 `license.txt` 后重新启动
- 备份并删除 `config.json` — 这将重置所有设置，解决因配置文件损坏引起的问题
- 备份并删除内容库中的 `cache.json`

</div>

<div class="faq-item" markdown="1">

### 每次启动都崩溃，回退到旧版本也没有帮助

这通常不是 DanceXR 本身的问题，而是 VR 运行时的问题。

- 如果安装了多个 VR 运行时，请尝试切换到其他运行时
- 对于 SteamVR：禁用不需要的启动覆盖层和插件；尝试重新安装
- 检查 SteamVR 的 `driver` 文件夹中是否有最近安装或更新的内容可以移除

</div>

<div class="faq-item" markdown="1">

### 被要求重新激活

OS 更新、硬件升级或其他系统变更后，设备 ID 可能会改变。只需重新执行激活步骤即可解决。如有问题请[联系我们](#contact)。

</div>

<div class="faq-item" markdown="1">

### 无法启动 VR

DanceXR 使用 OpenXR 初始化 VR。如果系统安装了多个 VR 运行时，需要将其中一个设置为活跃的 OpenXR 运行时：

- **Oculus / Meta：** 打开 Oculus 应用 → 设置 → 测试功能 → OpenXR 运行时 → "将 Oculus 设为活跃"
- **SteamVR：** 打开 SteamVR → 左上角菜单 → 设置 → 开发者 → "将 SteamVR 设置为 OpenXR 运行时"
- **Windows Mixed Reality：** 在微软商店下载 WMR OpenXR 开发者工具，从中将 WMR 设为活跃运行时

</div>

<div class="faq-item" markdown="1">

### 模型加载后全是白色

最常见的原因是文件名编码问题 — 当文件名使用不同字符编码时，贴图无法被定位。

- 对于 ZIP 包，可以在包名中添加编码信息，让 DanceXR 知道如何解析文件名。[详细说明 →](/dancexr/features/zip_format)
- 文件名中的多余空格也会导致贴图加载失败。请用 PMXEditor 打开模型，确认贴图引用与实际文件名完全一致

</div>

<div class="faq-item" markdown="1">

### 头发材质是透明的

透明度深度预处理默认开启。它通过只渲染最顶层的透明层来解决透明度排序问题，因此多层叠加的透明材质（如层叠的头发）只显示最顶层。

- 关闭透明度深度预处理可渲染所有透明层，但如果模型材质顺序不正确，可能会出现排序错误
- 目前没有完美的解决方案 — 请尝试不同配置，选择问题较少的那个

</div>

<div class="faq-item" markdown="1">

### 舞台模型的天空球有孔洞或看起来像素化

也是由透明度深度预处理引起的 — 当多个天空球都是透明的时，某些区域只完整渲染最顶层。

- 关闭透明度深度预处理，或
- 找到背景天空球，将其材质从透明改为不透明

</div>

</div>
</section>

<!-- ── Troubleshooting ───────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
故障排除

## 查找日志文件

报告 Bug 时附上日志文件非常有帮助。日志文件记录了错误发生时的详细信息，让我们能快速诊断问题。

**日志文件位置（PC）：**

```
C:\Users\[你的用户名]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

最后的文件夹名称取决于你安装的版本 — 可能是 `DanceXR HD`、`DanceXR LW` 或 `DanceXR RT`。

如果找不到 `AppData` 文件夹，请先 [在资源管理器中显示隐藏文件](https://support.microsoft.com/zh-cn/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)。

打开文件夹后，请将 **`Player.log`**（当前会话）和 **`Player-prev.log`**（上一次会话）附在报告中。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
快速修复

## 报告前请先尝试

以下步骤可解决大多数问题，请先逐一尝试：

1. **更新到最新版本** — 你的问题可能已经被修复
2. **重置配置** — 备份后删除 `config.json`，排除设置文件损坏的可能
3. **查看日志** — 打开 `Player.log`，搜索 `ERROR` 或 `Exception` 以定位问题
4. **VR 无法启动** — 确认 OpenXR 运行时已正确设置（见上方 FAQ）
5. **白色贴图** — 检查贴图引用中的文件名编码和多余空格

如果以上方法都无效，则值得提交报告。

</div>
</div>
</section>

<!-- ── Bug Report & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
联系我们

## 报告 Bug 或联系我们

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">推荐</p>
    <p class="edition-name">GitHub Issues</p>
    <p class="edition-price">Bug 追踪与功能请求</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>完整的问题历史与状态</li>
      <li>可附加截图和日志文件</li>
      <li>追踪报告进度</li>
      <li>功能请求</li>
    </ul>
    <a href="https://github.com/alloystorm/dvvr/issues" class="edition-cta">提交 Issue</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">快速</p>
    <p class="edition-name">Discord</p>
    <p class="edition-price">社区支持</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>社区快速解答</li>
      <li>分享作品和想法</li>
      <li>开发者在线</li>
      <li>实时交流</li>
    </ul>
    <a href="https://discord.gg/xN2MaM7C5q" class="edition-cta">加入 Discord</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">直接</p>
    <p class="edition-name">邮件</p>
    <p class="edition-price">商务与直接咨询</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>携附件的 Bug 报告</li>
      <li>商务合作咨询</li>
      <li>激活问题</li>
      <li>vrstormlab@gmail.com</li>
    </ul>
    <a href="mailto:vrstormlab@gmail.com" class="edition-cta">发送邮件</a>
  </div>

</div>
</section>
