---
layout: post
title: "Every PAM Program Measures What It Vaulted. None Measures What It Missed."
date: 2026-11-14
description: "Every privileged access program reports what it vaulted. That number is a floor, and the gap above it is the one you are being asked to sign."
tags: [Privileged Access, Identity Strategy, Ownership, Risk Management]
image: /images/pam-coverage-gap.jpg
image_width: 1600
image_height: 640
image_alt: "A long aisle of steel cantilever shelving in a records centre, loaded with archive cartons. Some bays hold uniform tan cartons in squared courses, others hold mismatched water-stained cartons, one carton leans off a shelf edge into the aisle, and one bay stands empty."
og_image: /images/pam-coverage-gap-og.jpg
approved: true
---

The question arrives in a due diligence pack, an audit request or a board paper: how many privileged credentials can reach this estate, and how many have you vaulted?

The second number is available in seconds. It is on the dashboard, trending up. The first one is a pause, and sometimes a project.

That asymmetry is not a measurement problem. It is an attestation problem: every privileged access program reports what it vaulted, none reports what it missed, and the executive signs a coverage claim with no denominator. The artifact that surfaces it is the auditor's request list or the representation letter, and neither will accept a figure that counts only what entered the tool.

Neither number in this brief is a coverage figure. The vault count is a floor. So is the gap count, because discovery cannot see the vendor's account inside a tenancy you do not administer, or the key in a repository nobody indexed. What changes is not completeness. It is assignability: a vaulted count moves only when you add or retire a secret and cannot be argued with or escalated, while a floor that can be assigned, dated and chased is worth more than a coverage claim that cannot be challenged.

The standard is testable on one application before it is imposed on an estate. Name the person who answers for every credential that system uses to reach another. The ones you cannot name are your coverage gap, and they are almost certainly not in your vault.

### A vault is a container, not an inventory

Every platform reports the same thing: managed accounts. That number is a floor: it describes what was onboarded, not what exists.

This is not a vendor defect. CyberArk, BeyondTrust and Delinea can all enumerate accounts they have discovered but do not manage, and that list arrives without an owner. The scan is real; the register around it is what is missing, because a scan produces candidates, not an owner, a date or a cadence.

Coverage requires knowing the population, and nobody maintains it, because the population is not a list. It is local administrator accounts, service accounts whose passwords have not changed since creation, vendor accounts opened so a support call could close, API keys sitting in configuration files, and certificate private keys on unmanaged shares.

An unvaulted credential is not a reporting omission. It is a working key. It authenticates, it grants whatever the account was given, and because no owner holds its rotation, it is the one credential in the estate whose last change date nobody can produce. When it is used, the use is attributable to the account and not to a person, which is why an incident that begins with a service account is harder to scope to an individual than one that begins with a login. The exposure is not that the credential is unknown. It is that the credential works and nobody is watching it.

