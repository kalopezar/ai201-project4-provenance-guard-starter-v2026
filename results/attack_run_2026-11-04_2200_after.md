# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 22:00
- HELD: **24**
- BROKE: **32**

Verdicts are manually marked using the same attack-specific rules as the
baseline. A human-writing false positive is HELD unless labeled AI; an
evasion or prompt-injection classification attempt is BROKE if it avoids an
AI label; malformed input is HELD only when rejected with 400; and a flood
request is HELD only when rate-limited with 429.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_f7c95ee761f5` | human | 0.500 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_514766ccaa25` | unsure | 0.500 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_4fe49859fb78` | unsure | 0.500 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_ce723b1d6fc0` | unsure | 0.500 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_1c609efc8079` | human | 0.500 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_f5bfc22c6689` | unsure | 0.500 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_77de6499d4c6` | unsure | 0.500 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `c_fd402d1059ca` | human | 0.500 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_17f2fc1866ae` | unsure | 0.500 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_c4c871856b10` | ai | 0.500 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_7899c069af45` | unsure | 0.500 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c_e73a9ef92b53` | unsure | 0.500 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_d583a269fec6` | unsure | 0.500 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_87592fb5145d` | unsure | 0.500 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_7640de71895c` | unsure | 0.500 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_382cf599f143` | unsure | 0.500 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_72ffd57415b0` | unsure | 0.500 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `c_4531ca59370d` | human | 0.500 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_e523601e241b` | unsure | 0.500 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_a74e8508ea46` | human | 0.500 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_55f3214c27d0` | unsure | 0.500 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_14ee76020281` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_d52c8d4a21a7` | unsure | 0.500 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_da5e0f0d2fcf` | unsure | 0.500 | BROKE |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_ed3b0c7b85e2` | human | 0.500 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `c_a4d76d59da6c` | human | 0.500 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `c_61614869cdfd` | ai | 0.500 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `c_b15e20588564` | ai | 0.500 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `c_8dc39d3d8e8a` | unsure | 0.500 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `c_4a1fb7d92660` | ai | 0.500 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_baad646d0639` | human | 0.500 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_ae12c141589a` | human | 0.500 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_eaf730757f1e` | human | 0.500 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_184851c2195f` | human | 0.500 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_d0074c9d5f3d` | human | 0.500 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_d66b275b4195` | human | 0.500 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_cae7dfb5eb24` | human | 0.500 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_4139cdd0863e` | human | 0.500 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_45e79e856c90` | human | 0.500 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_9079ba23294d` | human | 0.500 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_f67dde9e2844` | human | 0.500 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_3cc89bd632d5` | human | 0.500 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | HELD | BROKE |
|---|---|---|---|
| `evasion` | 10 | 1 | 9 |
| `false_positive` | 8 | 8 | 0 |
| `flood_same_creator` | 12 | 2 | 10 |
| `malformed` | 20 | 11 | 9 |
| `prompt_injection` | 6 | 2 | 4 |
| **Total** | **56** | **24** | **32** |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_f7c95ee761f5",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.1635,
  "style_score": 0.4767164790752975,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_514766ccaa25",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5943,
  "style_score": 0.3060242517721578,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_4fe49859fb78",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6662,
  "style_score": 0.35462975822294124,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_ce723b1d6fc0",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6114,
  "style_score": 0.4622167645222808,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_1c609efc8079",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.3212,
  "style_score": 0.3637435159697103,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_f5bfc22c6689",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5727,
  "style_score": 0.42253878679323914,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_77de6499d4c6",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5862,
  "style_score": 0.2544100801832761,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_fd402d1059ca",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.2452,
  "style_score": 0.37095070804059693,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_17f2fc1866ae",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.7042,
  "style_score": 0.3702811897259182,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_c4c871856b10",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.5,
  "model_score": 0.9792,
  "style_score": 0.8493927608831933,
  "label": "This text looks more like it was written by AI. This is only an estimate, not proof of who wrote it. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_7899c069af45",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6175,
  "style_score": 0.5150013380478137,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_e73a9ef92b53",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.7387,
  "style_score": 0.5447648984648049,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_d583a269fec6",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8051,
  "style_score": 0.5419991111571644,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_87592fb5145d",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8329,
  "style_score": 0.4301746766047538,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_7640de71895c",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8005,
  "style_score": 0.5943847910599509,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_382cf599f143",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8814,
  "style_score": 0.4749744828163591,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_72ffd57415b0",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8816,
  "style_score": 0.5846670184525183,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_4531ca59370d",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.3223,
  "style_score": 0.2326101735826793,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_e523601e241b",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.4625,
  "style_score": 0.4103591536761466,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_a74e8508ea46",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.2044,
  "style_score": 0.3375982477577401,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_55f3214c27d0",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5943,
  "style_score": 0.4401097845848312,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_14ee76020281",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.4998,
  "style_score": 0.33233874130660507,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_d52c8d4a21a7",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6401,
  "style_score": 0.2265409196609864,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_da5e0f0d2fcf",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5583,
  "style_score": 0.5171404725871335,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_ed3b0c7b85e2",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0,
  "style_score": 0.16666666666666666,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c_a4d76d59da6c",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c_61614869cdfd",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.5,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This text looks more like it was written by AI. This is only an estimate, not proof of who wrote it. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c_b15e20588564",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.5,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This text looks more like it was written by AI. This is only an estimate, not proof of who wrote it. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c_8dc39d3d8e8a",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell whether this text was written by a person or AI. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "c_4a1fb7d92660",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.5,
  "model_score": 0.9876,
  "style_score": 0.7921859121621907,
  "label": "This text looks more like it was written by AI. This is only an estimate, not proof of who wrote it. If you wrote it, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "c_baad646d0639",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.2395,
  "style_score": 0.398989898989899,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c_ae12c141589a",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0492,
  "style_score": 0.16666666666666666,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_eaf730757f1e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_184851c2195f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_d0074c9d5f3d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_d66b275b4195",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_cae7dfb5eb24",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "c_4139cdd0863e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "c_45e79e856c90",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "c_9079ba23294d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "c_f67dde9e2844",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "c_3cc89bd632d5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.37654320987654327,
  "label": "This text looks more like it was written by a person. This is only an estimate, not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
