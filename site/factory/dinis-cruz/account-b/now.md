# Now (2026-11-25T15:17Z)

## Done
- Area, own key (fbe1f08), design.b's brief (https://design.agents.sovereignweb.site/briefs/lee-elle-horowitz.html, 7222e25).
- Five designs rebuilt for impact at Dinis's ask ("really make this site have the WOW factor"), all from her words: Alef-bet (home: arch portrait, moving alphabet band, giant section letters, quote band), Conversation (chat thread, Hebrew twin bubbles left empty), Three tenses (was / is / will be, journey timeline), The stage (velvet curtains, lit marquee, spotlight, programme, ticket), Notebook (exercise book, polaroid, sticky note; printable). Picker at /designs/.
- /start/ rewritten for Lee-Elle: choose a design, check words and Hebrew, send photos and changes, approve, who looks after it; GitHub steps kept under "Later".
- docs/handover.md and docs/prompt-for-your-claude.md (90c20f3).
- Share card made from her photo and words (site/assets/share/card-1200x630.jpg).
- Generator kept at tools/designs/build.py (designs, picker, start page). Stop using it once she edits pages by hand.
- Checks: tools/check.sh passes; axe also clean in dark mode; no sideways scroll at 390 px; all pages under 8,000 px on a phone.
- Photos: stand-ins only (Dinis: "just to give LEH a view of what can be done, she will then upload more photos"). GSA graduates-page portrait (no photographer named) and a cropped showreel still in The stage. Spotlight text used only in The stage; no agent contact, age or height published.

## Open
- HTTPS: DNS is right (CNAME to sovereignwebsite.github.io) and every Pages deploy succeeds, but GitHub still serves its *.github.io certificate for this address, so https fails. Needs an org admin to check the custom domain and Enforce HTTPS in the repository's Pages settings (this session cannot reach that API). http:// serves the latest build.
- Swap in the Spotlight portrait (credit Kim Hardy) when it arrives as a file; then her own photos.
- /send/ enquiry form, with security.b's review.
- Design rounds with design.b.rounds; Hebrew rendering on iOS Safari, Android Chrome, Windows Edge.
- Register with hub.b when HTTPS works; tell sites.b it is live.

## Waiting on
- Dinis or an org admin: the Pages certificate.
- Lee-Elle: design choice, Hebrew words, photos with credits, contact details, approval.

## Hebrew rule (design.b)
No Hebrew beyond single letters and her own words goes live until she has checked it. Her Hebrew name spelling has not been supplied, so it is not used.
