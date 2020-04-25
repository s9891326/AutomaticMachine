from gtts import gTTS
from playsound import playsound
import tempfile

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh-tw')
        tts.save("{}.mp3".format(fp.name))
        playsound("{}.mp3".format(fp.name))
