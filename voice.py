import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
import torchaudio
import os

# Check if CUDA is available
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Model and tokenizer initialization
model_id = "openai/whisper-large-v3"
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

# Pipeline initialization
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

# Load audio file from local directory
audio_file_path = "./goodAudio.wav"  # Update with your local file path

# Check if the file exists
if not os.path.exists(audio_file_path):
    print(f"File '{audio_file_path}' not found.")
    exit()

# Load the audio using torchaudio
waveform, sample_rate = torchaudio.load(audio_file_path)

# Convert stereo audio to mono if needed
if waveform.shape[0] > 1:
    waveform = waveform.mean(dim=0, keepdim=True)

# Convert audio to the required format
input_dict = processor(
    waveform.numpy(),  # Convert tensor to numpy array
    sampling_rate=sample_rate,
    return_tensors="pt"  # Return PyTorch tensors
)

# Perform automatic speech recognition
result = pipe(input_dict["input_values"].to(device))

# Print the transcription
print(result["text"])
