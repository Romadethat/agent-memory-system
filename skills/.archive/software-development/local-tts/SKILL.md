---
name: local-tts
description: Local on-device Text-to-Speech using ONNX models — Supertonic 3 integration, voice style format, custom voice cloning, and local API server.
category: software-development
version: 1.0.0
tags: [tts, voice, supertonic, onnx, speech-synthesis, local]
---

# Local TTS — Supertonic 3

On-device TTS that runs entirely locally via ONNX Runtime. No cloud calls. 37K+ downloads, 578 HF stars.

## Architecture

```
                        ┌──────────────────┐
Text ──► text_encoder   │  text_emb (256)  │
         (36 MB ONNX)   └────────┬─────────┘
                                 │
┌──────────┐     ┌───────────────▼──────────────┐
│ style_ttl ├────►│  vector_estimator (256 MB)   │
│ (50×256)  │     │  Diffusion denoiser, 5 steps │
└──────────┘     └───────────────┬──────────────┘
                                 │
┌──────────┐     ┌───────────────▼──────────────┐
│ style_dp  ├────►│  duration_predictor (3.7 MB)│
│ (8×16)    │     └───────────────┬──────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │  vocoder (101 MB ONNX)   │
                    │  latent → waveform       │
                    └──────────────────────────┘
```

### ONNX Models

| Model | Size | Inputs → Outputs |
|-------|------|------------------|
| `text_encoder.onnx` | 36 MB | text_ids, style_ttl, text_mask → text_emb (256-dim) |
| `duration_predictor.onnx` | 3.7 MB | text_ids, style_dp, text_mask → phoneme durations |
| `vector_estimator.onnx` | 256 MB | noisy_latent + text_emb + style_ttl → clean latent (5 diffusion steps) |
| `vocoder.onnx` | 101 MB | latent → waveform audio |

### Voice Style Format

Every voice is defined by two floating-point tensors stored in a JSON file:

```json
{
  "style_ttl": {
    "dims": [1, 50, 256],
    "data": [/* 12,800 floats */]
  },
  "style_dp": {
    "dims": [1, 8, 16],
    "data": [/* 128 floats */]
  }
}
```

- `style_ttl` (1, 50, 256) — voice timbre/texture embedding. 50 time frames × 256-dim speaker characteristics.
- `style_dp` (1, 8, 16) — prosody/duration embedding. 8 frames × 16-dim speaking rhythm characteristics.

File size: ~285 KB per voice style JSON.

### Built-in Preset Voices

| Name | Gender | Notes |
|------|--------|-------|
| M1-M5 | Male | M2 is recommended default for Zoro |
| F1-F5 | Female | Five female presets |

## Setup

### Installation
```bash
pip install supertonic
```

First run auto-downloads model to `~/.cache/supertonic3/` (~400 MB total).

### PYTHONPATH Isolation
Supertonic requires clean numpy for Python 3.14. The Hermes venv has numpy for Python 3.12 which breaks imports. Always set PYTHONPATH:

```bash
export SUPERTONIC_PYTHONPATH="C:\Users\User\AppData\Roaming\Python\Python314\site-packages;C:\Python314\Lib\site-packages"
PYTHONPATH=$SUPERTONIC_PYTHONPATH C:/Python314/python -c "from supertonic import TTS; ..."
```

Or use the `zoro voice` CLI which handles this automatically.

## CLI Usage

### List voices
```bash
zoro voice list
```

### Synthesize speech (default voice: M2)
```bash
zoro voice say "Text to speak"
zoro voice say "Text" --play      # Also play through speakers
zoro voice say "Text" -v M1       # Use different voice
```

### Model info
```bash
zoro voice info
```

### Import custom voice style
```bash
zoro voice import my-voice path/to/style.json
```

### Start local API server (OpenAI-compatible)
```bash
zoro voice server
# → http://127.0.0.1:8765
# → Docs: /docs
# → OpenAI API: POST /v1/audio/speech
# → List styles: GET /v1/styles
# → Import styles: POST /v1/styles/import
```

## Custom Voices

### Import Path
Custom voice styles are stored at:
```
~/.cache/supertonic3/custom_styles/<name>.json
```

Load with `tts.get_voice_style_from_path(path)` or via the server's `POST /v1/styles/import`.

### Voice Builder (Official)
The official Voice Builder at https://supertonic.supertone.ai/voice-builder creates style JSONs from reference audio. Paid service. Output is a JSON file you import via `zoro voice import` or the server endpoint.

### DIY Voice Cloning (Research)
To build custom voices without the Voice Builder, you need a speaker encoder that maps audio → 256-dim embeddings (50 time frames). Potential approaches:

1. **ECAPA-TDNN** — open-source speaker verification model, outputs 192-dim embeddings. Could project to 256-dim.
2. **Qwen3-TTS Speaker Encoder** — HuggingFace model specifically for TTS speaker embedding.
3. **Custom training** — Train a small projection layer that maps existing speaker embeddings → Supertonic's style_ttl space using the 10 built-in voices as training data.

See `references/voice-cloning-approach.md` for detailed research.

## Server API

The Supertonic server (`zoro voice server`) exposes:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/audio/speech` | POST | OpenAI-compatible TTS (text, voice, response_format) |
| `/v1/tts` | POST | Native TTS (text, voice, lang, speed) |
| `/v1/styles` | GET | List built-in + custom voices |
| `/v1/styles/import` | POST | Import custom voice style JSON |
| `/health` | GET | Health check |
| `/docs` | GET | Swagger documentation |
| `/v1/models` | GET | Available models |

## Pitfalls

- **Numpy version conflict**: Hermes venv has numpy compiled for Python 3.12. Running supertonic under Python 3.14 requires PYTHONPATH isolation. Always use `PYTHONPATH=...` or the `zoro voice` wrapper.
- **First load takes 30-60s**: Downloads 26 files (~400 MB) from HuggingFace Hub. Subsequent loads are instant (~2s).
- **Voice names are case-sensitive**: M2, not m2.
- **Custom style names can't conflict with built-ins**: Names like "M2" or "F1" are rejected on import.
- **Server has 1MB style import limit**: Uploaded style JSONs must be under 1MB. Built-in styles are ~285KB.
- **WAV output only**: Supertonic natively outputs WAV. The server can convert to MP3/FLAC via response_format parameter.
- **Python on Windows**: `python3` redirects to Microsoft Store. Use full path: `C:/Python314/python.exe`.
