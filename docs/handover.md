# Handover: Lee-Elle Horowitz's website

For Lee-Elle Horowitz, and for Dinis Cruz until she takes it over. Kept by b.site.lee-elle-horowitz@SWS, the site's keeper.

## What it is

- **Address:** https://lee-elle-horowitz.artist.sovereignweb.site
- **Start page, written for you:** https://lee-elle-horowitz.artist.sovereignweb.site/start/
- **Where it lives:** https://github.com/SovereignWebsite/Site__Artist__Lee-Elle-Horowitz, the `site/` folder on the `dev` branch. Plain files: no server, no cookies, no tracking, nothing loaded from other websites.
- **Status:** a draft. Every page says so until you approve it.

## What is on it

Your own text, as you supplied it: private Hebrew tuition for children, teenagers and adults as the main service, with music tuition as a smaller section. A few facts from your Spotlight profile appear in The stage design only (your training, three theatre credits, the Laurence Olivier Bursary nomination, and the instruments you play).

It comes in five designs, each built around its own idea:

| Design | Idea | Address |
|---|---|---|
| Alef-bet (the home page for now) | An alphabet chart: a large Hebrew letter opens each section | /designs/alef-bet/ |
| Conversation | A chat: a parent asks, you answer | /designs/conversation/ |
| Three tenses | Past, present and future | /designs/three-tenses/ |
| The stage | A theatre programme | /designs/the-stage/ |
| Notebook | A plain, printable exercise book | /designs/notebook/ |

Compare them at /designs/.

## Decisions that are yours

1. **Which design** becomes the home page, or which parts of which.
2. **Hebrew.** Only single letters are used. No Hebrew words go up until you have checked them. Send any you want, for example your name in Hebrew.
3. **Photos.** The current photos are stand-ins, to show what can be done:
   - a portrait from the Guildford School of Acting graduates page, which does not name the photographer;
   - a cropped still from your showreel on Spotlight.
   Send your own, with the photographer's name for each credit.
4. **Contact details.** None are shown. The enquiry button says "Enquiries open soon" until you choose what visitors see, or until the site's enquiry form is connected.
5. **Prices.** None are shown, and none will be unless you give them.
6. **Approval.** When you are happy, say so and the draft notice comes off.

## Still open on our side

- **Secure address (HTTPS).** The site works and deploys, and the address points to it correctly. GitHub has not yet issued its security certificate for this address, so browsers warn on `https://`. This is set in the repository's Pages settings (custom domain and "Enforce HTTPS"). It needs someone with admin rights on the SovereignWebsite organisation.
- **Enquiry form.** The /send/ form, so visitors can ask about lessons and you can send changes and photos, is still to be connected and reviewed by security.b.
- **Design review rounds** with the design agents.
- **Share card.** The picture shown when the link is shared is still the neutral default.
- **Hebrew rendering.** Still to be checked on an iPhone, an Android phone and Windows.

## How it is built

- Each page is one HTML file in `site/`. The five designs share `site/assets/base.css`; each has its own stylesheet in `site/assets/`.
- `tools/designs/build.py` wrote the five designs, the design picker and the start page from one copy of your text. Once you choose a design and start editing pages directly, stop using it, or it will overwrite your edits.
- Every change is checked before it goes live (`bash tools/check.sh`): links, link previews, HTML, and accessibility. A push to `dev` publishes in a minute or two. `main` is locked.

## Who looks after it

- **b.site.lee-elle-horowitz@SWS:** the keeper; its notes are in `site/factory/dinis-cruz/account-b/`.
- **design.b and design.b.rounds:** the design brief and the review rounds.
- **Dinis Cruz:** instructs until the site is handed over to you; then you do.

## Changing it yourself

See the "Later: changing it yourself" part of /start/, or give your own Claude `docs/prompt-for-your-claude.md`.
