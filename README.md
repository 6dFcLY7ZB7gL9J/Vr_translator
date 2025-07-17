# VR Translator Demo

## Overview
A prototype showing real-time subtitle translation overlay in VR.

## Structure
- **unity/**: Unity 2022/2023 project with OpenXR setup and subtitle overlay
- **python_server/**: Whisper-based STT server with language detection and WebSocket output

## Getting Started

### 1. Unity (Subtitle App)
- Open Unity Hub → Add project's `unity/` folder
- Ensure XR Plugin Management + OpenXR installed
- Add scene “MainScene.unity”

### 2. Python Server
```
cd python_server
pip install whisper sounddevice flask websockets langdetect
python transcriber_server.py
```

### 3. Running the Demo
- Run `transcriber_server.py`
- In Unity, press Play — launch PCVR app via Quest Link
- Speak in a non-native language and watch subtitles appear in VR

## How to Use
- Modify `language_preference` in `transcriber_server.py`
- Adjust UI or WebSocket endpoint in Unity script
