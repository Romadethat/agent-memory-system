# Voice Cloning for Supertonic 3 — Research

## The Problem

Supertonic 3 has 10 preset voices (M1-5, F1-5) but no built-in audio-to-embedding pipeline for creating custom voices. The official Voice Builder (supertone.ai/voice-builder) is a paid web service that creates style JSONs from reference audio. We need a DIY approach.

## Voice Format Recap

Custom voice styles are JSON files with:
- `style_ttl`: (1, 50, 256) — timbre/texture embedding. 50 time-frames of 256-dim speaker characteristics.
- `style_dp`: (1, 8, 16) — prosody/duration embedding. 8 frames of 16-dim speaking rhythm.

## Approach A: Existing Speaker Encoder + Projection

Extract speaker embeddings using an open-source model, then project them into Supertonic's embedding space.

**Speaker encoder options:**

| Model | Output Dim | Size | Notes |
|-------|-----------|------|-------|
| ECAPA-TDNN (speechbrain) | 192 | ~20 MB | Well-established, good quality |
| Resemblyzer (voice encoder) | 256 | ~85 MB | Direct 256-dim output — perfect shape match |
| Wespeaker (ECAPA) | 192/256 | ~20 MB | Trained on VoxCeleb, state-of-the-art |

**Projection approach:**
1. Extract mean speaker embedding from reference audio (multi-segment for robustness)
2. Tile embedding across 50 time frames → (1, 50, 256) or (1, 50, 192)
3. If 192-dim, train a linear projection layer: 192 → 256 using the 10 built-in voices as training data
4. Use a fixed/filler `style_dp` — borrow from M2 or average built-in voices

**Quality caveat:** The `style_ttl` isn't just a tiled speaker embedding — it's a 50-frame sequence that encodes temporal prosody characteristics. A simple tiling produces flat-prosody voice. Still useful for short utterances, less natural for longer passages.

## Approach B: Voice Conversion via vector_estimator

The 256MB `vector_estimator.onnx` is a diffusion model that takes noisy_latent + text_emb + style_ttl → clean latent. Inverting this to extract style_ttl from audio requires the original training code — not practical without Supertone's internal tools.

## Approach C: Official Voice Builder (Recommended for Quality)

https://supertonic.supertone.ai/voice-builder — upload reference audio (30s-2min clean speech), generates custom style JSON, download and import with `zoro voice import`. Paid service.

## Quick Test — How We'd Attempt DIY

```python
# Extract ECAPA-TDNN embedding, tile to (50, 256), 
# build style JSON, load via get_voice_style_from_path()
# Borrow M2's dp embedding as filler
```

## Current Status

- M2 selected as Zoro's default voice ✓
- Local TTS server operational ✓
- Custom style import ready ✓
- Voice cloning: research phase (see Approach A for most viable DIY path)
