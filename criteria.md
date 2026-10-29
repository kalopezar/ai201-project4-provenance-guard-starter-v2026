# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

When I test 10 pieces I've written myself, no more than 1 should get the
high-confidence AI label in any of the three runs.

**Why this target:**

After reading this, I'm keeping my limit at 1 in 10. A wrong AI label can
upset a writer and make them feel they have to prove themselves, so the label
shouldn't be treated as proof, and they should be able to appeal it. I still
think missing some AI writing is less harmful than accusing real writers.
Anything above 1 false positive in 10 would be too many.

> "I wrote this myself, and now it's being called AI-generated. I don't know
> how I'm supposed to prove that, but I don't want this label attached to my
> work. Can someone please review it?"

---

## 2.

For 10 clearly AI-written pieces and 10 clearly human-written pieces, the
average combined score for the AI writing should be at least 0.20 higher in
each of the three runs. I'll calculate it using the returned `model_score` and
`style_score` with `scoring.combine_signals`.

**Why this target:**

I chose a 0.20 gap because the two groups should be noticeably different, but
I'm not expecting every piece to be classified correctly. Borderline writing
can still land in the unsure range.

---

## 3.

In each run, at least one submission should get each label: high-confidence
human, unsure, and high-confidence AI.

**Why this target:**

I want at least one example of each label in every run so I know all three
outcomes are reachable, rather than only being present in the code.

---

## 4.

When I appeal a real submission, the log should contain exactly 1 appeal entry
for that `content_id`, with my reason, the original creator ID, and status
`under_review`. The log should also still contain exactly 1 original decision
entry for that ID, with status `decided`.

**Why this target:**

I expect exactly one entry for each event so an appeal can't disappear or be
duplicated in the log. Keeping the original decision matters because a writer
should be able to see what they are appealing.

---

## 5.

If `text` is missing, null, empty, only spaces, or not a string, the service
should return HTTP 400. If it's over 100,000 characters, it should return
HTTP 413. In both cases, it shouldn't run either signal or log a decision.

**Why this target:**

I picked these responses so clients can tell a malformed request from one
that's too large. A 100,000-character limit gives ordinary writing room while
keeping oversized text from using model resources.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
