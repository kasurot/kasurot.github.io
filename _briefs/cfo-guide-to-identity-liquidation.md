---
layout: post
title: "Identity Liquidation: The Four Costs Your Renewal Quote Never Shows"
date: 2026-11-11
description: "A renewal quote is one number. The decision behind it is five, and only one of those appears on the page you were sent. Here is the arithmetic."
tags: [Capital Efficiency, Identity Strategy, Vendor Management]
topic: "Capital & Vendors"
image: /images/identity-liquidation.jpg
image_width: 1600
image_height: 640
image_alt: "A plant room with two parallel pipe runs crossing the frame. The upper run is wrapped in pale gray insulation held by metal banding. Below it a bare steel pipe runs rusted and flaking, fitted with an open cast iron valve dripping onto the concrete floor."
og_image: /images/identity-liquidation-og.jpg
approved: true
---

Your renewal quote will arrive with one number on it. That number is real. You negotiated hard for it. It is also the smallest number in the decision.

Identity platforms do get retired rather than renewed. A workforce identity provider reaches its renewal after the function has already moved somewhere else, or five Active Directory domains consolidate into one tenant across five markets. Neither is a rip and replace, and both cut where an access decision is made.

Liquidation means retiring a platform whose function has moved somewhere else. Not a license negotiation. A planned exit with a date on it.

## The quote prices one of five costs

The license is the only line a vendor prices. Four others are yours.

### You are paying twice for the same capability

You are paying twice and calling it best of breed. Single sign-on, multi-factor and provisioning exist in more than one platform in most estates. The renewal conversation is about the discount on each line, never about whether the line should exist. It is the easiest cost to find and the hardest to act on, because every platform has a sponsor.

### The integration work is absorbed by payroll

Making two identity systems agree is real engineering, and it is invisible because it is absorbed by payroll. SAML, OIDC and SCIM connectors are configuration. The custom parts are code: the attribute mapping nobody documented, the sync job that fails quietly at month end. Somebody senior maintains those, and the cost is that the same engineer is not doing something else.

### Onboarding slows and nobody can see why

When two or three systems must be satisfied, onboarding takes longer, and the delay lands on a delivery team that cannot see why. This is the cost a CFO is most likely to underweight, because it arrives as a missed date, not an invoice.

### A fragmented estate cannot answer who had access

A fragmented control plane produces fragmented answers. The question of who has access to what has a different answer in each tool, and none of them is the whole answer.

## You probably already own one

