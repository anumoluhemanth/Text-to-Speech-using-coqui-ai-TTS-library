import streamlit as st
import time
from TTS.api import TTS

st.title("Text to Voice Conversion")

option = st.selectbox(
    'Select a language model you want to convert to..',
    ('English', 'Japanese', 'French', 'Danish', 'Italian'))

if option:
    st.write('You selected:', option)

text = st.text_input('Enter text to convert to audio format!!')
st.write(text)

if st.button('Convert text to audio!'):
    if(option == 'English'):
        model = "tts_models/en/ljspeech/vits"
    elif(option == 'Japanese'):
        model = "tts_models/ja/kokoro/tacotron2-DDC"
    elif(option == 'French'):
        model = "tts_models/fr/css10/vits"
    elif(option == 'Danish'):
        model = "tts_models/da/cv/vits"
    elif(option == 'Italian'):
        model = "tts_models/it/mai_female/vits"
    # Init TTS with the target model name
    tts = TTS(model_name=model, progress_bar=False, gpu=False)
    if tts:
        with st.spinner('loading model...'):
            time.sleep(5)
        st.success('Model loaded successfully')
        # Run TTS
        tts.tts_to_file(text=text, file_path="out.wav")
        with st.spinner('converting to audio...'):
            time.sleep(5)
        st.success('Converted to audio successfully')

        audio_file = open('out.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        st.success("You can now play the audio by clicking on the play button!!")
    else:
        st.warning('Model failed to load!!')

