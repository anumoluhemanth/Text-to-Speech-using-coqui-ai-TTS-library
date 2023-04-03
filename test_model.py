from TTS.api import TTS
from playsound import playsound

print("Testing text to voice model..")

language = input("enter the language model you want to work with, you can choose from: \n1. English,\n 2.Japanese,\n 3.French,\n 4.Danish,\n 5.Italian\n enter an option number for ex: 1 or 2\n")

text = input("enter the text to convert.\n")

print('loadig model please be patient...')

if(language == 'English' or language == '1'):
    model = "tts_models/en/ljspeech/vits"
elif(language == 'Japanese' or language == '2'):
    model = "tts_models/ja/kokoro/tacotron2-DDC"
elif(language == 'French' or language == '3'):
    model = "tts_models/fr/css10/vits"
elif(language == 'Danish' or language == '4'):
    model = "tts_models/da/cv/vits"
elif(language == 'Italian' or language == '5'):
    model = "tts_models/it/mai_female/vits"

# Init TTS with the target model name
tts = TTS(model_name=model, progress_bar=False, gpu=False)
print('model loaded successfully!!')
print('converting text to audio...')
# Run TTS
tts.tts_to_file(text=text, file_path="out.wav")

playsound('./out.wav')
