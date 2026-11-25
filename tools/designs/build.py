#!/usr/bin/env python3
"""Build Lee-Elle Horowitz's design pages, in English and in Hebrew, from tools/designs/content.py.

Run from the repository root:  python3 tools/designs/build.py
All words come from the JSON files in site/data/content/ (en.json, he.json, site.json, start.json); this script holds none.
Writes, for each of the five designs, an English page (site/designs/<name>/) and a Hebrew page, right to left
(site/he/designs/<name>/); the home page in English (site/index.html) and in Hebrew (site/he/index.html); the two
design pickers; and the start page (site/start/). Once she starts editing pages
directly, stop using this script, or her edits are overwritten.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'site')
C = os.path.join(R, 'data', 'content')
def load(n): return json.load(open(os.path.join(C, n), encoding='utf-8'))
EN, HE, SITE, START = load('en.json'), load('he.json'), load('site.json'), load('start.json')
BASE, REPO, NAME, HOME = SITE['base'], SITE['repo'], SITE['name'], SITE['home_design']
SLUGS, GLYPH, THEME = SITE['designs'], SITE['glyph'], SITE['theme']
ALEFBET = [(a['letter'], a['name']) for a in SITE['alefbet']]
SHOWREELS = SITE['showreels'].replace('&', '&amp;')
PHOTO = SITE['photos']

def w(p, s):
    f = os.path.join(R, p); os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, 'w', encoding='utf-8').write(s)
def pre(L): return '/he' if L['code'] == 'he' else ''
def other(L): return EN if L['code'] == 'he' else HE

ICON = {
 'pin': '<path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z"/><circle cx="12" cy="9.5" r="2.6"/>',
 'screen': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 'one': '<circle cx="12" cy="8" r="3.6"/><path d="M5 21c.8-4 3.6-6 7-6s6.2 2 7 6"/>',
 'group': '<circle cx="8" cy="9" r="3"/><circle cx="16.5" cy="9.5" r="2.5"/><path d="M2.5 20c.6-3.4 2.8-5 5.5-5s4.9 1.6 5.5 5M13.5 15.3c.9-.4 1.9-.6 3-.6 2.3 0 4.2 1.4 4.8 4.3"/>',
 'note': '<path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>',
 'check': '<path d="M4 12.5l5 5L20 6.5"/>',
}

def icon(k): return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICON[k]}</svg>'
def ul(items, cls=''): return '<ul%s>' % (f' class="{cls}"' if cls else '') + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def paras(ps): return ''.join(f'<p>{p}</p>' for p in ps)
def ph(L, i=1):
    ph_, alt = (PHOTO['portrait'], L['alt']) if i == 1 else (PHOTO['bass'], L['alt2'])
    return f'<img src="{ph_["src"]}" width="{ph_["width"]}" height="{ph_["height"]}" alt="{alt}">'
def fig(L, cls, i=1):
    cap = L['credit'] if i == 1 else L['credit2']
    return f'<figure class="{cls}">{ph(L, i)}<figcaption>{cap}</figcaption></figure>'
def cta(L): return f'<p class="cta"><span class="btn" role="note">{L["cta"]} <span class="soon">{L["soon"]}</span></span></p>'
def draft(L): return f'<p class="draft" role="note">{L["draft"]}</p>'
def chips(L):
    return '<ul class="chips">' + ''.join(f'<li>{icon(k)}{t}</li>' for k, t in zip(['one', 'pin', 'screen', 'check'], L['chips'])) + '</ul>'
def he_on(L): return L['code'] == 'he'

def head(L, path, title, desc, css, theme, alt_path):
    url = BASE + path
    o = other(L)
    return f"""<!doctype html>
