import whisper

model = whisper.load_model("base")
result = model.transcribe("badAudio")
print(result["text"])