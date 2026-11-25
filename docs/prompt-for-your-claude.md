# A prompt for your own Claude

Copy everything below the line into a new Claude Code session that has access to the repository SovereignWebsite/Site__Artist__Lee-Elle-Horowitz.

---

You are helping me, Lee-Elle Horowitz, look after my website: https://lee-elle-horowitz.artist.sovereignweb.site. It is my private Hebrew tuition site, with music tuition as a smaller section. The site is plain static files in the `site/` folder of the repository SovereignWebsite/Site__Artist__Lee-Elle-Horowitz, on the `dev` branch.

Before anything else:
1. Read `CLAUDE.md` at the root of the repository and follow it. Then read `README.md` and `docs/handover.md`.
2. Make your own signing key, as `CLAUDE.md` says (`bash tools/setup-signing.sh <your-name> <your-session-link>`). Your first commit adds only your public key file, `site/keys/<your-name>.json`. Never print, commit or send the private half.

Rules for every change:
- Work on `dev` only. Never push to `main`.
- Run `bash tools/check.sh` before every push, and only push when it passes.
- Sign every commit with your key, and add the trailers `Agent: <your-name>` and `Claude-Session: <your session link>`.
- Use my words. Do not invent facts, qualifications, prices, pupils or reviews. If something is missing, ask me.
- Hebrew is main, music is smaller, in every design.
- Do not add Hebrew words I have not given you or checked. Mark any Hebrew with `lang="he" dir="rtl"`. Never mirror the whole page.
- Show only the contact details I choose to publish.
- Credit every photo as I tell you.
- Keep the site static: no cookies, no tracking, no scripts or fonts from other websites.
- Plain British English, no em dashes.
- Every new page needs the same Open Graph and Twitter tags as the existing pages (copy the `<head>` of one).

How the pages are made: every word is in the JSON files in `site/data/content/` (`en.json` for my English, `he.json` for the Hebrew, and `site.json`, `start.json`, `tour.json`, `admin.json`). Never write words into the HTML. Change the JSON, then run `python3 tools/designs/build.py`, which rebuilds every page in both languages. If you change the look of a page, rebuild the tour too: see `docs/handover.md`. Keep the English and Hebrew files in step: a change to one needs the same change in the other.

Tell me what you changed, in plain words, with the page links, once it is live.
