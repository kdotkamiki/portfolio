"""
Static site generator for ramtintotonchi.com. Run:  python3 _build/build.py
Reads _build/content.py and the media metadata, writes plain HTML to the repo root.
Nothing in _build/ is needed at runtime.
"""
import html, json, pathlib, sys
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
DESC = ("Ramtin Totonchi is a London-based social creative and strategy lead: organic-first social campaigns, "
        "creative direction and content for Google Cloud (at Jellyfish), Riot Games, G2 Esports and more.")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&amp;'
         'family=Space+Grotesk:wght@300;400;500;600&amp;display=swap" rel="stylesheet">')
VER = "3"  # bump to bust caches for CSS/JS


def e(s):
    return html.escape(str(s), quote=True)


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
        inner = (f'<video controls playsinline preload="none" poster="{p}assets/media/{name}.webp" width="{w}" height="{h}" '
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


def make_thumb(proj):
    """Card thumbnail (1600x1000) and case-study hero (1920x1080) for a project."""
    for folder, (W, H), spec in (("thumbs", (1600, 1000), proj["thumb"]), ("hero", (1920, 1080), proj.get("hero", proj["thumb"]))):
        out = ROOT / "assets/img" / folder / f"{proj['slug']}.webp"
        out.parent.mkdir(parents=True, exist_ok=True)
        if spec[0].startswith("composite"):
            canvas = _composite(spec, W, H)
        else:
            src = _source(spec)
            ar = src.width / src.height
            # Video frames often carry on-screen text: never crop them for a card, letterbox on a blur instead.
            if folder == "thumbs" and spec[0] in ("v", "frame") and abs(ar - W / H) > 0.05:
                canvas = _contain_on_blur(src, W, H)
            else:
                canvas = _cover(src, W, H)
        canvas.save(out, "WEBP", quality=80, method=6)


# ------------------------------------------------------------------ chrome
def head(title, desc, p, page="", body_class="", noindex=False, canonical=""):
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
  <div class="mobile-menu__foot"><span>London · <time data-clock>--:--:--</time></span><a href="mailto:{C.EMAIL}">Email me</a></div>
</div>
"""


def footer(p):
    li = f'<li><a class="link" href="{e(C.LINKEDIN)}" rel="me">LinkedIn</a></li>' if C.LINKEDIN else ""
    return f"""<footer class="site-footer">
  <p class="copy">© <span data-year>2026</span> Ramtin Totonchi</p>
  <ul class="social">
    <li><a class="link" href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
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
            <img src="{thumb(proj, '')}" alt="" width="1600" height="1000" loading="{'eager' if i < 3 or i > len(FEATURED) - 3 else 'lazy'}" decoding="async" draggable="false">
            <span class="card-quote" aria-hidden="true">{e(proj['quote'])}</span>
          </figure>
          <span class="card-meta"><span>{e(proj['title'])}</span><span>{e(proj['client'].split(' · ')[0])}</span></span>
        </a>
      </li>"""


def work_card(proj, p):
    return f"""    <li class="work-card reveal">
      <a href="{p}work/{proj['slug']}.html">
        <div class="work-card__top"><span>{e(proj['year'] or proj['via'])}</span><span>{e(proj['cat'])}</span></div>
        <figure><img src="{thumb(proj, p)}" alt="" width="1600" height="1000" loading="lazy" decoding="async"></figure>
        <div class="work-card__bottom"><h3 class="work-card__title">{e(proj['title'])}</h3><span class="work-card__client">{e(proj['client'])}<br><span class="muted">{e(proj['via'])}</span></span></div>
      </a>
    </li>"""


def work_row(proj, p):
    return f"""    <li class="xp-row" data-preview="{thumb(proj, p)}">
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
      <div class="toggle-group" role="group" aria-label="Layout">
        <button class="toggle" type="button" data-layout="grid" aria-pressed="true">Grid</button>
        <button class="toggle" type="button" data-layout="list" aria-pressed="false">List</button>
      </div>
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


def build_about():
    stack = []
    for i, (name, vid, items, eg) in enumerate(C.SERVICES):
        lis = "".join(f"<li>{e(x)}</li>" for x in items)
        stack.append(f"""      <article class="stack-card" style="--i:{i}">
        <div class="stack-card__foot"><span class="stack-card__num">{i+1:02d}/{len(C.SERVICES):02d}</span><span class="muted">{e(eg)}</span></div>
        <figure class="stack-card__media"><img src="assets/media/{vid}.webp" alt=""  width="{MEDIA.get(vid, {'w': 1280})['w']}" height="{MEDIA.get(vid, {'h': 720})['h']}" loading="lazy" decoding="async"></figure>
        <div class="stack-card__body">
          <ul class="stack-card__list">{lis}</ul>
          <h3 class="stack-card__title">{e(name)}</h3>
        </div>
      </article>""")
    stats = []
    for i, (n, suf, label) in enumerate(C.STATS):
        if n == 2021:
            num = '<span>2021</span>'
        else:
            num = f'<span data-count="{n}" data-suffix="{suf}">{n}{suf}</span>'
        stats.append(f'<div class="stat reveal" data-delay="{i}"><p class="stat__n">{num}</p><p class="stat__l">{e(label)}</p></div>')
    xp = "\n".join(f'      <li class="xp-row" data-preview="assets/media/{img}.webp"><div><span class="c1">{e(c)}</span><span class="c2">{e(r)}</span><span class="c3">{e(y)}</span></div></li>' for c, r, y, img in C.EXPERIENCE)
    body = "\n".join(f'        <p class="reveal">{e(t)}</p>' for t in C.ABOUT_BODY)
    brands = "".join(f"<li>{e(b)}</li>" for b in C.BRANDS)
    out = head("About — Ramtin Totonchi", DESC, "", "about", canonical="about.html") + header("", "about") + f"""<main id="main">
  <section class="split-hero split-hero--scroll" data-dark aria-label="Introduction">
    <div class="split-hero__sticky">
      <h1 class="visually-hidden">About Ramtin Totonchi</h1>
      <span class="split-hero__word split-hero__word--l" aria-hidden="true">About</span>
      <div class="split-hero__media"><img src="assets/img/work/g2-adidas-onset.webp" alt="A monitor on set during the G2 Esports × adidas shoot" width="2000" height="1333"></div>
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

  <section class="grid-12" aria-labelledby="services-h">
    <div class="section-head section-head--full"><h2 class="label" id="services-h">What I do</h2></div>
    <div class="stack">
{chr(10).join(stack)}
    </div>
  </section>

  <section class="section grid-12" aria-labelledby="approach-h">
    <div class="section-head"><h2 class="label" id="approach-h">How I work</h2></div>
    <div class="section-body">
      <p class="scroll-lit">Start with the audience, not the asset. Find the cultural moment the brand has a right to be in, build one idea strong enough to flex across markets and platforms, then make each version feel native to where it lands. Measure what matters, tell people the truth, and make the next one better.</p>
    </div>
  </section>

  <section class="section section--tight grid-12" aria-labelledby="numbers-h">
    <div class="section-head section-head--full"><h2 class="label" id="numbers-h">In numbers</h2></div>
    <div class="stats">
      {''.join(stats)}
    </div>
  </section>

  <section class="section section--tight grid-12" aria-labelledby="xp-h">
    <div class="section-head section-head--full"><h2 class="label" id="xp-h">Experience</h2></div>
    <ul class="xp">
{xp}
    </ul>
  </section>

  <section class="section section--tight grid-12" aria-labelledby="brands-h">
    <div class="section-head"><h2 class="label" id="brands-h">Brands and partners</h2></div>
    <div class="section-body"><ul class="brands reveal">{brands}</ul></div>
  </section>

  <section class="section section--tight grid-12" aria-labelledby="work-h">
    <div class="section-head section-head--full section-head--split"><h2 class="label" id="work-h">Selected work</h2><a class="link" href="work.html">All work →</a></div>
    <ul class="work-grid">
{chr(10).join(work_card(pr, '') for pr in FEATURED[:4])}
    </ul>
  </section>
</main>
""" + footer("")
    (ROOT / "about.html").write_text(out)


def build_contact():
    li = f'<a class="link" href="{e(C.LINKEDIN)}">LinkedIn →</a>' if C.LINKEDIN else ""
    out = head("Contact — Ramtin Totonchi", "Get in touch with Ramtin Totonchi about senior social and creative leadership roles or projects.", "", "contact", canonical="contact.html") + header("", "contact") + f"""<main id="main">
  <section class="split-hero split-hero--static" data-dark aria-labelledby="contact-h">
    <div class="split-hero__sticky">
      <h1 class="visually-hidden" id="contact-h">Contact</h1>
      <span class="split-hero__word split-hero__word--l" aria-hidden="true">Say</span>
      <div class="split-hero__media"><img src="assets/img/work/gekko-6.webp" alt="" width="2000" height="1125"></div>
      <span class="split-hero__word split-hero__word--r" aria-hidden="true">Hello</span>
    </div>
  </section>

  <section class="section grid-12" aria-labelledby="contact-copy-h">
    <div class="section-head"><h2 class="label" id="contact-copy-h">Contact</h2></div>
    <div class="section-body">
      <p class="contact-copy reveal">I'm open to senior social and creative leadership roles, and to the occasional project with a sharp brief. Tell me what you're working on, where it's at, and the part you haven't cracked yet.</p>
      <div class="contact-direct reveal"><a class="link" href="mailto:{C.EMAIL}">{C.EMAIL}</a>{li}</div>
      <form class="form" data-mailto-form="{C.EMAIL}" novalidate>
        <div class="field"><label for="f-first">First name</label><input id="f-first" name="first-name" autocomplete="given-name" required></div>
        <div class="field"><label for="f-last">Last name</label><input id="f-last" name="last-name" autocomplete="family-name"></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-topic">What's it about?</label>
          <select id="f-topic" name="topic">
            <option>A full-time role</option>
            <option>Social strategy</option>
            <option>Creative direction</option>
            <option>Something else</option>
          </select></div>
        <div class="field field--full"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required placeholder="A few lines is plenty."></textarea></div>
        <p class="form-status" role="status"></p>
        <button class="btn" type="submit">Send <span class="arrow" aria-hidden="true">→</span></button>
      </form>
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
        <p class="cs-note">Stats from SullyGnome. Charts redrawn from SullyGnome's 2018 follower and viewership graphs, so values are approximate.</p>
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

    others = "\n".join(f'      <li><a href="{o["slug"]}.html"><span>{e(o["title"])}</span><span>{e(o["client"].split(" · ")[0])}</span></a></li>' for o in PROJECTS if o is not proj)
    title = proj["title"]
    desc = proj["summary"][:155]
    out = head(f"{title} — Ramtin Totonchi", desc, p, "case", noindex=template, canonical=f"work/{proj['slug']}.html") + header(p, "work") + f"""<main id="main">
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
{block('challenge', 'The challenge', paras(proj['challenge']))}
{block('role', 'My role', paras(proj['role']))}
{block('approach', 'Strategic approach', paras(proj['approach']))}{gallery('after_approach')}
{block('idea', 'Creative idea', paras(proj['idea'])) if proj.get('idea') else ''}{gallery('after_idea')}{slate_html(proj, p) if proj.get('slate') else ''}
{block('delivered', 'What I delivered', delivered)}{gallery('after_delivered')}
    <section class="cs-block grid-12" aria-labelledby="s-results">
      <div class="section-head"><h2 id="s-results" class="label label--accent">Results</h2></div>
      <div class="section-body">{results}</div>
    </section>{gallery('after_results')}{creator_charts() if proj.get('creator') else ''}
{block('skills', 'Skills demonstrated', skills)}{extra}
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
    build_home(); build_work(); build_about(); build_contact(); build_404(); build_sitemap()
    for i, pr in enumerate(PROJECTS):
        (work_dir / f"{pr['slug']}.html").write_text(build_case(i, pr))
    print("built", len(PROJECTS), "case studies")
