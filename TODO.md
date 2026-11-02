# Site TODO

Issues found while auditing the non-brief pages and running the About/Capabilities roundtable, 2026-11-02. Ordered by what could actually cost something.

## P1 — employer-sensitive or credibility-damaging

- [ ] **`/resume/` publishes GCA's commercial model.** The page carries "Business Model Pivot (NRE to ARR)", "high-margin 'Managed Identity' subscriptions", "gamifying the acquisition of high-value technical competencies", the line "I don't just architect systems. I warrant the outcome", and client descriptors ("a National Retail Enterprise", Ping DaVinci NAF/ATO work). Kevin is redoing the resume; fold this into that pass rather than patching twice.
- [ ] **Home `<title>` is job-seeker framing.** "Kevin Armstrong | Strategic IT Executive & Systems Architect" appears in every browser tab and search snippet. Should read as what he does, not what he is applying for.
- [ ] **Briefs carry no employer attribution.** Ten briefs, zero mentions of GCA, while gca.net/blog runs overlapping posts by the same author (AI agents, Zero Trust, AD consolidation, platform consolidation). Decide a one-line byline plus a canonical/syndication rule with GCA marketing.

## P2 — structural

- [ ] **Extract the stylesheet.** An identical ~18KB `<style>` block is duplicated in every page; a CSS change means editing every file. Move to `/assets/site.css`.
- [ ] **Heading structure.** Two `<h1>`s per page (the wordmark in the header) and briefs use `###` for sections, skipping h2 entirely.
- [ ] **No post limits.** `/` and `/briefs.html` render every brief with no `limit:`. Fine at ten posts, unmanageable at thirty-four.
- [ ] **Tag filter drift.** `allowed_tags` is hardcoded in two files and the live tag "Ownership" has no filter button, so that brief cannot be filtered.
- [ ] **Social cards.** Nine of ten briefs have no `og:image`, so they unfurl as bare text links. The briefs index has no thumbnails; enable them once three briefs carry images so the index does not look half-built.

## P3 — polish

- [ ] **Hero image weight.** 235KB served at 716 CSS px. Add a 760w derivative and `srcset`.
- [ ] **Numbers below the fold on About.** 10,000+ users and roughly 1,700 service principals sit in paragraph two; both are worth more to a buyer than the entire certification list.
- [ ] **SC-401 naming.** Shown as "Information Security Administrator"; "Information Protection Administrator" may be the more recognisable label.
- [ ] **Retire `/engage/`.** It is now a redirect to `/capabilities/`; delete once old links have aged out.
- [ ] **Print check.** Print CSS forces all `details` open; confirm the resume prints within the intended page count.

## Done, so it does not get re-litigated

- Sitemap rebuilt from `absolute_url`; the apex domain it pointed at has no DNS record, so all 15 URLs were dead.
- `site.url` set, so `og:image` is https.
- Hero images render as a 5:2 band with intrinsic dimensions, `eager` and `fetchpriority=high`; the old full-width 4:5 portrait pushed the first sentence 1.5 screens down and caused an ~831px layout shift.
- Alt policy: `image_alt` renders as given, empty means decorative; the template no longer falls back to the page title.
- Certifications on About and Resume: highlights plus an expandable full list of 29 named credentials.
- Footer navigation is a row of five icon buttons on desktop, matching the mobile tab bar; the duplicate text-link row is gone.
- Home hero CTAs removed; the briefs list starts immediately below.
- Capabilities is public, linked and indexed; About carries a pointer instead of a duplicate grid.
