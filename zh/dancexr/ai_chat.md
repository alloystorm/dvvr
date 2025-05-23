---
locale: zh-CN
layout: single
title: AI驱动的语音聊天
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/ai_chat) | [繁中](/tw/dancexr/ai_chat) | [日本語](/jp/dancexr/ai_chat) | [한국어](/kr/dancexr/ai_chat) | [简中](/zh/dancexr/ai_chat)

## AI 驱动的语音聊天

### 主要特性
* 使用 OpenAI、本地或远程文本生成 WebUI 作为 AI 服务的选项
* 内置 TTS 引擎，将 AI 生成的消息转换为语音
* 内置口型同步，会自动为角色的面部动画同步他们的说话
* 内置语音识别，将您的语音转换为文本并发送给 AI
* 包含超过 900 种英语语音供选择，每个角色可以有自己独特的声音

### 限制
* 语音引擎仅支持 Windows。在其他平台上，您仍然可以使用语音识别进行对话，但回应将仅为文本。

## AI 服务
有多种选项可作为 AI 服务，为您的角色提供智能。我们将在下面讨论每种选项的优缺点。

### OpenAI（ChatGPT）
这是目前最智能的选项。

**优点：**
* 聪明
* 快速
* 成本效益高（与其他远程选项相比）

**缺点：**
* 审查

**设置：**
要将 OpenAI 服务与 DanceXR 一起使用，您需要一个 OpenAI API 密钥。
* 注册并登录您的 OpenAI 帐户。
* 点击页面右上角的个人资料图标。
* 选择“查看 API 密钥”打开 API 页面。
* 点击“创建新的密钥”并在显示时复制密钥。请记住，密钥 **只显示一次**，您不能稍后检索完整密钥，因此请勿丢失它。
* 打开 DanceXR，从聊天菜单中点击配置图标。
* 在 AI 服务中，将您的密钥粘贴到“OpenAI API 密钥”框中。
* 然后在“AI 服务”下拉菜单中选择“OpenAI（ChatGPT）”，您就可以开始使用了。
* 在聊天设置中，您可以选择要使用的模型。

### 本地运行 LLM（LM Studio, OobaBooga, Ollama）
如果您的计算机足够强大，也可以在本地运行 LLM。例如，最新的 Llama3 8b 对于角色扮演来说应该足够。我们测试了 OobaBooga、LM Studio 和 Ollama，它们与 DanceXR 配合良好。

请记住，AI 领域发展迅速，新工具和模型不断推出。此处的推荐基于我们在撰写时的知识，在您阅读时可能会过时。欢迎您探索自己的选择。DanceXR 应该可以与任何支持 OpenAI API 规范的 LLM 工具一起使用。

**优点：**
* 隐私，所有操作都在本地进行，没有数据被发送出去。
* 您可以选择任何模型进行运行，包括未审查的模型。
* 免费

**缺点：**
* 不如在线模型智能
* 需要一些设置
* 在本地运行 LLM 可能非常耗资源，特别是如果您计划在同一台机器上运行 DanceXR 和 LLM。

**设置：** 
目前，如果您不想使用命令行工具，LM Studio 是更好的选择。
对于 LM Studio，您可以按照以下说明进行操作：
* 从其网站下载并安装 LM Studio https://lmstudio.ai/
* 在 LM Studio 中选择并下载一个 LLM 模型。目前我们推荐使用 Llama3 8b。
* 切换到聊天选项卡并加载您下载的模型。
* 转到“本地服务器”选项卡并点击“启动服务器”。注意端口号（默认为 1234）。

对于 OobaBooga，您可以按照以下说明进行操作：
* 按此处的说明下载并安装 https://github.com/oobabooga/text-generation-webui
* 为了使 WebUI 能与 DanceXR 一起工作，您需要启用 API。为此，请打开 CMD_FLAGS.txt 文件并在其中添加“--listen --api”，然后重新启动。
* 一旦它正在运行，转到模型选项卡，如果您尚未拥有模型，请下载一个模型。
* 我们推荐使用以下 2 个模型中的一个：https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ (7b，更容易运行) 或 https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ (13b，更智能)
* 刷新模型列表并加载它。默认端口号是 5000。

