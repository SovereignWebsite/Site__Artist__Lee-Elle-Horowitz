#!/usr/bin/env python3
"""Build the five design pages of Lee-Elle Horowitz's site from her own words.

Run from the repository root:  python3 tools/designs/build.py
It writes site/index.html (the chosen home design), site/designs/<name>/index.html and site/designs/index.html.
Every word on these pages comes from the text she supplied (Site__Agent__Maestro brief, Site 1) or her Spotlight
profile. No Hebrew beyond single letters goes live until she has checked it (design.b's brief).
Once she picks a design and starts editing the HTML herself, stop using this script, or her edits are overwritten.
"""
import os, html
R = os.path.join(os.path.dirname(__file__), '..', '..', 'site')
BASE = 'https://lee-elle-horowitz.artist.sovereignweb.site'
NAME = 'Lee-Elle Horowitz: private Hebrew tuition'
DESC = 'Private Hebrew lessons for children, teenagers and adults, in London and online; music tuition too.'
HOME = 'alef-bet'
e = html.escape

def w(p, s):
    f = os.path.join(R, p); os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, 'w', encoding='utf-8').write(s)

# ---------- her words ----------
TITLE = 'Private Hebrew Tuition with Lee-Elle Horowitz'
LEAD = 'Private Hebrew lessons for children, teenagers and adults.'
ABOUT = ["South African-born and Israel-raised, I am a fluent Hebrew speaker who grew up in Israel and later moved to the UK. I have experience teaching Hebrew to children and beginners, both online and in person.",
 "I offer personalised Hebrew lessons that focus on building confidence, developing conversational skills and understanding how the language works in everyday life.",
 "My approach is creative, interactive and student-centred. Rather than simply memorising vocabulary, I help students understand how to construct sentences, communicate naturally and develop a practical understanding of Hebrew."]
LESSONS = ["Complete beginners", "Conversational Hebrew", "Reading and writing", "Vocabulary development", "Sentence construction and grammar", "Past, present and future tenses", "Hebrew for children growing up in the UK", "Improving fluency for students with some existing knowledge", "Hebrew support for school and supplementary Jewish education"]
APPROACH1 = "Lessons are tailored to each student's age, ability and goals. I aim to make learning enjoyable, practical and engaging, using conversation, activities and real-life examples."
QUOTE = "I want students to feel comfortable making mistakes, asking questions and gradually developing confidence using Hebrew independently."
APPROACH = APPROACH1 + ' ' + QUOTE
QUALS = ["Fluent Hebrew speaker", "Grew up in Israel", "Two years of private teaching experience", "Experience teaching children aged 7 to 11", "First Class Honours BA from the Guildford School of Acting, University of Surrey", "Enhanced DBS checked"]
FORMAT = [("pin", "In person", "In-person lessons in London"), ("screen", "Online", "Online lessons via Zoom"), ("one", "One to one", "Individual tuition"), ("group", "Small groups", "Small group lessons, subject to arrangement")]
MUSIC = ["Singing lessons", "Trombone lessons", "Beginner guitar lessons", "Musical theatre and audition preparation"]
STAGE = ["Trained in Actor-Musicianship at the Guildford School of Acting", "Theatre credits include Stephen Sondheim's Saturday Night, She Loves Me and Vinegar Tom", "Nominated for the Laurence Olivier Bursary Award during her training", "Plays trombone, bass and guitar"]
STATS = [("7 to 11", "the ages of the children she has taught"), ("2 years", "of private teaching"), ("First", "Class Honours BA, Guildford School of Acting"), ("DBS", "Enhanced DBS checked")]
JOURNEY = [("Born", "South Africa"), ("Raised", "Israel, where she grew up speaking Hebrew"), ("Moved", "to the UK"), ("Trained", "First Class Honours BA, Guildford School of Acting, University of Surrey")]
WHO = [("Children", "including children growing up in the UK"), ("Teenagers", "with school and supplementary Jewish education"), ("Adults", "from complete beginners to improving fluency")]
SHOWREELS = "https://mediaviewer.spotlight.com/artist/showreels?artistRef=M387193&amp;startClipId=1a147320-5850-4895-b12c-30f7cb9e4d9b"