If your organization runs Microsoft 365 E3, you already have [Entra ID P1](https://learn.microsoft.com/entra/fundamentals/licensing), which includes single sign-on, multi-factor and Conditional Access. On E5 you have P2 on top, which adds Privileged Identity Management and Identity Protection.

If you run Google Workspace, you own an identity provider too, and [it provides single sign-on for your applications over SAML or OIDC](https://support.google.com/a/answer/60224) without another platform in the path.

The question is not which identity platform to buy, but why you pay a separate invoice for a capability you already renewed.

One caution. Owning the identity provider is not owning the feature set. If your entitlement is P1 and the workload needs P2, that is one gap. Size it before you size the saving.

This cost hides because the bundled entitlement appears as a productivity license, owned and renewed by a different team, never as an identity line. Nobody puts the two invoices side by side, and the overlap survives another year.

The bundle is not a complete substitute. Okta's application catalog is deeper than most, its neutrality matters outside a Microsoft shop, and customer identity is a separate category neither bundle replaces well. That is the part worth paying for. The rest is duplication with a support contract, and the test is whether the applications that genuinely need the specialist justify a separate platform.

## The decision, before the arithmetic

The arithmetic later in this brief supports a direction you can take before it. Take the direction first: which platforms go, on what notice date, against what justification. Ratify each retirement once the governance tier is quoted, because that is the one input that can reverse the case.

**The ask.** The board directs management to consolidate to one platform per job and to bring the next technology and risk committee a liquidation list naming each platform's non-renewal notice date and planned retirement quarter, with no duplicative platform renewed absent documented justification.

**The reporting.** That committee sees four numbers every quarter: platforms held per job, license spend per platform and the spend on duplicate capability, platforms with a recorded notice date and a dated retirement decision, and capacity hours returned. The self-test is a two-quarter rule. Any job category still holding more than one platform for two consecutive quarters without a documented non-overlap justification escalates to the board.

That is a direction a board can record without ever seeing a payback calculation. The ratification is where the arithmetic belongs, and the rest of this brief is the working that shows what the arithmetic has to survive.

## Separate the subscription from the work

The subscription is the line on the invoice; the work around it never appears there.

Measure your own with four inputs. What the specialist platform costs all in, and how much is license rather than people. How much capability exists in more than one platform. What the move costs. And the surviving platform's run rate after the governance uplift and the repricing.

License and people have to be separated, because they behave differently. A retired license is cash that stops leaving the building. The people who ran it usually redeploy, so their cost returns as capacity, not money. Both are real. Only one pays back a project.

Then phase it. The move cost divided by the monthly saving is not a payback period, because the saving does not begin until the old contract ends. Payback from today is the months remaining on that contract plus the move cost divided by the monthly saving. Dividing only the move cost assumes savings start in month one.

A composite example, labeled as one: three thousand seats already running both platforms.

Okta publishes [17 dollars per user per month for its Essentials suite](https://www.okta.com/pricing/), which bundles single sign-on, lifecycle management and access governance. Microsoft publishes [10 dollars for Entra ID P2](https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing), whose own feature list includes basic entitlement management and basic access reviews. Both are list prices as of November 2026. Your agreement will differ from list, but the ratio is the point.

At three thousand seats Okta Essentials is 612,000 a year. The people who run it cost another 110,000, roughly two fully loaded engineers, but they redeploy rather than leave, so that is capacity, not cash. The cash saving is the subscription.

Say the contract runs another twelve months and the migration takes nine, so the work finishes first. The move costs 90,000 of migration labor, around half a year of one senior engineer plus contractor time, and nothing to leave, because you go at the notice date.

Then run it twice, because the entitlement decides the answer.

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
    position:absolute; top:-3px; bottom:-3px; left:60%; width:3px;
    background:var(--accent-gold);
  }
  .cashfig__detail { font-size:.9rem; line-height:1.5; color:var(--text-body); margin:0; }
  .cashfig__detail strong { color:var(--header-blue); }
  .cashfig__axis { position:relative; height:1.35rem; margin:.15rem 0 0;
    padding-top:.25rem; border-top:1px solid var(--border-medium);
    font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    font-size:.8rem; color:var(--text-body); }
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
    <p class="cashfig__psub">Against the $17 Okta charges. This is the line the entitlement decides.</p>
    <ul class="cashfig__rows">
      <li class="cashfig__row">
        <div class="cashfig__head">
          <span class="cashfig__who">E5, P2 already owned, best case</span>
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
    </ul>
  </div>

  <div class="cashfig__panel">
    <p class="cashfig__ptitle">When the cash comes back</p>
    <p class="cashfig__psub">Months until the cash is back, so <strong>shorter is better</strong>. The move costs $90,000 before any saving lands, and nothing is recovered until the contract ends. The gold line marks month 12.</p>
    <ul class="cashfig__rows">
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
    </ul>
    <div class="cashfig__axis" aria-hidden="true"><span style="left:0">0</span><span class="a-mid">12</span><span class="a-end">20 months</span></div>
  </div>

  <figcaption class="cashfig__caption">Three thousand seats. Vendor list prices as of November 2026: Okta Essentials $17 and Entra ID P2 $10 per user per month. A composite example, labeled as one in the brief. Your agreement will differ; the ratio is the point. Governance above P2 is a separate purchase that is quoted rather than listed, so it is not modeled here.</figcaption>
</figure>

If P2 is already paid for, the saving is the whole license: 612,000 a year at this size. Treat that as the ceiling rather than the expectation, because it holds only if P2's basic access reviews and basic entitlement management carry the governance you are retiring, and above P2 they do not.

The case that survives that check is the one where P2 has to be bought. The replacement is 10 dollars a seat, or 360,000 a year. The saving falls to 7 dollars a seat, about 21,000 a month and 252,000 a year.

Now the payback, done properly. The move costs 90,000 and nothing is recovered until the old contract ends. Divide 90,000 by the monthly saving of 21,000 and you get about four months, which is how long recovery takes once the saving starts. That is not the payback period. Say the contract runs another twelve months and the migration takes nine, so the work finishes first. From the day you begin it is sixteen months: twelve of waiting, then four of recovery.

That case assumes the surviving platform carries the governance capability you are retiring. Above P2 it does not, and that is the one number you cannot get from a vendor page. Governance sits in a separate product that Microsoft prices by agreement rather than by list, and the published suite that contains it needs P1 underneath and is quoted differently again for P2 and E5 customers. Quote it before you model it. At this size every dollar a seat costs 36,000 a year. Against the 7-dollar baseline, four dollars of governance cost roughly halves the saving and seven removes it entirely. Against the 17-dollar ceiling, four dollars removes about a quarter and seven about 40 percent.

The tier, not the migration, decides whether there is a business case at all.

## Two things come back and four things it costs

The estate becomes defensible. The first question in an incident, an audit or a review is who had access, and the answer has to be complete. An audit does not score your architecture. It asks who had access. Consolidation makes that answer cheaper to produce, but the governance tier is what makes it possible, which is why the tier matters more than the platform you retire.

Capacity comes back to delivery. Every platform you retire is a set of run tasks that stop existing: the certification campaign that runs in two tools, the connector fixed twice, the upgrade window that consumes a weekend. Measure it in hours per month from the people who do the work, not as a percentage. Then decide where those hours go, because if nobody decides, they get absorbed.

Four things it costs that the case usually omits.

The write-down. Migration labor, the months both platforms are live, and any termination fee if you cannot wait for the notice date, all land before any saving does. A program that shows savings without a payback period is a brochure.

The governance tier. P2 carries basic entitlement management and basic access reviews. Above P2 is a different purchase, quoted rather than listed, and it is the one input that can turn a positive case into a negative one. Reviewing service principals sits above both and needs Workload Identities Premium at 3 dollars per workload identity, which is not the same count as your seats.

Partial overlap. Two platforms rarely duplicate everything. When the part that does not overlap is a regulated requirement or a capability the survivor lacks, you keep both, and the saving you modeled was never available. Find that non-overlapping tail before you commit, not after.

Vendor concentration. Retiring platforms hands pricing power to the survivor, who reprices at the next renewal. Price protection and exit terms belong in the consolidation plan, not in a later negotiation.

## The notice date is the only free exit

No vendor deadline will force this, and you should not wait for one. Consolidation is cheapest when a renewal is already in front of you, because the notice date is the only point at which you can decline to renew at no cost. Once it passes you have bought another year of the thing you were trying to remove.

So put every identity platform's notice date on one page and work from the earliest. That is your window, and your contracts set it.

## The question to ask

Then ask one question in your next identity review. If we could keep only one platform per job, meaning one workforce identity provider, one customer identity platform, one governance tool and one privileged access platform, which would they be, and which of the rest are we keeping because nobody wants the conversation?

The answer gives you the liquidation list. The renewal notice date gives you the deadline. Which one are you retiring this fiscal year?
