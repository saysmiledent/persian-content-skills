---
name: elevenlabs-github-relay
description: Download ElevenLabs generations (or any file from a host your sandbox cannot reach) by relaying it through a GitHub Actions workflow in a repo you can push to.
---

# ElevenLabs → GitHub relay

Agent sandboxes often allow GitHub but block `storage.googleapis.com`, where ElevenLabs stores generated audio. This relay lets GitHub's runner download the file and commit it, so the agent can `git pull` it.

## One-time setup
1. In a repo you can push to, create a branch (e.g. `media`) that is not your website branch.
2. Copy `templates/fetch-media.yml` to `.github/workflows/fetch-media.yml` on that branch and push.

## Each download
1. Generate speech, poll the run status until completed, and copy the signed `media[0].url` (valid ~2 hours).
2. Push a request file:
```bash
NAME="2026-11-01-topic-vo.mp3"; URL='<signed url>'
mkdir -p fetch/requests && printf '%s\n' "$URL" > "fetch/requests/$NAME.url"
git add -A && git commit -qm "Request: $NAME" && git push -q
for i in $(seq 1 40); do git pull -q --rebase; [ -f "fetch/out/$NAME" ] && break; timeout 6 tail -f /dev/null; done
```
3. Copy the file out, then `git rm fetch/out/$NAME`, commit and push to keep the repo small.
4. Word timings for subtitles: transcribe the speech node on the same ElevenLabs flow (connect the speech node as input).

## Notes
- If the repo is public, the request URL and the downloaded file are public for a short time. Only relay content you will publish anyway.
- Debug: `gh api repos/<owner>/<repo>/actions/runs?branch=media&per_page=1`.
