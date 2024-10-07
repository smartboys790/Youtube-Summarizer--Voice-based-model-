from gtts import gTTS
import audio2text

#Test to speech
def speech(text):
    tts= gTTS(text, lang='en')
    file= tts.save('Converted_Audio/summary.mp3')
    return file
