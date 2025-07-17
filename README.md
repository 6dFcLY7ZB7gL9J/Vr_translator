
# VR Translator Overlay App

## 🎯 Purpose
This app provides real-time translation subtitles in VR environments on Meta Quest. It is designed to work in the background and can function via PCVR (using Quest Link) or natively on Quest headsets.

## 🚀 Key Features
- Translates any spoken language into the user’s native language
- Subtitle overlay visible inside any VR app
- Works via PCVR or directly on Quest (planned)
- Background mode support (if enabled)
- Triggered by specific languages or auto-activated on foreign language detection

## 📦 Architecture
```
[Microphone Input] → [Python Backend: STT + Translation + WebSocket] → [Unity Overlay Client]
```

## 🖥️ For PCVR (Development Mode)
1. Clone this repo
2. Open Unity project in `/UnityClient`
3. Run `server.py` from `/PythonServer` (requires Whisper + WebSocket + LangDetect)
4. Launch any PCVR game through Quest Link
5. Overlay will appear as translated subtitles

## 🔐 Privacy Notes
- No voice data is stored
- Player audio is anonymized (Player 1, Player 2, etc.)
- Optional cloud hosting planned for Meta environment

## 🛠️ Future Roadmap
- Native Quest integration with headset mic access
- Secure cloud deployment with Meta Hosting (if approved)
- More language options, speaker labeling, and voice audio playback

## 🤝 Contributions
Check `/CONTRIBUTING.md` and `/docs/roadmap.md` for how to get involved.

---
This app is developed by [Rachel French](mailto:Rachelspado@gmail.com)
