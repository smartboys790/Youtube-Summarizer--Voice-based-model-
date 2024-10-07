from flask import Flask, render_template, request
import download
import audio2text
import text2audio
import ai



app= Flask(__name__, template_folder='template')

@app.route('/')
def yt():
    return render_template('index.html')

@app.route('/youtube-summarizer', methods=["POST"])
def sum():
    # if request.method=="POST":
    url= request.form['geturl']
    print(url)   
    download.download_audio(url)
    text= audio2text.audio2text()
    summary= ai.chat1(text)
    audio =text2audio.speech(summary)

    return render_template('youtSumm.html', audio=audio, summary=summary)


if __name__ == '__main__':
    app.run(debug=True)