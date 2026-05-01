---
layout: release
title: AI Powered Voice Chat
locale: en-US
nav_links:
  - label: Intro
    url: /dancexr
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
---



## AI Powered Voice Chat

DanceXR now supports a more complete local AI chat workflow through DanceXR Operator, the dedicated local AI backend introduced in the 2026.5 release. Operator runs as a local server alongside the game and provides the foundation for AI conversation, roleplay, and character voice features without requiring any external online service.

If you want the most up-to-date AI chat experience in DanceXR, Operator is now the recommended setup.

### Key features
* Recommended support for DanceXR Operator as the dedicated local AI backend
* AI chat that can use scene context, memory, and multi-turn history for longer roleplay sessions
* TTS support to convert AI generated messages to voice
* Built-in lipsync that automatically animates characters' faces while they talk
* Built-in voice recognition to convert your voice to text and send it to AI
* Support for multiple voices and languages, so each character can have a distinct speaking style

### Limitations 
* Some voice features still depend on platform and backend configuration. On platforms where voice output is unavailable, AI responses can still be shown as text.


## AI Services
DanceXR now focuses on local AI chat backends. The recommended option is DanceXR Operator, but other manual local backends are still available if you prefer them.

### DanceXR Operator
DanceXR Operator is the dedicated local AI backend for DanceXR. It runs as a local server alongside the game, bundling voice synthesis and large language model chat behind a unified API so DanceXR can provide AI conversation, roleplay, and character voice features through one local service.

Operator is what powers the new AI chat stack introduced in the 2026.5 release. It is designed to run on your own gaming PC, manage the model and voice pipeline locally, and provide a more reliable foundation for longer, scene-aware character interaction.

**Pros:**
* Designed specifically for DanceXR
* Runs locally on your own hardware
* Supports AI chat, roleplay, and character voice through one backend
* Better suited for scene-aware, persistent multi-turn interaction

**Cons:**
* Requires a local install next to your DanceXR folder
* Performance still depends on your hardware and selected models

**Setup:**
* Install Operator next to your DanceXR folder. See the [DanceXR Operator](/dancexr/features/operator) feature page for installation details.
* Enable AI Chat in DanceXR and select Operator as the backend when available.
* Once installed in the recommended folder structure, Operator can start automatically with DanceXR and expose its web interface locally for model and TTS management.

### AI chat improvements in 2026.5
The latest AI chat stack includes several workflow improvements that apply most directly when using Operator:

* **Environment awareness**: Characters can use scene facts such as time, lighting, and stage context more consistently.
* **Memory and persistence**: Multi-turn history, intent tracking, session persistence, and memory compression help conversations carry forward more naturally.
* **Better interaction flow**: Prompt handling, speaker turns, startup behavior, and status reporting were refined for longer sessions.
* **Improved TTS behavior**: Voice quality, language support, and fallback behavior have all been improved.

### Running LLM Locally (LM Studio, OobaBooga, Ollama)
You can also run LLMs locally if your computer is powerful enough. For example, the latest Llama3 8b should be more than enough for role-playing. We have tested OobaBooga, LM Studio, and Ollama, and they work well with DanceXR.

These options are still useful if you want a custom manual setup, but they are now alternatives to Operator rather than the primary recommended path.

Keep in mind that the AI space is developing really fast and new tools and models are coming out all the time. The recommendations here are based on what we know at the time of writing and might be out of date when you are reading it. Feel free to explore your own options. DanceXR should work with local LLM tools that expose a compatible chat API.

**Pros:**
* Privacy, nothing is sent out, everything happens locally.
* You can choose any model to run, including uncensored ones.
* Free

**Cons:**
* Not as smart as online models
* Requires a bit of setup
* Running LLMs locally can be very resource-intensive, especially if you plan to run both DanceXR and LLMs on the same machine.

