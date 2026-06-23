---
layout: studio-home
title: 支持
toc: false
locale: zh-CN
lang_path: /dancexr/support
hero_compact: true
hero_title: 支持
hero_image: /images/hero.png
support_sections:
  - id: known-issues
    light: true
    label: 已知问题
    title: 已知问题与解决方法
    subsections:
      - title: 📌 版本 2026.6
        items:
          - question: 在动作设置中使用 T 姿势或自定义骨骼绑定时动作损坏
            answer: |
              这是由动作平滑系统中的 bug 引起的。临时解决方法：在动作设置中禁用动作平滑。
  - id: faq
    label: 常见问题
    title: 常见问题解答 (FAQ)
    subsections:
      - title: 🌐 常见问题
        items:
          - question: 模型已加载但全部显示为白色
            answer: |
              最常见的原因是文件名编码问题 —— 当文件名使用不同的字符编码时，将无法定位贴图。
              
              - 对于 ZIP 压缩包，请在压缩包名称中添加编码，以便 DanceXR 能够正确解析文件名。[详细信息请参阅此页面 →](features/zip_format)
              - 文件名中的额外空格也可能导致贴图无法加载。请在 PMXEditor 中打开模型，验证贴图引用是否与实际文件名完全一致。
          - question: 头发材质透光/透明
            answer: |
              半透明深度预处理（Transparency depth prepass）默认处于开启状态。它通过仅渲染最顶层的透明层来修正半透明排序问题 —— 这意味着多层叠加的半透明（如分层头发）只显示最外层。
              
              - 关闭半透明深度预处理以渲染所有半透明层。如果模型的材质顺序不正确，这可能会引入排序错误/伪影。
              - 没有十全十美的通用解决方案 —— 请尝试不同的配置，选择视觉问题较少的那一种。
          - question: 舞台模型的天空球有破洞或看起来有像素颗粒
            answer: |
              同样是由半透明深度预处理引起的 —— 当存在多个半透明天空球时，在某些区域只会完全渲染最顶层。
              
              - 关闭半透明深度预处理，或者
              - 找到背景天空球，并将其材质从半透明更改为不透明。
      - title: 🛠️ 报告问题前的检查清单
        items:
          - question: 在报告 bug 之前，请尝试以下快速修复方法：
            answer: |
              1. **更新至最新版本** —— 您的问题可能已在新版本中得到解决。
              2. **重置配置** —— 备份并删除 `config.json` 以排除配置文件损坏的情况。
              3. **重置授权/许可证** —— 如果应用无法启动或行为异常，请尝试从安装目录中删除 `license.txt` 并重新启动。
              4. **清除媒体库缓存** —— 备份并删除内容库文件夹中的 `cache.json`，以强制播放器重新扫描您的文件。
              5. **OpenXR 设置** —— 如果 VR 无法启动，请仔细检查您的 VR 软件设置中是否正确设置了当前活动的 OpenXR 运行时。
          - question: 在哪里可以找到日志文件？
            answer: |
              报告 bug 时，附上日志文件会非常有帮助。请在您的 bug 报告中附带 **`Player.log`**（当前会话）和 **`Player-prev.log`**（上一次会话）。
              
              **Windows PC 路径：**
              ```
              C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
              ```
              *注意：请将 `[User]` 替换为您的 Windows 用户名。如果 AppData 文件夹被隐藏，请在 Windows 文件资源管理器中启用“隐藏的项目”。*
              
              **Android 和 Meta Quest 路径：**
              ```
              /Android/data/com.vrstormlab.dancexr/files/Player.log
              ```
              *注意：通过 USB 将您的设备连接到电脑，并使用文件传输模式来定位此文件。*
      - title: 🖥️ 系统与 VR 启动
        items:
          - question: 只显示天空 —— 没有 UI 或相机控制界面
            answer: |
              这通常意味着在启动过程中出了问题。请按顺序尝试以下步骤：
              
              - 删除 `license.txt` 并重新启动。
              - 删除（请先备份）`config.json` —— 这将重置所有设置并修复由于配置文件损坏引起的问题。
              - 从您的内容媒体库中删除（请先备份）`cache.json`。
          - question: 每次启动都崩溃 —— 回退到旧版本也无济于事
            answer: |
              这通常是 VR 运行时的问题，而不是 DanceXR 本身的问题。
              
              - 如果您安装了多个 VR 运行时，请尝试切换到另一个。
              - 对于 SteamVR：禁用不需要的启动叠加层（overlays）和插件；尝试干净的重新安装。
              - 检查 SteamVR 的 `driver` 文件夹，看看是否有最近安装或更新的可以删除的项目。
          - question: 无法启动 VR
            answer: |
              DanceXR 使用 OpenXR 来初始化 VR。如果您安装了多个 VR 运行时，则需要将其中一个设置为活动的 OpenXR 运行时：
              
              - **Oculus / Meta：** 打开 Oculus 应用 → 设置 → 测试版 → OpenXR 运行时 → 点击“将 Oculus 设置为活动”。
              - **SteamVR：** 打开 SteamVR → 左上角菜单 → 设置 → 开发者 → 点击“将 SteamVR 设置为 OpenXR 运行时”。
              - **Windows Mixed Reality：** 从 Microsoft Store 下载 “Windows Mixed Reality OpenXR Developer Tools”，并从中将 WMR 设置为活动。
      - title: 📦 媒体库设置
        items:
          - question: 如何在 Android 或 Meta Quest 上设置我的内容媒体库？
            answer: |
              Android 系统具有严格的文件访问规则。默认情况下，内容媒体库位于应用内部存储中。
              
              - 通过 USB 将您的设备连接到电脑，选择“文件传输”模式，然后导航到 `/Android/data/com.vrstormlab.dancexr/files/` 或根目录的 `/DanceXR/` 文件夹以复制您的 zip/图像文件。
              - 在 Android 和 Meta Quest（自 2024.3 版本起）上，授予 DanceXR 存储权限以使用系统“文件”应用或内置的“内容管理器”应用来共享和管理您的媒体库。
              - 有关更多详细信息，请参阅 [Android 和 Quest 内容媒体库](content_android_quest) 指南。
      - title: 🔑 授权与支付
        items:
          - question: 提示需要再次激活
            answer: |
              在重大 OS 或硬件更改后，DanceXR 可能无法将系统识别为签发许可证时的系统。只需再次运行激活步骤即可 —— 没有额外费用。请参阅 [激活与授权](activation) 指南。如果您遇到问题，请 [联系我们](#contact)。
---


<div class="support-search-container">
  <input type="text" id="supportSearch" class="support-search-input" placeholder="Search issues, keywords, or error codes...">
</div>
<script src="/assets/js/support-search.js"></script>

{% for section in page.support_sections %}
<!-- ── {{ section.label }} ───────────────────────────────────────────── -->
<section class="section {% if section.light %}section-light{% endif %}" id="{{ section.id }}">
<div class="editions-header" markdown="1">

{:.section-label}
{{ section.label }}

## {{ section.title }}

</div>

{% for sub in section.subsections %}
<h3 class="faq-subsection">{{ sub.title }}</h3>
<div class="faq-grid">

{% for item in sub.items %}
<div class="faq-item{% if section.id == 'known-issues' %} known-issue{% endif %}" markdown="1">

### {{ item.question }}

{{ item.answer }}

</div>
{% endfor %}

</div>
{% endfor %}

</section>
{% endfor %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
支持中心

## 我们能为您提供什么帮助？

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">浏览文档</h3>
    <p class="support-desc">功能与选项指南</p>
    <a href="features" class="support-cta">打开文档</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">故障排除</h3>
    <p class="support-desc">报告前检查清单</p>
    <a href="#troubleshooting" class="support-cta">查看清单</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">激活</h3>
    <p class="support-desc">管理您的授权密钥</p>
    <a href="activation" class="support-cta">激活指南</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
联系我们

## 报告 Bug 或联系我们

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">Bug 追踪与功能请求</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">提交 Issue</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">社区支持</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">加入 Discord</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">邮件</h3>
    <p class="support-desc">商务与直接咨询</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">发送邮件</a>
  </div>

</div>

</section>