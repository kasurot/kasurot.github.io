# Visual formats for executive briefs

Design note for the weekly briefs on www.the-armstrongs.org. Companion to the
payment-controls brief and its review page at `/preview/every-control-asked-whether-visual/`.

Constraint, verbatim: *"Any visual we use should provide information while also
looking nice. If we have to drop information to fit the visual, then we've lost
the point."* Information is never dropped to fit a visual. No exceptions, no
"mobile version" that trims content.

## 1. Was the dense diagram's problem size, or content-architecture?

Content-architecture. Size was the symptom.

The dense diagram (880x1130) carried full explanatory sentences inside the image:
two-line card bodies ("A ceiling high enough to clear legitimate settlement and
payroll is high enough to bound nothing."), a four-line navy cause band, and a
second explanatory line under every one of the four requirements. Those sentences
are the argument. Putting them in an image asked the image to be a second copy of
the article, and a second copy cannot survive being scaled to 350px.

The compact version proved the diagnosis. It deleted the sentences and kept the
labels, and Kevin rejected it as "irrelevant" — because the sentences were doing
the work and the image had been promoted to do a job it cannot do. If the image
had only ever carried structure, the labels alone would have been enough and the
compact version would not have felt like a loss. The fact that compaction felt
like loss is evidence that the wrong content was inside the image in the first
place.

Size is real but secondary: an image that carries only structure (short labels,
position, sequence) scales to 350px with 14px type and loses nothing, because
structure does not need prose-sized type. The dense diagram could not scale
because it was carrying prose.

## 2. Division of labour between image and prose

Image carries structure only: topology, sequence, hierarchy, comparison,
magnitude, state, classification. Meaning is encoded in position, not in
sentences. Labels are short nouns or noun phrases (target <= 4 words, hard cap
~22 characters at 14px). The image is a map of the argument.

Prose carries everything else: claims, evidence, qualification, causation
("because", "therefore"), narrative, citations, caveats, numbers with units,
exceptions. If a sentence is essential to the argument, it is prose.

Rules:

- The figure is load-bearing for orientation, not for claims. Remove the figure:
  no claim becomes unsupported, because every claim is in prose. What is lost is
  the reader's ability to see the shape of the argument at a glance.
- Figure labels are headings that point at paragraphs, not summaries of them.
  The paragraph does the explaining.
- The caption says how to read the figure ("read top to bottom; the arrow is
  convergence"), never what it says.
- One figure = one structural claim: one relationship, one comparison on <= 4
  attributes, one sequence of <= 6 steps, or one 2x2 classification. Never two.
- Adjacent prose paragraphs anchor to the figure by name ("Figure 1"). The
  figure and its paragraphs are a unit; the figure is never a standalone
  exhibit.

Test before shipping: read the figure's alt text and labels with the prose
deleted. If it still argues, content leaked into the image and must move to
prose.

## 3. Formats that carry real information at 350px without type below ~14px

At 350px, 14px type fits roughly 20-24 characters per line. Every label must be
designed to that budget. Six formats:

1. Vertical step strip. 4-6 numbered nodes stacked top to bottom, each a circle
   plus a 2-4 word label, joined by a vertical rule. Carries order, stages,
   handoffs, and where a process breaks. Cannot express causation, magnitude, or
   branching. Budget: 6 nodes at ~40px = 240px tall; label <= 22 chars.

2. 2x2 (or 2x3) matrix. Four cells, each a short label (<= 12 chars) plus an
   optional one-line descriptor (<= 24 chars). Carries classification, trade-offs,
   positioning, ownership. Cannot express sequence or quantity. Budget: cell
   ~170x120px at 350px container.

3. Layered stack. 3-5 full-width horizontal bands, each with a left label
   (component) and a right short status. Carries where a control sits, gaps in a
   stack, trust boundaries. Cannot express process flow. Budget: full 350px width;
   label ~180px, status ~150px.

4. Small multiples. 3-4 mini bar or line charts, each one number (24px) plus one
   label (14px). Carries magnitude comparison, relative size, trend. Cannot
   express causation or mechanism. Budget: 2x2 grid of 165x80px charts.

5. Annotated artifact screenshot ("evidence plate"). A real, redacted UI, policy,
   or config screenshot with 2-4 word callout labels and leader lines. Carries
   concrete grounding: where the control lives, what the actual screen says.
   Cannot express abstract argument or generalisation. Budget: screenshot scaled
   to 350px wide, 3-4 callouts, label <= 18 chars.

6. Comparison table. 2-3 columns by 3-5 rows, cell values <= 18 chars, header
   row distinguished by weight not colour alone. Carries side-by-side attribute
   comparison. Cannot express long text or causation. Budget: 2 columns of
   ~160px plus gutter.

None of these requires shrinking type. None of them carries a sentence.

## 4. How much information can one figure carry?

One structural claim and no more. Concretely:

- <= 7 labeled elements (one chunk).
- <= 12 short labels total.
- Graspable in about 3 seconds. If it needs longer, it is an infographic or a
  document, not a figure.
- Exactly one of: one relationship, one comparison on <= 4 attributes, one
  sequence of <= 6 steps, or one 2x2 classification.

A 1,200-word brief gets 3-4 figures, each anchoring one section's claim. The
figure is a pin in the argument, not the argument. If a label grows past ~4
words, that content is prose that has leaked into the image and moves back to
the paragraph.

## 5. One approach that makes these briefs visibly better than every other security consultant's blog

Annotated real-artifact screenshots ("evidence plates"): one per brief, a
redacted screenshot of the actual thing the brief discusses (a payment authority
matrix, an Entra app-registration blade, a SWIFT CSCF control, a vendor price
sheet), with 2-4 word callouts, in one consistent branded frame, placed next to
the claim it supports.

Why it beats peers: every other security blog uses stock photography or abstract
diagrams; none show the control surface being discussed. An evidence plate
signals that the author has been inside these systems, which is the executive
differentiator the briefs exist to establish. It also converts an abstract claim
("the limit was attached to the wrong object") into something a CISO can point
at.

Feasible for one person per week: screenshot, redact, annotate in a reusable
Figma/Canva template, export, upload — roughly 30-45 minutes per brief, reusing
the existing hero-image pipeline. No new tooling, no designer. Falls back to a
structural diagram (formats 1-4) only when the brief discusses no concrete
artifact.

## What this is not

This note does not propose removing content from any brief, and it does not
propose a "mobile version" that trims labels. Every format above carries its
full label set at 350px. The prose carries the sentences; the image carries the
shape.
