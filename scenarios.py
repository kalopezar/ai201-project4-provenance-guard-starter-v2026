"""
What your test runs. ← UNIT 8, MILESTONE 3

Each measurable criterion has a scenario below. The false-positive criterion
uses the user's own writing; label coverage uses inputs intended to span the
score range.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Scenarios use the five targets in `criteria.md`. Appeal scenarios submit text,
use the returned content ID for an appeal, then verify both audit entries.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

    "appeals" a list of {text, creator_id, reasoning} cases. The runner submits
              each text, appeals the returned content ID, and checks the log.
"""

MY_WRITING = [
    "I moved here when I was nineteen with two suitcases and a phone card. My mom still asks if I'm eating enough. I tell her yes. She doesn't believe me. Fifteen years later, I still call every Sunday. I still switch to Spanish when I'm tired. Some things don't get left behind. They just get carried.",
    "My cat knocks my water glass off the desk every single morning. Always at 6:15. Always while holding eye contact. I've tried moving it. I've tried a heavier glass. She just adapts. Honestly, she'd make a great penetration tester.",
    "I spent most of last year learning that nobody actually reads the phishing training emails. Not the interns. Not the VPs. Me neither, if I'm being honest. The best defense we had was one tired woman in IT who noticed something weird at 2 a.m. Tools are great. People still catch the real stuff.",
    "The thing nobody tells you about the NYC subway is that you stop hearing it. Then you visit somewhere quiet and you can't sleep. Too much silence. I lay there in my friend's guest room in Vermont and missed the screeching. How is that normal?",
    "My husband and I have a rule. No hard conversations after 9 p.m. Nothing good ever gets said at that hour. Last week he broke it, and I broke it back. We were up until one. We cried a little. We laughed a lot. Rules are great. We keep them until we don't.",
    "I read this thing about how your brain edits memories every time you remember them. Like, every single time. So the story I tell about my childhood isn't the original. It's a copy of a copy of a copy. That freaked me out for about a week. Then I realized it explains why my sister and I never agree on what happened at Christmas.",
    "My dad just learned how to FaceTime. He's seventy-one. He calls me four times a day now. Mostly to show me his lunch. Sometimes he forgets to turn the camera around and I just see his ceiling. I'm not complaining. I'd take a hundred ceiling calls over silence.",
    "Everybody keeps saying AI is going to change everything. Maybe. Meanwhile my smart speaker still thinks I said \"play Taylor Swift\" when I asked for the weather. I'm cautiously optimistic. I'm also keeping my paper planner.",
    "I turned thirty-four this year and nothing looks like I thought it would. I don't own a house. I don't have a five-year plan. I do have a good group chat and a decent sense of humor. Some days that feels like enough. Other days I Google \"is it too late to learn piano.\"",
    "When my grandmother passed, we found a shoebox of her old immigration papers. Every stamp, every form, every rejected application. She never talked about it. We never asked. Now I keep that box on my shelf. I don't open it often. I just like knowing it's there.",
]

# These comparison passages were generated for this evaluation; they are not
# the user's own writing and are only the clearly-AI group for criterion 2.
AI_WRITING = [
    "Effective communication is essential in today's rapidly changing world. By sharing ideas clearly, individuals and organizations can build stronger relationships. This process also helps reduce misunderstandings and supports better outcomes. Ultimately, thoughtful communication creates opportunities for growth.",
    "Maintaining a healthy lifestyle involves several important habits. Regular exercise supports physical well-being, while balanced nutrition provides the energy needed for daily activities. Adequate rest is equally valuable because it allows the body to recover. Together, these practices contribute to long-term health.",
    "Technology continues to transform the way people work and learn. Digital tools make information more accessible and allow teams to collaborate across distance. However, successful adoption requires careful planning and responsible use. When applied thoughtfully, technology can improve productivity and create meaningful benefits.",
    "Education plays a vital role in personal and community development. Students gain knowledge, practice critical thinking, and discover new interests. Supportive teachers can make this experience more engaging and effective. A strong educational foundation helps people prepare for future challenges.",
    "Setting clear goals is an important step toward achieving success. A well-defined objective provides direction and makes progress easier to measure. Breaking a large goal into smaller tasks can also make the process less overwhelming. With consistent effort, meaningful progress becomes possible.",
    "Environmental responsibility is a shared concern for individuals and communities. Simple actions, such as reducing waste and conserving energy, can make a positive difference. Organizations can contribute by adopting sustainable practices. Through cooperation, society can protect resources for future generations.",
    "A positive workplace culture benefits both employees and organizations. Respectful communication encourages collaboration and helps people feel valued. Leaders can support this environment by listening to feedback and recognizing contributions. These efforts can improve morale and strengthen performance.",
    "Planning a successful project requires organization and flexibility. Teams should identify their objectives, assign responsibilities, and establish realistic timelines. Regular check-ins help reveal problems before they become serious. By adapting when necessary, a team can stay focused on its goals.",
    "Reading offers many benefits for people of all ages. It can expand vocabulary, introduce new perspectives, and provide opportunities for reflection. Developing a regular reading habit does not require a large time commitment. Even a few pages each day can create a rewarding routine.",
    "Preparing for change can help people respond with confidence. Gathering reliable information is a useful first step. It is also important to consider possible challenges and identify available support. Although change may feel uncertain, careful preparation can make the transition easier.",
]

BORDERLINE_WRITING = [
    "The meeting started early, which was probably a mistake. We had coffee, reviewed the plan, and changed two small things. By lunch, the project felt less complicated. Maybe the best part was simply having everyone in the same room.",
    "There are days when the familiar route home feels different. The corner store has a new sign, the bus arrives a minute late, and someone is carrying flowers. Nothing important has changed, but for a moment the whole street seems to be telling a story.",
    "A useful tool should solve a real problem without making the rest of the work harder. That sounds obvious, but it is easy to forget when a feature looks impressive in a demonstration. I try to ask who benefits, what might break, and whether a simpler option would do.",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        "name": "AI versus human score spread",
        "criterion": 2,
        # The first ten are generated comparison passages; the next ten are
        # the user's own writing. Compare the mean combined scores by group.
        "texts": AI_WRITING + MY_WRITING,
    },
    {
        "name": "label coverage across score range",
        "criterion": 3,
        "texts": AI_WRITING + MY_WRITING + BORDERLINE_WRITING,
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "appeals": [
            {
                "text": "I am submitting this paragraph to verify the appeal workflow. The service should return a content ID, accept a reasoned appeal, and preserve both events in its audit log.",
                "creator_id": "eval_appeal",
                "reasoning": "I wrote this text myself and request a review of the decision.",
            },
        ],
    },
    {
        "name": "bad input handling",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   ", "creator_id": "eval_bad_spaces"},
            {"text": 42, "creator_id": "eval_bad_number"},
            {"text": "x" * 100001, "creator_id": "eval_bad_oversized"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        appeals = scenario.get("appeals")

        if sum(bool(value) for value in (texts, bodies, appeals)) > 1:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has multiple input "
                f"types — choose texts, bodies, or appeals"
            )
            continue

        if appeals:
            for j, case in enumerate(appeals, 1):
                if not isinstance(case, dict):
                    problems.append(f"scenario {i}, appeal {j} is not a dict")
                    continue
                for field in ("text", "creator_id", "reasoning"):
                    if not isinstance(case.get(field), str) or not case[field].strip():
                        problems.append(
                            f"scenario {i}, appeal {j} needs non-empty string "
                            f"'{field}'"
                        )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
