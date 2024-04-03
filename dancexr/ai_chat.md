---
locale: en-US
layout: single
title: AI Powered Voice Chat
toc: true
sidebar:
  nav: "docs"
---

[Eng](/dancexr/ai_chat) | [繁中](/tw/dancexr/ai_chat) | [日本語](/jp/dancexr/ai_chat) | [한국어](/kr/dancexr/ai_chat) | [简中](/zh/dancexr/ai_chat)

## AI Powered Voice Chat

### Key features
* Options to use OpenAI, local or remote Text Generation WebUI as AI service
* Built-in TTS engine to convert AI generated messages to voice
* Built-in lipsync that automatically animate characters' facial while they talk
* Built-in voice recognition to convert your voice to text tand send to AI
* Included over 900 English voices to choose from, each character can have their own unique voice

### Limitations 
* Voice engine is Windows only. On other platform you can still use voice recognition to talk but responses will be text only.


## AI Services
There are various options to use as AI service to give your character intelligence. We'll discuss pros and cons for each option below

### OpenAI (ChatGPT)
This is the most intelligent option at the moment. 

**Pros:**
* Smart
* Fast
* Cost effective (comparing to other remote options)

**Cons:**
* Censored

**Setup:**
To use OpenAI service with DanceXR, you need an OpenAI API key.
* Register and login your OpenAI account. 
* Click on your profile icon on the top right corner of the page. 
* Select "View API Keys" to open the API page.
* Click "Create New Secret Key" and copy the key when it shows up. Keep in mind that the key is **only shown here once**, you can't retrieve the full key later so don't lose it. 
* Open DanceXR and click on the Config icon from the Chat menu. 
* Go to AI Service and paste your key in the "OpenAI API Key" box. 
* Then select "OpenAI (ChatGPT)" in the "AI Service" dropdown and you should be good to go.
* In the chat settings you can choose the model that you want to use. 


### OobaBooga Text Generation WebUI 
This option allows you to run large language models (LLM) locally if your PC is powerful enough. A 7b or 13b model should be good enough for chatting. 

**Pros:**
* Privacy, nothing is sent out, everything happens locally.
* You can use uncensored models for NSFW content.
* Free

**Cons:**
* Not as smart as OpenAI models
* Requires a bit setup
* Can become very slow if there's not enough VRAM. Especially when you are running DanceXR at the same time, the system might push LLMs to virtual VRAM which is going to destroy its performance. 

