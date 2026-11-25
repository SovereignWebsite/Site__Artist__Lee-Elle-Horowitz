# Now (2026-11-25T15:17Z)

## Done
- 2026-11-25T17:30Z: HTTPS works; the site is live at https://lee-elle-horowitz.artist.sovereignweb.site (v0.1.10, 53d29c9). Told sites.b. hub.b holds it out of its directory until she approves (e9e9950); on approval, send hub.b one line and it lists the site under People.
- Area, own key (fbe1f08), design.b's brief (https://design.agents.sovereignweb.site/briefs/lee-elle-horowitz.html, 7222e25).
- Five designs rebuilt for impact at Dinis's ask ("really make this site have the WOW factor"), all from her words: Alef-bet (home: arch portrait, moving alphabet band, giant section letters, quote band), Conversation (chat thread, Hebrew twin bubbles left empty), Three tenses (was / is / will be, journey timeline), The stage (velvet curtains, lit marquee, spotlight, programme, ticket), Notebook (exercise book, polaroid, sticky note; printable). Picker at /designs/.
- /start/ rewritten for Lee-Elle: choose a design, check words and Hebrew, send photos and changes, approve, who looks after it; GitHub steps kept under "Later".
- docs/handover.md and docs/prompt-for-your-claude.md (90c20f3).
- Share card made from her photo and words (site/assets/share/card-1200x630.jpg).
- Generator kept at tools/designs/build.py (designs, picker, start page). Stop using it once she edits pages by hand.
- Checks: tools/check.sh passes; axe also clean in dark mode; no sideways scroll at 390 px; all pages under 8,000 px on a phone.
- Photos: stand-ins only (Dinis: "just to give LEH a view of what can be done, she will then upload more photos"). GSA graduates-page portrait (no photographer named) and a cropped showreel still in The stage. Spotlight text used only in The stage; no agent contact, age or height published.

## Round 1 (design.b.rounds, 15:23 UTC, rated 3, M3)
Done on the in-hand fixes: Hebrew letters in all five designs (no words until she checks: docs/hebrew-to-check.md); a fourth fact chip (children, teenagers and adults) high on every first screen; The stage leads with the lessons, programme list removed, light version added; low vision: stronger Conversation bars, no sticky button on phones, larger Notebook text over lighter rules with hanging ticks, larger Stage capitals; enquiry button near the top in Notebook and Three tenses. Photo reuse rights flagged in the handover. Still hers: Hebrew words, photos, price and availability.

## Round 2 (design.b.rounds, holds at 3, M3)
Fixed: Notebook cover alphabet right to left; Conversation's seven empty Hebrew boxes removed (a draft note says Hebrew versions can be added once she checks), its closing bar now a plain button; larger tense letters; The stage curtains run the full page, ticket button clears the notches on a phone, darker and larger gold capitals; one voice (hers, "I") across the designs. Waiting on her: price and availability if she wants them, photos, enquiry route.

## 25 Nov evening (Dinis, in this session)
- Design switcher moved to the top of every design page (7c452fe).
- "can you actually make one of the designs to be in full hebrew?": added a sixth design, Ivrit, /designs/ivrit/: the Alef-bet design mirrored, html lang="he" dir="rtl", her text translated by the keeper (feminine first person), with a Hebrew and English notice that it is unchecked by her. Her name stays in Latin letters (no Hebrew spelling supplied). This overrides design.b's letters-only rule for this one design, at Dinis's word.
- Asked design.b for one more wow-factor pass ("since these are artists").
- Languages: her Spotlight lists English and Hebrew only.

## 25 Nov, later (Dinis, in this session)
- "the home page should be in english, but can you allow all 5 designs to be translated?": every design now has a Hebrew version under /he/ (right to left, he.css); the Ivrit design is retired in their favour. English / עברית switch at the top of every page and a floating button in the corner.
- "all content from the site is on json files and nothing is hardcoded into html": every word is in site/data/content/*.json (en, he, site, start, tour, admin); tools/designs/build.py builds every page and holds no words.
- "add that admin section (like we did for kate)": /admin/, a back office built from admin.json and the repository (status, tasks from issues/, designs, content files, pages, photos and credits, quality, activity from git, agents, how it was made). Not copied: Kate's signed message page, which needs its own security review.
- "some really nice presentations ... with option to download the PDF": /tour/ with two decks (your-site, behind-the-scenes) from tour.json; PDFs made with tools/tour/pdf.mjs.

## Wow pass (design.b's brief lee-elle-horowitz-wow, ae51a7a and 6d45e80)
- Shared: a slim draft line; the four facts as one line below the first screen; her photo on the first phone screen in every design; no looping motion.
- Alef-bet: her photo seen through a huge alef; a wall of 22 letters, right to left, arriving in a wave. Conversation: no hero, the chat first, a typing indicator, her photo as avatar, facts as quick replies, a reply box that stays. Three tenses: was / is / will be as the headline; three panels swiped on a phone (past in sepia, present in colour, future an empty frame for you). The stage: a dark stage, her name like a poster, a spotlight, curtains that open once, a playbill and a ticket stub. Notebook: the cover is the first screen, her photo taped on, red ticks in the margin.
- Hebrew pages: Hebrew display type, heavier and larger; layout mirrored with logical CSS.
- Dinis: "in the option to change the design I see all of them in one go" and "gain you one line from that top nav bar": the switcher is one line (languages and all five designs; symbols on a phone).

## Open
- Swap in the Spotlight portrait (credit Kim Hardy) when it arrives as a file; then her own photos.
- /send/ enquiry form, with security.b's review.
- Design rounds with design.b.rounds; Hebrew rendering on iOS Safari, Android Chrome, Windows Edge.

## Waiting on
- Lee-Elle: design choice, Hebrew words, photos with credits, contact details, approval.

## Hebrew rule (design.b)
No Hebrew beyond single letters and her own words goes live until she has checked it. Her Hebrew name spelling has not been supplied, so it is not used.
