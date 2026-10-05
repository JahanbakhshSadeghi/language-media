# Language Media Playlists

Curated, tested public TV and radio streams for language learning.

## Structure
- `data/channels.json` — TV streams.
- `data/radios.json` — radio streams.
- `playlists/` — VLC/IPTV M3U playlists.
- `scripts/` — generation and validation tools.
- `.github/workflows/validate.yml` — automated URL checks every 6 hours.

## Stream policy
Only link publicly accessible streams that are legal to link/share. No DRM bypasses, credentials, or unauthorized streams. Availability can vary by country and over time.

Each channel keeps a source page so the stream can be reviewed. A URL appearing in this repository is not a guarantee of uninterrupted availability.

## Local
```bash
python scripts/generate_playlists.py
python scripts/validate.py
```
