import speech_recognition as sr

def transcribe_audio(audio_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as audio_file:
        # Read the audio data
        audio_data = recognizer.record(audio_file)

    # Perform the transcription using the Google Speech Recognition engine
    try:
        transcription = recognizer.recognize_google(audio_data, language="en-US")
        return transcription
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Provide the path to your MP3 audio file
audio_file_path = "./audio.wav"

# Transcribe the audio file
transcription = transcribe_audio(audio_file_path)
print("Transcription:")
print(transcription)
