import streamlit as st
import random

st.title("📚 TBR Generator")


prompts = [
    "A story where the main character leaves their hometown or country.",
    "A book where the main character faces ultimate challenges and must make sacrifices.",
    "Something with cozy fall vibes.",
    "A story set in winter.",
    "A book involving political schemes, assassination attempts, high stakes, and warrior arcs.",
    "A book that feels like sitting with a hot cup of tea, a fluffy blanket, and dim lighting.",
    "A story with multiple characters, each following their own arcs.",
    "A book written by a male author featuring a female main character.",
    "A story where magic is forbidden.",
    "A deep character study exploring someone’s mind and inner life.",
    "A book that has been adapted into a TV show or film.",
    "A story that will touch your soul and leave an emotional impact.",

    "Enemies-to-lovers romance.",
    "A slow-burn romance that builds tension over time.",
    "A forbidden love story.",
    "A morally gray main character.",
    "A romance where love is complicated or toxic.",
    "A book with a villain protagonist or morally questionable main character.",

    "A chosen one who rejects their destiny.",
    "Magic that comes with a dangerous cost.",
    "A cursed kingdom or royal family.",
    "Dragons or mythical creatures in the story.",
    "A duology set in a magical world.",

    "A book that will emotionally destroy you.",
    "A story that feels like nostalgia.",
    "A bittersweet or tragic ending.",
    "A thriller that is eerie yet satisfying.",

    "A book you’ve heard mixed reviews about but still sounds interesting.",
    "A big, intimidating book that feels like a challenge.",
    "A book in a genre you don’t usually read.",
    "A book set somewhere you’d love to visit.",
    "A book you would recommend to your mom or dad.",
    "A book you picked up while traveling or on a trip abroad.",

    "A book with your favorite color featured on the cover.",
    "A book whose cover feels like it’s trying to tell you something.",

    "The book you’ve owned the longest but never read.",
    "The prettiest cover on your shelf.",
    "The book you keep postponing.",

    "A book where the protagonist is not the main hero of the story.",
    "A book where the villain is more interesting than the hero.",
    "A book told from multiple timelines.",
    "A book where nothing is what it seems at first.",
    "A book where the ending completely changes your understanding of the story.",

    "A book you would choose based only on its first sentence.",
    "A book you would read purely because a friend recommended it strongly.",
    "A book you feel guilty for not having read yet.",

    "A book that feels like it was written just for you.",
    "A book that feels like a dream you won’t be able to explain after finishing it.",
    "A book with a title you don’t fully understand.",
    "A book where the setting is more important than the plot.",
    "A book where the main character makes a morally wrong decision you understand.",
    "A book where the side character steals the entire story.",
    "A book that doesn’t fit neatly into any genre.",

    "A classic that focuses on messy, dramatic relationships.",
    "A classic with a morally complicated or flawed main character.",
    "A classic that feels like a romance at its core.",
    "A classic with betrayal, secrets, or scandal at the center of the story.",
    "A classic that is more emotional than intellectual.",
    "A classic where the characters make extremely questionable life choices.",
    "A classic that feels like modern-day drama in historical clothing.",
    "A classic with intense love or obsession at its core.",
    "A classic that explores jealousy, heartbreak, or toxic love.",
    "A classic that is surprisingly easy and addictive to read.",
    "A classic that feels like a character study of human emotions.",
    "A classic with strong feminist themes or a complex female lead.",
    "A classic where social pressure and reputation drive the entire plot.",
    "A classic that feels like a tragic romance.",
    "A classic that is dark, emotional, and intense rather than boring or slow.",

    "A story with a dark, gothic atmosphere.",
    "A story that feels like you live in a dark wooded castle with a huge ballroom library and wheeled ladders.",
    "A book set in a specific historical era in time.",

    "A book that feels like being a lonely warrior in Japan, searching for purpose.",
    "A book with a master and apprentice training in the shadows in a world that stands against them, preparing for war or a better future.",
    "A story where the character is fighting to become a better version of themselves in order to survive a war.",

    "A book with castles, nobles, and high-caste societies in a divided world.",

    "A book set in space where survival depends on technology or teamwork.",
    "A dystopian world controlled by technology or AI.",
    "A story where memory or identity has been altered.",
    "A futuristic world where humanity is no longer in control.",
    "A sci-fi story where science creates unexpected consequences.",
    "A book set on another planet or colony.",
    "A story where time travel changes everything.",
    "A world where humans and machines are deeply connected or merged.",

    "A thriller where nothing and no one can be trusted.",
    "A mystery where every clue leads to more questions.",
    "A story where the main character is hiding a dangerous secret.",
    "A book with a slow-building sense of paranoia and fear.",
    "A thriller where the truth is worse than the lie.",
    "A story involving a disappearance that changes everything.",
    "A psychological thriller that gets inside the main character’s mind.",
    "A book where you are solving a crime alongside the story.",

    "A book you expect to be boring but might surprise you.",
    "A book by an author you’ve heard many good things about.",
    "A book by an author you’ve heard bad reviews about.",

    "A story that gives Lana Del Rey vibes.",
    "A story with a dark, moody storyline.",
    "A book with a cover that feels like it’s hiding a deeper meaning.",

    "A book that is sitting horizontally on your shelf.",
    "A book that is buried in the middle of multiple books.",
    "A bingeable book you can’t stop reading.",
    "A book with a cover you don’t like.",

    "A book with a title that is two words or less.",
    "A book set on a different continent.",
    "A book you’ve owned for more than a year.",
    "A book that fits the current season.",
    "A book that is over 400 pages long.",
    "A book with orange on the cover.",
    "A book by an author you’ve never read before.",
    "A book with a great first sentence.",
    "A book with a cover you don’t like."
]

st.write("Press the button and let fate choose your next reading adventure 📚✨")

if st.button("Generate Prompt"):
    prompt = random.choice(prompts)
    st.success(prompt)
