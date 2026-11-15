# Site TODO

Issues found while auditing the non-brief pages and running the About/Capabilities roundtable, 2026-11-02. Ordered by what could actually cost something. Updated 2026-11-15 after the C-suite audience interviews and the six-seat design roundtable.

## P1 — employer-sensitive or credibility-damaging

- [x] **`/resume/` published GCA's commercial model.** Rebuilt from the new resume master, 2026-11-02: NRE-to-ARR, margin, "I warrant the outcome" and the client descriptors are gone; the page and the document now say the same thing.
- [ ] **Home `<title>` is job-seeker framing.** "Kevin Armstrong | Strategic IT Executive & Systems Architect" appears in every browser tab and search snippet. Should read as what he does, not what he is applying for.
- [ ] **Briefs carry no employer attribution.** Ten briefs, zero mentions of GCA, while gca.net/blog runs overlapping posts by the same author (AI agents, Zero Trust, AD consolidation, platform consolidation). Decide a one-line byline plus a canonical/syndication rule with GCA marketing.
- [ ] **The site reads as a consultant, not an operator.** Brand roundtable verdict, 2026-11-15. Six named causes: the three-noun pipe tagline; `/capabilities/` being a services page ("HOW I CAN HELP", "WHO THIS FITS", "Client engagements are contracted through GCA Technology Services"); the home hero being a value proposition rather than a point of view; "Director of Professional Services" sitting in the hero; the credential chips including an unfinished degree; `/resume/` existing at all. Kevin approved changing this. Smallest-first order: kill the hero pitch and capability band, demote the services title, remove `/resume/` from nav, fold Capabilities into About, change the tagline to a plain descriptor.
- [ ] **Credential chips say "MSIT, WGU 2026" as if pending.** The degree completed in October 2026. Update to reflect completion rather than an expected date.

## P2 — structural

- [ ] **Newsletter signup does not exist.** All four C-suite readers named a newsletter as the right ask; the CISO said "a newsletter signup is the right ask, not book a demo." There is no `<form>`, no input and no email field anywhere on the site. Requires wiring a system (provider, list, confirmation, double opt-in, unsubscribe). Highest-value missing element on the site.
- [ ] **Revisit the hero imagery.** Kevin's call 2026-11-15: keep for now, revisit later. The audience said atmospheric photography reads as filler and the CIO named AI-generated imagery as a credibility tell. Work artifacts are not available because almost all of the underlying work is under NDA. The ingots hero on every-control-asked-whether was removed because it predated the current image gate. Four heroes remain.
- [ ] **Heroes on a dark ground.** Three of four C-suite readers independently named this as the amateur tell that kills credibility: an image with a light background sitting as a hard bright rectangle on a dark page. All four heroes are opaque JPEGs, so in dark mode they punch a glowing box into the page. Options: a dark-mode `filter` to dim them, a dark variant of each, a subtle inner border to read them as intentional plates, or no heroes. Unresolved because it overlaps the hero-revisit decision above.
- [ ] **Extract the stylesheet.** An identical ~26KB `<style>` block is duplicated in every page; a CSS change means editing every file. Move to `/assets/site.css`. Low risk on GitHub Pages, and it buys cross-page caching.
- [ ] **Heading structure.** Two `<h1>`s per page (the wordmark in the header) and briefs use `###` for sections, skipping h2 entirely. The design roundtable flagged the H1 to H3 jump as an accessibility failure. Demote the masthead and promote section headings.
- [ ] **No skip-to-content link**, and three `<nav>` landmarks need distinct `aria-label`s.
- [ ] **Pop-out pattern removed.** The hover pop-out on pam-coverage-gap was deleted 2026-11-15 because it was `display:none` below 640px, which deleted the content on the phone-first audience rather than relocating it. The appendix at the end of the brief remains. If secondary detail is ever needed inline again, use native `<details>`.
- [ ] **Social cards.** Nine of ten briefs have no `og:image`, so they unfurl as bare text links.

## P3 — polish

- [x] **Hero image weight.** Was 159-190KB served at 716 CSS px. Now 716w and 1432w WebP plus JPEG derivatives in a `<picture>` with `srcset` and `sizes`: 24-36KB at 716w, a 5-7x cut. `fetchpriority="high"` removed because it prioritised a decorative image over the writing.
- [ ] **Numbers below the fold on About.** 10,000+ users and roughly 1,700 service principals sit in paragraph two; both are worth more to a buyer than the entire certification list.
- [ ] **SC-401 naming.** Shown as "Information Security Administrator"; "Information Protection Administrator" may be the more recognisable label.
- [ ] **Retire `/engage/`.** It is now a redirect to `/capabilities/`; delete once old links have aged out.
- [ ] **Print check.** Print CSS forces all `details` open; confirm the resume prints within the intended page count.
- [ ] **Lead paragraph treatment removed.** It was 5 percent larger in the accent colour at a phantom 500 weight. Cut 2026-11-15; the briefs open with a declarative that stands as body copy.

## Done, so it does not get re-litigated

- Sitemap rebuilt from `absolute_url`; the apex domain it pointed at has no DNS record, so all 15 URLs were dead.
- `site.url` set, so `og:image` is https.
- Alt policy: `image_alt` renders as given, empty means decorative; the template no longer falls back to the page title.
- Certifications on About and Resume: highlights plus an expandable full list of 29 named credentials.
- Footer navigation is a row of five icon buttons on desktop, matching the mobile tab bar; the duplicate text-link row is gone.
- Home hero CTAs removed; the briefs list starts immediately below.
- Capabilities is public, linked and indexed; About carries a pointer instead of a duplicate grid.
- The Wharton entry was wrong on the site and in the resume: it is a Business Foundations Specialization (Coursera / University of Pennsylvania), not Wharton Executive Education. Corrected in both.
- Resume rebuilt from the master: 34 Microsoft certifications, SC-300 and ISO 27701 named, no phone, no expiry dates.
- **Tag sprawl consolidated to three topics, 2026-11-15.** Fourteen tags became Identity & Access (5), Risk & Governance (3), Capital & Vendors (4). The briefs index is now topic-first with a chronological Latest section beneath, matching the Microsoft Security Blog pattern Kevin confirmed.
- **Read time and deks on every card, 2026-11-15.** Computed from stripped text at 200 wpm, rounded up.
- **Measure fixed, 2026-11-15.** `.post` constrained to 36rem and body raised to 1.15rem, which puts the line at roughly 65 characters instead of the measured 83.
- **Prose links given a rule, 2026-11-15.** No rule existed at all; links rendered as browser default `rgb(0,0,238)` at a measured 1.90:1 in dark mode. Now `#7A4800` light (7.05:1) and `#E9B65A` dark (9.66:1), always underlined, with hover, visited and focus states.
- **Heading scale fixed, 2026-11-15.** H1 and H2 were both 28px, so the brief title and its sections were the same size. Now H1 40px, H2 26px at 600, H3 22px.
- **Ground warmed, 2026-11-15.** `#f8fafc` cool blue-white to `#F7F6F3`, which is what every C-suite reader asked for.
- **Theme flash fixed, 2026-11-15.** The saved theme class was applied by a script at the end of `<body>`, so a saved-light reader on a dark-mode OS saw a dark flash before it flipped. Now a blocking script in `<head>` applies it to `:root` before first paint, and the toggle carries `aria-pressed`.
