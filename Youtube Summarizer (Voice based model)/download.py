from os import path
import subprocess
import yt_dlp
import AudioConverter
from pydub import AudioSegment

def download_audio(url):

    command = f"yt-dlp -f bestaudio --extract-audio --audio-format mp3 {url} -o Downloded_audio/transcribe "
    subprocess.call(command, shell=True)

# assign files 
    input_file = "Downloded_audio/transcribe.mp3"
    output_file = "./audio/transc.wav"

    # convert mp3 file to wav file 
    sound = AudioSegment.from_mp3(input_file) 
    sound.export(output_file, format="wav") 

# url = input("Enter the URL of the YouTube video: ")
# output_path = './Downloded_audio'
# output_path = os.path.join(output_path, '2.mp3')

# download_audio(url, output_path)

# print("Audio downloaded successfully!")