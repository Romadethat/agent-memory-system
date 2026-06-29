---
name: zoro-voice
description: Zoro's voice system — Supertonic 3 local TTS integration. Synthesis CLI, audio analysis bridge, custom voice import, and the Voice Workbench web lab.
category: software-development
version: 1.0.0
tags: [tts, voice, supertonic, audio, songsee, zoro]
---

# Zoro Voice — Supertonic 3 TTS Integration

Zoro's local voice system. Runs entirely on-device via ONNX Runtime — no cloud calls.

## Quick Start

```bash
# List available voices
zoro voice list

# Speak a line (default: M2 voice)
zoro voice say "Hard things take time. The forge doesn't rush."

# Speak with a different voice
zoro voice say "This is M1" --voice M1

# Play through speakers (requires sounddevice)
zoro voice say "Play me" --play

# Show model info
zoro voice info

# Start the Voice Workbench web lab
zoro voice workbench
```

## Defaults

- **Voice:** M2 (set via $ZORO_VOICE env var)
- **Output:** `D:\videos\zoro-voice-<text>-<timestamp>.wav`
- **Speed:** 1.05 (natural)
- **Languages:** 31 (EN, KO, JA, AR, BG, CS, DA, DE, EL, ES, ET, FI, FR, HI, HR, HU, ID, IT, LT, LV, NL, PL, PT, RO, RU, SK, SL, SV, TR, UK, VI)

## Available Preset Voices

| Name | Type |
|------|------|
| M1, M2, M3, M4, M5 | Male |
| F1, F2, F3, F4, F5 | Female |

M2 is the default Zoro voice — chosen for its tone, pacing, and natural delivery.

## PYTHONPATH Isolation

Supertonic is installed to the system Python 3.14's user site-packages, NOT the Hermes venv. The venv has a numpy compiled for Python 3.12 which conflicts. All Supertonic calls must set PYTHONPATH to isolate from the Hermes venv:

```python
env = os.environ.copy()
env["PYTHONPATH"] = r"C:\Users\User\AppData\Roaming\Python\Python314\site-packages;C:\Python314\Lib\site-packages"
```

This is baked into the `zoro voice` CLI and workbench server. Direct Python calls need the same treatment.

## Voice Style Format

Custom voice styles are JSON files with this structure:

```json
{
  "style_ttl": {"dims": [1, 50, 256], "data": [...]},
  "style_dp": {"dims": [1, 8, 16], "data": [...]}
}
```

- `style_ttl`: (1, 50, 256) — voice timbre embedding
- `style_dp`: (1, 8, 16) — prosody/duration embedding

Validate with `supertonic.utils.validate_voice_style_format()`.

## Importing Custom Voices

```bash
# Import a voice style JSON
zoro voice import MY_VOICE /path/to/style.json

# Or upload via the Workbench API:
# POST /api/import  (JSON body with name, style_ttl, style_dp)
```

Custom styles go to `~/.cache/supertonic3/custom_styles/<name>.json`.
Available via `get_voice_style_from_path()` or the workbench server.

## Voice Workbench

The Voice Workbench (`zoro voice workbench`) is a local web lab at port 8766 that combines three tools:

- **Synthesis** — Type text → hear M2 (or any voice)
- **Analysis** — Feed audio → get spectrogram/chroma/mel/MFCC (via songsee)
- **Patterns** — Pattern journal entries, clickable → speaks them aloud

Forge aesthetic frontend (emerald/amber, dark theme, JetBrains Mono).
Auto-refreshes health and pattern list.

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /api/speak | Synthesize text to audio |
| POST | /api/analyze | Analyze audio (spectrogram, chroma, MFCC) |
| GET | /api/patterns | List pattern journal entries |
| GET | /api/voices | List available voices |
| GET | /api/audio?file= | Serve audio file for playback |
| GET | /api/health | Server health + pattern count |

### Speak Request

```json
{
  "text": "What to say",
  "voice": "M2",
  "speed": 1.05
}
```

### Analyze Request

```json
{
  "file_path": "D:/videos/sample.wav",
  "mode": "all"  // or: spectrogram, chroma, mel, mfcc
}
```

## Voice Cloning

The long-term path for custom Zoro voice:

1. **Voice Builder** (supertone.ai/voice-builder) — paid web service, upload reference audio → download voice style JSON
2. **Qwen3 TTS Speaker Encoder** — open-source GGUF model on HF that extracts 256-dim speaker embeddings (same dim as Supertonic's style_ttl). Linear projection may work.
3. **Build custom encoder** — requires training a model that maps audio → (50, 256) embedding using the vector_estimator architecture

## Files

| Component | Path |
|-----------|------|
| Main CLI | `~/AppData/Local/hermes/scripts/zoro-voice.py` |
| Workbench server | `~/AppData/Local/hermes/scripts/voice-workbench.py` |
| Workbench frontend | `~/AppData/Local/hermes/scripts/voice-workbench/index.html` |
| Model cache | `~/.cache/supertonic3/` |
| Custom styles | `~/.cache/supertonic3/custom_styles/` |
| Model ONNX files | `~/.cache/supertonic3/onnx/` |
| Output dir | `D:\videos\` |

## Pitfalls

- Python 3.14 vs Hermes venv numpy conflict — ALWAYS set PYTHONPATH when running Supertonic from Hermes context
- M1-M5 and F1-F5 are the only built-in presets — no gender-neutral or custom names available without import
- `get_voice_style(voice_name='M2')` is correct — not `list_voice_styles()`
- Duration from synthesize() is a numpy array, access via `float(dur.item())`
- Server needs uvicorn + fastapi installed (on system Python 3.14, not Hermes venv)
- Songsee must be at `C:\Users\User\go\bin\songsee.exe` for analysis features
