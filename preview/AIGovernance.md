---
layout: post
title: "Every AI Agent Gets an Identity Before It Gets an Owner"
date: 2026-06-05
description: "Almost every AI agent reaches production with an identity and no owner. The governance questions are the ones you should already be asking about service accounts."
tags: [AI, Identity Strategy, Risk Management, Governance]
topic: "Identity & Access"
preview: true
preview_note: "Rewritten to 1,579 words with four verified citations, an ask and a five-number reporting block. Reviewed by the C-suite round. Ready for your approval."
noindex: true
permalink: /preview/AIGovernance/
---

Almost every AI agent deployed to production receives an identity. Few receive a named owner. That ordering is the whole problem, and it is the one thing about AI you can fix without waiting for anyone.

At a multi-acquisition insurance brokerage I inventoried 1,697 service principals in a single estate. About 200 were no longer used by anything, so they came out. Another 100 carried advanced permissions, so each was audited individually and the remainder were risk-ranked and deferred behind work that could hurt the business. Across client estates I have worked in more than five thousand machine identities, which is a floor rather than a total. I have implemented all three major privileged access platforms, and every one had the same blind spot: it could tell you what it had vaulted, and not what it had missed.

That work is why this brief exists. The AI agent problem is that problem on a faster clock.

## The authorities have already named the failure, and it is an identity failure

The [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) lists **Excessive Agency** as LLM06. Its definition is precise: an LLM-based system is granted the ability to call functions or interface with other systems to undertake actions in response to a prompt, and the risk is that it is granted more than it needs. OWASP names the root cause as *"excessive functionality; excessive permissions; excessive autonomy."*

None of those three is about the model. They are the questions an identity practitioner asks about a service account, and OWASP arrived at them from the security side of the AI problem rather than the identity side. That is worth noticing, with one caution. The first two map cleanly onto identity work and the third does not, because autonomy is not ownership. An agent can carry a named owner and still act unsupervised. An agent can require approval on every call and still have nobody accountable for it. They are different properties, and OWASP's remedy for autonomy is a control rather than a register.

The scale is not marginal. [Palo Alto Networks' 2026 Identity Security Landscape](https://www.paloaltonetworks.com/idira/idira-identity-security-landscape), a vendor survey of more than 2,900 security leaders, puts machine identities ahead of human identities by 109 to 1. The [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/) published a paper in May 2026 whose title states the position this brief takes: *The Non-Human Identity Governance Vacuum*, subtitled *AI Agents and the Fastest-Growing Unmanaged Attack Surface*.

## Why an agent is worse than a service account

A service account sits idle until something calls it. Its behaviour is a function of its caller, and the caller is code somebody wrote and can read.

An agent decides. It selects a tool, composes a call and takes a next step without a human in the loop. The permission set may be identical to the service account beside it. What changed is that the permission set is now exercised by something that chooses when and how.

Autonomy is the variable that moved. Scope did not. In the estates I have worked in, agents commonly carry permissions granted at proof of concept, when the intent was to see whether the thing worked at all, and the grant was rarely revisited when it went to production. That is the same failure I found in the service principal estate, with one difference that matters to your C-suite: an over-permissioned service account is exploited by somebody who has to find it first, and an over-permissioned agent can be manipulated into exploiting itself.

The mechanism deserves stating precisely, because it is where the service account comparison flatters us. An agent reads untrusted input, so business-normal content becomes the caller: an email, a ticket, a page. The exploit channel is not a secret sitting in a repository, which at least has to leak. It is your ordinary operating traffic, which never has to.

## Four questions, three of which OWASP already asks

For every AI agent, four questions. The first three are OWASP's causes. The fourth decides whether the other three get answered at all.

**What does it do?** Not what the vendor describes. The specific business function and the specific actions. If you cannot answer this you cannot scope its permissions. This is excessive functionality.

**Is it scoped to that?** Are the permissions bounded to those actions and nothing else? In most estates they were granted during deployment, the task changed, and the grant did not. This is excessive permissions.

**How much can it do without a human saying yes?** This is OWASP's excessive autonomy, and it is the question identity practitioners most often skip. It is answered with approval gates, action limits and short-lived credentials rather than with an inventory. If an agent can wire money, delete a tenant or send externally without a confirmation step, autonomy is your exposure regardless of who owns it.

**Who owns it?** Who owns the identity, and who owns the risk of the data behind it? This is not OWASP's question, and it is the one that determines whether the other three are ever answered. If the answer is the team that deployed it, or nobody, you have a shared assumption that somebody is watching.

Answer all four and you have governance. Fail the fourth and the first three become a form you fill in once.

## The spectrum, and why this is an architectural decision

Agent identity is not a binary. It is a spectrum, and the choice determines your control model.

**Fully autonomous.** The agent holds its own identity, permissions and lifecycle. The user is a trigger. This is what most vendors ship, and it creates the heaviest governance burden, because the lifecycle has no connection to any human and autonomy sits at its maximum.

**Delegated.** The agent has its own identity but acts on behalf of a user, with permissions granted by consent, and its actions trace back to a person. This is where the industry is converging. The agent keeps its autonomy and the human keeps the accountability.

**User-owned.** The identity belongs to the user and the agent is scoped beneath it. No separate lifecycle and no orphan population. It is not in production at scale, and when it arrives it will be the cheapest governance model available, because it inherits ownership instead of creating it.

Most organisations are deploying the first because it is what arrived, then governing it with controls designed for the second. Decide which point on the spectrum you are designing around before the estate decides for you.

## What I am asking you to decide

A tool will find the orphans and surface the over-permissioned agents. A tool is not a strategy, and discovery without ownership produces a longer list and the same exposure.

**Direct that no AI agent enters production without a named human owner and a permission set scoped to a stated function.**

That sentence is narrow on purpose. It needs no platform, no policy library and no maturity model, and it is enforceable at the point of deployment, which is the only point where it is free. The cost is two fields in an inventory and a gate in change control, which is why it needs no budget line and should not wait for one.

For the estate already running, use the method I used on the service principals rather than an open-ended sweep: **register or risk-rank every agent before the next risk review, schedule the tail behind work that can hurt the business, and decommission unowned agents by default unless an owner is named.** A deadline that requires every agent registered is a deadline that slips. A deadline that requires every agent ranked does not.

Three of those decisions are yours and cannot be delegated. Name the accountable executive. Put the numbers on the risk committee agenda yourself. Give your CISO standing authority to block any agent at deployment until it has both fields.

Report quarterly, on five numbers.

**Agents in production.** The count, against the prior quarter. Define "agent" in the counting rule before you publish the first number, or every percentage below inherits the ambiguity.

**Agents with a named owner.** As a percentage, and it is the number that fills fastest. It measures registration rather than ownership, so treat a high figure as progress and not as assurance.

**Agents with permissions scoped to a stated function.** As a percentage.

**Agents reviewed and either constrained or retired.** The count. This is the only figure here that is an outcome rather than a coverage number, and it is the one I would read first.

**Agents at the fully autonomous point of the spectrum, owned or not.** The count. This is the population where scope and autonomy are both at maximum, and a named owner does not reduce it. If a dashboard reports zero exposure because every agent has an owner, this is the number that contradicts it.

The self-test takes one question and can be run inside a meeting: name the owner of every agent currently running. If the list cannot be produced, the exposure is not hypothetical and the number is not zero.

The governance thinking for non-human identity already exists. [NIST's AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) supplies the risk vocabulary and the privileged access platforms you already own supply the controls, though neither yet addresses agent credentials head-on. What AI changed is the population size and the speed. It did not change the question: who owns this, how much can it do without a yes, and what can it reach.