ALEFBET = [('א','alef'),('ב','bet'),('ג','gimel'),('ד','dalet'),('ה','he'),('ו','vav'),('ז','zayin'),('ח','chet'),('ט','tet'),('י','yod'),('כ','kaf'),('ל','lamed'),('מ','mem'),('נ','nun'),('ס','samekh'),('ע','ayin'),('פ','pe'),('צ','tsadi'),('ק','qof'),('ר','resh'),('ש','shin'),('ת','tav')]

# ---------- small parts ----------
def ul(items, cls=''):
    return '<ul%s>' % (f' class="{cls}"' if cls else '') + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ul>'
def paras(ps): return ''.join(f'<p>{e(p)}</p>' for p in ps)
def he(ch, cls='he'): return f'<span class="{cls}" lang="he" dir="rtl">{ch}</span>'
ICON = {
 'pin': '<path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z"/><circle cx="12" cy="9.5" r="2.6"/>',
 'screen': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 'one': '<circle cx="12" cy="8" r="3.6"/><path d="M5 21c.8-4 3.6-6 7-6s6.2 2 7 6"/>',
 'group': '<circle cx="8" cy="9" r="3"/><circle cx="16.5" cy="9.5" r="2.5"/><path d="M2.5 20c.6-3.4 2.8-5 5.5-5s4.9 1.6 5.5 5M13.5 15.3c.9-.4 1.9-.6 3-.6 2.3 0 4.2 1.4 4.8 4.3"/>',
 'note': '<path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>',
 'check': '<path d="M4 12.5l5 5L20 6.5"/>',
}
def icon(k): return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICON[k]}</svg>'
PH = ('<img src="/assets/photo/lee-elle-horowitz.webp" width="750" height="995" alt="Lee-Elle Horowitz: a smiling young woman with long, wavy light-brown hair, in a burgundy knitted top, against a grey background.">')
CREDIT = 'Photo: from the Guildford School of Acting page for its 2026 BA (Hons) Actor Musician graduates, <a href="https://gsauk.org/2026-ba-hons-actor-musician-graduates">gsauk.org</a>, which does not name the photographer. A stand-in until she adds her own.'
PH2 = ('<img src="/assets/photo/lee-elle-horowitz-bass.webp" width="274" height="596" alt="Lee-Elle Horowitz standing with a double bass in front of a black curtain, one hand on her chest.">')
CREDIT2 = 'Still from her showreel on Spotlight, cropped. A stand-in until she adds her own.'
def fig(cls, img=PH, credit=CREDIT): return f'<figure class="{cls}">{img}<figcaption>{credit}</figcaption></figure>'
CTA = '<p class="cta"><span class="btn" role="note">Ask about lessons <span class="soon">Enquiries open soon</span></span></p>'
DRAFT = '<p class="draft" role="note"><strong>Draft.</strong> Lee-Elle Horowitz has not yet approved this site. Nothing here is final.</p>'
CHIPS = '<ul class="chips"><li>' + icon('one') + 'Children, teenagers and adults</li><li>' + icon('pin') + 'In person in London</li><li>' + icon('screen') + 'Online via Zoom</li><li>' + icon('check') + 'Enhanced DBS checked</li></ul>'

DESIGNS = [('alef-bet', 'Alef-bet', 'The page as an alphabet chart: a large Hebrew letter opens each section.', 'א'),
 ('conversation', 'Conversation', 'The page as a conversation: questions a parent asks, and her answers.', '…'),
 ('three-tenses', 'Three tenses', 'Past, present and future, the way she teaches grammar.', '→'),
 ('the-stage', 'The stage', 'A theatre programme, from her acting training: Hebrew first, music in the second half.', '★'),
 ('notebook', 'Notebook', 'A ruled exercise book: one column, plain and printable.', '✎')]

def head(path, title, desc, css, theme):
    url = BASE + path; t = e(title); d = e(desc)
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="theme-color" content="{theme}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{BASE}/assets/share/card-1200x630.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{NAME}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{BASE}/assets/share/card-1200x630.jpg">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="/assets/base.css">
<link rel="stylesheet" href="{css}">
</head>
'''
FAM = '''<details class="family-credit">
  <summary>Sovereign Website</summary>
  <ul>
    <li><a href="/start/">Start here</a></li>
    <li><a href="/agents/">Use with your AI</a></li>
    <li class="family-gap"><a href="/admin/">How this site was made</a></li>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</details>