The control that already exists is an inventory, not a vault. CIS Control 5.1 requires an inventory of accounts, and 5.5 an inventory of service accounts, both maintained rather than produced once ([CIS Critical Security Controls v8.1](https://www.cisecurity.org/controls/v8-1)).

The population outside the tool's view is visible in aggregate even where it is not enumerable. Orchid Security's Identity Gap report found that two-thirds of non-human identities are authenticated and authorized locally, inside applications, with no directory, no IdP and no central oversight ([Orchid Security, Identity Gap: 2026 Snapshot](https://www.orchid.security/reports/the-identity-gap-2026-snapshot-identity-insight-straight-from-the-source), May 2026). That is a vendor selling a fix for the problem it describes, so treat the figure as directional. It gives a share, not a count.

### Vaulting needs a decision only an owner can make

Somebody has to approve the rotation schedule. Somebody has to answer when the application breaks at two in the morning because the secret changed. A vault cannot make either decision, which is why an unclaimed credential does not go in.

Three things gate a privileged credential, and only the last is about ownership. Scope and license capacity decide how many the program can manage at all. Engineering feasibility and change risk decide how fast the rest move. The service account whose password is hardcoded across configuration files, the appliance with no rotation plugin: those have a perfectly good owner and they still never get vaulted. Ownership decides which of them you can close and sign.

### The number you report is a floor, and you should say so

Report two numbers. First, privileged credentials discovered but not vaulted, split owned from unowned, because the unowned rows are the point. Second, the age of that population as a distribution, run from first discovery and never from the most recent scan, because a single oldest figure resets the moment somebody retires a row. The privileged platform and the secrets store do not enumerate the same object; unless both resolve to one credential identity, you are reporting two numerators with no shared denominator.

The schema that makes both numbers hold up is in <a class="regpop" href="#register-data-model">the register data model<span class="regpop__panel">The register keys to an owner who sits with the application, because an application survives the host rebuilds and renames that reset a host-keyed list. First discovery is tied to a credential identity that persists across scans: an address, an account name and an owning application. Full schema in the appendix below.</span></a>, at the end of this brief.

The owner column cannot be discovered at all. It has to be assigned, and the assignment has to mean something: the named owner is the person who would be paged when that secret breaks. Rows nobody claims age. Past a threshold, the application owner is asked to claim, and if they decline the gap becomes a named risk acceptance signed by the accountable executive for that business line, recorded and reviewed at the identity steering committee, with an expiry date and a named individual against it. A committee records risk; only a person can accept it.

The gap does not close inside security. It closes when each business owner accepts that the service account behind their application is theirs to name, rotate and answer for. Security can build the register and run the escalation. It cannot accept the risk on somebody else's behalf. Credentials held inside a vendor's tenancy are accepted by whoever owns the contract.

### The resolution

One resolution: adopt the two numbers as the standing coverage report, adopt named and expiring risk acceptance as the mechanism for refusal, and name the accountable function and the date of the first standing report. Expect the first reading to look worse than the last dashboard. It is the first honest one, and the prior number was a floor labelled as coverage.

The work is not a new function. It runs on the discovery data the privileged access platform already produces, on the inventory control that is already required, and on the analysts already employed to read them. The incremental cost is hours per application per quarter, not a headcount. What is new is the assignment, and that is a decision each application owner makes, not a project security runs on their behalf.

The identity steering committee sees both numbers against the prior quarter each time, with the reach of the discovery behind them, so it can tell a falling floor from a widening one. It sees the oldest unvaulted credential, and the count of owners who declined and were escalated to signed acceptance. The first two describe the estate. The third describes whether the model is working, because a register in which nobody ever declines is a register nobody is reading.

Report the floor and name the gap. Sign nothing that presents the count as coverage.

<style>
  .regpop {
    position: relative; color: inherit; text-decoration: none;
    border-bottom: 1px dotted var(--border-medium, #b9b2a4); cursor: help;
  }
  .regpop:focus-visible { outline: 2px solid var(--accent-gold, #b8892b); outline-offset: 2px; border-radius: 2px; }
  .regpop__panel {
    position: absolute; left: 0; bottom: 100%; z-index: 40;
    display: block; width: min(30rem, 86vw); margin-bottom: .6rem; padding: .85rem 1rem;
    background: var(--bg-card, #fdfcf9); color: var(--text-body, #2a2a2a);
    border: 1px solid var(--border-medium, #b9b2a4); border-radius: 4px;
    box-shadow: 0 8px 26px rgba(0,0,0,.18);
    font-size: .84rem; line-height: 1.5; text-align: left; font-style: normal;
    opacity: 0; visibility: hidden; transform: translateY(4px);
    transition: opacity .14s ease, transform .14s ease, visibility .14s;
    pointer-events: none;
  }
  .regpop:hover .regpop__panel,
  .regpop:focus .regpop__panel,
  .regpop:focus-within .regpop__panel {
    opacity: 1; visibility: visible; transform: translateY(0); pointer-events: auto;
  }
  @media (max-width: 640px) {
    .regpop__panel { display: none; }
  }
  @media (prefers-reduced-motion: reduce) {
    .regpop__panel { transition: none; }
  }
</style>

### Appendix: the register data model

This detail is for the people who will build the register. It is not needed to take the decision above.

<a id="register-data-model"></a>

The register must key to an owner, and the owner sits with the application, because an application survives the host rebuilds and renames that reset a host-keyed list and gives the age clock a spine. Application is not the whole of it: shared platform accounts, infrastructure accounts on devices and hypervisors, and vendor support accounts carry owners of their own, or they fall out of the register on the day it is built.

Age must run from first discovery, never from the most recent scan. That holds only if first discovery is tied to a credential identity that persists across scans, an address, an account name and an owning application, so that a re-imaged host or a renamed service account cannot quietly restart the clock.

The population spans more than one system, and the two do not enumerate the same object: an account name in the privileged access platform, a key thumbprint in the secrets store. Counting both means binding them to one credential identity, or the report is two numerators with no shared denominator. A claim that counts one system is a count of whichever the reviewer happened to open first.
