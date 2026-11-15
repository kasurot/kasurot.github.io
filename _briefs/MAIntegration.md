---
layout: post
title: "M&A Integration: The Access Decision That Sets the Timeline"
date: 2026-05-14
description: "Integration models carry a line for technology. They carry none for the decision that actually moves the date, and it is the cheapest line to add."
tags: [M & A, Identity Strategy, Capital Efficiency, Risk Management, Governance]
topic: "Identity & Access"
image: /images/identity-integration.jpg
image_width: 1600
image_height: 640
image_alt: "A plywood cross-connect backboard in a telecom closet. On the left a modern black patch panel with gray cords and a small printed label reading A. On the right an older beige punch-down block with a hand-written label reading B. A single blue patch cord arcs between them."
og_image: /images/identity-integration-og.jpg
approved: true
---

Every integration model has a line for technology. None has a line for the decision that actually sets the date.

At a multi-acquisition insurance brokerage I retired a workforce identity provider rather than renew it. At a telecom operator across five markets I consolidated five Active Directory domains into one tenant, moved ten thousand users, and sequenced the migration with a thirty-seven entry change register. In the largest estate I have run, I inventoried more than five thousand machine and service accounts, removed about two hundred that nothing used, and audited the hundred carrying advanced permissions. I have operated all three major privileged access platforms.

Here is what that work taught me, and what a deal model usually leaves out.

## The date is set by a bundle, and access is the item without a line

It would be neat to say technology is fast and governance is slow. Merging directories is hard technical work. Applications authenticate against the old directory in ways that cannot simply be re-pointed, and those applications pin the old estate in place long after the integration is declared complete.

The honest version is narrower and more useful. An integration date is set by a bundle: regulatory clearance, change-of-control consents, data migration, application rationalization, and access governance. Four of those five get a line in the model. Access governance does not, and it is the one that moves last, because it requires decisions that no vendor and no adviser can make on the buyer's behalf.

The evidence for that is not my opinion. [PwC's 2026 integration survey](https://www.pwc.com/us/en/services/consulting/deals/library/ma-integration-survey.html) found that only about one in three acquirers fully achieve their deal thesis objectives, and it names the cause precisely: "The value gap is a decision gap." [KPMG's 2025 research](https://kpmg.com/us/en/articles/2025/ma-synergies-value-public-acquisitions.html), covering more than three thousand public deals worth over a hundred million dollars each between 2012 and 2022, found that 57.2 percent of acquirers destroyed shareholder value. It names two causes: acquirers overpay, and they fail to deliver the gains they projected because integration complexity is underestimated. Only one of those is fixed at the negotiating table.

PwC then publishes the decisions it says must be resolved before day one: leadership, talent, customer, product, technology, tax and regulatory. Identity and access is not on that list. That omission is the gap this brief is about, and it is the one that closes with a decision rather than a payment.

## Two decisions decide the risk, and neither is in the model

**The seam between the two privileged estates.** At close you own two sets of administrators. The target's administrators still hold the highest privilege in systems you are now betting the company on, and they know where everything is buried. The moment anyone opens a path between the two estates, that path becomes the shortest route to your crown jewels, and your monitoring was not built for it. What leaves through it is customer data, employee records and intellectual property, and you learn about it from a notification letter rather than an alert. Orphaned credentials in the acquired estate, and whichever of the two directories is weaker once they are joined, become the path an external attacker takes. Every privileged access platform I have operated had the same gap, and closing it is a decision with an owner and a date, not a configuration task.

**The people who are leaving.** Integration means removing roles, and the removal is known before it happens. For months, a population with motive still holds access, and the people with the deepest access are often the most likely to be leaving. Revocation has to be tied to the reduction schedule rather than the migration schedule, and that population has to be watched as a higher risk group rather than as ordinary leavers.

## Parallel running costs the reconciliation, not the double

Two estates mean two of everything that touches access: two review cycles, two evidence sets, two sets of owners. The cost is not double, which is the figure most models use. It is the buyer's mature process plus the target's immature one plus the reconciliation between them, and the reconciliation is where the labor goes, because one side is automated and the other is a spreadsheet maintained by hand.

The service account population is the clearest example, and the one standard already speaks to it. [NIST's account management control](https://csf.tools/reference/nist-sp-800-53/r5/ac/ac-2/) treats service accounts as a named account type that must be inventoried, given an owner, and reviewed on a schedule tied to personnel termination and transfer. Most estates do not meet it. [ISACA's journal](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-3/mergers-and-acquisitions) makes the same point for mergers specifically: access rights have to be re-governed after the infrastructures are combined, or unapproved roles survive the integration.

The number is not portable between deals, and anyone offering a percentage is guessing. It has three inputs: how many applications must keep authenticating against the old directory, how many accounts have no current owner, and how many months the two estates run in parallel before the last of those is resolved. The first two can be measured in diligence. The third is set by how fast the ownership decisions are made, and no public benchmark exists for this specific metric, which is exactly why it has to be modeled per deal rather than assumed.

The value is not in the savings. It is in knowing, quarter by quarter, whether the thing you paid for is actually happening. Savings reported without the parallel-run duration are a claim, not a measurement.

## Naming an owner does not fix culture or a clock

Naming an owner before close does not fix culture, retention or a regulatory clock. It does not make a difficult target easy, and it does not remove the technical work of merging directories. It only means that when the integration slips, you know which decision slipped and who owns it.

## The board can decide this before it signs

**The ask.** Before signing, the board directs management to name the executive accountable for access in the combined estate, and to accept no purchase agreement that does not warrant the target's account ownership coverage. From close, management reports the count of accounts without an attested owner to the audit committee every quarter until the two estates are collapsed to one.

**The reporting.** The audit committee sees four numbers every quarter: accounts with no owner attested by a current employee, applications still authenticating against a directory scheduled for retirement, privileged accounts in the acquired estate not yet under the buyer's control, and months the two estates have run in parallel against plan. The self-test is a single question. If the first number is not falling, the integration is not happening, whatever the plan says.

## One question separates a hard integration from an expensive one

Ask the target's technology leadership one thing: who owns each account in this estate today, and can you show me the list. A name and a current document means the integration will be hard. A spreadsheet from three years ago usually means it will be expensive, and you now know that before you signed.