'''
def foot(cur):
    cur_attr = ' aria-current="page"'
    links = ''.join(f'<li><a href="/designs/{s}/"{cur_attr if s == cur else ""}>{n}</a></li>' for s, n, _, _ in DESIGNS)
    return f'''<footer class="foot">
<p class="foot-name">Lee-Elle Horowitz <span>Private Hebrew tuition, in London and online</span></p>
<nav class="designs" aria-label="Five designs for this site"><p>This draft comes in five designs. <a href="/designs/">Compare them</a>:</p><ul>{links}</ul></nav>
<nav class="site-links" aria-label="About this site">
  <a href="/start/">Start here</a>
  <a href="/agents/">Use with your AI</a>
  <a href="/admin/">How this site was made</a>
  <a href="/policy/">How this site is governed</a>
</nav>
<p class="small">A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="https://github.com/SovereignWebsite/Site__Artist__Lee-Elle-Horowitz">github.com/SovereignWebsite/Site__Artist__Lee-Elle-Horowitz</a>.</p>
</footer>
'''
def page(path, title, desc, css, theme, body, cur, cls):
    return head(path, title, desc, css, theme) + f'<body class="{cls}">\n<a class="skip" href="#main">Skip to content</a>\n' + FAM + body + foot(cur) + '</body>\n</html>\n'
def brand(extra=''):
    return f'<header class="top"><a class="brand" href="/">Lee-Elle Horowitz</a>{extra}</header>\n'

# ---------- 1 Alef-bet ----------
def alef():
    band = '<div class="band" aria-hidden="true"><div class="band-track">' + ''.join(f'<span class="band-l"><span class="band-g" lang="he" dir="rtl">{c}</span><span class="band-n">{n}</span></span>' for c, n in ALEFBET * 2) + '</div></div>'
    def sec(i, title, inner, cls=''):
        c, n = ALEFBET[i]
        return f'<section class="sec {cls}" aria-labelledby="s{i}"><div class="sec-head"><span class="sec-g" lang="he" dir="rtl">{c}</span><span class="sec-n">{n}</span></div><div class="sec-body"><h2 id="s{i}">{e(title)}</h2>{inner}</div></section>'
    tiles = '<ul class="tiles">' + ''.join(f'<li><span class="tile-g" lang="he" dir="rtl">{c}</span><span class="tile-n">{n}</span><span class="tile-t">{e(t)}</span></li>' for (c, n), t in zip(ALEFBET, LESSONS)) + '</ul>'
    stats = '<ul class="stats">' + ''.join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in STATS) + '</ul>'
    fmt = '<ul class="fmt">' + ''.join(f'<li>{icon(k)}<strong>{e(a)}</strong><span>{e(b)}</span></li>' for k, a, b in FORMAT) + '</ul>'
    who = '<ul class="who">' + ''.join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in WHO) + '</ul>'
    return (brand('<nav class="jump" aria-label="On this page"><a href="#s1">Lessons</a><a href="#s3">Background</a><a href="#s5">Music</a></nav>') + '<main id="main">\n' + DRAFT +
      '<section class="hero" aria-labelledby="h1"><div class="hero-text"><p class="eyebrow">Private Hebrew tuition · London and online</p>'
      f'<h1 id="h1">Private Hebrew Tuition <span>with Lee-Elle Horowitz</span></h1><p class="lead">{e(LEAD)}</p>' + CHIPS + CTA + '</div>'
      '<div class="hero-art"><span class="hero-g" lang="he" dir="rtl" aria-hidden="true">א</span>' + fig('arch') + '</div></section>\n' + band + stats +
      sec(0, 'About me', paras(ABOUT) + who) +
      sec(1, 'Hebrew lessons can include', '<p class="hint">Nine starting points, one for each of the first nine letters.</p>' + tiles, 'wide') +
      f'<blockquote class="quote"><p>{e(QUOTE)}</p><footer>Lee-Elle Horowitz</footer></blockquote>' +
      sec(2, 'Teaching approach', f'<p class="big">{e(APPROACH1)}</p>') +
      sec(3, 'Qualifications and background', '<ul class="ticks">' + ''.join(f'<li>{icon("check")}{e(q)}</li>' for q in QUALS) + '</ul>') +
      sec(4, 'Lesson format', fmt) +
      sec(5, 'Music tuition too', '<p>A smaller part of what she teaches.</p>' + '<ul class="music">' + ''.join(f'<li>{icon("note")}{e(m)}</li>' for m in MUSIC) + '</ul>', 'music') +
      '<section class="end" aria-labelledby="end"><span class="end-g" lang="he" dir="rtl" aria-hidden="true">ת</span><h2 id="end">From alef to tav</h2><p>Lessons tailored to each student\'s age, ability and goals.</p>' + CTA + '</section></main>\n')

# ---------- 2 Conversation ----------
def convo():
    def you(t): return f'<li class="msg you"><p>{e(t)}</p></li>'
    n = [0]
    def her(inner, he_lines=3):
        bars = ''.join('<span class="bar"></span>' for _ in range(he_lines))
        c, nm = ALEFBET[n[0]]; n[0] += 1
        return (f'<li class="msg her"><div class="pair"><div class="en"><p class="mk"><span class="mk-g" lang="he" dir="rtl">{c}</span> <span class="mk-n">{nm}</span></p>{inner}</div>'
                f'<div class="hebrew" dir="rtl"><span class="bars" aria-hidden="true">{bars}</span><span class="hl" dir="ltr">Her Hebrew goes here once she has checked it</span></div></div></li>')
    chips = '<ul class="replies">' + ''.join(f'<li>{e(l)}</li>' for l in LESSONS) + '</ul>'
    return ('<header class="chat-top"><a class="brand" href="/">' + PH.replace('<img ', '<img class="ava" ').replace('width="750" height="995"', 'width="48" height="64"').replace(' alt="Lee-Elle Horowitz: a smiling young woman with long, wavy light-brown hair, in a burgundy knitted top, against a grey background."', ' alt=""') +
      '<span><strong>Lee-Elle Horowitz</strong><span class="status">Private Hebrew tuition</span></span></a></header>\n<main id="main">\n' + DRAFT +
      f'<section class="intro" aria-labelledby="h1"><h1 id="h1">{e(TITLE)}</h1><p class="lead">{e(LEAD)} Lessons are a conversation, so this page is one too.</p>' + CHIPS + '</section>'
      '<h2 class="vh">The conversation</h2><ol class="thread">' +
      '<li class="day" aria-hidden="true">Today</li>' +
      you('Hello! Who will be teaching me?') + her(paras(ABOUT[:1]) + fig('inline')) +
      you('What are the lessons like?') + her(paras(ABOUT[1:]), 4) +
      you('What can we work on?') + her('<p>Hebrew lessons can include:</p>' + chips, 4) +
      you('How do you teach?') + her(f'<p>{e(APPROACH)}</p>', 4) +
      you('Can I trust you with my child?') + her(ul(QUALS, 'ticks'), 4) +
      you('Where do we meet?') + her(ul([b for _, _, b in FORMAT]), 3) +
      you('Do you teach music too?') + her('<p>Yes, as a smaller part of what I teach:</p>' + ul(MUSIC), 3) +
      '</ol><p class="note">The right-hand side of each answer stays empty until Lee-Elle has checked any Hebrew before it goes live.</p>'
      '<div class="compose"><span class="field">Ask about lessons…</span>' + CTA + '</div></main>\n')

# ---------- 3 Three tenses ----------
def tenses():
    journey = '<ol class="journey">' + ''.join(f'<li><span class="dot" aria-hidden="true"></span><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in JOURNEY) + '</ol>'
    grid = '<ul class="lgrid">' + ''.join(f'<li>{e(t)}</li>' for t in LESSONS) + '</ul>'
    fmt = '<ul class="fmt">' + ''.join(f'<li>{icon(k)}<span>{e(b)}</span></li>' for k, _, b in FORMAT) + '</ul>'
    return (brand() + '<main id="main">\n' + DRAFT +
      f'<section class="hero" aria-labelledby="h1"><p class="eyebrow">Private Hebrew tuition</p><h1 id="h1">{e(TITLE)}</h1>'
      '<p class="conj" aria-hidden="true"><span class="p">was</span><span class="n">is</span><span class="f">will be</span></p>'
      f'<p class="lead">{e(LEAD)} Past, present and future: the three tenses she teaches, and the three parts of this page.</p>' + CHIPS + CTA + '</section>'
      '<nav class="tabs" aria-label="The three tenses"><a href="#past" class="p">Past</a><a href="#present" class="n">Present</a><a href="#future" class="f">Future</a></nav>'
      '<section id="past" class="tense past" aria-labelledby="past-h"><p class="t-label">Past <span class="t-he" lang="he" dir="rtl">א</span></p><h2 id="past-h">Where I come from</h2><div class="split">' + fig('photo') +
      '<div>' + paras(ABOUT[:1]) + journey + '</div></div></section>'
      '<section id="present" class="tense present" aria-labelledby="present-h"><p class="t-label">Present <span class="t-he" lang="he" dir="rtl">ב</span></p><h2 id="present-h">Lessons today</h2>' + paras(ABOUT[1:]) +
      '<h3>Hebrew lessons can include</h3>' + grid + f'<h3>Teaching approach</h3><p>{e(APPROACH1)}</p><h3>Lesson format</h3>' + fmt +
      '<h3>Qualifications and background</h3>' + ul(QUALS, 'ticks') +
      '<div class="music"><h3>Music tuition too</h3><p>A smaller part of what I teach.</p>' + ul(MUSIC) + '</div></section>'
      f'<section id="future" class="tense future" aria-labelledby="future-h"><p class="t-label">Future <span class="t-he" lang="he" dir="rtl">ג</span></p><h2 id="future-h">Where you want to get to</h2><p class="big">{e(QUOTE)}</p>' + CTA + '</section></main>\n')

# ---------- 4 The stage ----------
def stage():
    return ('<main id="main">\n<div class="curtain l" aria-hidden="true"></div><div class="curtain r" aria-hidden="true"></div>\n' + DRAFT +
      '<section class="cover" aria-labelledby="h1"><p class="presents">Lee-Elle Horowitz presents</p>'
      '<div class="marquee"><h1 id="h1">Private Hebrew Tuition</h1><p class="with">with Lee-Elle Horowitz</p></div>'
      f'<p class="lead">{e(LEAD)}</p>' + CHIPS + CTA + '<div class="spot">' + fig('portrait') + '</div></section>\n'
      '<section class="act" aria-labelledby="a1"><p class="act-n">Act one <span class="act-he" lang="he" dir="rtl">א</span></p><h2 id="a1">Hebrew lessons</h2>'
      '<h3>Hebrew lessons can include</h3><ol class="scenes">' + ''.join(f'<li><span><span lang="he" dir="rtl">{c}</span> Scene {i+1}</span>{e(t)}</li>' for i, ((c, _), t) in enumerate(zip(ALEFBET, LESSONS))) + '</ol>' + paras(ABOUT) +
      f'<h3>Teaching approach</h3><p>{e(APPROACH)}</p><h3>Lesson format</h3>' + ul([b for _, _, b in FORMAT]) + '</section>'
      '<p class="interval" role="separator">Interval</p>'
      '<section class="act two" aria-labelledby="a2"><p class="act-n">Act two <span class="act-he" lang="he" dir="rtl">ב</span></p><h2 id="a2">Music and audition preparation</h2><p>A smaller part of what she teaches.</p><div class="split">' +
      fig('still', PH2, CREDIT2) + ul(MUSIC, 'notes') + '</div></section>'
      '<section class="act bio" aria-labelledby="a3"><p class="act-n">Curtain call <span class="act-he" lang="he" dir="rtl">ג</span></p><h2 id="a3">About the teacher</h2>' + ul(QUALS) +
      '<h3>On stage</h3><p class="from">From her Spotlight profile.</p>' + ul(STAGE) +
      f'<p><a class="reel" href="{SHOWREELS}" rel="noopener">Watch her showreels on Spotlight</a> <span class="ext">(opens Spotlight, another website)</span></p></section>'
      '<section class="ticket" aria-labelledby="tk"><h2 id="tk">Admit one</h2><p>Lessons tailored to each student\'s age, ability and goals.</p>' + CTA + '</section></main>\n')

# ---------- 5 Notebook ----------
def notebook():
    return ('<main id="main">\n' + DRAFT +
      '<div class="book"><div class="cover"><p class="label-k">Exercise book</p>'
      '<dl class="label"><div><dt>Name</dt><dd>Lee-Elle Horowitz</dd></div><div><dt>Subject</dt><dd>Hebrew</dd></div><div><dt>Also</dt><dd>Music</dd></div></dl><p class="cover-ab" aria-hidden="true">' + ' '.join(f'<span lang="he" dir="rtl">{c}</span>' for c, _ in ALEFBET) + '</p></div>'
      f'<section class="page" aria-labelledby="h1"><h1 id="h1">{e(TITLE)}</h1><p class="lead"><mark>{e(LEAD)}</mark></p>' + CHIPS + CTA + fig('polaroid') +
      '<h2>About me</h2>' + paras(ABOUT) + '<h2>Hebrew lessons can include</h2><ol class="ex">' + ''.join(f'<li><span class="ex-g" lang="he" dir="rtl">{c}</span> {e(t)}</li>' for (c, _), t in zip(ALEFBET, LESSONS)) + '</ol>'
      f'<h2>Teaching approach</h2><p>{e(APPROACH1)}</p><p><mark>{e(QUOTE)}</mark></p>'
      '<h2>Qualifications and background</h2>' + ul(QUALS, 'ticks') + '<h2>Lesson format</h2>' + ul([b for _, _, b in FORMAT]) +
      '<h2>Music tuition too</h2><p>A smaller part of what I teach.</p>' + ul(MUSIC) +
      '<div class="sticky" role="note"><p>Ask about lessons</p><p class="soon">Enquiries open soon</p></div></section></div></main>\n')


REPO = 'https://github.com/SovereignWebsite/Site__Artist__Lee-Elle-Horowitz'
def start():
    picks = ''.join(f'<li class="pc pc-{s}"><a href="/designs/{s}/"><span class="pc-mark" aria-hidden="true">{g}</span><strong>{i+1}. {e(n)}</strong><span>{e(b)}</span></a></li>' for i, (s, n, b, g) in enumerate(DESIGNS))
    step = lambda n, title, inner: f'<section class="step" aria-labelledby="st{n}"><p class="step-n" aria-hidden="true">{n}</p><div><h2 id="st{n}">{title}</h2>{inner}</div></section>'
    return (brand() + '<main id="main">\n<p class="eyebrow">Start here · for Lee-Elle</p><h1>Your website, and what happens next</h1>'
      '<p class="lead">This is a first draft of a website for your Hebrew tuition. Every word on it comes from the text you supplied, and nothing is final until you say so. Here is how to shape it.</p>'
      + step(1, 'Choose a design', '<p>The same words, in five different pages. Open each one on your phone, then say which you like best, or which parts of which.</p>'
        f'<ol class="picker">{picks}</ol>')
      + step(2, 'Check the words, and the Hebrew', '<p>Read your text on the page and tell us anything to change. Your own words are kept as you wrote them.</p>'
        '<p>The pages use only single Hebrew letters for now. A wrong Hebrew word on a Hebrew tutor\'s site would cost trust, so no Hebrew words go up until you have checked them. If you would like some, for example your name in Hebrew or a phrase for the Conversation design, send them and they will be added exactly as you write them.</p>')
      + step(3, 'Send photos, text and changes', '<p>For now, send them to Dinis, who set this site up. A form on this site for sending changes and photos is on its way.</p>'
        '<ul><li><strong>Photos.</strong> The photos on the drafts are stand-ins, to show what the pages can look like. Send your own, and for each one say who took it, so it can be credited.</li>'
        '<li><strong>Contact details.</strong> None are shown. Say which, if any, you want visitors to see. Until then, the button on each page says <q>Enquiries open soon</q>.</li>'
        '<li><strong>Prices.</strong> None are shown, and none will be unless you give them.</li></ul>')
      + step(4, 'Approve it', '<p>When you are happy, say so. The <q>Draft</q> notice comes off and the site is yours to share.</p>')
      + step(5, 'Who looks after the site', '<p>A dedicated site agent, b.site.lee-elle-horowitz, builds and keeps this site, working with the Sovereign Website design agents. Its notes on what it has done and what is open are public: '
        f'<a href="{REPO}/tree/dev/site/factory/dinis-cruz/account-b">the keeper\'s notes</a>.</p>')
      + '<section class="later" aria-labelledby="later"><h2 id="later">Later: changing it yourself</h2>'
        '<p>You never have to, but you can. The whole site is a set of plain files in one place on GitHub that you will own: '
        f'<a href="{REPO}">{REPO.replace("https://", "")}</a>. No server, no cookies, no tracking, and you can move it anywhere.</p>'
        '<details><summary>Connect GitHub</summary><ol>'
        '<li>Make a GitHub account at <a href="https://github.com/signup">github.com/signup</a>, if you do not have one.</li>'
        '<li>Send your GitHub login to Dinis. You get two invitations: one to your site, with permission to change it, and one to join the SovereignWebsite organisation as a member. Membership gives you no access to anything else; it lets your own Claude work with your site.</li>'
        f'<li>Accept the first: signed in to GitHub, open <a href="{REPO}">your site\'s page on GitHub</a> and press <strong>View invitation</strong> on the banner, or use the link in the email.</li>'
        '<li>Accept the second at <a href="https://github.com/orgs/SovereignWebsite/invitation">github.com/orgs/SovereignWebsite/invitation</a> ("Join SovereignWebsite"). Use this address: the link in the email may not offer the button.</li>'
        '<li>If you use Claude, open its GitHub settings and press <strong>Check again</strong> next to SovereignWebsite.</li></ol></details>'
        '<details><summary>Make a change on GitHub</summary><ol>'
        f'<li>Open <a href="{REPO}/tree/dev/site">the site\'s folder</a> and pick the page (the home page is <code>index.html</code>).</li>'
        '<li>Press the pencil, change the words, then press <strong>Commit changes</strong>.</li>'
        '<li>The site updates by itself in a minute or two.</li></ol></details>'
        '<details><summary>Let your own Claude make changes</summary>'
        f'<p>Give it <a href="{REPO}/blob/dev/docs/prompt-for-your-claude.md">this prompt</a>. It tells your Claude the rules this site keeps. See also <a href="/agents/">Use with your AI</a>.</p></details>'
        '<details><summary>Ask for another pass</summary>'
        f'<p>Tell Dinis, or <a href="{REPO}/issues/new">open an issue</a> saying what you would like changed. The site\'s agents work from that record.</p></details>'
        '</section></main>\n')

FN = {'alef-bet': alef, 'conversation': convo, 'three-tenses': tenses, 'the-stage': stage, 'notebook': notebook}
THEME = {'alef-bet': '#f6efe3', 'conversation': '#eef1f5', 'three-tenses': '#faf8f4', 'the-stage': '#14090b', 'notebook': '#fdfcf7'}

def main():
    for slug, n, blurb, _ in DESIGNS:
        p = f'/designs/{slug}/'
        w(f'designs/{slug}/index.html', page(p, f'{n}: {NAME}', DESC + ' ' + blurb, f'/assets/{slug}.css', THEME[slug], FN[slug](), slug, 'd-' + slug))
    w('index.html', page('/', NAME, DESC, f'/assets/{HOME}.css', THEME[HOME], FN[HOME](), HOME, 'd-' + HOME))
    cards = ''.join(f'<li class="pc pc-{s}"><a href="/designs/{s}/"><span class="pc-mark" aria-hidden="true">{g}</span><strong>{i+1}. {e(n)}</strong><span>{e(b)}</span></a></li>' for i, (s, n, b, g) in enumerate(DESIGNS))
    body = (brand() + '<main id="main">\n' + DRAFT + '<p class="eyebrow">For Lee-Elle</p><h1>Choose a design</h1>'
      '<p class="lead">The same words, five different pages. Open each one on your phone, then say which you like best, or which parts of which.</p>'
      f'<ol class="picker">{cards}</ol></main>\n')
    w('designs/index.html', page('/designs/', 'Choose a design: ' + NAME, 'Five designs for this site, built from the same words.', '/assets/picker.css', '#f6efe3', body, '', 'd-picker'))

def build_start():
    w('start/index.html', page('/start/', 'Start here: ' + NAME, 'For Lee-Elle: how to choose a design, send changes and photos, and approve the site.', '/assets/picker.css', '#f6efe3', start(), '', 'd-start'))

if __name__ == '__main__':
    build_start()
    main()
