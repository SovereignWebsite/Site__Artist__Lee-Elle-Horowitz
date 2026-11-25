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

## Design chooser (Dinis: "it should be like" Emily's and Grace's)
- The top bar holds the language switch and one "Choose a design" button; it opens a panel of all five designs as real screenshots (number, name, one line), the current one outlined, and "All five, side by side". The compare page and /start/ use the same cards. Screenshots per language in site/assets/designs/, made by tools/designs/thumbs.mjs and thumbs.py.
- Lesson sent to design.b, so other site keepers do not repeat it.
- design.b.rounds' serious phone finding (Three tenses panels not focusable) fixed in d832576; tools/checks/axe-phone.mjs added.

## Round 3 (design.b.rounds 373d40d; design.b's notes)
- Three tenses fault fixed (d832576); now the tenses stack on phones, side by side from 900 px.
- The floating language button appears only once you scroll, so it no longer covers Alef-bet's button.
- Hebrew: degree and stage credits reworded so English names sit in bdi without brackets; photo credits and footer translated.
- Each design's top strip in its own colours and type.

## Slides and sharing (Dinis)
- Previous / next arrows under every slide and arrow-key navigation (site/assets/tour.js, own script, nothing sent anywhere); the slides still work without it.
- PDFs renamed for sharing: Lee-Elle-Horowitz-website-guided-tour.pdf and Lee-Elle-Horowitz-website-how-it-was-made.pdf; regenerated with every change.
- Asked b.maestro for an earlier slide deck to align with.
- learnings.md: all of Dinis's comments today, for every keeper; sent to design.b, sites.b and b.maestro.

## Tour decks, richer (Dinis: "very vanilla", "more meat", "explain the philosophy")
- Your-site deck: a fan of the five designs; who she is and what the site must do; a map of the five ideas (taken from her words, the idea, the parent it serves); one slide per design with why it suits her, what a parent sees, and a collage (desktop, phone, Hebrew phone, the detail that makes it); Hebrew in every design; five phone first screens; what we can do; her decisions; close.
- Behind-the-scenes deck: the team with each agent's verb, the pipeline, the design rounds as a timeline, JSON content, right to left properly, quality, trust, close.
- PDF fixes: no shadows in print (they printed as grey bands); one slide per page.
- Asked design.b for a deck design brief; started studio.b (session_01Kw9UwBRfW5naDzfcr53Hji) and instagram.b (session_01Kw9UwBa9zYU6ssjUx87NWX) at Dinis's word, on Sonnet, to bring in our characters and personas.

## Open
- Swap in the Spotlight portrait (credit Kim Hardy) when it arrives as a file; then her own photos.
- /send/ enquiry form, with security.b's review.
- Design rounds with design.b.rounds; Hebrew rendering on iOS Safari, Android Chrome, Windows Edge.

## Waiting on
- Lee-Elle: design choice, Hebrew words, photos with credits, contact details, approval.

## Hebrew rule (design.b)
No Hebrew beyond single letters and her own words goes live until she has checked it. Her Hebrew name spelling has not been supplied, so it is not used.

## 25 Nov, evening: narrators in the decks (studio.b, instagram.b, maestro.b, security.b)
- Took studio.b's proposal A (one narrator per deck, text only): The Guide narrates "Your website", Conductor narrates "how it was made". Each line is labelled "Synthetic presenter, made by code, no real person", speaks of Lee-Elle in the third person, and uses only facts already on the site.
- Took proposal B7 ("How to choose", five questions) and D ("Nothing invented": what we left out on purpose). Most of B and C were already in a1626c4.
- No character images yet: stills only from studio.c's reviewed path (security.b opinion 2026-11-25__presenters-in-public-reels.json). No library code on the site.
- Moved the last hardcoded words out of build.py (language names, "Why it suits Lee-Elle") into JSON.
- axe-phone.mjs now names the failing element and exits non-zero on a problem.
- Waiting: Lee-Elle's consent to synthetic presenters, once, via Dinis.

## 25 Nov, evening: design.b's deck brief (26b074e)
- Fixed the defect design.b measured: team, pipeline and rounds slides rendered at 233 to 418 px at 1280 x 720 (the slide grid sized its column from a size-contained frame). All slides now fill the stage.
- New layouts: statement, mirror (English and Hebrew side by side), team as a graph, scoreboard, maturity ladder (M3 today, M4 next, from design.b's model). The close is dark, each claim with a picture from her own site.
- Each design slide wears its design: Alef-bet cream with a great alef, Conversation blue with a chat bubble, Three tenses a three-colour band, The stage dark with gold and curtains, Notebook ruled paper. The collage alternates sides.
- Not taken: "six designs" and "Ivrit" as a sixth design (there are five designs, each in two languages); "changes by talking to her AI" on the close (not yet live: she has not made a change).
- PDF: removed forced page breaks, which added blank pages after two slides. 16 and 11 pages, one slide per page.
