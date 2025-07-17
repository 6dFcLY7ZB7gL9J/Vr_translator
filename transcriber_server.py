import sounddevice as sd
import numpy as np
import whisper
import asyncio
import websockets
from langdetect import detect
import queue

model = whisper.load_model("base")
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(indata.copy())

async def recognize_and_send(websocket):
    buffer = np.empty((0, 1), dtype=np.float32)
    with sd.InputStream(callback=callback, channels=1, samplerate=16000):
        while True:
            while not q.empty():
                chunk = q.get()
                buffer = np.append(buffer, chunk)
                if len(buffer) >= 16000 * 5:
                    audio = buffer[:16000 * 5]
                    buffer = buffer[16000 * 5:]
                    audio = whisper.pad_or_trim(audio.flatten())
                    mel = whisper.log_mel_spectrogram(audio).to(model.device)
                    options = whisper.DecodingOptions(fp16=False)
                    result = whisper.decode(model, mel, options)
                    lang = detect(result.text)
                    await websocket.send(f"[{lang}] {result.text}")

async def server():
    async with websockets.serve(recognize_and_send, "localhost", 6789):
        await asyncio.Future()  # run forever

asyncio.run(server())
