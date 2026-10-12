"""
Static site generator for ramtintotonchi.com. Run:  python3 _build/build.py
Reads _build/content.py and the media metadata, writes plain HTML to the repo root.
Nothing in _build/ is needed at runtime.
"""
import html, json, pathlib, re, sys
from PIL import Image, ImageFilter, ImageEnhance

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_build"))
import content as C

MEDIA = json.loads((ROOT / "assets/media/media.json").read_text())
IMAGES = json.loads((ROOT / "assets/img/work/images.json").read_text())
PROJECTS = C.P
FEATURED = [p for p in PROJECTS if p["featured"]]
SITE = "https://ramtintotonchi.com"
TITLE = "Ramtin Totonchi — Social Creative & Strategy Lead"
DESC = ("Ramtin Totonchi, London-based social creative and strategy lead: social-first campaigns and creative direction "
        "for Google Cloud, Riot Games, G2 Esports and more.")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&amp;'
         'family=Space+Grotesk:wght@300;400;500;600&amp;display=swap" rel="stylesheet">')
VER = "28"  # bump to bust caches for CSS/JS


def e(s):
    s = str(s)
    s = re.sub(r"(?<=\w)'(?=\w)", "\u2019", s)               # don't, Ramtin's
    s = re.sub(r"(?<=s)'(?=[\s,.;:)!?]|$)", "\u2019", s)       # players'
    s = re.sub(r"(?<=\s)'(?=\d)", "\u2019", s)                # '26
    return html.escape(s, quote=True)


# ------------------------------------------------------------------ media helpers
def dims(kind, name):
    if kind == "v":
        m = MEDIA[name]; return m["w"], m["h"]
    m = IMAGES[name]; return m["w"], m["h"]


def figure(item, p, eager=False):
    kind, name, cap = item
    if (kind == "v" and name not in MEDIA) or (kind == "i" and name not in IMAGES):
        return ""
    w, h = dims(kind, name)
    ar = w / h
    shape = "portrait" if ar < 0.9 else ("square" if ar < 1.15 else "landscape")
    if kind == "v":
        m = MEDIA[name]
        mins, secs = divmod(m["dur"], 60)
        inner = (f'<video controls playsinline preload="none" {"poster" if eager else "data-poster"}="{p}assets/media/{name}.webp" width="{w}" height="{h}" '
                 f'aria-label="{e(cap)}"><source src="{p}assets/media/{name}.mp4" type="video/mp4"></video>')
        meta = f'<span class="m-dur">{mins}:{secs:02d}</span>'
    else:
        shot = name.endswith("tweet") or name.startswith("luminary") or name in ("origin-ksi-comment", "admission-form", "g2-adidas-lockup", "montage-fortnite", "montage-gow3")
        lazy = "" if eager else 'loading="lazy" '
        inner = (f'<img src="{p}assets/img/work/{name}.webp" alt="{e(cap)}" width="{w}" height="{h}" '
                 f'{lazy}decoding="async">')
        meta = ""
        if shot:
            shape += " is-shot"
            return (f'<figure class="m m--{shape}" style="--ar:{ar:.4f};--maxw:{w}px"><div class="m-frame">{inner}</div>'
                    f'<figcaption>{e(cap)}</figcaption></figure>')
    return (f'<figure class="m m--{shape}" style="--ar:{ar:.4f}"><div class="m-frame">{inner}</div>'
            f'<figcaption>{e(cap)}{meta}</figcaption></figure>')


def media_row(items, p, cls="", eager=False):
    items = [i for i in items if (i[0] == "v" and i[1] in MEDIA) or (i[0] == "i" and i[1] in IMAGES)]
    if not items: return ""
    if all(dims(k, n)[0] / dims(k, n)[1] < 1.15 for k, n, *_ in items):
        cls += " is-portraits"
    cls += f" n{len(items)}"
    return f'<div class="media-row {cls}">' + "".join(figure(i, p, eager) for i in items) + "</div>"


# ------------------------------------------------------------------ thumbnails
def _load(k, n):
    return Image.open(ROOT / ("assets/media" if k == "v" else "assets/img/work") / f"{n}.webp").convert("RGB")


def _cover(im, w, h):
    r = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    l = (im.width - w) // 2; t = (im.height - h) // 2
    return im.crop((l, t, l + w, t + h))


def _contain_on_blur(im, w, h):
    bg = ImageEnhance.Brightness(_cover(im, w, h).filter(ImageFilter.GaussianBlur(36))).enhance(0.55)
    r = min(w / im.width, h / im.height)
    fg = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    bg.paste(fg, ((w - fg.width) // 2, (h - fg.height) // 2))
    return bg


def _source(spec):
    kind = spec[0]
    if kind == "frame":
        import subprocess, tempfile
        tmp = tempfile.mktemp(suffix=".png")
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(spec[2]), "-i", str(ROOT / "assets/media" / f"{spec[1]}.mp4"),
                        "-frames:v", "1", tmp], check=True)
        return Image.open(tmp).convert("RGB")
    return _load(kind, spec[1])


