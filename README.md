# ramtintotonchi.com

Static portfolio: semantic HTML, one CSS file, one vanilla JS file. Hosted on GitHub Pages at the custom domain in `CNAME`.

```
index.html               Home: 3D carousel of featured work (+ grid view)
work.html                All case studies (grid / list)
about.html               About, services, approach, numbers, experience, brands
contact.html             Contact details and form
work/<slug>.html         One page per case study (generated)
assets/css/styles.css    Design tokens at the top
assets/js/main.js        Clock, header, carousel, reveals, scroll effects, form
assets/media/            Web-encoded campaign videos (.mp4) and posters (.webp)
assets/img/work/         Campaign images (.webp)
assets/img/thumbs, hero  Generated card thumbnails and case-study heroes
_build/                  Generator and content (not needed at runtime)
```

## Editing content

All copy lives in `_build/content.py`. Every case study is one `P.append(dict(...))` block with the same fields: title, client, employer (`via`), year, platforms, overview, challenge, my role, strategic approach, creative idea, what I delivered, results, skills and media. That block *is* the reusable case-study layout: copy one, change it, rebuild.

```bash
pip install pillow          # once
python3 _build/build.py     # rebuild every page
python3 _build/build.py --thumbs   # also regenerate card thumbnails and heroes
```

`featured=True` puts a project in the homepage carousel. Media items are `("v", "video-name", "caption")` or `("i", "image-name", "caption")` and sit side by side at equal height without cropping.

Every figure on the site is traceable in `_build/SOURCES.md`. Keep it that way.

## Adding media

- Videos: H.264 MP4, 720p, with a `.webp` poster of the same name in `assets/media/`, then add an entry to `assets/media/media.json` (width, height, duration).
- Images: WebP in `assets/img/work/`, plus an entry in `assets/img/work/images.json`.
- GitHub rejects files over 100MB. Keep videos well under that.

## LinkedIn

Set `LINKEDIN` in `_build/content.py` to your profile URL and rebuild. The link stays hidden while it's empty.

## Contact form

GitHub Pages can't run server code, so the form opens the visitor's email app with a pre-filled message. To collect submissions in an inbox instead, create a free Formspree form, set `action="https://formspree.io/f/XXXX" method="POST"` on the `<form>` in `contact.html` (via `build.py`), and remove `data-mailto-form`.

## Deploying

Push to `main`. GitHub Pages serves the repo root; `.nojekyll` makes it serve files as-is.
