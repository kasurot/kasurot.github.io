---
layout: post
title: "Five Identity Failures, One Cause: Nobody Owns the Estate"
date: 2026-11-02
description: "Your identity program can pass an audit and still be breached. Five failures, one cause, and the test that separates an owner from a signature."
tags: [Identity Strategy, Ownership, Governance, Risk Management]
---

There is a moment in every identity assessment where the room goes quiet. Someone asks who owns a service principal, or a certificate template, or the account a vendor uses to reach the network. Not who created it. Not which team deployed it. Who owns it, and who carries the risk.

The answer is usually silence, then a name that turns out to be wrong.

That silence survived every control I have assessed, and it produces five consequences.

### 🔍 Failure One: You Cannot Enumerate What You Own

Most organizations can list their employees. Far fewer can list the service principals, credentials, managed identities, and certificate templates in their estate. Fewer still can name an owner.

I ran this exercise at a multi-acquisition insurance brokerage and found roughly 1,700 service principals carrying role assignments, many with permissions nobody could explain and no one accountable. The number was not unusual. It was simply the first time anyone had counted.

That count became a remediation roadmap across the acquired estates, sequenced by blast radius rather than acquisition date. Discovery tools find these objects; they do not create ownership, and without an owner every finding becomes a ticket for a team with no authority to delete anything.

### ⏱ Failure Two: Your Control Cadence Is Slower Than the Attack

Access recertification exists so an auditor can get a signature on a sample. It was never designed to catch a change.

I run that quarterly campaign for clients, and I will tell you what it cannot catch: the privilege granted on a Tuesday and used on a Tuesday. If your control cycle is measured in months, the review is not a control. It is an archive.

The measurement that matters is drift: every role assignment, credential addition, consent grant, and permission change lands in an audit log, and your process knows about some of them. The useful number is the median hours between a privileged change and a review or revocation decision tied to it. Most cannot produce it because nobody owns the alert.

### 🤖 Failure Three: The Population Grew Without a Process

Access reviews page humans. The fastest-growing identity population in your estate is not human.

Service principals are the clearest example, and the review capability exists: Microsoft ships access reviews for service principals, gated behind an extra license and scoped to privileged role assignments. Most tenants never bought it. Managed identities carry no owner attribute, which is the part no license fixes.

Certificates make the point harder. A certificate template is an Active Directory object whose permissions decide who can obtain a certificate as whom, and no cloud access review pages it. Microsoft documented in October 2026 how help-desk impersonation reached certificate services and produced certificates for eleven privileged accounts. The templates were not unowned. They were unreviewed, which is worse: the directory says they have an owner and everyone believes it.

### 💰 Failure Four: Unowned Work Is Unfunded

Identity is budgeted as a cost center: a per-user license, a platform renewal, a support contract. That framing guarantees the ownership problem survives, because naming owners and retiring standing privilege have no line item.

The number to argue is not cost per identity but cost per governed identity, plus the cost of an acquisition whose identities were never integrated. I consolidated five directory domains and four forests into a single tenant; the argument that carried was not license savings but what an unmanaged acquisition costs after close, when nobody can say who kept access.

### 👥 Failure Five: The Program Depends on One Person

Ownership without a second name is not ownership. It is a single point of failure with a salary.

The test is not whether the leader can do the work, but whether it still happens when they are on leave or hired away. A team of roughly ten across three countries, with two leads carrying delivery, survives an audit and survives attrition; a team that waits for instructions survives neither. Capability stays with the leader; capacity is delegated with review, and the review is what makes delegation safe.

### 🎯 The One Cause

These are not five problems. They are five symptoms of one.

The test is simple. An owner can say what the object does without asking, and can delete it. A name in a campaign that can do neither is a signature, and a signature satisfies an audit while changing nothing.

### ✅ The Recommendation

You should be able to name the person who can answer each of these.

**Can you enumerate every identity in your estate?** Not the human ones. The machine ones.

**Does every one of them have a named owner who signs?** One accountable person per application, even when a team does the work.

**How many hours pass between a privileged change and someone seeing it?** If you do not know, that is the finding.

**Which identity population has no review process at all?** Certificates and agents are the usual answers.

**What did the unowned objects cost you last year, and who signed that number?** This is the question your CFO asks.

An unowned object gets discovered during an incident. The controls that held in the estates I have run held because somebody could name what the object did and delete it.
