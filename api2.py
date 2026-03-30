import whisper
model=whisper.load_model("base")
result=model.transcribe("zr"C:\Users\kisho\PycharmProjects\PythonProject\test.mp3")
print(result["text"])