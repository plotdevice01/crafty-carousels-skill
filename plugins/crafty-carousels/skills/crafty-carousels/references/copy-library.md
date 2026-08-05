# Offline scripts and CTA library

This installed skill contains the complete purchased Personal Brand Launch copy library needed at runtime:

- 7 exact-source script frameworks;
- 100 exact-source hook starters in `assets/hook-library/personal-brand-hooks-100.json`;
- 39 exact-source calls to action: 13 engagement, 13 follow, and 13 sales.

The wording, punctuation, spelling, and placeholders are preserved from the owner-provided source. The skill never opens the original Notion workspace and stores no Notion URL.

Query scripts or CTAs locally:

```powershell
python scripts/copy_library.py --type script --search "myth" --count 3
python scripts/copy_library.py --type cta --category engagement --count 5
python scripts/copy_library.py --type cta --category sales --search "DM" --json
```

The frameworks are structures, not permission to invent client facts. Use approved evidence and voice. In `exact-source` mode, the supplied post copy still overrides every library suggestion.
