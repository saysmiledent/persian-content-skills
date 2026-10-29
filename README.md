# Persian Content Skills 🦷

**Skills for Claude to create Persian (RTL) content: motion reels with voice-over, Persian text lint, ElevenLabs downloads and Instagram auto-publishing.**

Built for the Persian-speaking dental education page of **Dr. Saywan Haghdoost — SaySmile** (St. Petersburg).

<p>
  <a href="https://instagram.com/saywan_h"><img alt="Instagram @saywan_h" src="https://img.shields.io/badge/Instagram-@saywan__h-E4405F?logo=instagram&logoColor=white"></a>
  <a href="https://t.me/saySmaile"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-saySmaile-26A5E4?logo=telegram&logoColor=white"></a>
  <a href="https://saysmiledent.github.io/SaySmile/"><img alt="Website SaySmile" src="https://img.shields.io/badge/Website-SaySmile-0EA5E9"></a>
</p>

---

## فارسی

این مجموعه، مهارت‌هایی برای Claude است که با آن‌ها محتوای آموزشی فارسی ساخته می‌شود: ریل‌های موشن‌گرافیک با تایپوگرافی فارسی، صداگذاری، موسیقی هماهنگ با ضرب و انتشار خودکار در اینستاگرام.

همه‌ی این ابزارها برای پیج آموزشی دندانپزشکی **دکتر سه‌یوان حق‌دوست (SaySmile)** ساخته و آزمایش شده‌اند.

- 📸 اینستاگرام: [@saywan_h](https://instagram.com/saywan_h). نکته‌های کوتاه و کاربردی درباره‌ی سلامت دهان و دندان
- 💬 تلگرام: [t.me/saySmaile](https://t.me/saySmaile). پرسش و پاسخ و نوبت‌دهی
- 🌐 سایت: [saysmiledent.github.io/SaySmile](https://saysmiledent.github.io/SaySmile/). خدمات و راه‌های تماس، به فارسی و روسی

---

## Skills

| Skill | What it does |
|---|---|
| [`persian-motion-reel`](skills/persian-motion-reel/SKILL.md) | 1080×1920 Persian kinetic-typography reels from HTML/SVG, beat-synced music and SFX, voice-over, rendered with Playwright + ffmpeg |
| [`persian-text-lint`](skills/persian-text-lint/SKILL.md) | Catches Arabic ي/ك, wrong digits, missing half-spaces and letter-spacing in Persian copy |
| [`elevenlabs-github-relay`](skills/elevenlabs-github-relay/SKILL.md) | Downloads ElevenLabs audio through a GitHub Actions relay when the sandbox can't reach Google Storage |
| [`metricool-auto-publish`](skills/metricool-auto-publish/SKILL.md) | Hosts media on a public branch and schedules Reel + Story in Metricool at the best time |

## Install

Copy a skill folder (for example `skills/persian-motion-reel`) into your Claude skills directory, or upload it as a custom skill in Claude. Each `SKILL.md` explains when and how to use it.

## License

MIT. Use freely, and a mention of [@saywan_h](https://instagram.com/saywan_h) is appreciated. 🙏
