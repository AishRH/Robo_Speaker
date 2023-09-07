
from flask import Flask, render_template, request,Response
import pyttsx3
import tempfile
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process():
    # while True:
    text = request.form['text']
    # Create a temporary WAV file to store the speech
    engine = pyttsx3.init()
    # Convert and play the text as speech
    engine.say(text)
    engine.runAndWait()    
    return render_template('index.html')                                          

if __name__ == '__main__':
    app.run(debug=True)



# text = request.form['text']
#     tts = gTTS(text)
#     audio_buffer = BytesIO()
#     tts.write_to_fp(audio_buffer)
#     audio_buffer.seek(0)
#     return Response(audio_buffer.read(), content_type='audio/mp3') 