# Bella Vita site recovery scaffold

This repo was initialized as a starting point for rebuilding `http://www.bellavitacaregiving.com/` outside IM Creator.

## What is here

- `scripts/mirror.sh` for mirroring the public site into `site-mirror/`
- `scripts/cleanup.py` for basic post-processing of mirrored HTML
- `site-mirror/.gitkeep` placeholder directory
- `.gitignore` and `package.json`

## Why this scaffold exists

The current environment used to prepare this repo could not directly reach the public website, so the live site assets could not be fetched from here. This repo is ready for you to run the mirror from a machine or Codespace with outbound network access.

## Quick start

```bash
npm install
bash scripts/mirror.sh
python3 scripts/cleanup.py
```

That will attempt to mirror the public website into `site-mirror/`.

## Notes

- Forms, embeds, and some IM Creator widgets may need manual recreation.
- After mirroring, inspect internal links and assets before cutover.
- If the source site blocks mirroring, fallback to manual page export and rebuild.
