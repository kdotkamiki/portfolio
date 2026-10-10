# Ramtin Totonchi — portfolio

Static site: semantic HTML, one CSS file, one small vanilla JS file. No build step, no framework, free to host on GitHub Pages.

```
index.html            One-screen home: 3D project carousel + grid view
work.html             All work (grid / list toggle)
about.html            About, services, approach, numbers, experience, contact
work/*.html           One case study per project
work/_template.html   Blank case-study layout to copy for new projects (noindex)
404.html              Not-found page
assets/css/styles.css Design tokens at the top (colours, fonts, spacing)
assets/js/main.js     Clock, carousel, reveals, scroll effects, form
assets/img/           Placeholder art (replace with your own)
```

## Editing

- **Case studies:** open `work/<project>.html` and replace the Lorem ipsum in each section (Summary, Challenge, My role, Strategic approach, Creative idea, What I delivered, Results, Skills demonstrated). Search for `TODO`.
- **New project:** copy `work/_template.html` to `work/new-slug.html`, fill it in, then add a card to `index.html` (inside `<ul class="ring">`), `work.html` (grid + list) and update the `/08` counts and `Work 08` in the nav.
- **Images:** add files to `assets/img/` and change the `src`. Keep landscape images around 1600×1000. Always write useful `alt` text for images that carry meaning.
- **Social links:** footer links in every page point to the LinkedIn/X/Instagram home pages. Replace them with your profile URLs (search `TODO: your`).
- **Colours and fonts:** edit the `:root` tokens at the top of `styles.css`. Fonts are Space Grotesk and Instrument Sans from Google Fonts (both open licence).
- **Contact form:** GitHub Pages can't run server code, so the form opens the visitor's email app with a pre-filled message. To receive submissions in an inbox instead, create a free Formspree form, set `action="https://formspree.io/f/XXXX" method="POST"` on the `<form>`, and remove the `data-mailto-form` attribute.

## Things to check before going live

- Every stat on `about.html` (15+ years, 40M+ peak reported reach, 9 markets, Creative Piece of the Year 2021) is taken from your notes/CV. Confirm each one and where it came from.
- "Esports Creative Piece of The Year 2021" is attributed to the G2 project. Move it if it belongs elsewhere.
- Project titles such as "Partners Fans Didn't Skip" are working titles. Rename freely.
- In `404.html`, set `<base href="/">` to `/repo-name/` if the site is a project repo (e.g. `username.github.io/portfolio`).

## Deploy to GitHub Pages

1. Push these files to the root of a repo's `main` branch.
2. Repo **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)`**.
3. The site appears at `https://<username>.github.io/<repo>/` (or `https://<username>.github.io/` if the repo is named `<username>.github.io`).

The `.nojekyll` file tells Pages to serve files as-is.

## Accessibility notes

Skip link, visible focus states, keyboard-operable carousel (arrow keys + buttons), live region announcing the current project, `prefers-reduced-motion` support (carousel starts in grid view, scroll effects off), and text colours that meet WCAG AA on their backgrounds.
