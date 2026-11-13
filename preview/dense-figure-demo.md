---
layout: post
title: "Dense figure component demo"
date: 2026-11-13
description: "Preview of the HTML/CSS dense figure component at 716px and 350px."
tags: [Preview]
noindex: true
permalink: /preview/dense-figure-demo/
---

This page renders the payment-controls diagram as a dense HTML/CSS figure instead of an SVG. Resize the window to 350px to confirm the cards stack and the text stays at a readable size.

{% capture fig_body %}
<ul class="dense-figure__grid dense-figure__grid--3">
  <li class="dense-figure__card">
    <p class="dense-figure__card-title">Set above the loss</p>
    <p class="dense-figure__card-body">Ceiling clears settlement and payroll, so it bounds nothing.</p>
  </li>
  <li class="dense-figure__card">
    <p class="dense-figure__card-title">Policy, not engine</p>
    <p class="dense-figure__card-body">The provider enforces its own limits on its own platform.</p>
  </li>
  <li class="dense-figure__card">
    <p class="dense-figure__card-title">Wrong object</p>
    <p class="dense-figure__card-body">Channel limit instead of payment-class limit.</p>
  </li>
</ul>
<ul class="dense-figure__list">
  <li><strong>Single cause</strong> - nobody owned the number or had the evidence to set it.</li>
  <li><strong>Enforced in the engine</strong> - bank side of the trust boundary.</li>
  <li><strong>Period total added</strong> - pacing problem, not a cap.</li>
  <li><strong>Approval stays real</strong> - threshold inside the reviewer envelope.</li>
  <li><strong>Revocation tested live</strong> - one channel cut this afternoon.</li>
</ul>
{% endcapture %}
{% include dense-figure.html title="A limit that exists is not a limit that binds" caption="Read top to bottom; the arrow is convergence. Every claim is argued in the paragraphs around it." body=fig_body %}

## Every control asked the same question

Strong customer authentication verifies that a customer's payment is the customer's. Payee alerts warn a customer about a new beneficiary. Customer anomaly scoring flags a payment that does not fit a customer's history.

The third-party program is the same story told differently. The contract, the certification, the questionnaire, the register of information the regulator requires. Every one of them describes the provider. None of them states what the connection is permitted to do.
