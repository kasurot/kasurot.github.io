---
layout: post
title: "Identity Liquidation: The Four Costs Your Renewal Quote Never Shows"
date: 2026-11-11
description: "A renewal quote is one number. The decision is five, and only one of them is on the page."
tags: [Capital Efficiency, Identity Strategy, Vendor Management]
image: /images/identity-liquidation.jpg
image_width: 1600
image_height: 640
image_alt: ""
og_image: /images/identity-liquidation-og.jpg
noindex: true
permalink: /preview/cfo-guide-figure/
---


Your renewal quote will arrive with one number on it. That number is real. You negotiated hard for it. It is also the smallest number in the decision.

Retiring identity platforms is a standing part of my practice, not a project I did once. At a multi-acquisition insurance brokerage I retired a workforce identity provider rather than renew it, and at a telecom operator across five markets I consolidated five Active Directory domains into one tenant.

Neither was a rip and replace, and both reduced the number of places an access decision had to be made.

Liquidation is the word I use for retiring a platform whose function has moved somewhere else. Not a license negotiation. A planned exit with a date on it.

## What the quote does not show

The license is the only line a vendor prices. Four others are yours, and no vendor quotes them.

### Redundant licensing

You are paying twice for the same capability and calling it best of breed. Single sign-on, multi-factor and provisioning exist in more than one platform in most estates I have seen. The renewal conversation is about the discount on each line, never about whether the line should exist. It is the easiest cost to find and the hardest to act on, because every platform has a sponsor.

### Integration labor

Making two identity systems agree is real engineering, and it is invisible because it is absorbed by payroll. SAML, OIDC and SCIM connectors are configuration. The custom parts are code: the attribute mapping nobody documented, the sync job that fails quietly at month end. Somebody senior maintains those, and the cost is that the same engineer is not doing something else.

### Operational friction

Every application onboarding touches identity. When two or three systems must be satisfied, onboarding takes longer, and the delay lands on a delivery team that cannot see why. This is the cost a CFO is most likely to underweight, because it arrives as a missed date rather than an invoice.

### Security gaps

A fragmented control plane produces fragmented answers. The question of who has access to what has a different answer in each tool, and none of them is the whole answer.

Consolidation makes enumeration cheaper. It does not make it possible. An identity governance platform is what produces cross-estate access visibility, and a consolidated identity provider does not produce it alone, nor does a customer identity platform.

## You probably already own one

The overlap is rarely hypothetical.