<html lang="{L['lang']}" dir="{L['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{theme}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{L['site_name']}">
<meta property="og:locale" content="{L['locale']}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}{SITE['share_card']}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{EN['site_name']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}{SITE['share_card']}">
<link rel="canonical" href="{url}">
""" + (f'<link rel="alternate" hreflang="{o["lang"]}" href="{BASE}{alt_path}">\n<link rel="alternate" hreflang="{L["lang"]}" href="{url}">\n' if alt_path else '') + \
      ''.join(f'<link rel="stylesheet" href="{c}">\n' for c in css) + '</head>\n'

F = SITE['family']
GAP = ' class="family-gap"'
FAM = ('<details class="family-credit" lang="en-GB" dir="ltr">\n  <summary>' + F['summary'] + '</summary>\n  <ul>\n' +
       ''.join(f'    <li{GAP if len(l) > 2 else ""}><a href="{l[0]}">{l[1]}</a></li>\n' for l in F['links']) + '  </ul>\n</details>\n')

def langs(L, here, there):
    """The language switch: both languages always shown, the current one filled."""
    en_href, he_href = (there, here) if he_on(L) else (here, there)
    cur = ' aria-current="true"'
    return (f'<p class="langs" role="group" aria-label="{L["lang_label"]}">'
            f'<a href="{en_href}" lang="en-GB" hreflang="en-GB"{cur if not he_on(L) else ""}>{SITE["lang_names"]["en"]}</a>'
            f'<a href="{he_href}" lang="he" hreflang="he"{cur if he_on(L) else ""}>{SITE["lang_names"]["he"]}</a></p>')

def thumb(L, s): return SITE['thumbs'].replace('{slug}', s).replace('{lang}', L['code'])
def card(L, s, i, cur=None, tag='li', lazy=True):
    """One design as a card: a real screenshot of it, its number and name, and one line about it."""
    p = pre(L); here = ' aria-current="page"' if s == cur else ''
    return (f'<{tag} class="dc"><a href="{p}/designs/{s}/"{here}><img src="{thumb(L, s)}" width="640" height="400" alt=""{' loading="lazy"' if lazy else ''}>'
            f'<strong>{i + 1}. {L["designs"][s][0]}</strong><span>{L["designs_short"][s]}</span></a></{tag}>')

def switcher(L, cur, here, there):
    """The language switch, and a "Choose a design" button that opens all five designs as screenshots (as on Emily's and Grace's sites)."""
    p = pre(L)
    cards = ''.join(card(L, s, i, cur) for i, s in enumerate(SLUGS))
    return (f'<nav class="switch" aria-label="{L["sw_label"]}"><div class="switch-in">' + langs(L, here, there) +
            f'<details class="chooser"><summary><span class="ch-ico" aria-hidden="true"></span>{L["sw_choose"]}</summary>'
            f'<div class="ch-panel"><ul class="ch-grid">{cards}</ul><p class="ch-all"><a href="{p}/designs/">{L["sw_all"]}</a></p></div></details></div>'
            f'<a class="lang-fab" href="{there}" lang="{other(L)["lang"]}" hreflang="{other(L)["lang"]}" aria-label="{L["other_lang_long"]}">'
            f'<span aria-hidden="true">{"A" if he_on(L) else "א"}</span>{L["other_lang"]}</a></nav>\n')

def foot(L):
    fl = L.get('footer_links', SITE['footer_links']); small = L.get('footer_small', SITE['footer_small'])
    attrs = '' if he_on(L) else ' lang="en-GB" dir="ltr"'
    links = ''.join(f'  <a href="{h}">{t}</a>\n' for h, t in fl)
    return (f'<footer class="foot">\n<p class="foot-name">{L["name"]} <span>{L["foot_line"]}</span></p>\n'
            f'<nav class="site-links"{attrs} aria-label="{L["about_links_label"]}">\n{links}</nav>\n'
            f'<p class="small"{attrs}>{small}</p>\n</footer>\n')

def page(L, path, title, desc, css, theme, body, cur, cls, there, switch=True):
    top = switcher(L, cur, path, there) if switch else ''
    css = ['/assets/base.css'] + css + (['/assets/he.css'] if he_on(L) else [])
    return head(L, path, title, desc, css, theme, there if switch else None) + f'<body class="{cls}">\n<a class="skip" href="#main">{L["skip"]}</a>\n' + FAM + top + body + foot(L) + '</body>\n</html>\n'

def brand(L, extra=''):
    return f'<header class="top"><a class="brand" href="{pre(L)}/">{L["name"]}</a>{extra}</header>\n'
def jump(L):
    return f'<nav class="jump" aria-label="{L["jump_label"]}">' + ''.join(f'<a href="#{i}">{t}</a>' for i, t in L['jump']) + '</nav>'

# ---------- shared by all five: a slim draft line, facts below the first screen ----------
def draft(L): return f'<p class="draft-line" role="note">{L["draft_line"]}</p>'
def facts(L):
    return f'<ul class="facts" aria-label="{L["facts_label"]}">' + ''.join(f'<li>{icon(k)}{t}</li>' for k, t in zip(['one', 'pin', 'screen', 'check'], L['chips'])) + '</ul>'
def hel(L, c, cls=''):
    """A single Hebrew letter: marked as Hebrew on English pages; plain on Hebrew pages."""
    c_ = f' class="{cls}"' if cls else ''
    return f'<span{c_} lang="he" dir="rtl">{c}</span>' if not he_on(L) else f'<span{c_}>{c}</span>'
def credit_line(L, i=1):
    return f'<p class="credit-line">{L["credit"] if i == 1 else L["credit2"]}</p>'
def wall(L):
    en = not he_on(L)
    return (f'<div class="wall" dir="rtl" role="img" aria-label="{L["wall_label"]}">' + ''.join(
        f'<span class="w" style="--i:{n}"><b lang="he">{c}</b>' + (f'<small lang="en-GB">{nm}</small>' if en else '') + '</span>' for n, (c, nm) in enumerate(ALEFBET)) + '</div>')

# ---------- 1 Alef-bet: her photo seen through a huge alef ----------
def alef(L):
    H = L['h']; en = not he_on(L)
    def sec(i, title, inner, cls=''):
        c, n = ALEFBET[i]
        return f'<section class="sec {cls}" aria-labelledby="s{i}"><div class="sec-head">{hel(L, c, "sec-g")}' + (f'<span class="sec-n">{n}</span>' if en else '') + f'</div><div class="sec-body"><h2 id="s{i}">{title}</h2>{inner}</div></section>'
    tiles = '<ul class="tiles">' + ''.join(f'<li>{hel(L, c, "tile-g")}' + (f'<span class="tile-n">{n}</span>' if en else '') + f'<span class="tile-t">{t}</span></li>' for (c, n), t in zip(ALEFBET, L['lessons'])) + '</ul>'
    stats = '<ul class="stats">' + ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in L['stats']) + '</ul>'
    fmt = '<ul class="fmt">' + ''.join(f'<li>{icon(k)}<strong>{a}</strong><span>{b}</span></li>' for k, a, b in L['fmt']) + '</ul>'
    who = '<ul class="who">' + ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in L['who']) + '</ul>'
    return (brand(L, jump(L)) + '<main id="main">\n' + draft(L) +
      f'<section class="hero" aria-labelledby="h1"><div class="alef-photo" role="img" aria-label="{L["alt"]}"><span class="alef-g" aria-hidden="true">א</span></div>'
      f'<div class="hero-text"><p class="eyebrow">{L["eyebrow"]}</p><h1 id="h1">{L["title_a"]} <span>{L["title_b"]}</span></h1><p class="lead">{L["lead"]}</p>' + cta(L) + '</div></section>\n' +
      credit_line(L) + facts(L) + wall(L) + stats +
      sec(0, H['about'], paras(L['about']) + who) +
      sec(1, H['lessons'], f'<p class="hint">{L["ab_hint"]}</p>' + tiles, 'wide') +
      f'<blockquote class="quote"><p>{L["quote"]}</p><footer>{L["name"]}</footer></blockquote>' +
      sec(2, H['approach'], f'<p class="big">{L["approach"]}</p>') +
      sec(3, H['quals'], '<ul class="ticks">' + ''.join(f'<li>{icon("check")}<span>{q}</span></li>' for q in L['quals']) + '</ul>') +
      sec(4, H['fmt'], fmt) +
      sec(5, H['music'], f'<p>{L["music_note"]}</p>' + '<ul class="music">' + ''.join(f'<li>{icon("note")}{m}</li>' for m in L['music']) + '</ul>', 'music') +
      f'<section class="end" aria-labelledby="end"><span class="end-g" lang="he" dir="rtl" aria-hidden="true">ת</span><h2 id="end">{L["ab_end"]}</h2><p>{L["ab_end_p"]}</p>' + cta(L) + '</section></main>\n')

# ---------- 2 Conversation: no hero, start talking ----------
def convo(L):
    n = [0]; en = not he_on(L)
    av = f'<img class="av" src="{PHOTO["portrait"]["src"]}" width="40" height="53" alt="">'
    def you(t): return f'<li class="msg you"><p>{t}</p></li>'
    def her(inner):
        c, nm = ALEFBET[n[0]]; n[0] += 1
        mk = hel(L, c, 'mk-g') + (f' <span class="mk-n">{nm}</span>' if en else '')
        return f'<li class="msg her">{av}<div class="en"><p class="mk">{mk}</p>{inner}</div></li>'
    q = L['cv_q']
    answers = [L['lead'], L['fmt'][0][2], L['fmt'][1][2], L['quals'][5]]
    quick = (f'<div class="quick" role="group" aria-label="{L["cv_quick"]}">' + ''.join(
        f'<details><summary>{icon(k)}{t}</summary><p>{a}</p></details>' for k, t, a in zip(['one', 'pin', 'screen', 'check'], L['chips'], answers)) + '</div>')
    replies = '<ul class="replies">' + ''.join(f'<li>{l}</li>' for l in L['lessons']) + '</ul>'
    return (f'<header class="chat-top"><a class="brand" href="{pre(L)}/"><img class="ava" src="{PHOTO["portrait"]["src"]}" width="48" height="64" alt="">'
      f'<span><strong>{L["name"]}</strong><span class="status">{L["cv_status"]}</span></span></a></header>\n<main id="main">\n' + draft(L) +
      f'<h1 id="h1" class="thread-title">{L["title"]}</h1>'
      f'<ol class="thread"><li class="day" aria-hidden="true">{L["cv_day"]}</li>' +
      you(q[0]) + f'<li class="typing" aria-hidden="true"><span></span><span></span><span></span></li>' +
      her(paras(L['about'][:1]) + fig(L, 'inline') + quick) +
      you(q[1]) + her(paras(L['about'][1:])) +
      you(q[2]) + her(f'<p>{L["cv_can"]}</p>' + replies) +
      you(q[3]) + her(f'<p>{L["approach"]} {L["quote"]}</p>') +
      you(q[4]) + her(ul(L['quals'], 'ticks')) +
      you(q[5]) + her(ul([b for _, _, b in L['fmt']])) +
      you(q[6]) + her(f'<p>{L["cv_music"]}</p>' + ul(L['music'])) +
      f'</ol><p class="note">{L["cv_note"]}</p><div class="compose"><span class="field">{L["cta"]}</span><span class="send">{L["soon"]}</span></div></main>\n')

# ---------- 3 Three tenses: three panels, one photo three ways ----------
def tenses(L):
    lab, hh = L['tn_labels'], L['tn_h']; H = L['h']
    journey = '<ol class="journey">' + ''.join(f'<li><span class="dot" aria-hidden="true"></span><strong>{a}</strong><span>{b}</span></li>' for a, b in L['journey']) + '</ol>'
    grid = '<ul class="lgrid">' + ''.join(f'<li>{t}</li>' for t in L['lessons']) + '</ul>'
    fmt = '<ul class="fmt">' + ''.join(f'<li>{icon(k)}<span>{b}</span></li>' for k, _, b in L['fmt']) + '</ul>'
    w0, w1, w2 = L['tn_words']
    return (brand(L) + '<main id="main">\n' + draft(L) +
      f'<section class="hero" aria-labelledby="h1"><h1 id="h1"><span class="vh">{L["title"]}: </span>'
      f'<span class="conj"><span class="p">{w0}</span><span class="n">{w1}</span><span class="f">{w2}</span></span></h1>'
      f'<p class="lead">{L["lead"]} {L["tn_lead_more"]}</p></section>'
      f'<nav class="tabs" aria-label="{L["tn_tabs"]}"><a href="#past" class="p">{lab[0]}</a><a href="#present" class="n">{lab[1]}</a><a href="#future" class="f">{lab[2]}</a></nav>'
      f'<div class="panels" tabindex="0" role="region" aria-label="{L["tn_tabs"]}">'
      f'<section id="past" class="tense past" aria-labelledby="past-h"><p class="t-label">{lab[0]} {hel(L, "א", "t-he")}</p><h2 id="past-h">{hh[0]}</h2>' + fig(L, 'photo') + paras(L['about'][:1]) + journey + '</section>'
      f'<section id="present" class="tense present" aria-labelledby="present-h"><p class="t-label">{lab[1]} {hel(L, "ב", "t-he")}</p><h2 id="present-h">{hh[1]}</h2>' + fig(L, 'photo') + paras(L['about'][1:]) +
      f'<h3>{H["lessons"]}</h3>' + grid + f'<h3>{H["fmt"]}</h3>' + fmt + '</section>'
      f'<section id="future" class="tense future" aria-labelledby="future-h"><p class="t-label">{lab[2]} {hel(L, "ג", "t-he")}</p><h2 id="future-h">{hh[2]}</h2>'
      f'<div class="you-frame" role="img" aria-label="{L["tn_you_label"]}"><span>{L["tn_you"]}</span></div><p class="big">{L["quote"]}</p>' + cta(L) + '</section></div>' +
      facts(L) +
      f'<section class="more" aria-labelledby="more-h"><h2 id="more-h">{H["quals"]}</h2>' + ul(L['quals'], 'ticks') +
      f'<h3>{H["approach"]}</h3><p>{L["approach"]}</p><div class="music"><h3>{H["music"]}</h3><p>{L["music_note"]}</p>' + ul(L['music']) + '</div></section></main>\n')

# ---------- 4 The stage: a spotlight, a curtain, a bill and a ticket ----------
def stage(L):
    a = L['st_acts']; H = L['h']
    def ah(c): return ' ' + hel(L, c, 'act-he')
    scenes = '<ol class="scenes">' + ''.join(f'<li><span>' + hel(L, c) + f' {L["st_scene"]} {i+1}</span>{t}</li>' for i, ((c, _), t) in enumerate(zip(ALEFBET, L['lessons']))) + '</ol>'
    bill = (f'<section class="bill" aria-labelledby="bill-h"><h2 id="bill-h" class="rule">{L["st_bill"]}</h2><ol class="running">'
            f'<li><span>{a[0]}</span>{L["st_a1"]}</li><li><span>{L["st_interval"]}</span></li><li><span>{a[1]}</span>{L["st_a2"]}</li><li><span>{a[2]}</span>{L["st_a3"]}</li></ol></section>')
    stub = f'<p class="cta stub"><span class="btn" role="note">{L["cta"]} <span class="soon">{L["soon"]}</span></span></p>'
    return ('<main id="main">\n<div class="curtain l" aria-hidden="true"></div><div class="curtain r" aria-hidden="true"></div>\n' + draft(L) +
      f'<section class="cover" aria-labelledby="h1"><div class="drape l" aria-hidden="true"></div><div class="drape r" aria-hidden="true"></div>'
      f'<p class="presents">{L["st_presents"]}</p><p class="poster-name" aria-hidden="true">{L["name"]}</p>'
      '<div class="spot">' + fig(L, 'portrait') + '</div>'
      f'<div class="marquee"><h1 id="h1">{L["title_a"]}</h1><p class="with">{L["title_b"]}</p></div>'
      f'<p class="lead">{L["lead"]}</p>' + stub + '</section>\n' + facts(L) + bill +
      f'<section class="act" aria-labelledby="a1"><p class="act-n">{a[0]}{ah("א")}</p><h2 id="a1">{L["st_a1"]}</h2>'
      f'<h3>{H["lessons"]}</h3>' + scenes + paras(L['about']) +
      f'<h3>{H["approach"]}</h3><p>{L["approach"]} {L["quote"]}</p><h3>{H["fmt"]}</h3>' + ul([b for _, _, b in L['fmt']]) + '</section>'
      f'<p class="interval" role="separator">{L["st_interval"]}</p>'
      f'<section class="act two" aria-labelledby="a2"><p class="act-n">{a[1]}{ah("ב")}</p><h2 id="a2">{L["st_a2"]}</h2><p>{L["music_note"]}</p><div class="split">' +
      fig(L, 'still', 2) + ul(L['music'], 'notes') + '</div></section>'
      f'<section class="act bio" aria-labelledby="a3"><p class="act-n">{a[2]}{ah("ג")}</p><h2 id="a3">{L["st_a3"]}</h2>' + ul(L['quals']) +
      f'<h3>{L["st_on"]}</h3><p class="from">{L["st_from"]}</p>' + ul(L['stage']) +
      f'<p><a class="reel" href="{SHOWREELS}" rel="noopener">{L["st_reel"]}</a> <span class="ext">{L["st_ext"]}</span></p></section>'
      f'<section class="ticket" aria-labelledby="tk"><h2 id="tk">{L["st_ticket"]}</h2><p>{L["st_ticket_p"]}</p>' + cta(L) + '</section></main>\n')

# ---------- 5 Notebook: the cover is the first screen ----------
def notebook(L):
    H = L['h']
    dl = '<dl class="label">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in L['nb_label']) + '</dl>'
    return ('<main id="main">\n' + draft(L) +
      f'<div class="book"><div class="cover"><p class="label-k">{L["nb_book"]}</p><div class="cover-row">' + dl + fig(L, 'polaroid') + '</div>'
      '<p class="cover-ab" dir="rtl" aria-hidden="true">' + ' '.join(hel(L, c) for c, _ in ALEFBET) + '</p><p class="open-hint" aria-hidden="true">↓</p></div>'
      f'<section class="page" aria-labelledby="h1"><h1 id="h1">{L["title"]}</h1><p class="lead"><mark>{L["lead"]}</mark></p>' + cta(L) + facts(L) +
      f'<h2>{H["about"]}</h2>' + paras(L['about']) + f'<h2>{H["lessons"]}</h2><ol class="ex">' + ''.join(f'<li>{hel(L, c, "ex-g")} {t}</li>' for (c, _), t in zip(ALEFBET, L['lessons'])) + '</ol>'
      f'<h2>{H["approach"]}</h2><p>{L["approach"]}</p><p><mark>{L["quote"]}</mark></p>'
      f'<h2>{H["quals"]}</h2>' + ul(L['quals'], 'ticks') + f'<h2>{H["fmt"]}</h2>' + ul([b for _, _, b in L['fmt']]) +
      f'<h2>{H["music"]}</h2><p>{L["music_note"]}</p>' + ul(L['music']) +
      f'<div class="sticky" role="note"><p>{L["cta"]}</p><p class="soon">{L["soon"]}</p></div></section></div></main>\n')

FN = {'alef-bet': alef, 'conversation': convo, 'three-tenses': tenses, 'the-stage': stage, 'notebook': notebook}

def picker(L):
    cards = ''.join(card(L, s, i, lazy=False) for i, s in enumerate(SLUGS))
    return (brand(L) + '<main id="main">\n' + draft(L) + f'<p class="eyebrow">{L["pk_eyebrow"]}</p><h1>{L["pk_h"]}</h1>'
      f'<p class="lead">{L["pk_lead"]}</p><ol class="ch-grid big">{cards}</ol></main>\n')
def start():
    T = START; rep = lambda h: h.replace('{repo}', REPO)
    picks = ''.join(card(EN, s, i, lazy=False) for i, s in enumerate(SLUGS))
    steps = ''
    for n, st in enumerate(T['steps'], 1):
        inner = rep(st['html']) + (f'<ol class="ch-grid big">{picks}</ol>' if st.get('picker') else '') + rep(st.get('after', ''))
        steps += f'<section class="step" aria-labelledby="st{n}"><p class="step-n" aria-hidden="true">{n}</p><div><h2 id="st{n}">{st["title"]}</h2>{inner}</div></section>'
    lt = T['later']
    later = (f'<section class="later" aria-labelledby="later"><h2 id="later">{lt["h2"]}</h2>' + rep(lt['intro']) +
             ''.join(f'<details><summary>{d["summary"]}</summary>{rep(d["html"])}</details>' for d in lt['details']) + '</section>')
    return (brand(EN) + f'<main id="main">\n<p class="eyebrow">{T["eyebrow"]}</p><h1>{T["h1"]}</h1><p class="lead">{T["lead"]}</p>' + steps + later + '</main>\n')

# ---------- Guided tour: slides from tour.json, PDFs made by tools/tour/pdf.mjs ----------
TOUR = load('tour.json')
def slide(d, sl, n, total):
    t = sl['type']; k = f'<p class="s-kicker">{sl.get("kicker", "")}</p>'; num = f'<p class="s-num" aria-hidden="true">{n} / {total}</p>'
    img = lambda src, cls='shot', w=1280, h=800: f'<img class="{cls}" src="{src if src.startswith("/") else "/tour/img/" + src + ".webp"}" alt="" width="{w}" height="{h}" loading="lazy">'
    pts = lambda xs, cls='s-points': f'<ul class="{cls}">' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    if t == 'cover':
        fan = '<div class="s-fan" aria-hidden="true">' + ''.join(f'<span style="--i:{i}">{img(x, "fan", 640, 400)}</span>' for i, x in enumerate(sl['imgs'])) + '</div>'
        inner = f'<div class="s-text">{k}<h2 class="s-h big">{sl["h"]}</h2><p class="s-sub">{sl["sub"]}</p><p class="s-note">{sl["note"]}</p></div>{fan}'
    elif t == 'brief':
        col = lambda c: f'<div class="s-col"><h3 class="s-h3">{c["title"]}</h3>{pts(c["points"])}</div>'
        inner = f'<div class="s-text wide">{k}<h2 class="s-h">{sl["h"]}</h2><div class="s-cols">{col(sl["left"])}{col(sl["right"])}</div></div>'
    elif t == 'map':
        head_ = ''.join(f'<th scope="col">{c}</th>' for c in sl['cols'])
        rows = ''.join('<tr>' + f'<th scope="row">{r[0]}</th>' + ''.join(f'<td>{x}</td>' for x in r[1:]) + '</tr>' for r in sl['rows'])
        inner = f'<div class="s-text wide">{k}<h2 class="s-h">{sl["h"]}</h2><p class="s-p">{sl["intro"]}</p><table class="s-map"><thead><tr>{head_}</tr></thead><tbody>{rows}</tbody></table></div>'
    elif t == 'design':
        im = sl['imgs']
        col = (f'<div class="s-collage">{img(im["desk"], "c-desk", 640, 400)}{img(im["phone"], "c-phone", 390, 844)}'
               f'{img(im["he"], "c-he", 390, 844)}{img(im["detail"], "c-detail", 1200, 400)}'
               f'<span class="c-tag c-tag-en">{SITE["lang_names"]["en"]}</span><span class="c-tag c-tag-he" lang="he">{SITE["lang_names"]["he"]}</span></div>')
        inner = (f'<div class="s-text">{k}<h2 class="s-h">{sl["h"]}</h2><p class="s-why">{TOUR["index"]["why_label"]}</p>{pts(sl["why"], "s-points tight")}'
                 f'<p class="s-sees">{sl["sees"]}</p></div>{col}')
    elif t in ('hebrew', 'phones'):
        row = f'<div class="s-row s-row-{len(sl["imgs"])}">' + ''.join(img(x, "p-phone", 390, 844) for x in sl['imgs']) + '</div>'
        extra = pts(sl['points'], 's-points tight') if sl.get('points') else ''
        inner = f'<div class="s-text">{k}<h2 class="s-h{" he-h" if t == "hebrew" else ""}">{sl["h"]}</h2><p class="s-p">{sl["p"]}</p>{extra}</div>{row}'
    elif t == 'capabilities':
        inner = f'<div class="s-text wide">{k}<h2 class="s-h">{sl["h"]}</h2><ul class="s-caps">' + ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in sl['items']) + '</ul></div>'
    elif t == 'team':
        inner = (f'<div class="s-text wide">{k}<h2 class="s-h">{sl["h"]}</h2><p class="s-p">{sl["intro"]}</p><ol class="s-team">' +
                 ''.join(f'<li><span class="verb">{v}</span><strong>{a}</strong><span>{b}</span></li>' for a, v, b in sl['steps']) + '</ol></div>')
    elif t == 'rounds':
        inner = (f'<div class="s-text wide">{k}<h2 class="s-h">{sl["h"]}</h2><p class="s-p">{sl["intro"]}</p><ol class="s-rounds">' +
                 ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in sl['rounds']) + '</ol></div>')
    elif t == 'points':
        code = f'<p class="s-code"><code>{sl["code"]}</code></p>' if sl.get('code') else ''
        inner = f'<div class="s-text wide">{k}<h2 class="s-h">{sl["h"]}</h2>{pts(sl["points"])}{code}</div>'
    elif t == 'flow':
        inner = f'<div class="s-text wide">{k}<h2 class="s-h">{sl["h"]}</h2><ol class="s-flow">' + ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in sl['steps']) + '</ol></div>'
    else:
        inner = f'<div class="s-text wide center">{k}<h2 class="s-h big">{sl["h"]}</h2><p class="s-p">{sl["p"]}</p><p class="s-links">' + ''.join(f'<a href="{h}"{" lang=\"he\"" if any("֐" <= ch <= "׿" for ch in x) else ""}>{x}</a>' for h, x in sl['links']) + '</p></div>'
    if sl.get('says') and d.get('narrator'):
        nr = d['narrator']
        says = (f'<div class="s-says" role="note"><p class="s-who"><span class="s-av" aria-hidden="true">{nr["initial"]}</span>'
                f'<strong>{nr["name"]}</strong> <span class="s-lbl">{nr["label"]}</span></p><p class="s-line">{sl["says"]}</p></div>')
        inner = inner.replace('</div>', says + '</div>', 1) if inner.startswith('<div class="s-text') else inner + says
    T = TOUR['index']; lbl = T['slide_of'].replace('{n}', str(n)).replace('{total}', str(total))
    prev = f'<a class="s-prev" href="#slide-{n - 1}" rel="prev"><span aria-hidden="true">&#8592;</span> {T["prev"]}</a>' if n > 1 else '<span class="s-prev off" aria-hidden="true"></span>'
    nxt = f'<a class="s-next" href="#slide-{n + 1}" rel="next">{T["next"]} <span aria-hidden="true">&#8594;</span></a>' if n < total else '<span class="s-next off" aria-hidden="true"></span>'
    nav = f'<nav class="s-nav" aria-label="{lbl}">{prev}<span class="s-count">{n} / {total}</span>{nxt}</nav>'
    return f'<section class="slide s-{t}" id="slide-{n}" aria-label="{lbl}"><div class="frame">{num}{inner}</div>{nav}</section>'

def tour_head(path, title, desc):
    return head(EN, path, title, desc, ['/assets/base.css', '/assets/tour.css'], '#14161c', None)

def build_tour():
    T = TOUR['index']
    cards = ''.join(f'<li class="deck" style="--deck:{d["accent"]}"><p class="d-for">{d["for"]}</p><h2>{d["title"]}</h2><p>{d["desc"]}</p>'
                    f'<p class="d-meta">{len(d["slides"])} {T["slides_word"]}</p><p class="d-act"><a class="d-open" href="/tour/{d["id"]}/">{T["open"]}</a>'
                    f'<a class="d-pdf" href="/tour/{d["pdf_name"]}" download="{d["pdf_name"]}">{T["pdf"]}</a></p></li>' for d in TOUR['decks'])
    body = (brand(EN) + f'<main id="main" class="tour-index"><p class="eyebrow">{T["eyebrow"]}</p><h1>{T["h1"]}</h1><p class="lead">{T["lead"]}</p><ul class="decks">{cards}</ul><p class="hint">{T["keys"]}</p><p class="hint">{T["says_note"]}</p></main>\n')
    w('tour/index.html', tour_head('/tour/', T['title'], T['desc']) + f'<body class="d-tour">\n<a class="skip" href="#main">{EN["skip"]}</a>\n' + FAM + body + foot(EN) + '</body>\n</html>\n')
    for d in TOUR['decks']:
        n = len(d['slides'])
        bar = (f'<header class="deck-bar"><a class="brand" href="/tour/">{T["eyebrow"]}</a><h1 class="deck-t">{d["title"]}</h1>'
               f'<a class="d-pdf" href="/tour/{d["pdf_name"]}" download="{d["pdf_name"]}">{T["pdf"]}</a></header>\n')
        slides = ''.join(slide(d, sl, i + 1, n) for i, sl in enumerate(d['slides']))
        w(f'tour/{d["id"]}/index.html', tour_head(f'/tour/{d["id"]}/', f'{d["title"]}: {EN["site_name"]}', d['desc']) +
          f'<body class="d-deck" style="--deck:{d["accent"]}">\n<a class="skip" href="#main">{EN["skip"]}</a>\n' + FAM + bar + f'<main id="main" class="deck-main">{slides}</main>\n' + foot(EN) + '<script src="/assets/tour.js" defer></script>\n</body>\n</html>\n')

# ---------- Admin: labels from admin.json; figures read from the repository ----------
import subprocess, glob, re, html as _html
ROOT = os.path.abspath(os.path.join(R, '..'))
def git(*a):
    try: return subprocess.check_output(['git', '-C', ROOT, *a], text=True, stderr=subprocess.DEVNULL)
    except Exception: return ''
def kb(n): return f'{n / 1024:.0f} KB' if n >= 1024 else f'{n} B'
def issues():
    out = {}
    for col in ('open', 'blocked', 'done'):
        cards = []
        for f in sorted(glob.glob(os.path.join(ROOT, 'issues', col, '*.md'))):
            t = open(f, encoding='utf-8').read(); fm = {}
            m = re.match(r'---\n(.*?)\n---\n', t, re.S)
            if m:
                for line in m.group(1).splitlines():
                    if ':' in line: k, v = line.split(':', 1); fm[k.strip()] = v.strip()
                t = t[m.end():]
            title = re.search(r'^# (.+)$', t, re.M); body = t.split('\n', 2)[-1].strip() if title else t
            cards.append((os.path.basename(f), title.group(1) if title else os.path.basename(f), body, fm))
        out[col] = cards
    return out

def thead(cols): return '<table><thead><tr>' + ''.join(f'<th scope="col">{c}</th>' for c in cols) + '</tr></thead>'

def build_admin():
    A = load('admin.json'); H = A['h']; Lb = A['labels']
    nav = f'<nav class="ad-nav" aria-label="{Lb["nav"]}">' + ''.join(f'<a href="#{i}">{t}</a>' for i, t in A['nav']) + '</nav>'
    commits = [l.split('\x1f') for l in git('log', '--format=%h\x1f%cI\x1f%s\x1f%(trailers:key=Agent,valueonly,separator=)').strip().splitlines() if l]
    iss = issues(); open_n = len(iss['open']); waiting = {}
    for _, t, _, fm in iss['open']:
        waiting.setdefault(fm.get('blocked_on', Lb['nobody']), []).append(t)
    tiles = list(zip([str(len(SLUGS)), '2', str(open_n), str(len(commits))], Lb['tiles']))
    ov = ('<dl class="ad-status">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in A['status']) + '</dl>'
          '<ul class="ad-tiles">' + ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in tiles) + '</ul>'
          f'<h3>{A["waiting"]}</h3><ul class="ad-wait">' + ''.join(f'<li><strong>{who}</strong><span>{", ".join(ts)}</span></li>' for who, ts in waiting.items()) + '</ul>'
          f'<p>{A["tour"]}</p>')
    cols = ''.join(f'<section class="ad-col ad-{c}"><h3>{n} <span>{len(iss[c])}</span></h3>' + ''.join(
        f'<article class="card"><h4>{t}</h4><p>{_html.escape(b)}</p><p class="meta">' + ' · '.join(f'{k}: {v}' for k, v in fm.items() if k in ('priority', 'blocked_on')) + f'</p><p class="file"><code>{f}</code></p></article>'
        for f, t, b, fm in iss[c]) + '</section>' for c, n in A['columns'])
    board = f'<p>{A["board_intro"]}</p><div class="ad-board">{cols}</div>'
    drows = ''.join(f'<tr><th scope="row">{EN["designs"][s][0]}</th><td>{EN["designs"][s][1]}</td><td><a href="/designs/{s}/">{Lb["english"]}</a> · <a href="/he/designs/{s}/" lang="he">{Lb["hebrew"]}</a></td></tr>' for s in SLUGS)
    designs = thead(Lb['designs_cols']) + f'<tbody>{drows}</tbody></table>'
    jrows = ''.join(f'<tr><td><a href="/data/content/{os.path.basename(f)}"><code>{os.path.basename(f)}</code></a></td><td>{_html.escape(json.load(open(f, encoding="utf-8")).get("_note", ""))}</td><td>{kb(os.path.getsize(f))}</td></tr>' for f in sorted(glob.glob(os.path.join(C, '*.json'))))
    pages = []
    for f in sorted(glob.glob(os.path.join(R, '**', 'index.html'), recursive=True)):
        rel = '/' + os.path.relpath(os.path.dirname(f), R).replace('\\', '/') + '/'; rel = '/' if rel == '/./' else rel
        if '/factory/' in rel: continue
        pages.append(f'<tr><td><a href="{rel}">{rel}</a></td><td>{kb(os.path.getsize(f))}</td></tr>')
    content = (f'<p>{A["content_intro"]}</p>' + thead(Lb['content_cols']) + f'<tbody>{jrows}</tbody></table>'
               f'<p>{A["pages_intro"]}</p>' + thead(Lb['pages_cols']) + f'<tbody>{"".join(pages)}</tbody></table>')
    prow = ''
    for src, cr in A['photo_rows']:
        f = os.path.join(R, src.lstrip('/')); credit = EN.get(cr, cr)
        prow += f'<li><img src="{src}" alt="" loading="lazy" width="120" height="120"><div><p><code>{src}</code> · {kb(os.path.getsize(f)) if os.path.exists(f) else Lb["missing"]}</p><p>{credit}</p></div></li>'
    photos = f'<p>{A["photos_intro"]}</p><ul class="ad-photos">{prow}</ul>'
    quality = f'<p>{A["quality_intro"]}</p><ul class="ad-checks">' + ''.join(f'<li class="{"ok" if r == "passed" else "todo"}"><span>{t}</span><strong>{r}</strong></li>' for t, r in A['checks']) + '</ul>'
    arows = ''.join(f'<tr><td><a href="{REPO}/commit/{h}"><code>{h}</code></a></td><td>{d[:16].replace("T", " ")}</td><td>{_html.escape(sub)}</td><td>{_html.escape(ag)}</td></tr>' for h, d, sub, ag in [(c + ["", "", "", ""])[:4] for c in commits])
    activity = f'<p>{A["activity_intro"]}</p>' + thead(Lb['activity_cols']) + f'<tbody>{arows}</tbody></table>'
    ag = json.load(open(os.path.join(R, 'data', 'agents.json'), encoding='utf-8'))['agents']
    agents = f'<p>{A["agents_intro"]}</p><ul class="ad-agents">' + ''.join(f'<li><strong>{x["name"]}</strong><span>{x["role"]}</span><span><a href="/{x["key"].removeprefix("site/")}">{Lb["key"]}</a> · <a href="{REPO}/tree/dev/{x["area"]}">{Lb["notes"]}</a></span></li>' for x in ag) + '</ul>'
    secs = dict(overview=ov, board=board, designs=designs, content=content, photos=photos, quality=quality, activity=activity, agents=agents, made=A['made'])
    body = (brand(EN) + f'<main id="main" class="admin"><p class="eyebrow">{A["eyebrow"]}</p><h1>{A["h1"]}</h1><p class="lead">{A["lead"]}</p>' + nav +
            ''.join(f'<section id="{i}" class="ad-sec" aria-labelledby="{i}-h"><h2 id="{i}-h">{H[i]}</h2>{secs[i]}</section>' for i, _ in A['nav']) + '</main>\n')
    w('admin/index.html', head(EN, '/admin/', A['title'], A['desc'], ['/assets/base.css', '/assets/admin.css'], '#f6f5f1', None) +
      f'<body class="d-admin">\n<a class="skip" href="#main">{EN["skip"]}</a>\n' + FAM + body + foot(EN) + '</body>\n</html>\n')

def main():
    for L in (EN, HE):
        p = pre(L); o = other(L); po = pre(o)
        for s in SLUGS:
            path = f'{p}/designs/{s}/'; there = f'{po}/designs/{s}/'
            n, b = L['designs'][s]
            title = f'{n}: {L["site_name"]}'
            w(path.lstrip('/') + 'index.html', page(L, path, title, L['desc'] + ' ' + b, [f'/assets/{s}.css'], THEME[s], FN[s](L), s, f'd-{s}', there))
        home = f'{p}/'; w(home.lstrip('/') + 'index.html', page(L, home, L['site_name'], L['desc'], [f'/assets/{HOME}.css'], THEME[HOME], FN[HOME](L), HOME, f'd-{HOME}', f'{po}/'))
        pk = f'{p}/designs/'; w(pk.lstrip('/') + 'index.html', page(L, pk, f'{L["pk_h"]}: {L["site_name"]}', L['pk_lead'], ['/assets/picker.css'], '#f6efe3', picker(L), '', 'd-picker', f'{po}/designs/'))
    w('start/index.html', page(EN, '/start/', START['title'], START['desc'], ['/assets/picker.css'], '#f6efe3', start(), '', 'd-start', None, switch=False))

if __name__ == '__main__':
    main()
    build_tour()
    build_admin()
