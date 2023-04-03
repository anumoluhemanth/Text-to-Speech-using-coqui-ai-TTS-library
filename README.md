# Text-to-Speech-using-coqui-ai-TTS-library
Text to speech converter streamlit application using Coqui ai: TTS library </br>
</br>
Coqui-ai TTS library https://github.com/coqui-ai/TTS</br>
A deep learning toolkit for Text-to-speech conversion.</br>
</br>
Requirements: (Windows)</br>
Python version--3.8</br>
pip</br>
espeak-ng</br>
</br>
Steps to run the library: (Windows)</br>
Step 1: create a python virtual env </br>
python -m venv .</br>
</br>
Step 2: Activate the venv</br> 
</br>
cd Scripts </br>
 ./activate</br>
</br>
Step 3: update the wheel 
pip list</br> 
pip install pip setuptools wheel -U</br>
</br>
Step-4: Install TTS library</br>
pip install TTS==0.8.0</br>
Step-5: Install pyworld</br>
pip install pyworld==0.3.0</br>
Step-6: check TTS installation </br>
tts-server --list_models</br>
</br>
play with the library:</br>
converts the text to audio using the default model</br>
tts --text "Hello world"</br>
</br>
creates a local web interface to interact and convert the text to audio</br>
tts-server --model_name tts_models/en/ljspeech/tacotron2-DDC</br>
