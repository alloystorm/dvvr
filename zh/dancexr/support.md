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

<!-- ── Support Hub Navigation ───────────────────────────────── -->
<section class="section">
<div class="editions-header" markdown="1">

{:.section-label}
支持中心

## 我们能为您提供什么帮助？

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">文档</p>
    <p class="edition-name">浏览文档</p>
    <p class="edition-price">功能与选项指南</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>详细的功能文档</li>
      <li>自定义内容准备</li>
      <li>VR/屏幕设置详情</li>
      <li>系统要求与支持格式</li>
    </ul>
    <a href="features" class="edition-cta">打开文档</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">快速修复</p>
    <p class="edition-name">故障排除</p>
    <p class="edition-price">报告前检查清单</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>验证运行环境与设置</li>
      <li>重置损坏的配置</li>
      <li>使用日志诊断问题</li>
      <li>解决常见的崩溃状态</li>
    </ul>
    <a href="#troubleshooting" class="edition-cta">查看清单</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">许可授权</p>
    <p class="edition-name">激活</p>
    <p class="edition-price">管理您的授权密钥</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>硬件变更重新激活</li>
      <li>Patreon 验证步骤</li>
      <li>不同平台版本差异</li>
      <li>购买与退款咨询</li>
    </ul>
    <a href="activation" class="edition-cta">激活指南</a>
  </div>

</div>
</section>

<!-- ── Troubleshooting & Logs ───────────────────────────────── -->
<section class="section section-light" id="troubleshooting">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
快速修复

## 报告前请先尝试

在提交 Bug 报告前，请先执行以下快速故障排除步骤：

1. **更新到最新版本** — 您遇到的问题可能已经在较新的版本中被修复。
2. **重置配置** — 备份后删除 `config.json`，以排除设置文件损坏的可能性。
3. **重设授权** — 如果应用程序无法启动或行为异常，请尝试从安装目录中删除 `license.txt` 并重新启动。
4. **清除缓存** — 备份并删除内容库文件夹中的 `cache.json`，以强制播放器重新扫描您的文件。
5. **OpenXR 设置** — 如果 VR 无法启动，请再次确认您的 VR 软件设置中是否正确设置了活动的 OpenXR 运行时。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
故障排除

## 查找日志文件

报告 Bug 时附上日志文件非常有帮助。日志文件记录了错误发生时的详细信息，让我们能够快速诊断问题。

**Windows PC 路径：**
```
C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
```
*\*注意：请将 [User] 替换为您的 Windows 用户名。最后一个文件夹名称取决于您的版本（例如 DanceXR HD、DanceXR LW 或 DanceXR RT）。如果找不到 AppData 文件夹，请在资源管理器中开启“隐藏的项目”。\**

**Android & Meta Quest 路径：**
```
/Android/data/com.vrstormlab.dancexr/files/Player.log
```
*\*注意：请使用 USB 将您的设备连接到 PC 并选择文件传输，或使用设备上具有适当权限的文件浏览器应用程序来找到此文件。\**

请将 **`Player.log`**（当前会话）和 **`Player-prev.log`**（上一次会话）附在您的 Bug 报告中。

</div>
</div>
</section>

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section">
<div class="editions-header" markdown="1">

{:.section-label}
常见问题

## 常见问题解答

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🖥️ 系统与 VR 启动</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 只显示天空，没有 UI 或相机控制

这通常意味着启动时出现了问题。请按顺序尝试以下步骤：

- 删除 `license.txt` 后重新启动。
- 删除（先备份）`config.json` — 这将重置所有设置，解决因配置文件损坏引起的问题。
- 删除（先备份）内容库中的 `cache.json`。

</div>

<div class="faq-item" markdown="1">

### 每次启动都崩溃，回退到旧版本也没有帮助

这通常不是 DanceXR 本身的问题，而是 VR 运行时的问题。

- 如果您安装了多个 VR 运行时，请尝试切换到其他运行时。
- 对于 SteamVR：禁用不需要的启动覆盖层和插件；尝试进行干净重装。
- 检查 SteamVR 的 `driver` 文件夹中是否有最近安装或更新的内容可以移除。

</div>

<div class="faq-item" markdown="1">

### 无法启动 VR

DanceXR 使用 OpenXR 来初始化 VR。如果您安装了多个 VR 运行时，需要将其中一个设置为活动的 OpenXR 运行时：

- **Oculus / Meta：** 打开 Oculus 应用 → 设置 → Beta → OpenXR 运行时 → "设为活动"
- **SteamVR：** 打开 SteamVR → 左上角菜单 → 设置 → 开发者 → "设为 OpenXR 运行时"
- **Windows Mixed Reality：** 从 Microsoft Store 下载“Windows Mixed Reality OpenXR Developer Tools”，并从中将 WMR 设为活动运行时

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">📦 模型与内容库</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 模型加载但所有内容都是白色

最常见的原因是文件名编码——当文件名使用不同的字符编码时，贴图无法被定位。

- 对于 ZIP 包，请将编码添加到包名中，以便 DanceXR 知道如何解析文件名。[在此查看详情 →](features/zip_format)
- 文件名中的额外空格也会阻止贴图加载。请在 PMXEditor 中打开模型，并确认贴图引用与实际文件名完全匹配。

</div>

<div class="faq-item" markdown="1">

### 如何在 Android 或 Meta Quest 上设置内容库？

Android 系统有严格的文件访问限制。默认情况下，内容库会放置在应用程序内部存储空间中。

- 使用 USB 将您的设备连接到 PC，选择“文件传输”，然后移至 `/Android/data/com.vrstormlab.dancexr/files/` 或根目录 `/DanceXR/` 文件夹以复制您的 zip/图片文件。
- 在 Android 和 Meta Quest（自版本 2024.3 起），授权 DanceXR 存储访问权限，以便使用系统“文件”应用程序或内置的“内容管理器”应用程序来分享与管理您的库。
- 更多详细信息，请参阅 [Android 与 Quest 内容库](content_android_quest) 指南。

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🎨 画面与渲染</h3>
<div class="faq-grid">

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
- 找到背景天空球，并将其材质从透明更改为不透明。

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🔑 授权与付款</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 被要求重新激活

在进行重大操作系统或硬件更改后，DanceXR 可能无法识别该系统与您的许可证发行时相同的系统。只需再次执行激活步骤即可——不会产生额外费用。请参阅 [激活与许可](activation) 指南。[联系我们](#contact) 如果您遇到问题。

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