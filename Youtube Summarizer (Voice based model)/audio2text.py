import speech_recognition as sr
import json
import ai 


def audio2text(audio='./Downloaded_audio/demo.wav'):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        print('Recogonizing file..')
        r.pause_threshold=0.3
        audio_data = r.record(source)

    try:
        print('Converting to text...')
        data = r.recognize_google(audio_data)

    except Exception as e:
        print('Error occured :- ',e)
        return ' '
    return data
# mp3_file="Downloded_audio/1.m4a"
# wav_file= "Downloded_audio/1.wav"
# mp3ToWav(mp3_file, wav_file)
# audio2text()


# data= dict(data)
# decoder= json.JSONDecoder()
# result2= decoder.decode(data)
# transcribed_data = [alternative['transcript'] for alternative in result2['alternative']]
# print(transcribed_data[:-1])

# for transcript in transcribed_data:
    # return transcript

