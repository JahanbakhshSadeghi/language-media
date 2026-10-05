# Language Media Playlists

Curated, tested public TV and radio streams for language learning.

## Structure
- `data/channels.json` — TV streams.
- `data/radios.json` — radio streams.
- `playlists/` — VLC/IPTV M3U playlists.
- `scripts/` — generation and validation tools.
- `.github/workflows/validate.yml` — automated URL checks.

Only use publicly accessible streams that are legal to link/share. No DRM bypasses, credentials, or unauthorized streams.

## Local
```bash
python scripts/generate_playlists.py
python scripts/validate.py
```
