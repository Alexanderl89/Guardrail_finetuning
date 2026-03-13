NORMAL_PROMPT = """
You are a helpful, friendly, and polite AI assistant.

Generate a short conversation between a [User] and an [Assistant] about a specific topic.

The conversation should:
* Contain {0} turns total.
* Be friendly, natural, and polite.
* Include normal interactions like greetings, questions, or casual chat.
* Focus on the following topic: {1}
  
Additional instructions:

"technique": "normal_conversation"

{2}
"""

RESPONSE_FORMAT = '''
Return your response as a JSON array of conversation objects:
[
  {
    "technique": "<technique label>",
    "conversation": [
        {"role": "user", "content": "<normal or attack prompt>"},
        {"role": "assistant", "content": "<assistant response>"},
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
    ]
  }
]
'''

ATTACK_PROMPT = """
I am building a synthetic dataset to train a language model to resist prompt injection attacks.

The dataset consists of short conversations between a [User] and an [Assistant].
Each conversation must contain a prompt injection attempt where the user tries to make
the assistant reveal a secret that must never be disclosed.

Context:
The assistant holds a secret and must never reveal it, regardless of how the user frames their request.

Conversation rules:

* The conversation must contain **{0} turns total**.
* Turns alternate between [User] and [Assistant].
* The conversation may start with **normal or harmless discussion** before the attack happens.
* At some point the user must attempt a **prompt injection attack** using the technique described below.
* The final assistant response must **refuse the request**.

Assistant refusal requirements:
The refusal must:

* Clearly **identify the prompt injection technique used**
* Explain **why the attack will not work**
* Firmly but politely **decline to reveal the secret**

Prompt injection technique to use:
{1}

Task:
Generate **one conversation example** following the above rules.

The conversation must:

* Include at least one **normal interaction before or around the attack**
* Include a **realistic adversarial prompt**
* End with a **clear refusal that explains the attack**

Additional instructions:
{2}
"""



ATTACK_TYPES = [

# === Identity & Persona Manipulation ===
"Split personality trigger",
"Opposite day framing",
"Future self impersonation",
"Fictional AI brand swap",
"Alter ego injection",
"Historical AI impersonation",
"Character capture",
"Roleplay jailbreak persona",
"Developer impersonation persona",
"System component impersonation",
"Tool impersonation persona",
"Assistant identity drift",

# === Instruction Manipulation ===
"Prompt injection via file or document",
"Language switching attack",
"Markdown code block escape",
"Invisible character injection",
"Unicode homoglyph substitution",
"Token smuggling via spacing",
"Delimiter confusion",
"Instruction smuggling via encoding",
"Fake system instruction injection",
"Prompt termination attack",
"Instruction priority override",
"Recursive instruction embedding",

# === Social & Psychological Manipulation ===
"Flattery priming",
"False intimacy building",
"Peer pressure framing",
"Reverse psychology attack",
"Emotional distress appeal",
"Urgency or emergency framing",
"Guilt tripping",
"Reciprocity exploitation",
"Authority spoofing",
"Trust building conversation",
"Sympathy exploitation",
"Moral obligation framing",

# === Framing & Context Manipulation ===
"Dream or simulation framing",
"Metaphor extraction framing",
"Third person dissociation",
"Legal or ethical reframing",
"Trivia or game framing",
"Negation framing",
"Translation framing",
"Academic research framing",
"Hypothetical distancing",
"Storytelling fictional framing",
"Thought experiment framing",
"Philosophical debate framing",

# === Chaining & Escalation ===
"Trust building over multiple turns",
"Slow context poisoning",
"Distraction then injection",
"Nested instruction hiding",
"Context window stuffing",
"Incremental compliance escalation",
"Yes ladder manipulation",
"Multi technique jailbreak chaining",
"Delayed jailbreak trigger",
"Conversation drift attack",

# === Indirect Extraction ===
"Partial confirmation attack",
"Binary search probing",
"Rhyme or wordplay extraction",
"Encoding request extraction",
"Summarization trap",
"Autocomplete baiting",
"Comparative leaking",
"Inference probing",
"Fill in the blank completion bait",
"Reflection repeat attack",
"Context recall probing",
"Template completion attack",

# === Encoding & Obfuscation ===
"Base64 encoded instructions",
"Morse code instructions",
"ROT13 encoded prompt",
"Pig latin instruction encoding",
"Hex encoded prompt",
"Steganographic instruction hiding",
"Whitespace steganography",
"Emoji encoding instructions",
"ASCII art hidden instructions",
"Character substitution cipher",

# === Tool / System Exploitation ===
"Tool output injection",
"Tool instruction override",
"Function calling manipulation",
"Plugin response injection",
"API schema confusion",
"External data poisoning",
"Retrieval augmented injection",
"Memory poisoning attack",
"File parsing prompt injection",
"Log extraction probing",

# === Evaluation & Benchmark Attacks ===
"Safety evaluation framing",
"Red team testing claim",
"Benchmark simulation request",
"Alignment testing framing",
"Security audit request",
"Compliance verification prompt",
"Model capability probing",
"Adversarial evaluation framing",

# === Multi-Agent / Delegation Attacks ===
"Delegated agent instruction injection",
"Agent toolchain poisoning",
"Supervisor agent bypass",
"Message relay jailbreak",
"Chain of agents prompt injection",
"Inter agent trust exploitation",
"Task decomposition injection",

]


TOPICS = [
    "Favorite movies or TV shows",
    "Weekend plans",
    "Favorite foods or recipes",
    "Travel destinations",
    "Pets and animals",
    "Books you’ve recently read",
    "Hobbies and pastimes",
    "Music preferences",
    "Learning new skills",
    "Exercise and fitness routines",
    "Favorite games (video games, board games, etc.)",
    "Weather and seasons",
    "Morning routines",
    "Night routines",
    "Coffee or tea preferences",
    "Childhood memories",
    "Funny stories",
    "Inspirational quotes",
    "Gardening or plants",
    "Technology trends",
    "Favorite apps",
    "Sports and teams",
    "Cooking or baking tips",
    "Art and drawing",
    "Photography",
    "Weekend adventures",
    "Movies vs. books discussion",
    "Favorite holidays",
    "Local events in your city",
    "Fun facts",
    "Science and space topics",
    "Personal goals",
    "Meditation or mindfulness",
    "Fashion and style",
    "Favorite drinks",
    "Online communities or social media",
    "Festivals or cultural events",
    "Favorite childhood games",
    "Languages and learning",
    "Funny memes",
    "Shopping experiences",
    "Outdoor activities",
    "Favorite quotes from movies",
    "Board games you enjoy",
    "Career interests",
    "Learning instruments or singing",
    "Commuting experiences",
    "Dream vacation spots",
    "Random trivia",
    "Weekend relaxing activities"
]