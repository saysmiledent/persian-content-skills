---
name: metricool-auto-publish
description: Schedule an approved Instagram Reel plus a follow-up Story in Metricool automatically, hosting the media on a public GitHub branch so Metricool can fetch it.
---

# Metricool auto-publish (Reel + Story)

Only run after the account owner approved the final video, caption and day.

1. **Host the media publicly.** Commit `reels/YYYY-MM-DD-topic.mp4`, `reels/YYYY-MM-DD-topic-cover.jpg` and `stories/YYYY-MM-DD-topic-story.png` to a public branch (e.g. `media`). Public URL: `https://raw.githubusercontent.com/<owner>/<repo>/media/<path>`.
2. **Best time.** `getBestTimeToPostByNetwork` for `instagram` with the brand's timezone; pick the highest hour of the target day.
3. **Reel.** `createScheduledPost` with `autoPublish: true`, `media: [mp4 url]`, `videoThumbnailUrl: cover url`, `instagramData: {type: "REEL", showReelOnFeed: true, isAiGenerated: <owner's choice>}`, `text: caption + hashtags`.
4. **Story** ~15 minutes later: `media: [story image url]`, no text, `instagramData: {type: "STORY"}`.
5. **Verify.** In the response, media URLs should now point to `static.metricool.com` (Metricool fetched them). Report both times and the planner links.

## Caption pattern (Persian educational page)
Hook line → myth/fact pairs with ❌/✅ → one "golden rule" line → a question for comments → a share prompt → a short disclaimer ("educational, not a substitute for an in-person exam") → 10–15 hashtags in Persian plus the brand tag.

Stickers (poll, "add reel to story") cannot be set through Metricool; add them in the Instagram app if needed.
