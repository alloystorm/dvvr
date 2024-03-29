---
locale: zh-CN
layout: single
title: 人工智能语音聊天
toc: true
sidebar:
  nav: "docs-zh"
---

[Eng](/dancexr/ai_chat) | [繁中](/tw/dancexr/ai_chat) | [日本語](/jp/dancexr/ai_chat) | [한국어](/kr/dancexr/ai_chat) | [简中](/zh/dancexr/ai_chat)

## 人工智能语音聊天

### 主要特点
* 可选择使用OpenAI、本地或远程文本生成WebUI作为人工智能服务
* 内置TTS引擎，将人工智能生成的消息转换为语音
* 内置的口型同步功能，在角色说话时自动为其面部进行动画
* 内置语音识别，将您的语音转换为文本并发送给人工智能
* 包含超过900种英文语音可供选择，每个角色都可以拥有自己独特的声音

### 限制
* 语音引擎仅适用于Windows。在其他平台上，您仍然可以使用语音识别进行交流，但回复将仅为文本形式。
## ## AI服务
有各种选项可用作AI服务，为您的角色赋予智能。我们将在下面讨论每个选项的利弊。

### OpenAI（ChatGPT）
这是目前最智能的选项。

**优点：**
* 聪明
* 快速
* 成本效益（与其他远程选项相比）

**缺点：**
* 被审查

**设置：**
要在DanceXR中使用OpenAI服务，您需要一个OpenAI API密钥。
* 注册并登录您的OpenAI帐户。
* 单击页面右上角的个人资料图标。
* 选择“查看API密钥”以打开API页面。
* 单击“创建新的秘密密钥”，并在显示时复制密钥。请记住，密钥**只在此处显示一次**，以后无法检索完整密钥，因此不要丢失。
* 打开DanceXR，单击聊天菜单中的配置图标。
* 转到AI服务，并将密钥粘贴到“OpenAI API密钥”框中。
* 然后在“AI服务”下拉菜单中选择“OpenAI（ChatGPT）”，然后应该可以使用了。
* 在聊天设置中，您可以选择要使用的模型。

### OobaBooga文本生成WebUI
如果您的PC性能足够强大，此选项允许您在本地运行大型语言模型（LLM）。7b或13b模型应该足够用于聊天。

**优点：**
* 隐私，不会发送任何内容，一切都在本地发生。
* 您可以使用NSFW内容的未经审查的模型。
* 免费

**缺点：**
* 不如OpenAI模型聪明
* 需要一些设置
* 如果VRAM不足，可能会变得非常慢。特别是当您同时运行DanceXR时，系统可能会将LLM推送到虚拟VRAM，这将破坏其性能。

**设置：**
* 按照此处的说明下载并安装https://github.com/oobabooga/text-generation-webui
* 要使WebUI与DanceXR配合工作，您需要打开API。要做到这一点，打开CMD_FLAGS.txt文件，并在其中添加“--listen --api”，然后重新启动它。
* 运行后，转到模型选项卡并下载模型（如果尚未拥有）。
* 我们建议使用以下两个模型之一：https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ（7b，更容易运行）https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ（13b，更聪明）
* 刷新模型列表并加载它。
* 在DanceXR中，从AI服务->选择服务中选择“本地WebUI”。
* 默认URL（http://127.0.0.1:5000）应该有效，除非您的设置需要不同的端口或URL。

### 使用Runpod等远程服务运行WebUI
有一些服务允许您租用GPU并运行AI模型。Runpod就是其中之一。他们有一个WebUI的模板，比在本地运行更容易设置。

**优点：**
* 快速且简单
* 自由选择要运行的任何模型。甚至是在本地GPU上无法运行的模型。

**缺点：**
* 比OpenAI稍微昂贵一些
* 每次运行模型都需要下载。但这应该只需要几分钟。

**设置：**
* 从“社区云”中选择一个GPU，然后单击“部署”。3080ti应该足够运行13b模型。每小时需要花费26美分。
* 从模板下拉菜单中选择“RunPod TheBloke LLMs”。
* 运行后，单击连接，它将为您提供WebUI和API的链接，将API的URL复制并粘贴到DanceXR中的“远程WebUI URL”框中。
* 单击WebUI链接，然后转到模型选项卡以下载模型。
* 我们建议使用以下两个模型之一：https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ（7b，更容易运行）https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ（13b，更聪明）
* 刷新模型列表并加载它。
## ## 聊天控制

### 模板
模板是驱动AI模型为每个角色生成聊天消息的内容。你可能会认为它很复杂，但实际上它非常简单。你可以打开chat/templates文件夹来打开默认模板，看看它是如何工作的。

基本上就像是用纯文本告诉某人为你做某些事情。你可以修改默认模板并保存为不同的名称，看看它如何影响聊天内容。例如，你可以在其中添加环境的描述，为聊天设置情景。

在DanceXR中，转到聊天设置 -> 模板，选择你创建的模板。


