
import asyncio
import websockets
import whisper
from langdetect import detect

model = whisper.load_model("base")
connected_clients = set()

async def transcribe_and_send():
    import pyaudio
    import numpy as np

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    print("Listening...")

    while True:
        data = np.frombuffer(stream.read(4096), dtype=np.int16)
        audio = whisper.pad_or_trim(data.astype(np.float32) / 32768.0)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(fp16=False)
        result = whisper.decode(model, mel, options)
        text = result.text.strip()

        if text:
            lang = detect(text)
            message = f"[{lang.upper()}] {text}"
            print("Sending:", message)
            await asyncio.gather(*[client.send(message) for client in connected_clients])

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(handler, "localhost", 8765)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.create_task(transcribe_and_send())
loop.run_forever()