**Ollama 的设置：**
Ollama 提供了一种轻松在本地运行 AI 模型的方法，设置非常简单。
* 从他们的网站下载并安装 Ollama：https://ollama.ai/
* 打开 Ollama 应用程序并下载您选择的模型。
* 在 DanceXR 中，从 AI 服务选择“Ollama” -> 选择服务。
* 在“模型名称”框中输入模型名称。例如，输入“llama2-7b-chat”。
* 现在您应该能够将 Ollama 作为您的 AI 后端使用。

DanceXR 中的配置： 
* 在 DanceXR 中，从 AI 服务选择“本地 WebUI” -> 选择服务
* 输入服务器 URL 和端口号。例如“http://127.0.0.1:1234”（LM Studio）或“http://127.0.0.1:5000”（OobaBooga）。 

### 使用像 Runpod 这样的远程服务运行 WebUI
有些服务允许您租用 GPU 并运行 AI 模型。Runpod 便是其中之一。他们有一个 WebUI 模板，比在本地运行更容易设置。

**优点：** 
* 快速和简单
* 自由选择您想要运行的任何模型。甚至可以运行本地 GPU 无法运行的模型。

**缺点：**
* 比 OpenAI 稍贵
* 每次运行时都需要下载模型，但应该只需几分钟。

**设置：**
* 从“社区云”中选择一个 GPU 并点击“部署”。一块 3080ti 就足以运行一个 13b 模型。费用为每小时 26 美分。
* 从模板下拉菜单中选择“RunPod TheBloke LLMs”。
* 一旦它正在运行，点击连接，它会给您提供 WebUI 和 API 的链接，复制 API 的 URL 并粘贴到 DanceXR 的“远程 WebUI URL”框中。
* 点击 WebUI 链接，然后转到模型选项卡下载模型。
* 我们推荐使用以下 2 个模型中的一个：https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ (7b，更容易运行) 或 https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ (13b，更智能)
* 刷新模型列表并加载它。 

### 改进本地模型的提示
DanceXR 现在包含改进的提示技术，以增强对话质量，尤其是在使用较小的本地模型时。这确保了更好的回应和更有趣的互动。

## 聊天控制

### 模板
模板驱动 AI 模型为每个角色生成聊天消息。您可能认为这很复杂，但其实很简单。您可以打开聊天/模板文件夹，查看默认模板以了解它是如何工作的。

基本上，这就像用普通文本告诉某人为您做某些事情一样。您可以修改默认模板并另存为不同的名称，以查看它对聊天内容的影响。例如，您可以在其中添加环境描述，以设置聊天的场景。

在 DanceXR 中，转到聊天设置 -> 模板，以选择您创建的模板。

### 角色
角色是由演员模型的名称派生而来的。例如，“Koharu Bouquet Cattleya Hair B Side Ponytail”，其中“Koharu”将被解释为角色名称，剩下的“Bouquet Cattleya Hair B Side Ponytail”将作为她的服装描述。

如果角色是知名的，语言模型可能具备一些角色的知识，因此它有时会知道他们是谁以及他们的行为方式，尤其是当您使用 OpenAI 时。

在角色设置中，您可以输入角色的描述和个性，这将极大地影响他们在聊天中的行为。例如，您可以将一个骄傲和傲慢的角色通过将其描述为“顺从和渴望取悦”而改造成顺从的角色。

“玩家”实际上也是一个角色，您可以更改自己的名称、描述和个性，成为您想要的任何人。

### 人物
角色设置还有一个“人物”下拉菜单。这允许您使用从 AI 角色扮演程序（如 TavernAI）下载的角色。这些通常以 PNG 格式提供。PNG 图像的元数据包含角色的描述。

使用此在线角色编辑器将 PNG 角色转换为 JSON 格式 https://zoltanai.github.io/character-editor/

