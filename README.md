
# Whisper Transkriberingsverktøy

Et enkelt Python-skript som bruker OpenAI Whisper-modellen til å transkribere lydfiler (.m4a, .wav, .mp3) til tekst.

## 📦 Funksjoner
- Laster inn Whisper-modellen (small/medium)
- Transkriberer lydfil til tekst
- Lagrer transkripsjon til `transkripsjon.txt`
- Terminalbasert statusvisning

## 🛠️ Kom i gang

### 1. Installer avhengigheter

```bash
pip install git+https://github.com/openai/whisper.git
pip install torch
```

> ❗ Du må også ha [ffmpeg](https://ffmpeg.org/download.html) installert og lagt til i systemets PATH.

### 2. Kjør scriptet

```bash
python transkriber.py
```

## 📝 Eksempel på output
Se `transkripsjon.txt` etter at scriptet er kjørt.

## 🔒 Lisens
Se [LICENSE](LICENSE) for mer info.

## 💡 Om prosjektet
Dette prosjektet er laget av Elisabet Witsø for utforsking av AI-verktøy.