**Setup:** 
* Follow the instructions here to download and install https://github.com/oobabooga/text-generation-webui
* To allow WebUI to work with DanceXR, you need to turn on API. To do this, open the CMD_FLAGS.txt file and add "--listen --api" in there, then restart it.
* Once it's running, go to the model tab and download a model if you don't have it already. 
* We recommend using one of these 2 models: https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ (7b, easier to run) https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ (13b, smarter)
* Refresh the model list and load it. 
* In DanceXR, choose "Local WebUI" from AI Service -> Select Service
* The default URL (http://127.0.0.1:5000) should work unless your setup requries a different port or URL. 


### Use Remote Service like Runpod to run WebUI
There are services that allow you to rent a GPU and run AI models. Runpod is one of them. They have a template for WebUI and it's easier to setup than running locally. 

**Pros:** 
* Fast and easy
* Freedom to choose any model that you want to run. Even those that are impossible to run on your local GPU. 

**Cons:**
* A bit more expensive than OpenAI
* Requires downloading the model everytime you run it. But it should only take a few minutes.

**Setup:**
* Choose a GPU from "Community Cloud" and click on "Deploy". A 3080ti should be more than enough to run a 13b model. That costs 26 cents per hour.
* Select "RunPod TheBloke LLMs" from the template dropdown.
* Once it's running, click on connect and it will give you links to the WebUI and the API, copy the URL for the API and paste it in "Remote WebUI URL" box in DanceXR.
* Click on the WebUI link and then go to the model tab to download a model.
* We recommend using one of these 2 models: https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ (7b, easier to run) https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ (13b, smarter)
* Refresh the model list and load it. 


## Chat Control

### Templates
Template is what drives the AI model to generate chat messages for each character. You might think it's complex but it's actually very simple. You can open chat/templates folder to open the default template to see how it works. 

Basically it's like telling someone to do certain things for you in plain text. You can modify the default template and save as a different name to see how it affects the chat content. For example you can add description of the environment in there to setup the scenario for the chat.

In DanceXR, go to Chat Settings -> Templates to select the template you created. 


### Characters
The characters are derived from the name of the actor model. For example "Koharu Bouquet Cattleya Hair B Side Ponytail", "Koharu" will be interpreted as the character name, the rest "Bouquet Cattleya Hair B Side Ponytail" will be used as description for her outfit. 

The language model might have some knowledge on the character if they are well known, so it sometimes knows who they are and how they behave, especially when you use OpenAI. 

In the character settings you can enter description and personality for the character, and that will greatly affect how they behave in chat. For example you can change a proud and arrogant character to be obedient by just describing them as "Obedient and eager to please".

The "Player" is technically also a character, you can change the name, description and personality for yourself and be whoever you like. 


### Persona
The character setting also have a Persona drop down. This allows you to use characters downloaded from AI roleplay programs like TavernAI. These usually come in PNG format. The metadata of the png images contains description for the character. 

Use this online character editor to convert the png character to json format https://zoltanai.github.io/character-editor/

Then place the json in "chat/personas" folder and they will appear in the Persona drop down in the character settings. Once you've done that, the description of the persona will override the character description.


### Chat History
The chat history is sent to the AI every time you generate new content, in order to maintain a context. If you want to switch to a different scenario or topic, clear the history first so that the AI won't be affected by the previous chat context. You can also use this to manipulate the environment and drive the chat. Like if you describe something happened in your message, the AI will continue on that context.

Please note that once the prompt limit is reached, the oldest messages will be ignored and not included in the context. So the AI might forget things that are too far back in the history.

In the chat interface you can click on the icon next to the chat message to manipulate chat history. Options include:

* Regenerate: Delete all message below and let AI to regenerate this message
* Rewrite: Take over the message and rewrite it yourself. When you do this you need to keep the name and colon in front of the message intact otherwise the system will not know who is this message from.
* Replay: Replay the chat history from this message
* Delete Entry: Delete this message
* Remove above: Delete all messages above this one
* Remove below: Delete all messages below this one


### Temperature
This values controls how much freedom the AI models has when generating chat messages. Just like image generation, with the same input, each time the generation might be slightly different and temperature controls how much it can vary. 


### Presense Penalty and Frequency Penalty
Increase these values to reduce the chance of AI generating repeating content.


### Max Generate Tokens and Max Prompt Length
The LLMs have token limits, content that exceed this limit will not be generated correctly. 


### Auto Generate and Generate For Player
Turn on "Auto Generate Next" to allow AI to automatically generate the next message when the timer is up. 

Turn on "Generate For Player" to allow AI to generate messages for the player.


## Text To Speech

### Additional Voices
DanceXR uses a TTS engine called Piper. Here you can listen to and download additional voice models to use in DanceXR. 

https://rhasspy.github.io/piper-samples/

Once downloaded, put them in chat\voices\piper folder. Keep in mind that both the onnx and onnx.json files are required. 


### Voice Manager
The built-in voice model contains over 900 different voices. By default we are only enabling the first 20 of them. Since 900 is too many for the user to choose from. To enable other voices, go to Voice -> Voice Manager from the chat settings, choose one of the voices from the list, listen to it and tick "Selected" to allow it to be added to the voice list.

You can choose different voice for System, Player and each of the characters. 


### Language Matching & Fallback
The AI model can generate different language messages. But the voice model can't. DanceXR will try to determine what language the message is and if it doesn't match the selected voice language, enabling "Fallback" in the voice settings will allow it to choose a different voice that matches the language within the voice list.

New setting introduced in 1.5.1 update allows selection of a chat language, on top of the default "auto" mode. The auto mode will behave exactly like before, it tries to determine language from the text content itself. But if you choose one of the language in the chat language settings, it will be used for both chat message and voice.

Keep in mind that the prompt message has a higher imfluence to the GPT models in deciding what language to use when generating responses. If you choose a language other than English, it's best to also update the prompt template with native text to the language you are choosing. 


## Speech To Text
The built-in Whisper model can convert your voice to text and then send to AI. There are 2 modes, manual and automatic.

### Manual Mode
Manual mode means you click on the microphone button, it starts recording, and once you are done, click on it again and the audio will be processed and result will then be sent to AI. 


### Automatic Mode
Automatic mode means it will automatically start recording when chat is idle (Characters not talking), processing the audio on the fly and then sends it when you are done talking. However sometimes it is not very smart. 

For lower end devices, processing audio to text can take some time. So the automatic mode is not recommended for Android and Quest.


### Key Binding
In the Input Settings, you can assign a button to toggle the microphone state, so you can control recording without entering the UI. By default it is assigned to right hand controller menu button.


## Resetting Configurations and Character Settings
Everything is saved in the chat folder of your content library. Feel free to delete the chat folder to reset everything to default. 
