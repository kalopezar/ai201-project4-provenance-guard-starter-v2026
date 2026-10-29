"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures below capture sentence-length spread, vocabulary repetition,
and punctuation density. They are simple heuristics, not proof of authorship.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics
import unicodedata


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures ───────────────────────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies, as a coefficient of variation.

    Returns:
        A non-negative float. Higher means sentence lengths vary more, which
        is treated as more human-like by `style_signal`.

    A one-sentence submission returns 0.0 because there is no variation to
    measure.
    """
    sentence_word_counts = [len(words(sentence)) for sentence in sentences(text)]
    if len(sentence_word_counts) < 2:
        return 0.0

    mean_length = statistics.mean(sentence_word_counts)
    if mean_length == 0:
        return 0.0
    return statistics.stdev(sentence_word_counts) / mean_length


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def punctuation_density(text: str) -> float:
    """
    How much punctuation there is, relative to the number of words.

    Returns:
        A float counting Unicode punctuation characters per word.
    """
    word_count = len(words(text))
    if word_count == 0:
        return 0.0

    punctuation_count = sum(
        1 for char in text if unicodedata.category(char).startswith("P")
    )
    return punctuation_count / word_count


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Low sentence-length variation and a lower type-token ratio increase the
    score; more punctuation per word reduces it. The vocabulary ratio is mapped
    from 0.8 (score 0) to 0.3 (score 1), and punctuation density from 0.0
    (score 1) to 0.3 (score 0), with both values clamped to 0–1. Sentence
    regularity is 1 / (1 + coefficient of variation). The three components
    are averaged equally. These rough ranges make the signals comparable, but
    the measures remain sensitive to text length and deliberate editing.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    token_count = len(words(text))
    if token_count == 0:
        return 0.5

    sentence_count = len(sentences(text))
    spread = sentence_length_spread(text)
    regularity_score = 1 / (1 + spread) if sentence_count > 1 else 0.5

    vocabulary_ratio = type_token_ratio(text)
    vocabulary_score = max(0.0, min(1.0, (0.8 - vocabulary_ratio) / 0.5))

    punctuation_rate = punctuation_density(text)
    punctuation_score = max(0.0, min(1.0, 1 - punctuation_rate / 0.3))

    return (regularity_score + vocabulary_score + punctuation_score) / 3


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nHigher style_signal means more likely AI; this is a heuristic, not proof of authorship.")
