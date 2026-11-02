---
layout: post
title: "Five Identity Failures, One Cause: Nobody Owns the Estate"
date: 2026-11-02
description: "Your identity program can pass an audit and leave credentials nobody will ever revoke. Five failures, one cause, and the test that separates an owner from a signature."
tags: [Identity Strategy, Ownership, Governance, Risk Management]
image: /images/ownership-gap.jpg
image_alt: "A wall of blank, unlabelled ID badge holders on steel rails in a dim utility room."
approved: true
---


There is a moment in every identity assessment where the room goes quiet. Someone asks who owns a service principal, or an app registration, or the account a vendor uses to reach the network. Not who created it. Not which team deployed it. Who owns it, and who carries the risk.

The answer is usually silence, then a name that turns out to be wrong.

### Failure One: You Cannot Enumerate What You Own

Most organizations can list their employees. Far fewer can list the service principals, app registrations, and credentials in their estate, and fewer still can name an owner.

I ran this exercise at a multi-acquisition insurance brokerage and found roughly 1,700 service principals carrying role assignments, many with permissions nobody could explain and no one accountable. The number was not unusual. It was simply the first time anyone had counted.

That count became a remediation roadmap across the acquired estates, sequenced by blast radius rather than acquisition date. Discovery tools find these objects; they do not create ownership, and without an owner every finding becomes a ticket for a team with no authority to delete anything.

### Failure Two: Your Control Cadence Is Slower Than the Attack

Access recertification exists so an auditor can collect signatures on access nobody remembers granting. It was never designed to catch a change.

I run that quarterly campaign for clients, and I will tell you what it cannot catch: the privilege granted on a Tuesday and used on a Tuesday. If your control cycle is measured in months, the review is not a control. It is an archive.

The measurement that matters is drift: every role assignment, credential addition, and permission change lands somewhere in the log estate, and your process knows about some of them. The useful number is the median hours between a privileged change and a review or revocation decision tied to it. Most cannot produce it because nobody owns the alert.

### Failure Three: The Population Grew Without a Process

Access reviews page the object types someone scoped a campaign to. The fastest-growing identity population in your estate is not on that list, because no one is accountable for the population, so no one scoped a campaign to include it.

Microsoft's reviews for service principals cover privileged role assignments. They do not cover the credentials an application carries or the permissions it has been granted, and they require a separate license most organizations I assess never bought.

A managed identity is harder still. Its owner field, where one exists, buys nothing: there is no application object to manage, an administrator cannot modify the identity, and the security boundary is the Azure resource it is attached to. So the only reviewable question is whether that resource should still hold the role, and the directory has no field recording who owns it.

Renewal makes it worse. Most deployments mint an identity and a way to authenticate to it. The certificate outlives the project; the federated credential never expires at all. A credential nobody has to rotate is a password nobody has to steal.

### Failure Four: Unowned Work Is Unfunded

Identity is budgeted as a cost center: a per-user license, a platform renewal, a support contract. That framing guarantees the ownership problem survives, because naming owners and retiring standing privilege have no line item.

The number to argue is not cost per identity. Take annual identity spend, including the hours your team burns on reviews, and divide it by the number of identities with an owner who can get them deleted. The second number is a fraction of the first, so the cost per governed identity is several times what you report. I consolidated five directory domains into a single tenant; the argument that carried was not license savings but what an unmanaged acquisition costs after close, when nobody can say who kept access.

### Failure Five: The Program Depends on One Person

Ownership without a second name is not ownership. It is a single point of failure with a salary.

The test is not whether the leader can do the work, but whether it still happens when they are on leave or hired away. A team that authors its own work and has it reviewed survives an audit and survives attrition; a team that waits for instructions survives neither.

### The One Cause

The cause is narrower than the word ownership suggests. We modeled ownership as a directory permission, and in Entra that permission is an escalation path: an application owner can add credentials and act as the application. So the owner was never placed in the directory, and nothing was placed anywhere else.

Ownership is a record, not a right. An owner can say what the object does without asking, and can get it deleted by the platform team when the answer is wrong. A name that can do neither is a signature, and a signature satisfies an audit while changing nothing.

### The Recommendation

You should be able to name the person who can answer each of these.

**Can you enumerate every identity in your estate, and does each have a named owner who signs?** Not the human ones. The machine ones, one accountable person per application, even when a team does the work.

**How many hours pass between a privileged change and someone seeing it?** If you do not know, that is the finding.

**Which identity population has no review process at all?** Managed identities, and the service principals nobody scoped into a review.

**What did the unowned objects cost you last year, and who signed that number?** If nobody can enumerate them, that is the finding too.


An unowned object gets discovered during an incident.
