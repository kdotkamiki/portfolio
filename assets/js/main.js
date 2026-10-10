/* Ramtin Totonchi — portfolio interactions. Vanilla JS, no dependencies.
   Each feature checks for its own markup, so one file serves every page. */
(() => {
  "use strict";

  const doc = document.documentElement;
  doc.classList.remove("no-js");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- London clock ---------- */
  const clocks = $$("[data-clock]");
  if (clocks.length) {
    const fmt = new Intl.DateTimeFormat("en-GB", {
      timeZone: "Europe/London", hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false,
    });
    const tick = () => {
      const now = new Date();
      clocks.forEach((c) => {
        c.textContent = fmt.format(now);
        c.setAttribute("datetime", now.toISOString());
      });
    };
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- Footer year ---------- */
  $$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

  /* ---------- Mobile menu ---------- */
  const menuBtn = $(".menu-toggle");
  const menu = $(".mobile-menu");
  if (menuBtn && menu) {
    const setOpen = (open) => {
      doc.classList.toggle("menu-open", open);
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.querySelector(".menu-label").textContent = open ? "Close" : "Menu";
      menu.inert = !open;
      if (open) menu.querySelector("a")?.focus();
    };
    menu.inert = true;
    menuBtn.addEventListener("click", () => setOpen(!doc.classList.contains("menu-open")));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && doc.classList.contains("menu-open")) { setOpen(false); menuBtn.focus(); }
    });
    $$("a", menu).forEach((a) => a.addEventListener("click", () => setOpen(false)));
  }

  /* ---------- Split text into words ---------- */
  const splitWords = (el) => {
    const words = el.textContent.trim().split(/\s+/);
    el.setAttribute("aria-label", el.textContent.trim());
    el.innerHTML = words
      .map((w, i) => `<span class="w" aria-hidden="true" style="--i:${i}"><span>${w}</span></span>`)
      .join(" ");
  };
  $$(".split-words").forEach(splitWords);

  /* ---------- Reveal on scroll ---------- */
  const revealables = $$(".reveal, .split-words");
  if ("IntersectionObserver" in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.1 });
    revealables.forEach((el) => {
      // Anything already on screen at load animates in straight away
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) requestAnimationFrame(() => el.classList.add("is-in"));
      else io.observe(el);
    });
  } else {
    revealables.forEach((el) => el.classList.add("is-in"));
  }

  /* ---------- Rolling digit counter ---------- */
  const makeRoller = (el, value) => {
    el.innerHTML = "";
    const digits = String(value).padStart(2, "0").split("");
    const cols = digits.map((d) => {
      const wrap = document.createElement("span");
      wrap.className = "digit";
      const strip = document.createElement("span");
      strip.innerHTML = "0123456789".split("").map((n) => `<span style="display:block">${n}</span>`).join("");
      wrap.appendChild(strip);
      el.appendChild(wrap);
      return strip;
    });
    const set = (v) => {
      String(v).padStart(2, "0").split("").forEach((d, i) => {
        cols[i].style.transform = `translateY(${-Number(d) * 10}%)`;
      });
    };
    set(value);
    return set;
  };

  /* ---------- Home: 3D ring carousel ---------- */
  const stage = $("[data-carousel]");
  if (stage) {
    const ring = $(".ring", stage);
    const cards = $$(".card", ring);
    const N = cards.length;
    const step = 360 / N;
    const nowEl = $(".counter--now");
    const live = $("[data-carousel-live]");
    const setCounter = nowEl ? makeRoller(nowEl, 1) : () => {};
    const mqVertical = window.matchMedia("(max-width: 760px)");

    let rot = 0;          // current rotation (deg)
    let target = 0;       // where we're easing to
    let radius = 600;
    let vertical = mqVertical.matches;
    let paused = false;   // hover / focus / drag
    let dragging = false;
    let lastPos = 0;
    let idleTimer = 0;
    let front = -1;
    let gridMode = false;
    let raf = 0;

    cards.forEach((c, i) => c.style.setProperty("--i", i));

    const measure = () => {
      vertical = mqVertical.matches;
      const r = cards[0].getBoundingClientRect();
      const w = cards[0].offsetWidth;
      const h = cards[0].offsetHeight || r.height;
      const size = vertical ? h + 56 : w + 36;
      radius = size / (2 * Math.tan(Math.PI / N));
    };

    const normalize = (a) => ((a % 360) + 540) % 360 - 180;

    const render = () => {
      let best = 0, bestCos = -2;
      cards.forEach((card, i) => {
        const a = normalize(i * step + rot);
        const rad = (a * Math.PI) / 180;
        const cos = Math.cos(rad);
        const rotate = vertical ? `rotateX(${-a}deg)` : `rotateY(${a}deg)`;
        card.style.transform =
          `translate(-50%, -50%) translateZ(${radius}px) ${rotate} translateZ(${-radius}px)`;
        const vis = vertical
          ? Math.max(0, Math.min(1, (cos - 0.6) / 0.3))
          : Math.max(0, Math.min(1, (cos - 0.05) / 0.35));
        card.style.opacity = vis.toFixed(3);
        card.style.zIndex = String(Math.round(cos * 100) + 100);
        card.style.pointerEvents = cos > 0.75 ? "auto" : "none";
        card.querySelector("a").tabIndex = cos > 0.75 ? 0 : -1;
        if (cos > bestCos) { bestCos = cos; best = i; }
      });
      if (best !== front) {
        cards[front]?.classList.remove("card--front");
        cards[best].classList.add("card--front");
        front = best;
        setCounter(best + 1);
        if (live) live.textContent = `Project ${best + 1} of ${N}: ${cards[best].dataset.title}`;
      }
    };

    const snap = () => { target = Math.round(target / step) * step; };

    const loop = () => {
      if (!paused && !dragging && !reduceMotion) target -= 0.045;   // slow drift
      rot += (target - rot) * (reduceMotion ? 1 : 0.075);
      render();
      raf = requestAnimationFrame(loop);
    };

    const goTo = (index) => {
      // shortest path to bring card[index] to the front
      const desired = -index * step;
      const diff = normalize(desired - target);
      target += diff;
    };
    const nudge = (dir) => { snap(); target -= dir * step; };

    const scheduleSnap = () => {
      clearTimeout(idleTimer);
      idleTimer = setTimeout(snap, 180);
    };

    // Wheel / trackpad
    stage.addEventListener("wheel", (e) => {
      if (gridMode) return;
      e.preventDefault();
      const d = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
      target -= d * 0.06;
      scheduleSnap();
    }, { passive: false });

    // Drag (mouse + touch)
    let moved = 0;
    stage.addEventListener("pointerdown", (e) => {
      if (gridMode || e.button !== 0) return;
      dragging = true; moved = 0;
      lastPos = vertical ? e.clientY : e.clientX;
    });
    window.addEventListener("pointermove", (e) => {
      if (!dragging) return;
      const p = vertical ? e.clientY : e.clientX;
      const d = p - lastPos;
      lastPos = p;
      moved += Math.abs(d);
      target += d * (vertical ? -0.12 : 0.12);
    });
    window.addEventListener("pointerup", () => {
      if (!dragging) return;
      dragging = false;
      snap();
    });
    // Don't follow a link at the end of a drag
    stage.addEventListener("click", (e) => { if (moved > 8) { e.preventDefault(); moved = 0; } }, true);

    // Pause drift on hover / focus
    stage.addEventListener("pointerenter", () => (paused = true));
    stage.addEventListener("pointerleave", () => { paused = false; });
    stage.addEventListener("focusin", (e) => {
      paused = true;
      const card = e.target.closest(".card");
      if (card && !gridMode) goTo(cards.indexOf(card));
    });
    stage.addEventListener("focusout", () => (paused = false));

    // Keyboard
    stage.addEventListener("keydown", (e) => {
      if (gridMode) return;
      const next = vertical ? "ArrowDown" : "ArrowRight";
      const prev = vertical ? "ArrowUp" : "ArrowLeft";
      if (e.key === next) { e.preventDefault(); nudge(1); }
      if (e.key === prev) { e.preventDefault(); nudge(-1); }
      if (e.key === "Enter" && e.target === stage) cards[front]?.querySelector("a").click();
    });
    $$("[data-step]").forEach((b) => b.addEventListener("click", () => nudge(Number(b.dataset.step))));

    // Carousel / Grid toggle
    const toggles = $$("[data-view]");
    const setView = (view) => {
      gridMode = view === "grid";
      stage.classList.toggle("is-grid", gridMode);
      toggles.forEach((t) => t.setAttribute("aria-pressed", String(t.dataset.view === view)));
      $$("[data-step]").forEach((b) => (b.hidden = gridMode));
      if (gridMode) {
        cancelAnimationFrame(raf);
        cards.forEach((c) => { c.querySelector("a").tabIndex = 0; });
      } else {
        measure(); render(); raf = requestAnimationFrame(loop);
      }
    };
    toggles.forEach((t) => t.addEventListener("click", () => setView(t.dataset.view)));

    // Pause when tab hidden
    document.addEventListener("visibilitychange", () => {
      if (document.hidden) cancelAnimationFrame(raf);
      else if (!gridMode) raf = requestAnimationFrame(loop);
    });

    window.addEventListener("resize", () => { measure(); render(); });
    mqVertical.addEventListener?.("change", () => { measure(); render(); });

    measure();
    render();
    if (reduceMotion) setView("grid"); else raf = requestAnimationFrame(loop);
  }

  /* ---------- Work index: grid / list toggle ---------- */
  const workIndex = $(".work-index");
  if (workIndex) {
    const btns = $$("[data-layout]", workIndex);
    btns.forEach((b) => b.addEventListener("click", () => {
      const list = b.dataset.layout === "list";
      workIndex.classList.toggle("is-list", list);
      btns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    }));
  }

  /* ---------- Scroll-driven effects (one rAF-throttled listener) ---------- */
  const heroes = $$(".split-hero--scroll");
  const lits = $$(".scroll-lit");
  const parallax = $(".cs-hero__img img");

  lits.forEach((el) => {
    const words = el.textContent.trim().split(/\s+/);
    el.setAttribute("aria-label", el.textContent.trim());
    el.innerHTML = words.map((w) => `<span class="w" aria-hidden="true">${w}</span>`).join(" ");
  });

  if (!reduceMotion && (heroes.length || lits.length || parallax)) {
    let ticking = false;
    const onScroll = () => {
      const vh = window.innerHeight;
      heroes.forEach((h) => {
        const r = h.getBoundingClientRect();
        const p = Math.min(1, Math.max(0, -r.top / (r.height - vh)));
        const eased = 1 - Math.pow(1 - p, 2);
        const media = $(".split-hero__media", h);
        media.style.setProperty("--p", eased.toFixed(4));
        const l = $(".split-hero__word--l", h), rr = $(".split-hero__word--r", h);
        if (l && rr && !window.matchMedia("(max-width: 760px)").matches) {
          l.style.transform = `translate(${-eased * 6}vw, -50%)`;
          rr.style.transform = `translate(${eased * 6}vw, -50%)`;
        }
      });
      lits.forEach((el) => {
        const r = el.getBoundingClientRect();
        const p = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
        const ws = el.children;
        const on = Math.round(p * ws.length);
        for (let i = 0; i < ws.length; i++) ws[i].classList.toggle("on", i < on);
      });
      if (parallax) {
        const y = Math.min(window.scrollY, vh);
        parallax.style.setProperty("--parallax", `${-y * 0.12}px`);
      }
      ticking = false;
    };
    window.addEventListener("scroll", () => {
      if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
    }, { passive: true });
    onScroll();
  }

  /* ---------- Hover preview image that follows the cursor ---------- */
  const previewRows = $$("[data-preview]");
  if (previewRows.length && window.matchMedia("(hover: hover)").matches) {
    const box = document.createElement("div");
    box.className = "hover-preview";
    box.setAttribute("aria-hidden", "true");
    box.innerHTML = '<img alt="">';
    document.body.appendChild(box);
    const img = box.firstChild;
    let x = 0, y = 0, cx = 0, cy = 0, running = false;
    const follow = () => {
      cx += (x - cx) * 0.18; cy += (y - cy) * 0.18;
      box.style.transform = `translate(${cx}px, ${cy}px) translate(-50%, -50%) scale(${box.classList.contains("on") ? 1 : 0.85})`;
      if (running) requestAnimationFrame(follow);
    };
    previewRows.forEach((row) => {
      row.addEventListener("pointerenter", (e) => {
        img.src = row.dataset.preview;
        x = cx = e.clientX; y = cy = e.clientY;
        box.classList.add("on");
        if (!running) { running = true; requestAnimationFrame(follow); }
      });
      row.addEventListener("pointermove", (e) => { x = e.clientX; y = e.clientY; });
      row.addEventListener("pointerleave", () => { box.classList.remove("on"); setTimeout(() => { if (!box.classList.contains("on")) running = false; }, 400); });
    });
  }

  /* ---------- Count-up numbers ---------- */
  const counters = $$("[data-count]");
  if (counters.length) {
    const run = (el) => {
      const end = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || "";
      if (reduceMotion) { el.textContent = end + suffix; return; }
      const dur = 1400, t0 = performance.now();
      const frame = (t) => {
        const k = Math.min(1, (t - t0) / dur);
        const e = 1 - Math.pow(1 - k, 3);
        el.textContent = Math.round(end * e) + suffix;
        if (k < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };
    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver((ens) => ens.forEach((en) => {
        if (en.isIntersecting) { run(en.target); io.unobserve(en.target); }
      }), { threshold: 0.5 });
      counters.forEach((c) => io.observe(c));
    } else counters.forEach(run);
  }

  /* ---------- Contact form → opens the visitor's email app ----------
     GitHub Pages can't run server code. This builds a pre-filled email.
     To collect submissions instead, point the form's action at a form
     service (e.g. Formspree) and delete this block. */
  const form = $("[data-mailto-form]");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const d = new FormData(form);
      const name = `${d.get("first-name")} ${d.get("last-name")}`.trim();
      const subject = `${d.get("topic")} — ${name}`;
      const body = `${d.get("message")}\n\n${name}\n${d.get("email")}`;
      const to = form.dataset.mailtoForm;
      window.location.href = `mailto:${to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      const status = $(".form-status", form);
      if (status) status.textContent = "Opening your email app… If nothing happens, email " + to + " directly.";
    });
  }
})();
