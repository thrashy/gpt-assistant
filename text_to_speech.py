from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


class TextToSpeech:
    def __init__(self, lang: str = 'en', filename: str = 'text_to_speech.mp3'):
        self.lang = lang
        self.filename = filename

    def convert(self, text: str):
        speech = gTTS(text=text, lang=self.lang, slow=False)
        speech.save(self.filename)

    def play_audio(self):
        audio = AudioSegment.from_file(self.filename)
        play(audio)
