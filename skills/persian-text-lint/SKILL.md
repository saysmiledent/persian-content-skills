---
name: persian-text-lint
description: Lint Persian copy inside HTML before rendering or publishing — catches Arabic ي/ك, Arabic-Indic digits, Latin digits or "?" inside Persian text, missing ZWNJ after می/نمی, and letter-spacing.
---

# Persian text lint

Run before every render of Persian on-screen text and before publishing a page:

```bash
python3 scripts/lint.py film.html   # prints LINT OK or one line per problem
```

Fix every problem, then run again. Checks:
- Arabic YEH `ي` (U+064A) and KAF `ك` (U+0643) → use Persian `ی` / `ک`.
- Arabic-Indic digits (U+0660…) and Latin digits inside Persian text → use ۰–۹ (wrap mixed numbers in `<bdi>`).
- Latin `?` inside Persian text → use `؟`.
- `می ` / `نمی ` followed by a space → use a half-space (ZWNJ, `&zwnj;`).
- Any `letter-spacing` (it breaks Persian joining).
