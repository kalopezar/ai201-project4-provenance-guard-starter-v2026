# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writing site sends `POST /submit` a JSON object with `text` and
   `creator_id`.
2. The service checks that the JSON is an object and that `text` is a
   non-empty string. Invalid requests get HTTP 400 before either signal runs.
3. `detector.model_signal` measures how predictable the text is to a local
   language model. It returns a 0–1 score; higher means more AI-like.
4. `stylometry.style_signal` measures sentence-length variation, vocabulary
   repetition, and punctuation density, then returns its own 0–1 score.
5. `scoring.combine_signals` combines the two scores using a 70% model / 30%
   style weighted average.
6. `scoring.score_to_label` uses the combined score to choose human (0.00–0.35),
   unsure (between 0.35 and 0.65), or AI (0.65–1.00). The service logs the
   decision and returns a `content_id`, both signal scores, the combined
   score, the guess, and the reader-facing label. `confidence` is currently a
   placeholder value of 0.5.
7. If the writer disagrees, they can send the `content_id` and their reasoning
   to `POST /appeal`. The service appends an appeal to the audit log with
   status `under_review`; `GET /log` shows the decision and appeal entries.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** `detector.model_signal` estimates how predictable each
word is to a local GPT-2 language model and turns that into a 0–1 score.

**Why that might differ between human and AI writing:** AI-generated text can
favor common, predictable word choices, so it may be easier for another
language model to predict.

**What it can't see:** It cannot tell who actually wrote the text. Plain,
conventional human writing may also be predictable, while unusual human prose
may be hard to predict.

### Signal two — the style signal

**What it measures:** `stylometry.style_signal` looks at sentence-length
variation, the ratio of unique words to total words, and punctuation per
word. It combines these surface measurements into a 0–1 score.

**Why that might differ between human and AI writing:** Generated writing
often uses a more even sentence rhythm and repeats familiar vocabulary.
Human writing can vary more in sentence length and punctuation.

**What it can't see:** It does not understand the text or know its author.
Formal human prose can resemble AI writing, and someone can change these
measurements by editing sentence breaks, vocabulary, or punctuation without
changing the ideas.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** I combine the two 0–1 scores with a weighted average. If they
disagree, the result lands between them instead of letting either signal make
the decision on its own. I give the model signal more weight, but the style
signal can still pull the score away from a high-confidence accusation.

**The numbers:** 70% model signal and 30% style signal. The current label
thresholds in `config.py` are 0.35 for human and 0.65 for AI; scores between
them are unsure.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**Four-input calibration (model / style / combined):**

| Input | Model signal | Style signal | Combined score |
|---|---:|---:|---:|
| Clearly AI | 0.7544 | 0.4001 | 0.6481 |
| Clearly human | 0.4089 | 0.2701 | 0.3673 |
| Formal human | 0.7643 | 0.3824 | 0.6497 |
| Lightly edited AI | 0.7423 | 0.3945 | 0.6380 |

The formal human result surprised me: its model score is even higher than the
clearly-AI sample, and the style score is close to the clearly-AI score too.
That suggests the model signal is treating formal, predictable prose as AI-like;
stylometry doesn't distinguish these two well either. The lightly edited AI
sample also stays close to the clearly-AI sample on both signals. With the
current 0.65 threshold, all three AI-like scores above are just below a
high-confidence AI label. These examples show why the scores need cautious
labels and an appeal path—they don't establish who wrote a text.

An earlier comparison showed the signals can also rank nearby texts in
opposite directions: the borderline sample's model score (0.3134) was below
the clearly-human sample's (0.4089), while its style score (0.3106) was above
the clearly-human score (0.2701). The 70/30 weighted average keeps the result
between the two signals and leans toward the model signal; disagreement is
not proof of authorship.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 ≤ score ≤ 0.35 | This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it. |
| unsure | 0.35 < score < 0.65 | We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result. |
| high-confidence AI | 0.65 ≤ score ≤ 1.00 | This text looks more like it was written by AI. This is only an estimate, not proof of who wrote it. If you wrote it, you can appeal this result. |

