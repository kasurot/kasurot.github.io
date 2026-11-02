# Site map and information architecture

Written 2026-11-02 after the About/Capabilities overlap became confusing.

## What exists today

Public and linked:

- `/` Home: positioning, trust chips, the ten most recent briefs
- `/about/` Bio, a two-column "What I Do" grid, "Where I've Been", credentials, education
- `/resume/` Full experience, competencies, certifications, education
- `/briefs.html` Index of every brief, filterable by tag
- `/briefs/<Slug>/` Ten individual briefs

Public but unlinked:

- `/engage/` Capability page: five service areas, who it fits, contact through GCA. `noindex`, absent from the nav, footer and sitemap. Reachable only by typing the URL.

## Why it is confusing

Two pages answer "what do you do": the About page's "What I Do" grid and the `/engage/` capability page. That happened because `/engage/` was rewritten from an availability page into a capability page while staying unlinked, so its content was never reconciled with About. The URL still says "engage", which is the opposite of what the page now says.

## Proposed structure

One page per question, four questions:

| Question | Page |
|---|---|
| Who are you? | About: bio, history, credentials, education |
| What do you do? | Capabilities: the five service areas, who it fits, delivered through GCA |
| Can you prove it? | Briefs (writing) and Resume (full record) |

Navigation: Home, About, Capabilities, Briefs, plus LinkedIn. Resume stays in the footer button row to keep the top nav at four items.

Changes required:

1. Move the capability page to `/capabilities/` and leave `/engage/` as a redirect so existing links keep working.
2. Drop About's two-column "What I Do" grid, replacing it with two sentences and a link to Capabilities. About keeps bio, history, credentials, education.
3. Add Capabilities to the nav, the footer buttons and the sitemap; remove `noindex`.
4. Keep the rule that nothing about availability, rates, retainers, interim work or relocation appears anywhere on the site; engagements are framed as delivered through GCA Technology Services.

## If a separate capability page is unwanted

Alternative: fold the five service areas into About beneath the bio and delete `/engage/` entirely. Fewer pages, but About becomes long and mixes biography with sales content.

## Changelog

- 2026-11-02: map written; overlap between About and /engage/ identified; proposal recorded but not implemented pending a decision.