If your organization runs Microsoft 365 E3, you already have [Entra ID P1](https://learn.microsoft.com/entra/fundamentals/licensing), which includes single sign-on, multi-factor and Conditional Access. On E5 you have P2 on top, which adds Privileged Identity Management and Identity Protection.

If you run Google Workspace, you own an identity provider too, and [it provides single sign-on for your applications over SAML or OIDC](https://support.google.com/a/answer/60224) without another platform in the path.

So the question is not which identity platform to buy. It is why you are paying a separate invoice for a capability that arrived inside a license you already renewed.

One caution before anyone acts. Owning the identity provider is not owning the feature set. If your entitlement is P1 and the workload needs P2, that is one gap. If the certification function you are replacing sits above P2, that is a larger one. Size it before you size the saving, because the example below shows what happens when you do not.

This cost hides better than the other three because the bundled entitlement never appears as an identity line. It appears as a productivity license, owned by a different budget and renewed by a different team. Nobody puts the two invoices side by side, and the overlap survives another year.

The honest counter is that the bundle is not a complete substitute. Okta's application catalog is deeper than most, its neutrality matters outside a Microsoft shop, and customer identity is a separate category neither bundle replaces well. That is the part worth paying for. The rest is duplication with a support contract, and the test is whether the applications that genuinely need the specialist justify a separate platform.

## Separate the subscription from the work

The subscription is the line on the invoice. The work around the platform is the line that never appears there: the people who keep it in step, the connectors, the reviews that run twice.

So measure your own. Four inputs produce it. What the specialist platform costs all in, and how much of that is license rather than people. How much capability exists in more than one platform. What the move costs. And the surviving platform's run rate after the governance uplift and the repricing.

License and people have to be separated, because they behave differently. A retired license is cash that stops leaving the building. The people who ran it usually redeploy, so their cost returns as capacity, not money. Both are real. Only one pays back a project.

Then phase it. The move cost divided by the monthly saving is not a payback period, because the saving does not begin until the old contract ends. Payback from today is the months remaining on that contract plus the move cost divided by the monthly saving. Divide only the cost of the move and you assume savings start in month one, which understates payback by the remaining term.

Here is a composite example, and I am labeling it as one. Three thousand seats, already running both platforms, which is the situation this brief is about.

Okta publishes 17 dollars per user per month for its Essentials suite, which bundles single sign-on, lifecycle management and access governance. Microsoft publishes [10 dollars for Entra ID P2](https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing), whose own feature list includes basic entitlement management and basic access reviews, and 7 dollars for the governance tier above it. Your agreement will differ from list, but the ratios hold.

At three thousand seats Okta Essentials is 612,000 a year. The people who run it cost another 110,000, but they redeploy rather than leave, so that is capacity, not cash. The cash saving is the subscription.

Say the contract runs another twelve months and the migration takes nine, so the work finishes first. The move costs 90,000 of migration labor and nothing to leave, because you go at the notice date.

Now run it three times, because the tier decides the answer.

<style>
  .cashfig { margin: 2.4rem 0 2.6rem; }
  .cashfig__title {
    font-family:'Book Antiqua',Palatino,'Palatino Linotype',Georgia,serif;
    font-size:1.18rem; font-weight:700; color:var(--header-blue);
    margin:0 0 1.3rem; line-height:1.3;
  }
  .cashfig__panel + .cashfig__panel { margin-top:1.9rem; padding-top:1.6rem; border-top:2px solid var(--border-medium); }
  .cashfig__ptitle {
    font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    font-size:.74rem; letter-spacing:1.5px; text-transform:uppercase;
    font-weight:700; color:var(--text-gray); margin:0 0 .3rem;
  }
  .cashfig__psub { font-size:.9rem; color:var(--text-gray); margin:0 0 1rem; line-height:1.45; }
  .cashfig__rows { list-style:none; margin:0; padding:0; }
  .cashfig__row { padding:.85rem 0; border-top:1px solid var(--border-light); }
  .cashfig__row:first-child { border-top:none; padding-top:0; }
  .cashfig__head { display:flex; justify-content:space-between; align-items:baseline; gap:.5rem 1rem; flex-wrap:wrap; }
  .cashfig__who {
    font-family:'Book Antiqua',Palatino,'Palatino Linotype',Georgia,serif;
    font-weight:700; font-size:.97rem; color:var(--header-blue); line-height:1.35;
  }
  .cashfig__val {
    font-family:'Book Antiqua',Palatino,'Palatino Linotype',Georgia,serif;
    font-weight:700; font-size:1.16rem; color:var(--header-blue); white-space:nowrap;
  }
  .cashfig__val small { font-family:inherit; font-weight:400; font-size:.8rem; color:var(--text-gray); }
  .cashfig__track {
    position:relative; display:block; width:100%; height:13px; margin:.55rem 0 .45rem;
    background:var(--border-light); border-radius:3px; overflow:hidden;
  }
  .cashfig__fill { display:block; height:100%; background:var(--header-blue); border-radius:3px 0 0 3px; }
  /* Month 12: the contract ends and saving can begin. Marked on every row so the wait is
     visible rather than buried in a sentence. */
  .cashfig__tick {
    position:absolute; top:-3px; bottom:-3px; left:60%; width:2px;
    background:var(--accent-gold);
  }
  /* Not applicable rather than zero: a hatch, so the never row cannot be read as a
     short bar, which in this panel would mean the best outcome. */
  .cashfig__track--never {
    background: repeating-linear-gradient(45deg,
      var(--border-medium) 0 4px, transparent 4px 9px);
    background-size: 40% 100%; background-position: 60% 0; background-repeat: no-repeat;
  }
  .cashfig__detail { font-size:.9rem; line-height:1.5; color:var(--text-body); margin:0; }
  .cashfig__detail strong { color:var(--header-blue); }
  .cashfig__scale {
    display:flex; justify-content:space-between;
    font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    font-size:.74rem; color:var(--text-gray); margin:.1rem 0 0;
  }
  .cashfig__axis { position:relative; height:1.05rem; margin:.1rem 0 0;
    font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    font-size:.74rem; color:var(--text-gray); }
  .cashfig__axis span { position:absolute; top:0; }
  .cashfig__axis .a-mid { left:60%; transform:translateX(-50%); color:var(--accent-gold); font-weight:700; }
  .cashfig__axis .a-end { right:0; }
  .cashfig__caption { margin-top:1.2rem; font-size:.85rem; color:var(--text-gray); font-style:italic; }
  .sr-only { position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0; }
  @media (prefers-color-scheme: dark) {
    body:not(.light-mode) .cashfig__detail strong { color:var(--text-dark); }
    body:not(.light-mode) .cashfig__tick { background:var(--accent-gold); }
  }
</style>

<figure class="cashfig" aria-labelledby="cashfig-title">
  <p class="cashfig__title" id="cashfig-title">What you save, and when it comes back</p>

  <div class="cashfig__panel">
    <p class="cashfig__ptitle">What you save each month, per seat</p>
    <p class="cashfig__psub">Against the $17 Okta charges. This is the line the tier decides.</p>
    <ul class="cashfig__rows">
      <li class="cashfig__row">
        <div class="cashfig__head">
          <span class="cashfig__who">E5, P2 already owned</span>
          <span class="cashfig__val">$17</span>
        </div>
        <span class="cashfig__track" aria-hidden="true"><span class="cashfig__fill" style="width:100%"></span></span>
        <span class="sr-only">Bar length: 100 percent of the $17 maximum. Saves 17 dollars per seat per month.</span>
      </li>
      <li class="cashfig__row">
        <div class="cashfig__head">
          <span class="cashfig__who">Buy P2 at $10</span>
          <span class="cashfig__val">$7</span>
        </div>
        <span class="cashfig__track" aria-hidden="true"><span class="cashfig__fill" style="width:41%"></span></span>
        <span class="sr-only">Bar length: 41 percent of the $17 maximum. Saves 7 dollars per seat per month.</span>
      </li>
      <li class="cashfig__row">
        <div class="cashfig__head">
          <span class="cashfig__who">Buy P2 plus governance, $10 and $7</span>
          <span class="cashfig__val">$0</span>
        </div>
        <span class="cashfig__track" aria-hidden="true"></span>
        <span class="sr-only">No saving. Zero percent of the $17 maximum.</span>
      </li>
    </ul>
  </div>

  <div class="cashfig__panel">
    <p class="cashfig__ptitle">When the cash comes back</p>
    <p class="cashfig__psub">Months until the cash is back, so <strong>shorter is better</strong>. The move costs $90,000 before any saving lands, and nothing is recovered until the contract ends. The gold line marks month 12.</p>
    <ul class="cashfig__rows">
      <li class="cashfig__row">
        <div class="cashfig__head">
          <span class="cashfig__who">E5, P2 already owned</span>
          <span class="cashfig__val">14 <small>months</small></span>
        </div>
        <span class="cashfig__track" aria-hidden="true">
          <span class="cashfig__fill" style="width:70%"></span>
          <span class="cashfig__tick"></span>
        </span>
        <span class="sr-only">Payback at 14 months: 12 months waiting for the contract to end, then about 2 months of recovery.</span>
        <p class="cashfig__detail">Twelve months of waiting, then <strong>two of recovery</strong>. Saves <strong>$612,000 a year</strong> once it starts.</p>
      </li>
      <li class="cashfig__row">
        <div class="cashfig__head">
          <span class="cashfig__who">Buy P2 at $10</span>
          <span class="cashfig__val">16 <small>months</small></span>
        </div>
        <span class="cashfig__track" aria-hidden="true">
          <span class="cashfig__fill" style="width:80%"></span>
          <span class="cashfig__tick"></span>
        </span>
        <span class="sr-only">Payback at 16 months: 12 months waiting, then about 4 months of recovery.</span>
        <p class="cashfig__detail">Twelve months of waiting, then <strong>four of recovery</strong>. Saves <strong>$252,000 a year</strong> once it starts.</p>
      </li>
      <li class="cashfig__row">
        <div class="cashfig__head">
          <span class="cashfig__who">Buy P2 plus governance</span>
          <span class="cashfig__val">never</span>
        </div>
        <span class="cashfig__track cashfig__track--never" aria-hidden="true"><span class="cashfig__tick"></span></span>
        <span class="sr-only">No payback. Saving is zero, so the 90,000 dollar move never comes back on the subscription line.</span>
        <p class="cashfig__detail">Saving is zero, so <strong>the $90,000 never comes back</strong> on the subscription line. License governance to the subset that needs it and the case rests on control and capacity, not cash.</p>
      </li>
    </ul>
    <div class="cashfig__axis" aria-hidden="true"><span style="left:0">0</span><span class="a-mid">12</span><span class="a-end">20 months</span></div>
  </div>

  <figcaption class="cashfig__caption">Three thousand seats. Vendor list prices: Okta Essentials $17, Entra ID P2 $10, the governance tier above P2 $7 per user per month. A composite example, labeled as one in the brief. Your agreement will differ; the ratios are the point.</figcaption>
</figure>


On Microsoft 365 E5, P2 is already paid for, so the whole 612,000 comes out. Divide 90,000 by the monthly saving of 51,000 and you get under two months, which is how long recovery takes once the saving starts. It is not the payback period, because nothing is recovered until the old contract ends. From the day you begin it is fourteen months: twelve of waiting, then two of recovery.

If P2 has to be bought, the replacement is 10 dollars a seat, or 252,000 a year here. The saving falls to 7 dollars a seat, about 21,000 a month, and payback is sixteen months.

If the estate needs the governance tier as well, P2 plus Governance is 17 dollars a seat. That is exactly what Okta charges, so the cash saving is zero. The case does not fail, but it stops being a cost case and has to stand on capacity and defensibility alone.

The license comparison, not the migration, decides whether there is a business case at all.


## What comes back, and what it costs

Two things come back.

**The estate becomes defensible.** An estate you cannot enumerate is one you cannot defend, because the first question in an incident, an audit or a review is who had access, and a fragmented estate answers it differently in every tool. An audit does not score your architecture. It asks who had access, and the answer has to be complete. Consolidation makes that answer cheaper to produce. The governance tier is what makes it possible, which is why the tier matters more than the platform you retire.

**Capacity comes back to delivery.** Every platform you retire is a set of run tasks that stop existing: the certification campaign that runs in two tools, the connector fixed twice, the upgrade window that consumes a weekend. Measure it in hours per month from the people who do the work, not as a percentage. Then decide where those hours go, because if nobody decides, they get absorbed.

Four things it costs, and the case for consolidation usually omits all four.

**The write-down.** Migration labor, the months both platforms are live, and any termination fee if you cannot wait for the notice date, all land before any saving does. A program that shows savings without a payback period is a brochure.

**The governance tier.** P2 already carries basic entitlement management and basic access reviews, which Microsoft states on its own pricing page. Above P2 is a different tier: [machine-assisted certifications, catalog-wide reviews, custom data resources and lifecycle workflows](https://learn.microsoft.com/entra/id-governance/licensing-fundamentals), published at 7 dollars a seat. That is a separate purchase, and the example above shows what it does to the arithmetic. Reviewing service principals sits above both and needs Workload Identities Premium at 3 dollars a seat.

**Partial overlap.** Two platforms rarely duplicate everything. When the part that does not overlap is a regulated requirement or a capability the survivor lacks, you keep both, and the saving you modeled was never available. Find that non-overlapping tail before you commit, not after.

**Vendor concentration.** Retiring platforms hands pricing power to the survivor, who reprices at the next renewal. Price protection and exit terms belong in the consolidation plan, not in a later negotiation.

## The trigger, and the question

No vendor deadline will force this, and you should not wait for one. Consolidation is cheapest when a renewal is already in front of you, because the notice date is the only point at which you can decline to renew at no cost. Once it passes you have bought another year of the thing you were trying to remove.

So put every identity platform's notice date on one page and work from the earliest. That is your window, and your contracts set it.

Then ask one question in your next identity review. If we could keep only one platform per job, meaning one workforce identity provider, one customer identity platform, one governance tool and one privileged access platform, which would they be, and which of the rest are we keeping because nobody wants the conversation?

The answer gives you the liquidation list. The renewal notice date gives you the deadline. Which one are you retiring this fiscal year?