**Why I worded the "unsure" one this way:**
I don't want an unsure result to sound like an accusation. It says plainly
that the service can't tell, and lets someone who wrote the text know they can
appeal.

**Label reachability check:** I submitted these three examples to `/submit`.
Each label was returned, with the combined scores shown.

- Human: "Time management matters more than people admit, especially now that
  work moves as fast as it does. If you're organised you hit deadlines, and
  you're less frazzled doing it. A few things actually help. Prioritise - work
  out what genuinely matters and do that first. Cut the interruptions;
  notifications wreck focus and the damage is worse than it feels at the
  time. And take breaks, short ones, often." → `human`, **0.3443**
- Unsure: "The importance of effective time management cannot be overstated
  in today's fast-paced work environment. Professionals who develop strong
  organizational habits are better positioned to meet deadlines and reduce
  stress. There are several key strategies that can help individuals improve
  their productivity. First, prioritization is essential. By identifying the
  most important tasks and addressing them first, workers can ensure that
  critical objectives are met. Second, minimizing distractions plays a
  significant role. Setting aside dedicated blocks of time for concentrated
  work is widely considered beneficial. Finally, regular breaks are important
  for maintaining performance." → `unsure`, **0.6481**
- AI: "The cat sat on the mat. The cat was happy. The cat saw a dog. The dog
  was happy. The cat and the dog played. The dog and the cat had fun. The cat
  went home. The dog went home." → `ai`, **0.8383**

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"Time management matters more than people admit, especially now that work moves as fast as it does. If you're organised you hit deadlines, and you're less frazzled doing it. A few things actually help. Prioritise - work out what genuinely matters and do that first. Cut the interruptions; notifications wreck focus and the damage is worse than it feels at the time. And take breaks, short ones, often.\", \"creator_id\": \"label_human_ascii\"}"
```

```json
{
  "combined_score": 0.3443468368771283,
  "confidence": 0.5,
  "content_id": "c_39e7666f7a82",
  "guess": "human",
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "model_score": 0.3485,
  "style_score": 0.3346561229237612
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "c_39e7666f7a82", "reasoning": "I wrote this myself. Please review the decision and the writing samples I can provide."}'
```

```json
{
  "content_id": "c_39e7666f7a82",
  "message": "Your appeal has been recorded for review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.3443468368771283,
      "content_id": "c_39e7666f7a82",
      "creator_id": "label_human_ascii",
      "guess": "human",
      "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
      "model_score": 0.3485,
      "status": "decided",
      "style_score": 0.3346561229237612,
      "timestamp": "2026-10-29T02:06:38+00:00"
    },
    {
      "content_id": "c_39e7666f7a82",
      "creator_id": "label_human_ascii",
      "event": "appeal",
      "reasoning": "I wrote this myself. Please review the decision and the writing samples I can provide.",
      "status": "under_review",
      "timestamp": "2026-10-29T02:08:57+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help me get `/submit` from a placeholder response to a
  working route using the model signal, and check malformed requests before
  running the model.
- *What came back:* The route needed to validate the payload first, then run
  the signal, create an appeal-ready `content_id`, and log the decision.
- *What I changed:* I used that flow, checked it with a mocked signal and with
  `curl`, and kept the guess and label as placeholders until the scoring and
  label steps were ready.

**Moment 2**

- *What I asked for:* Compare the model and style signals on the same examples
  and help choose a combining rule that handles disagreement.
- *What came back:* The formal human sample scored almost like the clearly-AI
  sample on both signals. A weighted average would keep the combined score
  between the two inputs.
- *What I changed:* I chose a 70/30 model-to-style weighted average, documented
  the surprising calibration results and the false-positive risk, and made
  sure the appeal path was recorded rather than presenting a score as proof.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