然后将 JSON 文件放入“chat/personas”文件夹中，它们将出现在角色设置的人物下拉菜单中。一旦完成，人物的描述将覆盖角色的描述。

### 聊天历史
聊天历史每次生成新内容时都会发送给 AI，以保持上下文。如果您想切换到不同的场景或主题，请先清除历史记录，以便 AI 不会受到先前聊天上下文的影响。您还可以使用此功能来操控环境并推动聊天进程。如果您在消息中描述某件事情，AI 将会继续该上下文。

请注意，一旦达到提示限制，最旧的消息将被忽略，不会包括在上下文中。因此，AI 可能会忘记历史中太久远的内容。

在聊天界面中，您可以点击聊天消息旁边的图标来操控聊天历史。选项包括：

* 重新生成：删除下面的所有消息，让 AI 重新生成此消息
* 重写：接管该消息并自行重写。当您这样做时，必须保持消息前面的名称和冒号不变，否则系统将不知道此消息来自谁。
* 重播：从此消息重新播放聊天历史
* 删除条目：删除此消息
* 移除上方：删除此消息上方的所有消息
* 移除下方：删除此消息下方的所有消息

### 温度
该数值控制 AI 模型在生成聊天消息时的自由度。就像图像生成一样，相同的输入每次生成可能会略有不同，而温度控制它的变化程度。

### 存在惩罚和频率惩罚
增加这些值以减少 AI 生成重复内容的可能性。

### 最大生成令牌和最大提示长度
LLM 有令牌限制，超过此限制的内容将无法正确生成。

### 自动生成和为玩家生成
开启“自动生成下一个”以允许 AI 在计时器到期时自动生成下一个消息。

开启“为玩家生成”以允许 AI 为玩家生成消息。

## 语音合成

### 附加语音
DanceXR 使用名为 Piper 的 TTS 引擎。在这里，您可以收听并下载额外的语音模型以在 DanceXR 中使用。

https://rhasspy.github.io/piper-samples/

下载后，将它们放入 chat\voices\piper 文件夹。请记住，onnx 和 onnx.json 文件都是必需的。

### 语音管理器
内置的语音模型包含超过 900 种不同的声音。默认情况下，我们只启用前 20 种。因为 900 种选择对于用户来说太多了。要启用其他声音，请从聊天设置转到语音 -> 语音管理器，从列表中选择一种声音，收听并勾选“已选择”，以允许它添加到语音列表中。

您可以为系统、玩家和每个角色选择不同的声音。

### 语言匹配与回退
AI 模型可以生成不同语言的消息。但语音模型不能。DanceXR 将尝试判断消息的语言，如果它与所选语音语言不匹配，则启用语音设置中的“回退”将允许其在语音列表中选择匹配语言的不同声音。

在 1.5.1 更新中引入的新设置允许选择聊天语言，除了默认的“自动”模式。自动模式的行为与之前完全相同，尝试根据文本内容判断语言。但是，如果您在聊天语言设置中选择了一种语言，则将用于聊天消息和语音。

请记住，提示消息在决定生成回应时对 GPT 模型的影响较大。如果您选择的语言不是英语，最好也用您选择的语言更新提示模板。

## 语音转文本
内置的 Whisper 模型可以将您的语音转换为文本，然后发送给 AI。有两种模式，手动和自动。

### 手动模式
手动模式意味着您点击麦克风按钮，它开始录音，完成后再次点击，音频将被处理，结果将发送给 AI。

### 自动模式
自动模式意味着在聊天空闲时（角色未说话）会自动开始录音，实时处理音频，完成后将其发送。但是有时它不是很聪明。

对于低端设备，处理音频转文本可能需要一些时间。因此，不建议在 Android 和 Quest 上使用自动模式。

### 关键绑定
在输入设置中，您可以为切换麦克风状态分配一个按钮，这样您就可以在不进入 UI 的情况下控制录音。默认情况下，它被分配给右手控制器的菜单按钮。

## 重置配置和角色设置
所有内容都保存在您的内容库的聊天文件夹中。随时可以删除聊天文件夹以将所有内容重置为默认设置。