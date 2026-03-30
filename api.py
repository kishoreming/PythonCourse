'''
from gtts import gTTS
text="hello nan than king pesuran "
tts=gTTS(text=text,lang='en')
tts.save("test.mp3")
print("audiofile created suceesfully")
'''
import whisper
model=whisper.load_model("base")
result=model.transcribe("test.mp3")
print(result["text"])