### 角色
角色是根据演员模型的名称派生的。例如，“Koharu Bouquet Cattleya Hair B Side Ponytail”，“Koharu”将被解释为角色名称，“Bouquet Cattleya Hair B Side Ponytail”将被用作她的服装描述。

语言模型可能对角色有一些了解，特别是当你使用OpenAI时，它有时会知道他们是谁以及他们的行为方式。

在角色设置中，你可以输入角色的描述和个性，这将极大地影响他们在聊天中的行为。例如，你可以通过描述将一个骄傲和傲慢的角色改变为服从的角色，只需描述他们为“服从并渴望取悦”。

“玩家”在技术上也是一个角色，你可以更改名称、描述和个性，成为你喜欢的任何人。


### 人物
角色设置还有一个Persona下拉菜单。这允许你使用从AI角色扮演程序（如TavernAI）下载的角色。这些通常以PNG格式提供。PNG图像的元数据包含了角色的描述。

使用这个在线角色编辑器将png角色转换为json格式 https://zoltanai.github.io/character-editor/

然后将json放在“chat/personas”文件夹中，它们将出现在角色设置中的Persona下拉菜单中。一旦你这样做了，Persona的描述将覆盖角色的描述。


### 聊天历史
每次生成新内容时，聊天历史都会发送给AI，以保持上下文。如果你想切换到不同的情景或话题，首先清除历史，这样AI就不会受到先前聊天上下文的影响。你也可以用这个来操纵环境和驱动聊天。比如，如果你在你的消息中描述了发生的事情，AI将继续在那个情景下进行。

请注意，一旦达到提示限制，最旧的消息将被忽略，不会包含在上下文中。所以AI可能会忘记太久远的事情。

在聊天界面中，你可以点击聊天消息旁边的图标来操纵聊天历史。选项包括：

* 重新生成：删除下面的所有消息，让AI重新生成这条消息
* 重写：接管消息并自己重写。当你这样做时，你需要保持消息前面的名称和冒号不变，否则系统将不知道这条消息是谁发出的。
* 重播：从这条消息开始重播聊天历史
* 删除条目：删除这条消息
* 删除上面的：删除这条消息上面的所有消息
* 删除下面的：删除这条消息下面的所有消息


### 温度
这个值控制AI模型在生成聊天消息时的自由度。就像图像生成一样，使用相同的输入，每次生成可能会略有不同，温度控制它可以变化多少。


### 存在惩罚和频率惩罚
增加这些值可以减少AI生成重复内容的机会。


### 最大生成标记和最大提示长度
LLMs有标记限制，超出这个限制的内容将无法正确生成。


### 自动生成和为玩家生成
打开“自动生成下一条”以允许AI在计时器结束时自动生成下一条消息。

打开“为玩家生成”以允许AI为玩家生成消息。
## ## 文字转语音

### 附加语音
DanceXR使用一个名为Piper的TTS引擎。在这里，您可以收听并下载其他语音模型，以在DanceXR中使用。

https://rhasspy.github.io/piper-samples/

下载后，请将它们放入chat\voices\piper文件夹中。请记住，onnx和onnx.json文件都是必需的。

### 语音管理器
内置语音模型包含超过900种不同的语音。默认情况下，我们只启用前20种。因为900种对用户来说太多了。要启用其他语音，请转到聊天设置中的Voice -> Voice Manager，从列表中选择一种语音，收听它并选中“Selected”以允许将其添加到语音列表中。

您可以为系统、播放器和每个角色选择不同的语音。

### 语言匹配和回退
AI模型可以生成不同语言的消息。但语音模型不能。DanceXR将尝试确定消息的语言，如果与所选语音的语言不匹配，则在语音设置中启用“Fallback”将允许它选择与语音列表中的语言匹配的其他语音。

1.5.1更新中引入的新设置允许选择聊天语言，除了默认的“auto”模式。自动模式将与以前完全相同，它会尝试从文本内容本身确定语言。但如果您在聊天语言设置中选择了一种语言，它将用于聊天消息和语音。

请记住，提示消息对于GPT模型在决定生成响应时使用的语言具有更高的影响。如果您选择的语言不是英语，最好还更新提示模板，使用所选择语言的本地文本。

## 语音转文字
内置的Whisper模型可以将您的语音转换为文本，然后发送给AI。有两种模式，手动和自动。

### 手动模式
手动模式意味着您点击麦克风按钮，它开始录音，一旦完成，再次点击它，音频将被处理，然后结果将被发送给AI。

### 自动模式
自动模式意味着当聊天处于空闲状态（角色不说话）时，它将自动开始录音，实时处理音频，然后在您说完后发送它。但有时它并不是很智能。

对于低端设备，处理音频到文本可能需要一些时间。因此，不建议在Android、Quest和Pico上使用自动模式。

### 按键绑定
在输入设置中，您可以分配一个按钮来切换麦克风状态，这样您就可以在不进入UI的情况下控制录音。默认情况下，它被分配给右手控制器的菜单按钮。

## 重置配置和角色设置
所有内容都保存在您内容库的chat文件夹中。随时删除chat文件夹以将所有内容重置为默认值。