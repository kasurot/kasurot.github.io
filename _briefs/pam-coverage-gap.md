---
layout: post
title: "Every PAM Program Measures What It Vaulted. None Measures What It Missed."
date: 2026-11-14
description: "Every privileged access program reports what it vaulted. That number is a floor, and the gap above it is the one you are being asked to sign."
tags: [Privileged Access, Identity Strategy, Ownership, Risk Management]
approved: true
---

The question arrives in a due diligence pack, an audit request or a board paper: how many privileged credentials can reach this estate, and how many have you vaulted?

The second number is available in seconds. It is on the dashboard, trending up. The first one is a pause, and sometimes a project.

That asymmetry is not a measurement problem. It is an attestation problem: every privileged access program reports what it vaulted, none reports what it missed, and the executive signs a coverage claim with no denominator. The artifact that surfaces it is the auditor's request list or the representation letter, and neither will accept a figure that counts only what entered the tool.

### A vault is a container, not an inventory

Every platform reports the same thing: managed accounts. That number is a floor: it describes what was onboarded, not what exists.

This is not a vendor defect. CyberArk, BeyondTrust and Delinea can all enumerate accounts they have discovered but do not manage, and that list arrives without an owner. The scan is real; the register around it is what is missing, because a scan produces candidates, not an owner, a date or a cadence.

Coverage requires knowing the population, and nobody maintains it, because the population is not a list. It is local administrator accounts, service accounts whose passwords have not changed since creation, vendor accounts opened so a support call could close, API keys sitting in configuration files, and certificate private keys on unmanaged shares.

The control that already exists is an inventory, not a vault. CIS Control 5.1 requires an inventory of accounts, and 5.5 an inventory of service accounts, both maintained rather than produced once (CIS Critical Security Controls v8.1).

The population outside the tool's view is visible in aggregate even where it is not enumerable. Orchid Security's Identity Gap Report found that 67 percent of non-human accounts are created directly inside the application rather than through the identity system (Orchid Security, Identity Gap: 2026 Snapshot, May 2026). That is a vendor selling a fix for the problem it describes, so treat the figure as directional. It gives a share, not a count.

### Vaulting needs a decision only an owner can make

Somebody has to approve the rotation schedule. Somebody has to answer when the application breaks at two in the morning because the secret changed. A vault cannot make either decision, which is why an unclaimed credential does not go in.

Three things gate a privileged credential, and only the last is about ownership. Scope and license capacity decide how many the program can manage at all. Engineering feasibility and change risk decide how fast the rest move. The service account whose password is hardcoded across configuration files, the appliance with no rotation plugin: those have a perfectly good owner and they still never get vaulted. Ownership decides which of them you can close and sign.

### The number you report is a floor, and you should say so

What you require is two numbers, not one.

The first is the count of privileged credentials discovered but not yet vaulted, split into owned and unowned, because the unowned rows are the point. The register must key to an owner, and the owner sits with the application, because an application survives the host rebuilds and renames that reset a host-keyed list and gives the age clock a spine. Application is not the whole of it: shared platform accounts, infrastructure accounts on devices and hypervisors, and vendor support accounts carry owners of their own, or they fall out of the register on the day it is built.

The second is the age of the unvaulted population, reported as a distribution rather than a single oldest figure, because a single number resets the moment somebody retires one row. Age must run from first discovery, never from the most recent scan. That holds only if first discovery is tied to a credential identity that persists across scans, an address, an account name and an owning application, so that a re-imaged host or a renamed service account cannot quietly restart the clock.

The population spans more than one system, and the two do not enumerate the same object: an account name in the privileged access platform, a key thumbprint in the secrets store. Counting both means binding them to one credential identity, or the report is two numerators with no shared denominator. A claim that counts one system is a count of whichever the reviewer happened to open first.

The owner column cannot be discovered at all. It has to be assigned, and the assignment has to mean something: the named owner is the person who would be paged when that secret breaks. Rows nobody claims age. Past a threshold, the application owner is asked to claim, and if they decline the gap becomes a named risk acceptance signed by the accountable executive for that business line, recorded and reviewed at the identity steering committee, with an expiry date and a named individual against it. A committee records risk; only a person can accept it. A standard with no consequence for refusal is a reporting ritual.

The gap does not close inside security. It closes when each business owner accepts that the service account behind their application is theirs to name, rotate and answer for. Security can build the register and run the escalation. It cannot accept the risk on somebody else's behalf. Credentials held inside a vendor's tenancy are accepted by whoever owns the contract, which is where the risk acceptance and the right to audit meet.

The standard can be tested on one application before it is imposed on the estate. Name the person who answers for every credential that system uses to reach another. The ones you cannot name are your real coverage gap, and they are almost certainly not in your vault.

### The instrument is a floor, not a coverage guarantee

The two numbers are a management instrument, not a coverage guarantee, and the obvious criticism is that discovery has the same flaw as the vault. It does. A scan enumerates what the scanner can reach, and it will miss the vendor's account inside a SaaS tenancy you do not administer, the key in a repository nobody indexed. So the gap count is a numerator over a denominator it cannot see. A program that reports it as coverage has repeated the original error with more steps and a longer runbook.

What changes is not completeness. It is assignability. A vaulted count moves only when you add or retire a secret, and it cannot be argued with or escalated. A gap list can be assigned, dated and chased, and every row that is assigned a claimant has entered the accountable set for the first time, whether or not that claimant has yet accepted it. The residue is that the denominator stays wrong. Report it as a floor: at least this many credentials sit outside the vault, and this is the oldest one.

### The claim fails on a fully enumerated estate

The claim fails on an estate that is fully enumerated, with every row carrying a named owner and the vault count equal to the population. If those estates are common, the gap is already closed and this paper describes a laggard. They are rare, and the reason is structural rather than cultural: the enumeration has to be redone as the estate changes, and nobody has been given that job.

### What you are asking to be approved

One resolution: adopt the two numbers as the standing coverage report, adopt named and expiring risk acceptance as the mechanism for refusal, and name the accountable function and the date of the first standing report. Expect the first reading to look worse than the last dashboard. It is the first honest one, and the prior number was a floor labelled as coverage.

### What the identity steering committee sees each quarter

Both numbers against the prior quarter, with the reach of the discovery behind them, so the committee can tell a falling floor from a widening one. The oldest unvaulted credential. The count of owners who declined and were escalated to signed acceptance. The first two describe the estate. The third describes whether the model is working, because a register in which nobody ever declines is a register nobody is reading.

### What you sign is the standard you set

Contracts have owners. Budget lines have owners. The credentials behind them are the one population nobody is asked to account for.

Report the floor and name the gap. Sign nothing that presents the count as coverage.
