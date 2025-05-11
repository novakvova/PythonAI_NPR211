from gtts import gTTS
import os

text = "Привіт! Ганих канікул і хорошого настрою."

tts = gTTS(text=text, lang='uk')
tts.save("hello.mp3")

os.system("start hello.mp3")