---
layout: home
title: 支持
toc: false
locale: zh-CN
lang_path: /dancexr/support
hero_compact: true
hero_title: 支持
hero_image: /images/hero.png
---

<!-- ── Get Help ──────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
文档

## 浏览文档

最快找到答案的方式是查阅文档。功能页面详细介绍了每个选项，故障排除指南则针对最常见的问题提供了解决方案。

[功能文档 →](features){: .btn-ghost}

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
- 删除（先备份）`config.json` — 这将重置所有设置，解决因配置文件损坏引起的问题
- 删除（先备份）内容库中的 `cache.json`

</div>

<div class="faq-item" markdown="1">

### 每次启动都崩溃，回退到旧版本也没有帮助

这通常不是 DanceXR 本身的问题，而是 VR 运行时的问题。

- 如果您安装了多个 VR 运行时，请尝试切换到其他运行时
- 对于 SteamVR：禁用不需要的启动覆盖层和插件；尝试进行干净重装
- 检查 SteamVR 的 `driver` 文件夹中是否有最近安装或更新的内容可以移除

</div>

<div class="faq-item" markdown="1">

### 被要求重新激活

在进行重大操作系统或硬件更改后，DanceXR 可能无法识别该系统与您的许可证发行时相同的系统。只需再次执行激活步骤即可——不会产生额外费用。请参阅 [激活与许可](activation) 指南。[联系我们](#contact) 如果您遇到问题。

</div>

<div class="faq-item" markdown="1">

### 无法启动 VR

DanceXR 使用 OpenXR 来初始化 VR。如果您安装了多个 VR 运行时，需要将其中一个设置为活动的 OpenXR 运行时：

- **Oculus / Meta：** 打开 Oculus 应用 → 设置 → Beta → OpenXR 运行时 → "设为活动"
- **SteamVR：** 打开 SteamVR → 左上角菜单 → 设置 → 开发者 → "设为 OpenXR 运行时"
- **Windows Mixed Reality：** 从 Microsoft Store 下载“Windows Mixed Reality OpenXR Developer Tools”，并从中将 WMR 设为活动运行时

</div>

<div class="faq-item" markdown="1">

### 模型加载但所有内容都是白色

最常见的原因是文件名编码——当文件名使用不同的字符编码时，贴图无法被定位。

- 对于 ZIP 包，请将编码添加到包名中，以便 DanceXR 知道如何解析文件名。[在此查看详情 →](features/zip_format)
- 文件名中的额外空格也会阻止贴图加载。请在 PMXEditor 中打开模型，并确认贴图引用与实际文件名完全匹配。

</div>

<div class="faq-item" markdown="1">

### 头发材质是透明的

透明度深度预处理默认处于开启状态。它通过只渲染最顶层的透明层来解决透明度排序问题——这意味着堆叠的透明层（如分层的头发）只会显示最上层。

- 关闭透明度深度预处理可以渲染所有透明层。但是，如果模型材质顺序不正确，可能会引入排序伪影。
- 目前没有完美通用的解决方案——请尝试不同的配置，并使用视觉问题较少的一个。

</div>

<div class="faq-item" markdown="1">

### 舞台模型的天空球有孔洞或看起来像素化

这也是由透明度深度预处理引起的——当多个天空球都是透明的时，某些区域只会完整渲染最顶层。

- 关闭透明度深度预处理，或
- 找到背景天空球，并将其材质从透明更改为不透明

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

报告 Bug 时附上日志文件非常有帮助。日志文件记录了错误发生时的详细信息，让我们能够快速诊断问题。

**日志文件位置（PC）：**

```
C:\Users\[你的用户名]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

最后的文件夹名称取决于您的版本——可能是 `DanceXR HD`、`DanceXR LW` 或 `DanceXR RT`。

默认情况下有些文件夹是隐藏的。如果找不到 `AppData`，请先[在资源管理器中启用隐藏文件](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)。

打开文件夹后，请将 **`Player.log`**（当前会话）和 **`Player-prev.log`**（上一次会话）附在您的报告中。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
快速修复

## 报告前请先尝试

请按顺序尝试以下步骤——它们可以解决大多数问题：

1. **更新到最新版本** — 您的问题可能已经被修复
2. **重置配置** — 备份后删除 `config.json`，以排除设置文件损坏的可能性
3. **检查日志** — 打开 `Player.log` 并搜索 `ERROR` 或 `Exception` 来识别问题
4. **VR 无法启动** — 确认您的 OpenXR 运行时已正确设置（参见上方 FAQ）
5. **白色贴图** — 检查贴图引用中的文件名编码和额外空格

如果以上方法均无效，则值得提交报告。

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