**Setup:** 
At the moment LM Studio is a better choice if you don't want to fiddle with command line tools. 
For LM Studio, you can follow the instructions here:
* Download and install LM Studio from their website https://lmstudio.ai/
* Choose and download a LLM model from within LM Studio. At the moment we recommend using Llama3 8b.
* Switch to the chat tab and load the model you downloaded.
* Go to "Local Server" tab and click "Start Server". Note the port number (Default is 1234).
  
For OobaBooga, you can follow the instructions here:
* Follow the instructions here to download and install https://github.com/oobabooga/text-generation-webui
* To allow WebUI to work with DanceXR, you need to turn on API. To do this, open the CMD_FLAGS.txt file and add "--listen --api" in there, then restart it.
* Once it's running, go to the model tab and download a model if you don't have it already. 
* We recommend using one of these 2 models: https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ (7b, easier to run) https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ (13b, smarter)
* Refresh the model list and load it. The default port number is 5000.

**Setup for Ollama:**
Ollama provides an easy way to run local AI models with minimal setup.
* Download and install Ollama from their website: https://ollama.ai/
* Open the Ollama app and download a model of your choice.
* In DanceXR, choose "Ollama" from AI Service -> Select Service.
* Enter the model name in the "Model Name" box. For example, "llama2-7b-chat".
* You should now be able to use Ollama as your AI backend.

Configurations in DanceXR: 
* In DanceXR, choose "Local WebUI" from AI Service -> Select Service
* Type in the server URL and port number. For example "http://127.0.0.1:1234"(LM Studio) or "http://127.0.0.1:5000"(OobaBooga). 


### Improved Prompting for Local Models
DanceXR now includes improved prompting techniques to enhance conversation quality, especially when using smaller local models. This ensures better responses and more engaging interactions.


## Chat Control

### Templates
Template is what drives the AI model to generate chat messages for each character. You might think it's complex but it's actually very simple. You can open chat/templates folder to open the default template to see how it works. 

Basically it's like telling someone to do certain things for you in plain text. You can modify the default template and save as a different name to see how it affects the chat content. For example you can add description of the environment in there to setup the scenario for the chat.

In DanceXR, go to Chat Settings -> Templates to select the template you created. 


### Characters
The characters are derived from the name of the actor model. For example "Koharu Bouquet Cattleya Hair B Side Ponytail", "Koharu" will be interpreted as the character name, the rest "Bouquet Cattleya Hair B Side Ponytail" will be used as description for her outfit. 

The language model might have some knowledge on the character if they are well known, so it sometimes knows who they are and how they behave depending on the model you are using.

In the character settings you can enter description and personality for the character, and that will greatly affect how they behave in chat. For example you can change a proud and arrogant character to be obedient by just describing them as "Obedient and eager to please".

The "Player" is technically also a character, you can change the name, description and personality for yourself and be whoever you like. 


### Persona
The character setting also have a Persona drop down. This allows you to use characters downloaded from AI roleplay programs like TavernAI. These usually come in PNG format. The metadata of the png images contains description for the character. 

Use this online character editor to convert the png character to json format https://zoltanai.github.io/character-editor/

Then place the json in "chat/personas" folder and they will appear in the Persona drop down in the character settings. Once you've done that, the description of the persona will override the character description.


### Chat History
The chat history is sent to the AI every time you generate new content, in order to maintain a context. If you want to switch to a different scenario or topic, clear the history first so that the AI won't be affected by the previous chat context. You can also use this to manipulate the environment and drive the chat. Like if you describe something happened in your message, the AI will continue on that context.

Please note that once the prompt limit is reached, the oldest messages will be ignored and not included in the context. So the AI might forget things that are too far back in the history.

With the newer Operator-based workflow, DanceXR can also make better use of multi-turn history, session persistence, and memory compression, which helps longer roleplay sessions stay coherent even as the conversation grows.

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

Keep in mind that the prompt message has a strong influence on language models when deciding what language to use for responses. If you choose a language other than English, it's best to also update the prompt template with native text in the language you are choosing. 


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
