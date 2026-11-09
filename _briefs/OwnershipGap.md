---
layout: post
title: "Five Identity Failures, One Cause: Nobody Owns the Estate"
date: 2026-11-02
description: "Your identity program can pass an audit and leave credentials nobody will ever revoke. Five failures, one cause, and the test that separates an owner from a signature."
tags: [Identity Strategy, Ownership, Governance, Risk Management]
image: /images/ownership-gap.jpg
image_width: 1080
image_height: 1350
image_alt: ""
approved: true
---

Ask one question in your next identity review: who owns the app registration whose service principal holds the permissions nobody has explained?

Not who created it. Not which team deployed it. Who owns it, and who carries the risk.

If the answer takes a pause rather than a name, the answer is nobody. At an insurance brokerage that had absorbed several acquisitions, the count came back at 1,697 service principals, many with permissions nobody could explain and no one accountable. The number was not unusual. It was the first time anyone had counted.

The cause is structural rather than cultural. We modeled ownership as a directory permission, and in Entra that permission is an escalation path, so no owner was ever written down anywhere that binds.

### Failure One: You Cannot Enumerate What You Own

Most organizations can list their employees. Far fewer can list the service principals, app registrations, credentials and vendor accounts in their estate, and fewer still can name an owner for any of them.

The count became a remediation roadmap across the acquired estates, sequenced by blast radius rather than acquisition date. Discovery tools find these objects. They do not create ownership, and without an owner every finding becomes a ticket for a team with no authority to delete anything.

### Failure Two: Your Control Cadence Is Slower Than the Attack

Access recertification exists so an auditor can collect signatures on access nobody remembers granting. It was never designed to catch a change.

I run that quarterly campaign for clients, and I will tell you what it cannot catch: the privilege granted on a Tuesday and used on a Tuesday. If your control cycle is measured in months, the review is not a control. It is an archive.

The measurement that matters is drift. Every role assignment, credential addition and permission change lands in the log estate. Your process sees only some of them. The number to produce is the median hours between a privileged change and a review or revocation decision, and most organizations cannot produce it, because nobody owns the alert.

### Failure Three: The Population Grew Without a Process

The fastest-growing identity population in your estate is the one your review process cannot see, because nobody is accountable for the population, so nobody scoped a campaign to include it.

A review covers only the object types someone remembered to add to the campaign. Microsoft's reviews for service principals cover privileged role assignments. They do not cover the credentials an application carries or the permissions it has been granted, and they require Microsoft Entra Workload ID Premium on top of Entra ID P2 or Governance, a license most organizations I assess never bought.

A managed identity is harder still. There is no application object to manage, the directory object cannot be modified, and the security boundary is the Azure resource it is attached to. The owners collection exists on every service principal and is inert here, because a non-admin owner is allowed to modify an object that cannot be modified. So the only reviewable question is whether the resource should still hold the role, and no accountable owner is recorded anywhere.

Renewal makes it worse. Most deployments mint an identity and a way to authenticate to it. The certificate outlives the project, so a credential nobody has to rotate becomes a password nobody has to steal. The federated credential never expires at all, which is worse in a quieter way: there is no secret to steal and no renewal date to trigger a review of who still needs the trust.

### Failure Four: Unowned Work Is Unfunded

Identity is budgeted as a cost center: a per-user license, a platform renewal, a support contract. That framing guarantees the ownership problem survives, because naming owners and retiring standing privilege have no line item.

The number to argue is not cost per identity. Take annual identity spend, including the hours your team burns on reviews, and divide it by the number of identities with an owner who can get them deleted. That denominator is a fraction of your estate, so the cost per governed identity is several times the cost per identity you report. I consolidated five directory domains into a single tenant, and the argument that carried was not license savings. It was what an unmanaged acquisition costs after close, when nobody can say who kept access.

### Failure Five: The Program Depends on One Person

Ownership without a second name is not ownership. It is a single point of failure with a salary.

Microsoft recommends at least two owners per application, and nothing enforces it. The test is not whether the leader can do the work, but whether it still happens when they are on leave or hired away. Who signs the access review in week three of a vacation? What evidence shows the team authored the work rather than waited for instruction? A team that authors its own work and has it reviewed survives an audit and survives attrition. A team that waits for instructions survives neither.

### The One Cause

The cause is narrower than the word ownership suggests. We modeled ownership as a directory permission, and in Entra that permission is an escalation path: the owner of an app registration can add a credential and act as the application. Microsoft's own documentation warns that an application owner can create or update objects while impersonating the application. So the permission was never granted, and no record took its place.

Ownership is a record, not a right.

An owner can say what the object does without asking, and can get it deleted by the platform team when the answer is wrong. A name that can do neither is a signature, and a signature satisfies an audit while changing nothing.

### The Recommendation: Four Questions

Bring these four to your next review, in this order.

**Can you enumerate every identity in your estate, and does each have a named owner who can answer for it?** Not the human ones. The machine ones, one accountable person per application, even when a team does the work.

**How many hours pass between a privileged change and someone seeing it?** If you do not know, that is the finding.

**Which identities can only be reviewed as role holders, never as objects?** Managed identities, and the service principals nobody scoped into a campaign.

**What did the unowned objects cost you last year, and who signed that number?** If nobody can enumerate them, that is the finding too.

An unowned object gets discovered during an incident. An owned one has a name in a record before it, and someone who can answer for it.

