# Visual production for the weekly brief

Companion to VISUAL-FORMATS.md (what may go in a figure) and the dense-figure
HTML/CSS component (how it renders). This note answers the production question:
what does one person actually do each week, for how many minutes, with which
files, without the process collapsing by week five.

## 1. Minimum viable visual package per brief

One figure per brief is the default. A second figure is allowed only when the
thesis has two independent structural claims, and it costs an extra 15 minutes.
A brief with no figure (hero photo only) is a legitimate ship.

Per-brief elements and their cost:

- Hero photo (1600x640, doubles as the 5:2 band): 5 to 10 minutes. Source from
  Unsplash or Pexels, crop to 1600x640, export the 1200x630 OG variant. If an
  AI image is used instead, 10 to 15 minutes.
- One figure, templated HTML/CSS (dense-figure include or a template from the
  set below): 15 to 25 minutes. This is the default.
- One figure, templated SVG (one of the six structural formats): 20 to 30
  minutes. Use when the claim is topological (sequence, hierarchy, layering) and
  vector scaling matters.
- One figure, generated chart (Python, data already in hand): 5 to 10 minutes.
  Use when the claim is quantitative. Budget 30 plus minutes if the data needs
  cleaning; in that case the chart is not a this-week task.
- Evidence plate (annotated screenshot): 30 to 45 minutes. The differentiator.
  Use when the brief discusses a concrete artifact the reader can point at.
- LinkedIn card derived from the figure: 2 minutes automated via
  _visuals/render.py, plus 3 minutes of caption writing.
- Phone QA at 350px: 5 minutes.

Realistic weekly total: 30 to 45 minutes for a templated figure plus the hero
and the LinkedIn card. Hard cap: 60 minutes. If the figure is not done by
minute 40, ship hero-only and log the topic for a future template.

## 2. Where the reuse comes from

Author each figure bespoke only when no template fits, which should be rare.
Build a small library of templates and fill them. The eight templates below
cover roughly 85 to 90 percent of the structural claims in identity and IAM
leadership briefs.

Template set (one file each under _visuals/templates/):

1. Vertical step strip (sequence, stages, handoffs, where a process breaks).
2. 2x2 matrix (classification, trade-off, ownership, build versus buy).
3. Layered stack (control placement, gaps, trust boundaries).
4. Small multiples (magnitude comparison, relative size, trend).
5. Comparison table (side-by-side attributes across 2 to 3 options).
6. Evidence plate (annotated screenshot of a real artifact).
7. Card grid (dense-figure HTML, 3 to 4 named sub-claims with one-line bodies).
8. Timeline or roadmap (phases, waves, migration sequence).

Coverage by topic type:

- Process and lifecycle claims (provisioning, onboarding, incident response):
  templates 1 and 8, about 30 percent of briefs.
- Architecture and control placement (zero trust, IAM maturity, trust
  boundaries): templates 3 and 2, about 25 percent.
- Comparison and selection (vendor, tool, tier): templates 5 and 2, about 20
  percent.
- Quantitative claims (coverage, cost, adoption): template 4, about 10 percent.
- Concrete artifact grounding: template 6, about 10 percent, and it is the
  differentiator.
- Multi-claim overviews: template 7, about 5 percent, used sparingly.

That leaves roughly 10 to 15 percent of briefs needing a bespoke figure or no
figure at all. A bespoke figure is a monthly budget item (one per month at
most), never a weekly one.

Setup cost: a one-time 4 hour sprint to create the eight template files and
the render script. After that, weekly work is filling slots.

## 3. Dark mode maintenance burden

Hand-authored SVG with hardcoded fills is the expensive path. Every colour
needs a light and dark variant, the two palettes drift apart over time, and
each figure has to be checked in both themes. For one person that is the
single most likely reason the process dies.

Cheaper ways to get both, in order of preference:

- HTML/CSS figures using the site's CSS variables. Dark mode is free because
  the variables already flip. Zero extra minutes per figure. This is the
  default.
- SVG authored with currentColor and CSS variables inside the SVG, so it
  inherits the theme. About 5 extra minutes per figure, and it still has to be
  checked in both themes.
- SVG placed on a light card (white or near-white background with a border)
  so it always renders on a light surface regardless of site theme. Zero
  dark-mode work, and it reads as intentional. Use this for the six structural
  formats.
- For screenshots used on LinkedIn, always render on a white background. Never
  screenshot a dark-themed page for a social card.

Recommendation: default to HTML/CSS figures for the article. Reserve SVG for
the six structural formats where vector scaling matters, and author those with
currentColor inside a light card wrapper.

## 4. LinkedIn: highest-value visual per brief

The highest-value output is an image post, not a link preview. A single card
at 1200x627 (or 1080x1080 for a square) that carries the figure plus the
brief's title, posted as an image with the summary in the caption and the
link in the first comment.

It is derived from the article figure without a second design job:

1. The figure already exists as a standalone HTML file in _visuals/ (one file
   per figure, created during the brief's figure step).
2. Run `python3 _visuals/render.py <figure.html> <out_basename>` to produce
   the 1200x627 and 1080x1080 PNGs. Two minutes, no design work.
3. Upload the PNG to LinkedIn. Caption is the brief's two-sentence summary.
   Link goes in the first comment.

Why this works: image posts outperform link previews on LinkedIn, and the
figure already carries the insight. The render step is mechanical. No Figma,
no Canva, no second pass.

## 5. Failure mode and how to avoid it

The failure mode is per-brief bespoke design. A new figure designed from
scratch each week takes 60 to 90 minutes, the weekly budget slips, the figure
becomes the thing that gets cut, and by week four or five the briefs go back
to prose plus a stock photo. The process is abandoned not because it failed but
because it was never sized to one person's week.

Avoidance, concretely:

- Week zero: one 4 hour sprint creates the eight templates and render.py.
  Nothing else ships that week.
- Weekly rule: fill a template, never design. If no template fits, use no
  figure and log the topic.
- Hard cap of 60 minutes. At minute 40 with no figure, stop and ship hero-only.
- Figure on 3 of 4 briefs. The newsy or reactive brief ships hero-only.
- One bespoke figure per month at most, budgeted separately.
- Measure by "did a figure ship this week," not by how good it was.

Files involved each week:

- _briefs/<slug>.md (the brief)
- _includes/figures/<slug>.html (the figure, single source for article and
  LinkedIn)
- _visuals/render.py (mechanical export)
- images/<slug>.jpg and images/<slug>-og.jpg (hero)
- The LinkedIn PNG in _visuals/out/ (throwaway, not committed)

The process survives because the weekly decision is "which template" (2
minutes) and "which words" (15 minutes), not "what should this look like."
