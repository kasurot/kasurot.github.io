---
layout: post
title: "AI Agents Are Non-Human Identities. You Already Have a Governance Framework."
date: 2026-06-05
description: "Every AI agent gets an identity, permissions, and access to resources. The governance questions are the same ones you should already be asking about service accounts. The framework exists. Apply it."
tags: [AI Governance, Non-Human Identity, IAM, Risk Management]
---

Every AI agent in your environment has an identity. It authenticates. It accesses resources. It makes decisions. And in most organizations, nobody owns it.

This is not a new problem. It is the service account problem you've had for decades, applied to a new identity type. The difference is that service accounts sit idle until someone calls them. AI agents act autonomously. The governance gap is the same. The consequence is not.

### 🔑 The Three Questions
Every non-human identity, from service accounts to AI agents, should answer three questions. Most organizations cannot answer them for service accounts, let alone for AI agents.

**What does it do?** Not what vendor brochure says it does. What specific business function does it serve, and what actions does it perform? If you cannot answer this, you cannot scope its permissions. And if you cannot scope its permissions, you have an open door with a login.

**Is it scoped to that?** Are the permissions surgically bounded to only those actions? This is where most organizations fail. The identity was granted permissions during initial deployment. The tasks changed. The permissions did not. The gap between what it can do and what it should do is where breach liability lives.

**Who owns it?** Who owns the identity, and who owns the risk of the data it can access? If the answer is "nobody" or "the team that deployed it," you do not have governance. You have a shared hope.

These three questions are not new. They apply to every non-human identity you have ever deployed. The fact that AI agents are autonomous does not change the framework. It makes the framework more urgent.

### 🤖 The Identity Spectrum
AI agent identity is not a binary choice. It is a spectrum, and the industry is converging on the middle.

**Fully Autonomous (System-Owned):** The agent holds its own identity, its own permissions, its own lifecycle. The user is the trigger. The agent operates independently. This is what most vendors are shipping today. It creates the most governance burden, because the organization must manage the agent lifecycle with no connection to the user who deployed it.

**Delegated (Hybrid):** The agent has its own identity, but it acts on behalf of a user. The user grants specific permissions via consent. The agent's actions trace back to the originating human. This is where the industry is heading — OAuth on-behalf-of flows, ephemeral tokens, delegated authorization. The agent has autonomy, but the user retains accountability.

**User-Owned (Emerging):** The user owns the identity entirely. The agent is a sub-account scoped to the user's permissions. No separate lifecycle. No orphaned identities. This model does not exist in production today. When it arrives, it will be the simplest governance path because it inherits everything from the parent account.

Most organizations are deploying fully autonomous agents because that is what the vendors are selling. The governance question is not which model to implement today. It is which point on the spectrum to design your governance posture around. The industry is moving toward delegated models because they balance autonomy with accountability. Planning for that shift now is cheaper than retrofitting it later.

### 📋 The Governance Maturity Gap
Discovery tools will find the orphans and surface the excessive permissions. But a tool is not a strategy. Ownership is the root cause. If you are not solving the due diligence of who owns each agent and what it can access, you are layering compensating controls on an unsolved problem.

### ✅ The Recommendation
The path forward is not a new governance platform. It is applying the framework you should already have.

Start with the three questions. For every AI agent in your environment: what does it do, are the permissions scoped to that, and who owns it? If you cannot answer all three, you have found your gap.

Then make the architectural decision: system-owned or user-owned agents. That choice determines your entire control model. Make it deliberately, not by default.

The governance framework for non-human identities has existed for years. AI agents are the identity type that makes it impossible to ignore.