def _composite(spec, W, H):
    from PIL import ImageDraw
    names = spec[1]
    light = spec[0] == "composite-light"
    ims = [_load("v" if n in MEDIA else "i", n) for n in names]
    if light:
        canvas = Image.new("RGB", (W, H), (233, 228, 218))
    else:
        canvas = ImageEnhance.Brightness(_cover(ims[0], W, H).filter(ImageFilter.GaussianBlur(40))).enhance(0.45)
    gap = round(W * 0.0225); pad = round(H * 0.07)
    avail_h = H - 2 * pad
    widths = [round(avail_h * im.width / im.height) for im in ims]
    total = sum(widths) + gap * (len(ims) - 1)
    if total > W - 2 * pad:
        sc = (W - 2 * pad) / total; avail_h = round(avail_h * sc); widths = [round(w * sc) for w in widths]
        total = sum(widths) + gap * (len(ims) - 1)
    x = (W - total) // 2; y = (H - avail_h) // 2
    for im, w in zip(ims, widths):
        tile = im.resize((w, avail_h), Image.LANCZOS)
        mask = Image.new("L", tile.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, avail_h - 1), radius=round(H * 0.018), fill=255)
        canvas.paste(tile, (x, y), mask); x += w + gap
    return canvas


def _grid(spec, W, H):
    """2x2 collage of video stills / images on a dark ground, for projects that are a slate of pieces."""
    from PIL import ImageDraw
    names = spec[1]
    ims = [_load("v" if n in MEDIA else "i", n) for n in names]
    pad = round(H * 0.03); gap = round(H * 0.02)
    cw = (W - 2 * pad - gap) // 2; ch = (H - 2 * pad - gap) // 2
    canvas = Image.new("RGB", (W, H), (18, 18, 18))
    for i, im in enumerate(ims[:4]):
        tile = _cover(im, cw, ch)
        mask = Image.new("L", tile.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, cw - 1, ch - 1), radius=round(H * 0.014), fill=255)
        canvas.paste(tile, (pad + (i % 2) * (cw + gap), pad + (i // 2) * (ch + gap)), mask)
    return canvas


def make_thumb(proj):
    """Card thumbnail (1920x1200) and case-study hero (1920x1080) for a project."""
    for folder, (W, H), spec in (("thumbs", (1920, 1200), proj["thumb"]), ("hero", (1920, 1080), proj.get("hero", proj["thumb"]))):
        out = ROOT / "assets/img" / folder / f"{proj['slug']}.webp"
        out.parent.mkdir(parents=True, exist_ok=True)
        if spec[0].startswith("composite"):
            canvas = _composite(spec, W, H)
        elif spec[0] == "grid":
            canvas = _grid(spec, W, H)
        else:
            src = _source(spec)
            ar = src.width / src.height
            # Video frames often carry on-screen text: never crop them for a card, letterbox on a blur instead.
            if spec[0] in ("v", "frame") and abs(ar - W / H) > (0.05 if folder == "thumbs" else 0.15):
                canvas = _contain_on_blur(src, W, H)
            else:
                canvas = _cover(src, W, H)
        canvas.save(out, "WEBP", quality=80, method=6)


# ------------------------------------------------------------------ chrome
def head(title, desc, p, page="", body_class="", noindex=False, canonical="", og="assets/img/og/site.jpg", og_alt="Selected work by Ramtin Totonchi"):
    return f"""<!doctype html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{SITE}/{canonical}">'}
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ramtin Totonchi">
<meta property="og:url" content="{SITE}/{canonical}">
<meta property="og:image" content="{SITE}/{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/{og}">
<meta name="theme-color" content="#f3f1ec">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{p}assets/css/styles.css?v={VER}">
<script src="{p}assets/js/main.js?v={VER}" defer></script>
</head>
<body class="{body_class}" data-page="{page}">
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(p, current=""):
    def cur(n): return ' aria-current="page"' if n == current else ""
    return f"""<header class="site-header">
  <a class="wordmark" href="{p}index.html"><span>Ramtin</span> <span>Totonchi</span></a>
  <nav class="site-nav" aria-label="Main">
    <ul>
      <li><a href="{p}work.html"{cur('work')}>Work <sup>{len(PROJECTS):02d}</sup></a></li>
      <li><a href="{p}about.html"{cur('about')}>About</a></li>
      <li><a href="{p}contact.html"{cur('contact')}>Contact</a></li>
    </ul>
  </nav>
  <p class="locale"><span>London</span><time data-clock>--:--:--</time></p>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu"><span class="menu-label">Menu</span><span class="bars" aria-hidden="true"></span></button>
</header>
<div class="mobile-menu" id="mobile-menu">
  <nav aria-label="Mobile">
    <ul>
      <li><a href="{p}index.html"{cur('home')}>Home</a></li>
      <li><a href="{p}work.html"{cur('work')}>Work <sup>{len(PROJECTS):02d}</sup></a></li>
      <li><a href="{p}about.html"{cur('about')}>About</a></li>
      <li><a href="{p}contact.html"{cur('contact')}>Contact</a></li>
    </ul>
  </nav>
  <div class="mobile-menu__foot"><span>London · <time data-clock>--:--:--</time></span><a href="{p}contact.html">Get in touch →</a></div>
</div>
"""


def footer(p):
    li = f'<li><a class="link" href="{e(C.LINKEDIN)}" rel="me">LinkedIn</a></li>' if C.LINKEDIN else ""
    return f"""<footer class="site-footer">
  <p class="copy">© <span data-year>2026</span> Ramtin Totonchi</p>
  <ul class="social">
    <li><a class="link" href="{p}contact.html">Contact</a></li>
    {li}
  </ul>
  <a class="top link" href="#main">Back to top ↑</a>
</footer>
</body>
</html>
"""


# ------------------------------------------------------------------ cards
def thumb(proj, p):
    return f"{p}assets/img/thumbs/{proj['slug']}.webp"


def carousel_card(proj, i):
    return f"""      <li class="card" data-title="{e(proj['title'])}">
        <a href="work/{proj['slug']}.html" draggable="false">
          <figure>
            <img src="{thumb(proj, '')}" alt="" width="1920" height="1200" loading="{'eager' if i < 3 or i > len(FEATURED) - 3 else 'lazy'}" decoding="async" draggable="false">
            <span class="card-quote" aria-hidden="true">{e(proj['quote'])}</span>
          </figure>
          <span class="card-meta"><span>{e(proj['title'])}</span><span>{e(proj['client'].split(' · ')[0])}</span></span>
        </a>
      </li>"""


FILTERS = [("all", "All"), ("google-cloud", "Google Cloud"), ("valorant", "VALORANT Esports"), ("g2", "G2 Esports"), ("creator", "Creator")]


def group_of(proj):
    c = proj["client"]
    if "Google Cloud" in c: return "google-cloud"
    if "Riot" in c: return "valorant"
    if "G2" in c: return "g2"
    return "creator"


def work_card(proj, p):
    return f"""    <li class="work-card reveal" data-group="{group_of(proj)}">
      <a href="{p}work/{proj['slug']}.html">
        <div class="work-card__top"><span>{e(proj['year'] or proj['via'])}</span><span>{e(proj['cat'])}</span></div>
        <figure><img src="{thumb(proj, p)}" alt="" width="1920" height="1200" loading="lazy" decoding="async"></figure>
        <div class="work-card__bottom"><h2 class="work-card__title">{e(proj['title'])}</h2><span class="work-card__client">{e(proj['client'])}<br><span class="muted">{e(proj['via'])}</span></span></div>
        <p class="work-card__line">{e(proj['line'])}</p>
      </a>
    </li>"""


def work_row(proj, p):
    return f"""    <li class="xp-row" data-preview="{thumb(proj, p)}" data-group="{group_of(proj)}">
      <a href="{p}work/{proj['slug']}.html">
        <span class="c1">{e(proj['title'])}</span><span class="c2">{e(proj['client'])} · {e(proj['via'])}</span><span class="c3">{e(proj['year'] or '')}</span><span class="c4" aria-hidden="true">→</span>
      </a>
    </li>"""


# ------------------------------------------------------------------ pages
def build_home():
    n = len(FEATURED)
    out = head(TITLE, DESC, "", "home", "home") + header("", "home") + f"""<main id="main" class="home-main">
  <h1 class="visually-hidden">Ramtin Totonchi, social creative and strategy lead</h1>
  <p class="intro split-words">{e(C.HOME_INTRO)}</p>

  <section class="stage" data-carousel tabindex="0" aria-roledescription="carousel" aria-label="Selected work. Use the arrow keys to move between projects.">
    <ul class="ring">
{chr(10).join(carousel_card(pr, i) for i, pr in enumerate(FEATURED))}
    </ul>
    <p class="visually-hidden" aria-live="polite" data-carousel-live></p>
  </section>
  <div class="counter counter--now" aria-hidden="true"></div>
  <div class="counter counter--total" aria-hidden="true">/{n:02d}</div>

  <div class="home-bar">
    <div class="toggle-group" role="group" aria-label="View">
      <button class="toggle" type="button" data-view="carousel" aria-pressed="true">Carousel</button>
      <button class="toggle" type="button" data-view="grid" aria-pressed="false">Grid</button>
    </div>
    <p class="section-name"><a class="link" href="work.html">All {len(PROJECTS)} projects →</a></p>
    <div class="hint">
      <span class="hint-text">Drag, scroll or use the arrows</span>
      <button class="step-btn" type="button" data-step="-1" aria-label="Previous project"><span aria-hidden="true">←</span></button>
      <button class="step-btn" type="button" data-step="1" aria-label="Next project"><span aria-hidden="true">→</span></button>
    </div>
  </div>
</main>
</body>
</html>
"""
    (ROOT / "index.html").write_text(out)


GROUPS = [("Jellyfish", "At Jellyfish, on the Google Cloud account"), ("Edelman", "At Edelman, on the Riot Games account"),
          ("Riot", "Riot Games, VALORANT Esports EMEA"), ("G2", "G2 Esports"), ("Self", "Independent")]


def build_work():
    out = head("Work — Ramtin Totonchi", "Case studies: Google Cloud (at Jellyfish), Riot Games and VALORANT Esports, G2 Esports, and more.", "", "work", canonical="work.html") + header("", "work") + f"""<main id="main" class="page-top">
  <section class="grid-12 work-index">
    <div class="index-head">
      <h1>Work<sup>{len(PROJECTS):02d}</sup></h1>
      <div class="index-controls">
        <div class="toggle-group filter-group" role="group" aria-label="Filter by client">
          {"".join(f'<button class="toggle" type="button" data-filter="{k}" aria-pressed="{str(k == 'all').lower()}">{lbl}<sup>{sum(1 for pr in PROJECTS if k == "all" or group_of(pr) == k)}</sup></button>' for k, lbl in FILTERS)}
        </div>
        <div class="toggle-group" role="group" aria-label="Layout">
          <button class="toggle" type="button" data-layout="grid" aria-pressed="true">Grid</button>
          <button class="toggle" type="button" data-layout="list" aria-pressed="false">List</button>
        </div>
      </div>
      <p class="visually-hidden" aria-live="polite" data-filter-status></p>
    </div>
    <ul class="work-grid">
{chr(10).join(work_card(pr, '') for pr in PROJECTS)}
    </ul>
    <ul class="work-list xp">
{chr(10).join(work_row(pr, '') for pr in PROJECTS)}
    </ul>
  </section>
</main>
""" + footer("")
    (ROOT / "work.html").write_text(out)


def acct_period(pd):
    tiles = "".join(f'<div class="stat reveal" data-delay="{j % 3}"><p class="stat__n">{e(n)}</p><p class="stat__l">{e(l)}</p><p class="stat__d">{e(d)}</p></div>'
                    for j, (n, l, d) in enumerate(pd["stats"]))
    return (f'<div class="acct-period">'
            f'<div class="cs-results acct-grid">{tiles}</div><p class="cs-note">{e(pd["note"])}</p></div>')


def build_about():
    stats = []
    for i, (n, suf, label) in enumerate(C.STATS):
        if n == 2021:
            num = '<span>2021</span>'
        else:
            num = f'<span data-count="{n}" data-suffix="{suf}">{n:,}{suf}</span>'
        stats.append(f'<div class="stat reveal" data-delay="{i}"><p class="stat__n">{num}</p><p class="stat__l">{e(label)}</p></div>')
    xp = "\n".join(f'      <li class="xp-row" data-preview="assets/media/{img}.webp"><div><span class="c1">{e(c)}</span><span class="c2">{e(r)}</span><span class="c3">{e(y)}</span></div></li>' for c, r, y, img in C.EXPERIENCE)
    body = "\n".join(f'        <p class="reveal">{e(t)}</p>' for t in C.ABOUT_BODY)
    brands = "".join(f"<li>{e(b)}</li>" for b in C.BRANDS)
    marquee = '<div class="marquee__group">' + "".join(f'<span class="wm wm--{i % 5}">{e(b)}</span>' for i, b in enumerate(C.BRANDS)) + "</div>"
    out = head("About — Ramtin Totonchi", DESC, "", "about", canonical="about.html", og="assets/img/og/about.jpg", og_alt="Ramtin Totonchi in the VCT EMEA studio") + header("", "about") + f"""<main id="main">
  <section class="split-hero split-hero--scroll" data-dark aria-label="Introduction">
    <div class="split-hero__sticky">
      <h1 class="visually-hidden">About Ramtin Totonchi</h1>
      <span class="split-hero__word split-hero__word--l" aria-hidden="true">About</span>
      <div class="split-hero__media split-hero__media--portrait"><img src="assets/img/work/ramtin-portrait.webp" alt="Ramtin Totonchi in the VCT EMEA studio" width="{IMAGES['ramtin-portrait']['w']}" height="{IMAGES['ramtin-portrait']['h']}"></div>
      <span class="split-hero__word split-hero__word--r" aria-hidden="true">Ramtin</span>
    </div>
  </section>

  <section class="section grid-12 statement" aria-labelledby="about-h">
    <div class="section-head"><h2 class="label" id="about-h">About</h2></div>
    <div class="section-body">
      <p class="lede reveal">{e(C.ABOUT_LEDE)}</p>
      <div class="body">
{body}
      </div>
      <p class="reveal about-cta"><a class="btn" href="contact.html">Get in touch <span class="arrow" aria-hidden="true">→</span></a> <a class="link" href="work.html">See the work →</a></p>
    </div>
  </section>

  <section class="section grid-12" aria-labelledby="approach-h">
    <div class="section-head"><h2 class="label" id="approach-h">How I work</h2></div>
    <div class="section-body">
      <p class="scroll-lit">Start with the audience, not the asset.<br>Find the cultural tension worth exploring. Build one big idea that travels across markets and platforms, then make it feel native to each. Measure what matters, learn what resonates, and make the next idea even stronger.</p>
    </div>
  </section>

  <section class="section section--tight grid-12" aria-labelledby="numbers-h">
    <div class="section-head section-head--full"><h2 class="label" id="numbers-h">In numbers</h2></div>
    <div class="stats">
      {''.join(stats)}
    </div>
  </section>

  <section class="section section--tight grid-12" aria-labelledby="acct-h">
    <div class="section-head"><h2 class="label label--accent" id="acct-h">{e(C.ACCOUNT_RESULTS['title'])}</h2></div>
    <div class="section-body">
      <p class="acct-intro reveal">{e(C.ACCOUNT_RESULTS['intro'])}</p>
      {''.join(acct_period(pd) for pd in C.ACCOUNT_RESULTS['periods'])}
    </div>
  </section>

  <section class="section section--tight grid-12" aria-labelledby="xp-h">
    <div class="section-head section-head--full"><h2 class="label" id="xp-h">Experience</h2></div>
    <ul class="xp">
{xp}
    </ul>
  </section>

  <section class="section section--tight section--label grid-12" aria-labelledby="brands-h">
    <div class="section-head section-head--full"><h2 class="label" id="brands-h">Brands I’ve worked with</h2></div>
  </section>
  <div class="marquee">
    <ul class="visually-hidden">{brands}</ul>
    <div class="marquee__track" aria-hidden="true">{marquee}{marquee}</div>
  </div>
  <div class="marquee-gap"></div>
</main>
""" + footer("")
    (ROOT / "about.html").write_text(out)


def build_contact():
    li = f'<a class="link" href="{e(C.LINKEDIN)}">LinkedIn →</a>' if C.LINKEDIN else ""
    out = head("Contact — Ramtin Totonchi", "Get in touch with Ramtin Totonchi about senior social and creative leadership roles or projects.", "", "contact", canonical="contact.html") + header("", "contact") + f"""<main id="main">
  <section class="say-hello" data-dark aria-labelledby="contact-h">
    <h1 class="say-hello__title split-words" id="contact-h">Say Hello</h1>
  </section>

  <section class="section grid-12" aria-labelledby="contact-copy-h">
    <div class="section-head"><h2 class="label" id="contact-copy-h">Contact</h2></div>
    <div class="section-body">
      <p class="contact-copy reveal">I’m interested in ambitious teams, creative challenges, and work that makes people pay attention. If you’re looking for someone who connects strategy, culture and creativity to create work that cuts through, let’s talk.</p>
      <div class="contact-direct reveal">{li}</div>
      <form class="form" action="https://formspree.io/f/xyekjory" method="POST" data-formspree novalidate>
        <input type="hidden" name="_subject" value="New message from ramtintotonchi.com">
        <div class="hp" aria-hidden="true"><label for="f-gotcha">Leave this empty</label><input id="f-gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>
        <div class="field"><label for="f-first">First name</label><input id="f-first" name="first_name" autocomplete="given-name" required aria-describedby="e-first_name" data-fs-field><span class="field-error" id="e-first_name" data-error-for="first_name"></span></div>
        <div class="field"><label for="f-last">Last name <span class="opt">(optional)</span></label><input id="f-last" name="last_name" autocomplete="family-name"></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required aria-describedby="e-email" data-fs-field><span class="field-error" id="e-email" data-error-for="email"></span></div>
        <div class="field"><label for="f-topic">What’s it about?</label>
          <select id="f-topic" name="topic">
            <option>A full-time role</option>
            <option>Social strategy</option>
            <option>Creative direction</option>
            <option>Something else</option>
          </select></div>
        <div class="field field--full"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required minlength="10" placeholder="A few lines is plenty." aria-describedby="e-message" data-fs-field></textarea><span class="field-error" id="e-message" data-error-for="message"></span></div>
        <p class="form-status" role="status" aria-live="polite"></p>
        <button class="btn" type="submit"><span class="btn-label">Send</span> <span class="arrow" aria-hidden="true">→</span></button>
      </form>
      <div class="form-success" tabindex="-1" hidden>
        <p class="form-success__title">Thanks, your message is on its way.</p>
        <p>I’ll get back to you at the email you gave, usually within a couple of working days.</p>
        <button class="link" type="button" data-form-reset>Send another message →</button>
      </div>
    </div>
  </section>
</main>
""" + footer("")
    (ROOT / "contact.html").write_text(out)


def paras(blocks):
    out = []
    for b in blocks or []:
        if isinstance(b, tuple) and b[0] == "list":
            out.append('<ul class="cs-bullets">' + "".join(f"<li>{x}</li>" for x in b[1]) + "</ul>")
        elif isinstance(b, tuple) and b[0] == "h":
            out.append(f'<h3 class="cs-sub">{e(b[1])}</h3>')
        elif isinstance(b, tuple) and b[0] == "steps":
            out.append('<ol class="cs-steps">' + "".join(f'<li><strong>{e(t)}</strong><span>{e(d)}</span></li>' for t, d in b[1]) + "</ol>")
        else:
            out.append(f"<p>{e(b)}</p>")
    return "\n".join(out)


def creator_charts():
    d = json.loads((ROOT / "_build/creator-data.json").read_text())
    f, v = d["followers"], d["viewers"]
    W, H = 600, 220
    fmax = 60000
    pts = " ".join(f"{i*(W/(len(f)-1)):.1f},{H - x/fmax*H:.1f}" for i, x in enumerate(f))
    area = f"0,{H} {pts} {W},{H}"
    vmax = 4500; bw = W / len(v)
    bars = "".join(f'<rect x="{i*bw:.2f}" y="{H - x/vmax*H:.1f}" width="{max(bw-0.6,0.6):.2f}" height="{x/vmax*H:.1f}"/>' for i, x in enumerate(v) if x > 0)
    months = "".join(f'<text x="{(i+0.5)*W/12:.0f}" y="{H+18}">{m}</text>' for i, m in enumerate("JFMAMJJASOND"))
    tiles = [("343", "Average viewers", "+1,272%"), ("753,523", "Hours watched", "+3,032%"), ("54,293", "Followers gained", "+2,109%"),
             ("21,943", "Peak viewers", "+883.5%"), ("2,187", "Hours streamed", "+133.4%"), ("380", "Streams", "+100%")]
    t = "".join(f'<div class="ct"><p class="ct-n">{n}</p><p class="ct-l">{l}</p><p class="ct-d">{dlt} vs 2017</p></div>' for n, l, dlt in tiles)
    return f"""
    <section class="cs-block grid-12" aria-labelledby="s-stream">
      <div class="section-head"><h2 id="s-stream" class="label">Streaming, 2018</h2></div>
      <div class="section-body">
        <div class="creator-tiles reveal">{t}</div>
        <div class="charts">
          <figure class="chart reveal">
            <figcaption><strong>Followers through 2018</strong><span>From about 2,600 to 57,000</span></figcaption>
            <svg viewBox="0 -10 {W} {H+30}" role="img" aria-label="Line chart: Twitch followers grew from about 2,600 to about 57,000 during 2018, accelerating from June.">
              <g class="grid">{''.join(f'<line x1="0" x2="{W}" y1="{H - k/fmax*H:.1f}" y2="{H - k/fmax*H:.1f}"/><text x="0" y="{H - k/fmax*H - 4:.1f}">{k//1000}K</text>' for k in (20000, 40000, 60000))}</g>
              <polygon class="area" points="{area}"/><polyline class="line" points="{pts}"/>
              <g class="axis">{months}</g>
            </svg>
          </figure>
          <figure class="chart reveal" data-delay="1">
            <figcaption><strong>Daily average viewers, 2018</strong><span>Spikes above 4,000</span></figcaption>
            <svg viewBox="0 -10 {W} {H+30}" role="img" aria-label="Bar chart: daily average viewers through 2018, rising from under 100 to a typical 300 to 600 in the second half, with spikes above 3,000 in September, October and November.">
              <g class="grid">{''.join(f'<line x1="0" x2="{W}" y1="{H - k/vmax*H:.1f}" y2="{H - k/vmax*H:.1f}"/><text x="0" y="{H - k/vmax*H - 4:.1f}">{k/1000:g}K</text>' for k in (1000, 2000, 3000, 4000))}</g>
              <g class="bars">{bars}</g>
              <g class="axis">{months}</g>
            </svg>
          </figure>
        </div>
        <p class="cs-note">Stats from SullyGnome. Charts redrawn from SullyGnome’s 2018 follower and viewership graphs, so values are approximate.</p>
      </div>
    </section>"""


def slate_html(proj, p):
    items = []
    for title, name, kind, desc, stat in proj["slate"]:
        fig = figure((kind, name, title), p)
        items.append(f"""<article class="slate-item reveal">{fig}<div class="slate-text"><h3>{e(title)}</h3><p>{e(desc)}</p>{f'<p class="slate-stat">{e(stat)}</p>' if stat else ''}</div></article>""")
    partners = "".join(f"<li>{e(x)}</li>" for x in proj.get("partners", []))
    return f"""
    <section class="cs-block grid-12" aria-labelledby="s-slate">
      <div class="section-head"><h2 id="s-slate" class="label">The slate</h2></div>
      <div class="section-body"><div class="slate">{''.join(items)}</div>
      {f'<div class="partners"><p class="label">2023 partners</p><ul class="brands">{partners}</ul></div>' if partners else ''}</div>
    </section>"""


def stat_tiles(stats, cls="cs-results"):
    rs = "".join(f'<div class="stat reveal" data-delay="{j % 3}"><p class="stat__n">{e(s[0])}</p><p class="stat__l">{e(s[1])}</p>'
                 f'{f"<p class=stat__d>{e(s[2])}</p>" if len(s) > 2 and s[2] else ""}</div>' for j, s in enumerate(stats))
    return f'<div class="{cls}">{rs}</div>' if stats else ""


def piece_html(pc, p):
    """One piece of work inside a chapter of a hub page: text column, then full-width media rows."""
    role = f'<div class="piece-role"><p class="label">My role</p><p>{e(pc["role"])}</p></div>' if pc.get("role") else ""
    note = f'<p class="cs-note">{e(pc["note"])}</p>' if pc.get("note") else ""
    rows = "".join(f'\n    <div class="cs-media grid-12 reveal">{media_row(r, p)}</div>' for r in pc.get("media", []))
    return f"""
    <article class="piece" id="{pc['id']}" aria-labelledby="{pc['id']}-h">
      <div class="grid-12">
        <div class="section-head"><p class="piece-kicker">{e(pc.get('kicker', ''))}</p></div>
        <div class="section-body prose reveal"><h3 class="piece-title" id="{pc['id']}-h">{e(pc['title'])}</h3>{paras(pc.get('text'))}{role}{stat_tiles(pc.get('stats', []), 'cs-results piece-stats')}{note}</div>
      </div>{rows}
    </article>"""


def chapters_html(proj, p):
    out = []
    for k, c in enumerate(proj["chapters"], 1):
        pieces = "".join(piece_html(pc, p) for pc in c.get("pieces", []))
        compact = ""
        if c.get("compact"):
            items = "".join(f"""<article class="slate-item reveal"{f' id="{it[5]}"' if len(it) > 5 else ''}>{figure((it[2], it[1], it[0]), p)}<div class="slate-text"><h3>{e(it[0])}</h3><p>{e(it[3])}</p>{f'<p class="slate-stat">{e(it[4])}</p>' if it[4] else ''}</div></article>"""
                            for it in c["compact"])
            partners = "".join(f"<li>{e(x)}</li>" for x in c.get("partners", []))
            compact = f"""
    <div class="grid-12 chapter-slate">
      <div class="section-head"><p class="piece-kicker">{e(c.get('compact_label', 'Also in this chapter'))}</p></div>
      <div class="section-body"><div class="slate">{items}</div>{f'<div class="partners"><p class="label">{e(c.get("partners_label", "Partners"))}</p><ul class="brands">{partners}</ul></div>' if partners else ''}</div>
    </div>"""
        related = ""
        if c.get("related"):
            links = " ".join(f'<a class="link" href="{s}.html">{e(t)} →</a>' for s, t in c["related"])
            related = f'\n    <div class="grid-12 chapter-related"><div class="section-body"><p>{e(c.get("related_label", "See also"))}: {links}</p></div></div>'
        out.append(f"""
  <section class="chapter" id="{c['id']}" aria-labelledby="ch-{c['id']}">
    <div class="grid-12 chapter-head reveal">
      <div class="section-head"><p class="chapter-num" aria-hidden="true">{k:02d}</p></div>
      <div class="section-body"><h2 class="chapter-title" id="ch-{c['id']}">{e(c['title'])}</h2><p class="chapter-intro">{e(c['intro'])}</p></div>
    </div>{pieces}{compact}{related}
  </section>""")
    return "".join(out)


def chapter_nav(proj):
    lis = "".join(f"""<li><a href="#{c['id']}"><span class="cn-num">{k:02d}</span><span class="cn-title">{e(c['title'])}</span>"""
                  f"""<span class="cn-items">{e(' · '.join([pc['title'] for pc in c.get('pieces', [])] + [it[0] for it in c.get('compact', [])]))}</span></a></li>"""
                  for k, c in enumerate(proj["chapters"], 1))
    return f"""
    <nav class="cs-block grid-12 chapter-nav" aria-label="On this page">
      <div class="section-head"><h2 class="label">On this page</h2></div>
      <div class="section-body"><ol>{lis}</ol></div>
    </nav>"""


def build_case(i, proj, template=False):
    p = "../"
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    M = proj["media"]
    num = f"{i+1:02d}"

    def block(id_, label, inner, accent=False):
        return f"""
    <section class="cs-block grid-12" aria-labelledby="s-{id_}">
      <div class="section-head"><h2 id="s-{id_}" class="label{' label--accent' if accent else ''}">{label}</h2></div>
      <div class="section-body prose reveal">{inner}</div>
    </section>"""

    def gallery(key, cls=""):
        items = M.get(key)
        return f'\n    <div class="cs-media grid-12 reveal">{media_row(items, p, cls)}</div>' if items else ""

    employer = {"At Jellyfish": "Jellyfish", "At Edelman": "Edelman", "Self-employed": "Self-employed",
                "In-house, then at Edelman": "Riot Games, then Edelman"}.get(proj["via"], proj["client"].split(" · ")[0] + " (in-house)")
    meta = [("Client", proj["client"]), ("Employer", employer), ("Year", proj["year"]), ("Platforms", proj["platforms"])]
    meta = [(k, v) for k, v in meta if v]
    meta_html = "".join(f"<div><dt>{k}</dt><dd>{e(v)}</dd></div>" for k, v in meta)

    results = ""
    if proj["results"]:
        rs = "".join(f'<div class="stat reveal" data-delay="{j%3}"><p class="stat__n">{e(n)}</p><p class="stat__l">{e(l)}</p>{f"<p class=stat__d>{e(d)}</p>" if d else ""}</div>' for j, (n, l, d) in enumerate(proj["results"]))
        results = f'<div class="cs-results">{rs}</div>'
    if proj["results_note"]:
        results += f'<p class="cs-note reveal">{e(proj["results_note"])}</p>'

    results_block = (f"""    <section class="cs-block grid-12" aria-labelledby="s-results">
      <div class="section-head"><h2 id="s-results" class="label label--accent">Results</h2></div>
      <div class="section-body">{results}</div>
    </section>""" if results else "")

    delivered = '<ol class="cs-list">' + "".join(f"<li>{e(x)}</li>" for x in proj["delivered"]) + "</ol>"
    skills = '<ul class="cs-tags">' + "".join(f'<li class="tag">{e(x)}</li>' for x in proj["skills"]) + "</ul>"
    hero_img = f"{p}assets/img/hero/{proj['slug']}.webp"

    extra = ""
    if M.get("extra"):
        extra = f"""
    <section class="cs-block cs-block--extra grid-12" aria-labelledby="s-extra">
      <div class="section-head"><h2 id="s-extra" class="label">Also on the account</h2></div>
      <div class="section-body"><p class="cs-sub-lede">{e(M['extra_title'])}</p><p class="cs-note">{e(M['extra_note'])}</p></div>
    </section>
    <div class="cs-media grid-12 reveal">{media_row(M['extra'], p)}</div>"""

    hub = bool(proj.get("chapters"))
    if hub:
        hub_top = (f"""
    <section class="cs-block grid-12" aria-labelledby="s-highlights">
      <div class="section-head"><h2 id="s-highlights" class="label label--accent">Highlights</h2></div>
      <div class="section-body">{stat_tiles(proj['results'])}</div>
    </section>""" if proj["results"] else "") + chapter_nav(proj)
        body_rest = chapters_html(proj, p)
    else:
        hub_top = ""
        body_rest = (f"""
{block('idea', 'Creative idea', paras(proj['idea'])) if proj.get('idea') else ''}{gallery('after_idea')}{slate_html(proj, p) if proj.get('slate') else ''}
{block('delivered', 'What I delivered', delivered) if proj['delivered'] else ''}{gallery('after_delivered')}
{results_block}{gallery('after_results')}{creator_charts() if proj.get('creator') else ''}""")
    related_block = ""
    if proj.get("related"):
        related_block = block("related", "Related projects", '<ul class="related-list">' + "".join(
            f'<li><a class="link" href="{s}.html">{e(tt)} →</a></li>' for s, tt in proj["related"]) + "</ul>")
    others = "\n".join(f'      <li><a href="{o["slug"]}.html"><span>{e(o["title"])}</span><span>{e(o["client"].split(" · ")[0])}</span></a></li>' for o in PROJECTS if o is not proj)
    title = proj["title"]
    desc = proj["summary"] if len(proj["summary"]) <= 158 else proj["summary"][:152].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    out = head(f"{title} — Ramtin Totonchi", desc, p, "case", noindex=template, canonical=f"work/{proj['slug']}.html", og=f"assets/img/og/{proj['slug']}.jpg", og_alt=f"{title}: {proj['cat']}") + header(p, "work") + f"""<main id="main">
  <section class="cs-hero" data-dark aria-labelledby="cs-title">
    <div class="cs-hero__img"><img src="{hero_img}" alt="" width="1920" height="1080" fetchpriority="high"></div>
    <div class="cs-hero__inner">
      <p class="cs-hero__num" aria-hidden="true">{num}</p>
      <div class="cs-hero__title">
        <p class="cs-hero__kicker">{e(proj['cat'])}</p>
        <h1 id="cs-title">{e(title)}</h1>
        <p>{e(proj['client'])} · {e(proj['via'])}</p>
      </div>
    </div>
  </section>

  <div class="grid-12 cs-meta-wrap">
    <dl class="cs-meta reveal">{meta_html}</dl>
  </div>

  <article class="cs">
    <section class="cs-block grid-12" aria-labelledby="s-summary">
      <div class="section-head"><h2 id="s-summary" class="label label--accent">Overview</h2></div>
      <div class="section-body"><p class="prose--big reveal">{e(proj['summary'])}</p></div>
    </section>{gallery('hero', 'is-hero')}
{hub_top}
{block('challenge', 'The challenge', paras(proj['challenge']))}
{block('role', 'My role', paras(proj['role']))}
{block('approach', 'Strategic approach', paras(proj['approach']))}{gallery('after_approach')}{body_rest}
{block('skills', 'Skills demonstrated', skills)}{related_block}{extra}
  </article>

  <section class="next-project" aria-label="Next project">
    <a href="{nxt['slug']}.html">
      <span class="label">Next project</span>
      <span class="np-title">{e(nxt['title'])}</span>
      <span class="np-arrow" aria-hidden="true">→</span>
    </a>
  </section>

  <section class="section section--tight grid-12 other-projects" aria-labelledby="others-h">
    <div class="section-head section-head--full"><h2 class="label" id="others-h">Other projects</h2></div>
    <ul>
{others}
    </ul>
  </section>
</main>
""" + footer(p)
    return out


def build_404():
    out = head("Not found — Ramtin Totonchi", DESC, "/", "404", noindex=True) + header("/", "") + """<main id="main" class="notfound">
  <div>
    <h1>404</h1>
    <p>This page wandered off the feed.</p>
    <a class="btn" href="/index.html">Back to the work <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</main>
</body>
</html>
"""
    (ROOT / "404.html").write_text(out)



def make_og():
    """1200x630 JPEG link-preview images (LinkedIn, X, WhatsApp): one per case study, one for About, one for the site."""
    out = ROOT / "assets/img/og"; out.mkdir(parents=True, exist_ok=True)
    W, H = 1200, 630
    for pr in PROJECTS:
        _cover(Image.open(ROOT / "assets/img/hero" / f"{pr['slug']}.webp").convert("RGB"), W, H).save(out / f"{pr['slug']}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    port = Image.open(ROOT / "assets/img/work/ramtin-portrait.webp").convert("RGB")
    _cover(port, W, H).save(out / "about.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    # site-wide: a 2x2 of four projects that show the range (B2B tech, esports, brand partnership)
    from PIL import ImageDraw
    picks = ["google-cloud-london-summit", "valorant-masters", "the-fa-x-google-cloud", "g2-esports-x-adidas"]
    pad, gap = 18, 12
    cw, ch = (W - 2 * pad - gap) // 2, (H - 2 * pad - gap) // 2
    canvas = Image.new("RGB", (W, H), (18, 18, 18))
    for i, s in enumerate(picks):
        tile = _cover(Image.open(ROOT / "assets/img/hero" / f"{s}.webp").convert("RGB"), cw, ch)
        mask = Image.new("L", tile.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, cw - 1, ch - 1), radius=10, fill=255)
        canvas.paste(tile, (pad + (i % 2) * (cw + gap), pad + (i // 2) * (ch + gap)), mask)
    canvas.save(out / "site.jpg", "JPEG", quality=84, optimize=True, progressive=True)

REDIRECTS = {  # old slug -> new page (and section) after the October 2026 restructure into year pages
    "love-what-you-do": "vct-emea-2024#meet-the-player", "meet-the-player": "vct-emea-2024#meet-the-player",
    "vct-emea-2024-season-teasers": "vct-emea-2024#teasers", "vct-emea-2024-content-slate": "vct-emea-2024#always-on",
    "valorant-masters-madrid": "valorant-masters#madrid", "valorant-masters-tokyo": "valorant-masters#tokyo",
    "join-us-vct-emea-2023": "vct-emea-2023#join-us", "unlocked": "vct-emea-2023#unlocked",
    "frenzy-fire": "vct-emea-2023#frenzy-fire", "run-it-back": "vct-emea-2023#run-it-back",
    "lock-your-tickets": "vct-emea-2023#lock-your-tickets", "gekko-truck-and-fan-wall": "vct-emea-2023#gekko",
    "vct-emea-2023-content-slate": "vct-emea-2023#always-on",
}


def build_redirect(new):
    page, _, anchor = new.partition("#")
    frag = f"#{anchor}" if anchor else ""
    return f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><title>Moved</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{SITE}/work/{page}.html">
<meta http-equiv="refresh" content="0; url={page}.html{frag}"></head>
<body><p><a href="{page}.html{frag}">This case study has moved.</a></p></body></html>
"""


def build_sitemap():
    urls = ["", "work.html", "about.html", "contact.html"] + [f"work/{p['slug']}.html" for p in PROJECTS]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                                      "".join(f"  <url><loc>{SITE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    missing = [n for pr in PROJECTS for key in pr["media"] if isinstance(pr["media"][key], list)
               for (k, n, *_ ) in pr["media"][key] if (k == "v" and n not in MEDIA) or (k == "i" and n not in IMAGES)]
    if missing: print("MISSING MEDIA:", missing)
    for pr in PROJECTS:
        t = ROOT / "assets/img/hero" / f"{pr['slug']}.webp"
        if "--thumbs" in sys.argv or not t.exists():
            try: make_thumb(pr)
            except FileNotFoundError as ex: print("thumb pending:", pr["slug"], ex.filename)
    work_dir = ROOT / "work"; work_dir.mkdir(exist_ok=True)
    for old in work_dir.glob("*.html"): old.unlink()
    if "--thumbs" in sys.argv or not (ROOT / "assets/img/og/site.jpg").exists() or any(not (ROOT / "assets/img/og" / f"{pr['slug']}.jpg").exists() for pr in PROJECTS):
        make_og()
    build_home(); build_work(); build_about(); build_contact(); build_404(); build_sitemap()
    for i, pr in enumerate(PROJECTS):
        (work_dir / f"{pr['slug']}.html").write_text(build_case(i, pr))
    for old, new in REDIRECTS.items():
        (work_dir / f"{old}.html").write_text(build_redirect(new))
    print("built", len(PROJECTS), "case studies")
