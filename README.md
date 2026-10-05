# Language Media Playlists

Curated public TV and radio streams for language learning.

## VLC

Use the generated all-in-one playlist:

`playlists/all-tv.m3u`

VLC can open the playlist from a URL. The `group-title` field is used for language/topic grouping where supported by the player.

Language-specific playlists are also available:
- `playlists/english.m3u`
- `playlists/german.m3u`
- `playlists/turkish.m3u`

## Add a stream

1. Open `data/channels.json`.
2. Add one object to `channels`.
3. Required fields: `id`, `name`, `language`, `group`, `country`, `url`, `source_page`.
4. Put the direct public HLS URL in `url`.
5. Use the official channel/source page for `source_page`.
6. Run:
   `python scripts/generate_playlists.py`
7. Commit both the data change and regenerated playlist files.
8. Test the direct URL in VLC before considering the stream verified.

Example:
```json
{
  "id": "example-en",
  "name": "Example English",
  "language": "English",
  "group": "News",
  "country": "Example",
  "url": "https://example.com/live/master.m3u8",
  "source_page": "https://example.com/live"
}
```

## Stream policy

Only link publicly accessible streams that are legal to link/share. No DRM bypasses, credentials, or unauthorized streams. Availability can vary by country and over time.

A URL appearing in this repository is not a guarantee of uninterrupted availability.

## Validation

Validation is manual-only and checks whether the stream URL responds over HTTP. It does not enforce resolution.

`python scripts/validate.py`
