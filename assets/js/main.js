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
    const fmt = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/London", hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false });
    const tick = () => { const now = new Date(); clocks.forEach((c) => { c.textContent = fmt.format(now); c.setAttribute("datetime", now.toISOString()); }); };
    tick(); setInterval(tick, 1000);
  }
  $$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

  /* ---------- Header: solid after scrolling, light over dark heroes ---------- */
  const header = $(".site-header");
  if (header) {
    const darkHeroes = $$("[data-dark]");
    const update = () => {
      const h = header.offsetHeight;
      const overDark = darkHeroes.some((el) => { const r = el.getBoundingClientRect(); return r.top <= 0 && r.bottom > h; });
      const scrolled = window.scrollY > 8;
      header.classList.toggle("on-dark", overDark);
      header.classList.toggle("is-solid", scrolled && !overDark);
    };
    let t = false;
    window.addEventListener("scroll", () => { if (!t) { t = true; requestAnimationFrame(() => { update(); t = false; }); } }, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  /* ---------- Mobile menu ---------- */
  const menuBtn = $(".menu-toggle");
  const menu = $(".mobile-menu");
  if (menuBtn && menu) {
    const setOpen = (open, focusBack) => {
      doc.classList.toggle("menu-open", open);
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.querySelector(".menu-label").textContent = open ? "Close" : "Menu";
      menu.inert = !open;
      if (open) menu.querySelector("a")?.focus({ preventScroll: true });
      else if (focusBack) menuBtn.focus();
    };
    menu.inert = true;
    menuBtn.addEventListener("click", () => setOpen(!doc.classList.contains("menu-open")));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && doc.classList.contains("menu-open")) setOpen(false, true); });
    $$("a", menu).forEach((a) => a.addEventListener("click", () => setOpen(false)));
    window.matchMedia("(min-width: 761px)").addEventListener?.("change", (m) => { if (m.matches) setOpen(false); });
  }

  /* ---------- Word split + reveal ---------- */
  $$(".split-words").forEach((el) => {
    const text = el.textContent.trim();
    el.setAttribute("aria-label", text);
    el.innerHTML = text.split(/\s+/).map((w, i) => `<span class="w" aria-hidden="true" style="--i:${i}"><span>${w}</span></span>`).join(" ");
  });
  const revealables = $$(".reveal, .split-words");
  if ("IntersectionObserver" in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
    }), { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealables.forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) requestAnimationFrame(() => el.classList.add("is-in"));
      else io.observe(el);
    });
  } else revealables.forEach((el) => el.classList.add("is-in"));

  /* ---------- Rolling digit counter ---------- */
  const makeRoller = (el) => {
    el.innerHTML = "";
    const cols = [0, 1].map(() => {
      const wrap = document.createElement("span"); wrap.className = "digit";
      const strip = document.createElement("span");
      strip.innerHTML = "0123456789".split("").map((n) => `<span>${n}</span>`).join("");
      wrap.appendChild(strip); el.appendChild(wrap); return strip;
    });
    return (v) => String(v).padStart(2, "0").split("").forEach((d, i) => { cols[i].style.transform = `translateY(${-Number(d) * 10}%)`; });
  };

  /* ==========================================================================
     Home carousel
     A ring of cards. State is a single number, `pos` (in slides), that eases
     toward an integer `target`. Every input changes `target` by whole slides,
     except dragging, which moves `pos` directly and snaps on release.
     ========================================================================== */
  const stage = $("[data-carousel]");
  if (stage) {
    const ring = $(".ring", stage);
    const cards = $$(".card", ring);
    const N = cards.length;
    const step = 360 / N;
    const live = $("[data-carousel-live]");
    const nowEl = $(".counter--now");
    const setCounter = nowEl ? makeRoller(nowEl) : () => {};
    const mqVertical = window.matchMedia("(max-width: 760px)");
    const mod = (n, m) => ((n % m) + m) % m;

    let pos = 0, target = 0, radius = 600, vertical = mqVertical.matches;
    let raf = 0, last = 0, front = -1, gridMode = false;

    cards.forEach((c, i) => { c.style.setProperty("--i", i); c.querySelector("a").draggable = false; });

    const measure = () => {
      vertical = mqVertical.matches;
      const c = cards[0];
      const size = vertical ? c.offsetHeight + 28 : c.offsetWidth + 32;
      radius = size / (2 * Math.tan(Math.PI / N));
    };

    const render = () => {
      for (let i = 0; i < N; i++) {
        let rel = i - pos;
        rel = mod(rel + N / 2, N) - N / 2;           // shortest offset, -N/2..N/2
        const a = rel * step;
        const cos = Math.cos((a * Math.PI) / 180);
        const card = cards[i];
        const rot = vertical ? `rotateX(${a}deg)` : `rotateY(${-a}deg)`;   // next slide sits right / below
        card.style.transform = `translate(-50%, -50%) translateZ(${radius}px) ${rot} translateZ(${-radius}px)`;
        const vis = (cos - 0.62) / 0.24;   // front ±1 fully visible, the rest fade out
        card.style.opacity = Math.max(0, Math.min(1, vis)).toFixed(3);
        card.style.zIndex = String(Math.round(cos * 100) + 100);
        const near = Math.abs(rel) < 0.5;
        const reachable = Math.abs(rel) < 1.5;
        card.style.pointerEvents = reachable ? "auto" : "none";
        card.querySelector("a").tabIndex = near ? 0 : -1;
        card.setAttribute("aria-hidden", near ? "false" : "true");
      }
      const f = mod(Math.round(pos), N);
      if (f !== front) {
        cards[front]?.classList.remove("card--front");
        cards[f].classList.add("card--front");
        front = f;
        setCounter(f + 1);
      }
    };

    const announce = () => { if (live) live.textContent = `Project ${front + 1} of ${N}: ${cards[front].dataset.title}`; };

    const loop = (t) => {
      const dt = Math.min(64, t - (last || t)); last = t;
      const k = reduceMotion ? 1 : 1 - Math.exp(-dt / 110);   // frame-rate independent easing
      if (!dragging) pos += (target - pos) * k;
      if (!dragging && Math.abs(target - pos) < 0.0005) { pos = target; render(); raf = 0; last = 0; announce(); return; }
      render();
      raf = requestAnimationFrame(loop);
    };
    const kick = () => { if (!raf && !gridMode) raf = requestAnimationFrame(loop); };
    const go = (delta) => { target = Math.round(target) + delta; kick(); };
    const goTo = (i) => {
      const cur = mod(Math.round(target), N);
      let d = i - cur; d = mod(d + N / 2, N) - N / 2;
      target = Math.round(target) + Math.round(d); kick();
    };

    // Wheel / trackpad. A mouse notch moves one slide. A trackpad swipe moves one slide per
    // gesture: the gesture ends after a short quiet gap, so momentum can't skip slides.
    let wheelAcc = 0, wheelUsed = false, lastWheel = 0, notchLock = 0;
    stage.addEventListener("wheel", (e) => {
      if (gridMode) return;
      e.preventDefault();
      const d = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
      const now = performance.now();
      const notch = e.deltaMode === 1 || (Math.abs(d) >= 50 && Number.isInteger(d));
      if (notch) { if (now > notchLock) { go(Math.sign(d)); notchLock = now + 260; } lastWheel = now; return; }
      if (now - lastWheel > 220) { wheelUsed = false; wheelAcc = 0; }
      lastWheel = now;
      if (wheelUsed) return;
      wheelAcc += d;
      if (Math.abs(wheelAcc) > 30) { go(Math.sign(wheelAcc)); wheelUsed = true; wheelAcc = 0; }
    }, { passive: false });

    // Pointer drag / swipe
    let dragging = false, startP = 0, startPos = 0, moved = 0, lastP = 0, lastT = 0, vel = 0, pid = null;
    const pxPerSlide = () => (vertical ? cards[0].offsetHeight + 28 : cards[0].offsetWidth + 32);
    stage.addEventListener("pointerdown", (e) => {
      if (gridMode || (e.pointerType === "mouse" && e.button !== 0)) return;
      dragging = true; moved = 0; vel = 0; pid = e.pointerId;
      startP = lastP = vertical ? e.clientY : e.clientX; lastT = performance.now(); startPos = pos;
      stage.classList.add("is-dragging");
    });
    stage.addEventListener("pointermove", (e) => {
      if (!dragging || e.pointerId !== pid) return;
      const p = vertical ? e.clientY : e.clientX;
      const now = performance.now();
      moved = Math.max(moved, Math.abs(p - startP));
      if (moved > 6 && !stage.hasPointerCapture(pid)) { try { stage.setPointerCapture(pid); } catch (_) {} }
      vel = (p - lastP) / Math.max(1, now - lastT); lastP = p; lastT = now;
      pos = startPos - (p - startP) / pxPerSlide();
      if (!raf) { render(); }
    });
    const endDrag = (e) => {
      if (!dragging || (e && e.pointerId !== pid)) return;
      dragging = false; stage.classList.remove("is-dragging");
      if (moved > 6) {
        let t = Math.round(pos);
        if (Math.abs(vel) > 0.35 && t === Math.round(startPos)) t -= Math.sign(vel);   // a flick always moves one slide
        target = t; kick();
      }
    };
    stage.addEventListener("pointerup", endDrag);
    stage.addEventListener("pointercancel", endDrag);
    stage.addEventListener("lostpointercapture", endDrag);

    // Clicks: a drag never opens a link; a side card comes to the front instead of opening.
    stage.addEventListener("click", (e) => {
      const a = e.target.closest(".card a");
      if (!a || gridMode) return;
      if (moved > 6) { e.preventDefault(); moved = 0; return; }
      const i = cards.indexOf(a.closest(".card"));
      if (i !== front) { e.preventDefault(); goTo(i); }
    });
    stage.addEventListener("dragstart", (e) => e.preventDefault());

    // Keyboard
    stage.addEventListener("keydown", (e) => {
      if (gridMode) return;
      const next = ["ArrowRight", "ArrowDown"], prev = ["ArrowLeft", "ArrowUp"];
      if (next.includes(e.key)) { e.preventDefault(); go(1); }
      else if (prev.includes(e.key)) { e.preventDefault(); go(-1); }
      else if (e.key === "Home") { e.preventDefault(); goTo(0); }
      else if (e.key === "End") { e.preventDefault(); goTo(N - 1); }
      else if (e.key === "Enter" && e.target === stage) cards[front]?.querySelector("a").click();
    });
    stage.addEventListener("focusin", (e) => { const c = e.target.closest(".card"); if (c && !gridMode) goTo(cards.indexOf(c)); });
    $$("[data-step]").forEach((b) => b.addEventListener("click", () => go(Number(b.dataset.step))));

    // Carousel / Grid
    const toggles = $$("[data-view]");
    const setView = (view) => {
      gridMode = view === "grid";
      stage.classList.toggle("is-grid", gridMode);
      toggles.forEach((t) => t.setAttribute("aria-pressed", String(t.dataset.view === view)));
      $$("[data-step]").forEach((b) => (b.hidden = gridMode));
      stage.setAttribute("aria-roledescription", gridMode ? "grid" : "carousel");
      if (gridMode) {
        cancelAnimationFrame(raf); raf = 0;
        cards.forEach((c) => { c.querySelector("a").tabIndex = 0; c.removeAttribute("aria-hidden"); });
      } else { measure(); render(); }
    };
    toggles.forEach((t) => t.addEventListener("click", () => setView(t.dataset.view)));

    const onResize = () => { if (!gridMode) { measure(); render(); } };
    window.addEventListener("resize", onResize);
    mqVertical.addEventListener?.("change", onResize);

    measure(); render(); announce();
    if (reduceMotion) setView("grid");
  }

  /* ---------- Work index: grid / list ---------- */
  const workIndex = $(".work-index");
  if (workIndex) {
    const btns = $$("[data-layout]", workIndex);
    btns.forEach((b) => b.addEventListener("click", () => {
      workIndex.classList.toggle("is-list", b.dataset.layout === "list");
      btns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    }));
  }

  /* ---------- Scroll-driven effects ---------- */
  const heroes = $$(".split-hero--scroll");
  const lits = $$(".scroll-lit");
  const parallax = $(".cs-hero__img img");
  lits.forEach((el) => {
    const lines = el.innerHTML.split(/<br\s*\/?>/i);
    el.setAttribute("aria-label", lines.join(" ").replace(/\s+/g, " ").trim());
    el.innerHTML = lines.map((ln) => ln.trim().split(/\s+/).map((w) => `<span class="w" aria-hidden="true">${w}</span>`).join(" ")).join("<br>");
  });
  if (!reduceMotion && (heroes.length || lits.length || parallax)) {
    const mqMobile = window.matchMedia("(max-width: 760px)");
    let ticking = false;
    const onScroll = () => {
      const vh = window.innerHeight;
      heroes.forEach((h) => {
        const r = h.getBoundingClientRect();
        const p = Math.min(1, Math.max(0, -r.top / (r.height - vh)));
        const eased = 1 - Math.pow(1 - p, 2);
        $(".split-hero__media", h).style.setProperty("--p", eased.toFixed(4));
        h.style.setProperty("--wp", eased.toFixed(4));
      });
      lits.forEach((el) => {
        const r = el.getBoundingClientRect();
        // Starts as the block enters the viewport (top at 100%) and is fully lit once its bottom reaches 82%,
        // so it is always finished before the section that follows it appears.
        const p = Math.min(1, Math.max(0, (vh - r.top) / (r.height + vh * 0.18)));
        const ws = el.querySelectorAll(".w"); const on = Math.round(p * ws.length);
        for (let i = 0; i < ws.length; i++) ws[i].classList.toggle("on", i < on);
      });
      if (parallax) parallax.style.setProperty("--parallax", `${-Math.min(window.scrollY, vh) * 0.1}px`);
      ticking = false;
    };
    window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
    window.addEventListener("resize", onScroll);
    onScroll();
  }

  /* ---------- Hover preview that follows the cursor (mouse only) ---------- */
  const previewRows = $$("[data-preview]");
  if (previewRows.length && window.matchMedia("(hover: hover) and (pointer: fine)").matches && !reduceMotion) {
    const box = document.createElement("div");
    box.className = "hover-preview"; box.setAttribute("aria-hidden", "true"); box.innerHTML = '<img alt="">';
    document.body.appendChild(box);
    const img = box.firstChild;
    let x = 0, y = 0, cx = 0, cy = 0, running = false, active = false;
    const follow = () => {
      cx += (x - cx) * 0.2; cy += (y - cy) * 0.2;
      box.style.transform = `translate(${cx + 24}px, ${cy - 90}px)`;
      if (active || Math.abs(x - cx) > 0.5) requestAnimationFrame(follow); else running = false;
    };
    previewRows.forEach((row) => {
      row.addEventListener("pointerenter", (e) => {
        if (e.pointerType !== "mouse") return;
        img.src = row.dataset.preview; x = cx = e.clientX; y = cy = e.clientY; active = true;
        box.classList.add("on"); if (!running) { running = true; requestAnimationFrame(follow); }
      });
      row.addEventListener("pointermove", (e) => { x = e.clientX; y = e.clientY; });
      row.addEventListener("pointerleave", () => { active = false; box.classList.remove("on"); });
    });
    window.addEventListener("scroll", () => { active = false; box.classList.remove("on"); }, { passive: true });
  }

  /* ---------- Count-up numbers ---------- */
  const counters = $$("[data-count]");
  if (counters.length) {
    const run = (el) => {
      const end = parseFloat(el.dataset.count), suffix = el.dataset.suffix || "";
      const fmt = (x) => x.toLocaleString("en-GB", { minimumFractionDigits: dec, maximumFractionDigits: dec });
      const dec = (String(end).split(".")[1] || "").length;
      if (reduceMotion) { el.textContent = fmt(end) + suffix; return; }
      const dur = 1300, t0 = performance.now();
      const frame = (t) => { const k = Math.min(1, (t - t0) / dur); const v = end * (1 - Math.pow(1 - k, 3)); el.textContent = fmt(v) + suffix; if (k < 1) requestAnimationFrame(frame); };
      requestAnimationFrame(frame);
    };
    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver((ens) => ens.forEach((en) => { if (en.isIntersecting) { run(en.target); io.unobserve(en.target); } }), { threshold: 0.5 });
      counters.forEach((c) => io.observe(c));
    } else counters.forEach(run);
  }

  /* ---------- Only one video plays at a time ---------- */
  const videos = $$("video");
  videos.forEach((v) => v.addEventListener("play", () => videos.forEach((o) => { if (o !== v && !o.paused) o.pause(); })));

  /* ---------- Contact form → Formspree (AJAX) ----------
     Without JavaScript the form still posts to Formspree normally.
     With it, we validate inline, submit with fetch and show the result in place. */
  const form = $("[data-formspree]");
  if (form) {
    const status = $(".form-status", form);
    const btn = $("button[type=submit]", form);
    const label = $(".btn-label", btn);
    const success = form.parentElement.querySelector(".form-success");
    const fallback = 'Something went wrong sending your message. Please try again, or message me on <a href="https://www.linkedin.com/in/rtotonchi4412">LinkedIn</a>.';
    const messages = {
      first_name: { valueMissing: "Please add your first name." },
      email: { valueMissing: "Please add your email so I can reply.", typeMismatch: "That email address doesn't look quite right." },
      message: { valueMissing: "Please add a short message.", tooShort: "A little more detail, please (10 characters or more)." },
    };
    const setError = (name, msg) => {
      const field = form.elements[name];
      const slot = $(`[data-error-for="${name}"]`, form);
      if (field) field.setAttribute("aria-invalid", msg ? "true" : "false");
      if (slot) slot.textContent = msg || "";
    };
    const validate = () => {
      let first = null;
      Object.keys(messages).forEach((name) => {
        const f = form.elements[name]; const v = f.validity; let msg = "";
        for (const k of Object.keys(messages[name])) if (v[k]) { msg = messages[name][k]; break; }
        setError(name, msg);
        if (msg && !first) first = f;
      });
      if (first) first.focus();
      return !first;
    };
    Object.keys(messages).forEach((name) => form.elements[name].addEventListener("input", () => {
      if (form.elements[name].getAttribute("aria-invalid") === "true" && form.elements[name].checkValidity()) setError(name, "");
    }));
    const setBusy = (busy) => { btn.disabled = busy; form.setAttribute("aria-busy", String(busy)); label.textContent = busy ? "Sending…" : "Send"; };

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      status.textContent = ""; status.classList.remove("is-error");
      if (!validate()) return;
      const data = new FormData(form);
      const name = `${data.get("first_name")} ${data.get("last_name") || ""}`.trim();
      data.set("_subject", `${data.get("topic")}: message from ${name} via ramtintotonchi.com`);
      setBusy(true);
      try {
        const res = await fetch(form.action, { method: "POST", body: data, headers: { Accept: "application/json" } });
        if (res.ok) {
          form.reset(); form.hidden = true;
          if (success) { success.hidden = false; success.focus(); }
          return;
        }
        const body = await res.json().catch(() => ({}));
        const errs = Array.isArray(body.errors) ? body.errors : [];
        let shown = false;
        errs.forEach((er) => { if (er.field && messages[er.field]) { setError(er.field, er.message); shown = true; } });
        const general = errs.filter((er) => !er.field || !messages[er.field]).map((er) => er.message).join(" ");
        status.classList.add("is-error");
        status.innerHTML = general ? `${general} You can also message me on <a href="https://www.linkedin.com/in/rtotonchi4412">LinkedIn</a>.` : (shown ? "Please check the highlighted fields." : fallback);
      } catch (_) {
        status.classList.add("is-error");
        status.innerHTML = fallback;
      } finally { setBusy(false); }
    });

    $("[data-form-reset]", success || document)?.addEventListener("click", () => {
      success.hidden = true; form.hidden = false; form.elements.first_name.focus();
    });
  }
})();
