# Supertonic Voice Style JSON Format

Detailed reference for the voice style format used by Supertonic 3 TTS.

## JSON Structure

```json
{
  "style_ttl": {
    "dims": [1, 50, 256],
    "data": [/* float array, length = 12,800 */]
  },
  "style_dp": {
    "dims": [1, 8, 16],
    "data": [/* float array, length = 128 */]
  }
}
```

### Validation Rules

From `supertonic.utils.validate_voice_style_format()`:
- Must have top-level keys `style_ttl` and `style_dp`
- Each must have `dims` (list) and `data` (list) keys
- No other fields are validated (extra fields are ignored)

### style_ttl (Text-to-Latent)

- **Dims:** [batch=1, time_frames=50, features=256]
- **Layout:** 50 time frames, each with 256 speaker/timbre features
- **Data length:** 1 × 50 × 256 = 12,800 floats
- **Float range:** typically -0.7 to 0.8 (from M2 inspection: min=-0.74, max=0.81, mean≈0.0015)
- **Role:** Conditions the text_encoder and vector_estimator to produce speech with the target voice's timbre and texture
- **Storage:** ~51 KB per style (12,800 floats × 4 bytes = 51.2 KB data, plus JSON overhead ~290 KB total)

### style_dp (Duration Predictor)

- **Dims:** [batch=1, time_frames=8, features=16]
- **Data length:** 1 × 8 × 16 = 128 floats
- **Float range:** typically -0.7 to 0.6 (from M2 inspection: min=-0.71, max=0.63, mean≈0.011)
- **Role:** Conditions the duration predictor for speaking rhythm/prosody
- **Storage:** ~512 bytes data, ~1 KB total in JSON

## Loading

```python
from supertonic import TTS

tts = TTS(auto_download=True)

# Load built-in voice by name
style = tts.get_voice_style(voice_name="M2")

# Load custom voice from JSON file
style = tts.get_voice_style_from_path("path/to/custom.json")

# Load built-in voice as Style object
print(type(style))        # <class 'supertonic.core.Style'>
print(style.ttl.shape)    # (1, 50, 256)
print(style.dp.shape)     # (1, 8, 16)
```

## Saving Custom Styles

```python
import json
import numpy as np

style_dict = {
    "style_ttl": {
        "dims": [1, 50, 256],
        "data": my_ttl_embedding.tolist()  # 12,800 floats
    },
    "style_dp": {
        "dims": [1, 8, 16],
        "data": my_dp_embedding.tolist()    # 128 floats
    }
}

with open("my_voice.json", "w") as f:
    json.dump(style_dict, f)
```

## Storage Locations

| Type | Path |
|------|------|
| Built-in presets | `~/.cache/supertonic3/voice_styles/M2.json` (and 9 others) |
| Custom styles | `~/.cache/supertonic3/custom_styles/<name>.json` |
| Config override | `SUPERTONIC_CUSTOM_STYLES_DIR` env var |
| All styles | `~/.cache/supertonic3/` |

## Preset Voice Files

From model inspection:
- 10 preset JSON files, each ~285-292 KB
- M1-M5 (male), F1-F5 (female)
- Filenames map directly to voice names (e.g., `M2.json` → voice_name="M2")

## Format Compatibility

- **Supertonic 3** uses this format (tts.json version "v1.7.3")
- **Supertonic 2** likely uses same format with different dims
- **Supertonic v1** (original) probably uses different format entirely
