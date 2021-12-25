from scene_engine import run_game

keywords = ["chalice", "mantle", "beast", "arcane", "ceremony", "lenkar", "elderberry", "corrupted"]

lairs = ["The Mountains of Despair", "The Dragon Mountains", "The Orange Swamp", "The Dungeons of Errinhold", "The Ruins of Freidberg Castle", "The Blasted Waste"]

import random
keyword = random.choice(keywords)
lair = random.choice(lairs)

death = random.choice(lairs)
while death == lair:
    death = random.choice(lairs)

death2 = random.choice(lairs)
while death2 == death or death2 == lair:
    death2 = random.choice(lairs)

portals = sorted([lair, death, death2])

def calc_gronk_q_and_a_lines(question):
    return [
        "q: is Gronk strong? a: yes",
        "q: does Gronk hate elves? a: yes",
        "q: is there a dragon here? a: no",
        f"q: {question}? a:"
    ]

def calc_silverleaf_gronk():
    return {
        "pdesc": "A slight female elf is here, dressed in a travelling cloak. A bow and quiver lean against her table.",
        "shortdesc": "The elf",
        "about_lines": [
            "The elf is calmly watching the brutish man.",
            "The elf has a mischevious look in her eye."
        ],
        "talk_lines": [
            "The elf says: Well dear fellow, you're entitled to your opinion, but perhaps you'd be best to keep it to yourself.",
            "The elf says: I can see why you'd be worried about ears, with those big cauliflower lumps on the sides of your head.",
            "The elf says: You're like a big, barking dog, aren't you? Sit, rover! Roll over!"
        ],
        "talk_prompt": "The elf says:"
    }

def calc_silverleaf_after_gronk():
    return {
        "pdesc": "A slight female elf is here, dressed in a travelling cloak. A bow and quiver lean against her table.",
        "shortdesc": "The elf",
        "about_lines": [
            "The elf's name is Silverleaf.",
            "She has just beaten Gronk, and now wants to talk to the Barkeep and settle in for a drink.",
            "Silverleaf is wondering where her friend Lungar is.",
            "She is supposed to meet Lungar here in the tavern.",
            "Lungar is a big barrel chested warrior. Some people call him a barbarian, but he is a knight."
        ],
        "talk_lines": [
            "The elf says: Hi there, my name is Silverleaf!",
            "The elf says: That Gronk was certainly a character, wasn't he? In my forest we would feed him to the Ravener.",
            "The elf says: Thanks for your help. Have you seen a big barbarian wandering around? He's either wearing armour, or he might just be wearing underpants.",
            "The elf says: Have you seen Lungar? He's either wearing armour, or he might just be wearing underpants."
        ],
        "talk_prompt": "The elf says:",
    }

def calc_silverleaf_running_from_zombies():
    return {
        "pdesc": "A slight female elf is here, dressed in a travelling cloak. She is running from the zombies. She carries a bow and quiver of arrows.",
        "shortdesc": "The elf",
        "about_lines": [
            "The elf's name is Silverleaf.",
            "She is running with the barkeep from a horde of zombies.",
            "Silverleaf is wondering where her friend Lungar is.",
            "She is looking for Lungar amongst the people running from the zombies.",
            "Lungar is a big barrel chested warrior. Some people call him a barbarian, but he is a knight."
        ],
        "talk_lines": [
            "The elf says: We'd better keep running, those monsters are everywhere!",
            "The elf says: Can you run any faster? We've got to go quickly!",
            "The elf says: Oh these creatures smell terrible. I'd like to shoot them with my arrows!",
            "The elf says: Can you seen a big barbarian running around? He might be just wearing underpants.",
            "The elf says: Have you seen Lungar? He's either wearing armour, if he hasn't lost it."
        ],
        "talk_prompt": "The elf says:",
    }

def calc_silverleaf_fighting_zombies():
    return {
        "pdesc": "Silverleaf the Elf is here, shooting zombies with arrows and kicking them.",
        "shortdesc": "Silverleaf",
        "about_lines": [
            "Silverleaf is fighting for her life.",
            "Silverleaf shoots the zombies full of arrows."
        ],
        "talk_lines": [
            "Silverleaf says: I keep shooting them but they wont die! What do I do?",
            "Silverleaf says: Barkeep, can you think of some way to kill these things?",
            "Silverleaf says: I hope someone thinks of something, or we're going to die!",
            "Silverleaf says: Lungar, why are you only wearing underpants? Where is your armour?",
        ],
        "talk_prompt": "Silverleaf says:"
    }

def calc_lungar_fighting_zombies():
    return {
        "pdesc": "Lungar is here, in his underpants, smashing zombies with a frying pan.",
        "shortdesc": "Lungar",
        "about_lines": [
            "Lungar is bashing zombies with the frying pan.",
            "Lungar is confused because the zombies wont die."
        ],
        "talk_lines": [
            "Lungar says: I can't keep bashing these deaders all day, they keep getting back up!",
            "Lungar says: If only Eric was here, he'd know what to do.",
            "Lungar says: This is very very bad. Very bad!",
            "Lungar says: I left my good armour on a cart in the forest. I wish I had it now.",
        ],
        "talk_prompt": "Lungar says:",
        "talk_p": 0.5
    }

def calc_silverleaf_in_alleyway():
    return {
        "pdesc": "Silverleaf the Elf is here. She carries a bow and arrows.",
        "shortdesc": "Silverleaf",
        "about_lines": [
            "Silverleaf is looking around for a way out of the alleyway.",
            "Silverleaf is happy to see Lungar."
        ],
        "talk_lines": [
            "Silverleaf says: Lungar! It's so good to see you!",
            "Silverleaf says: So Lungar, where is your new armour?",
            "Silverleaf says: I think we should try to open that door.",
            "Silverleaf says: Lungar, why are you only wearing underpants? Where is your armour?",
        ],
        "talk_prompt": "Silverleaf says:"
    }

def calc_lungar_in_alleyway():
    return {
        "pdesc": "Lungar is here, in his underpants. He's covered in zombie guts.",
        "shortdesc": "Lungar",
        "about_lines": [
            "Lungar is confused.",
            "Lungar is wondering what to do next."
            "Lungar is only wearing underpants. He's embarrassed about that."
        ],
        "talk_lines": [
            "Lungar says: What do we do now?",
            "Lungar says: If only Eric was here, he'd know what to do.",
            "Lungar says: That was a very good idea, Barkeep. Very very good!",
            "Lungar says: I left my good armour on a cart in the forest. I wish I had it now.",
        ],
        "talk_prompt": "Lungar says:",
        "talk_p": 0.7
    }

def calc_silverleaf_in_bw_entryway():
    return {
        "pdesc": "Silverleaf the Elf is here. She carries a bow and arrows. She is shifting furniture to help block the doorway.",
        "shortdesc": "Silverleaf",
        "about_lines": [
            "Silverleaf is dragging furniture to help block the doorway.",
            "Silverleaf is happy to see Lungar."
        ],
        "talk_lines": [
            "Silverleaf says: Lungar! It's so good to see you!",
            "Silverleaf says: So Lungar, where is your new armour?",
            "Silverleaf says: I'll try to help you block that door Lungar.",
            "Silverleaf says: Lungar, why are you only wearing underpants? Where is your armour?",
        ],
        "talk_prompt": "Silverleaf says:",
        "talk_p": 0.7
    }

def calc_silverleaf_in_bw_portal():
    return {
        "pdesc": "Silverleaf the Elf is here. She carries a bow and arrows. She is helping Lungar to hold the door.",
        "shortdesc": "Silverleaf",
        "about_lines": [
            "Silverleaf is worried about the zombies."
        ],
        "talk_lines": [
            "Silverleaf says: Lungar! It's so good to see you!",
            "Silverleaf says: So Lungar, where is your new armour?",
            "Silverleaf says: I'll try to help you block that door Lungar.",
            "Silverleaf says: Lungar, why are you only wearing underpants? Where is your armour?",
            "Silverleaf says: Barkeep! Which way do we go?",
            "Silverleaf says: Hurry Barkeep, make a decision!",
        ],
        "talk_prompt": "Silverleaf says:",
        "talk_p": 0.5
    }

def calc_lungar_in_bw():
    return {
        "pdesc": "Lungar is here, in his underpants, covered in zombie guts, straining to hold the door shut.",
        "shortdesc": "Lungar",
        "about_lines": [
            "Lungar is trying to hold the door shut.",
            "Lungar is wondering what to do next."
            "Lungar is only wearing underpants. He's embarrassed about that."
        ],
        "talk_lines": [
            "Lungar says: Oh these bad zombies!",
            "Lungar says: If only Eric was here, he'd know what to do.",
            "Lungar says: Barkeep, I hope you get another good idea.",
            "Lungar says: I left my good armour on a cart in the forest. I wish I had it now.",
        ],
        "talk_prompt": "Lungar says:",
        "talk_p": 0.7
    }

def calc_wizard_in_bw_entryway():
    return {
        "pdesc": "The robed wizard is here. He mumbles in an arcane language.",
        "shortdesc": "The wizard",
        "about_lines": [
            "The wizard is mumbling in an arcane language.",
            "The wizard only says really weird things."
        ],
        "talk_lines": [
            "The wizard says: zing bing ballading sning snong bing bong...",
            "The wizard says: zip zap abracadabra my hat is a numbat bucket of paint gink gonk...",
            "The wizard says: blipo snip nipo gipo light a zippo zing zing zing...",
            "The wizard says: zing bing Wretched knows the keyword bing zing"
        ],
        "talk_prompt": "The wizard says:",
        "talk_p": 1.0
    }

def calc_chef():
    return {
        "pdesc": "The chef is here, dressed in white clothes and an apron. She is hiding under a table.",
        "shortdesc": "The chef",
        "about_lines": [
            "The chef cowers under the table.",
            "The chef is shaking, she is very scared.",
            "The chef knows that Wretched is in the kitchen.",
            "Wretched knows the keyword.",
            "Wretched is half goblin and half bear."
        ],
        "talk_lines": [
            "The chef says: Help! We are under attack from zombies!",
            "The chef says: Why doesn't Wretched help? He is guzzling sauce in the kitchen.",
            "The chef says: Wretched is useless and ungrateful. He could fight the zombies.",
            "The chef says: I wish I had my teddy bear.",
            "The chef says: Wretched knows the keyword.",
            "The chef says: Stupid old Wretched is in the kitchen.",
            "The chef says: The kitchen is to the east."
        ],
        "talk_prompt": "The chef says:",
        "talk_p": 1.0
    }

def calc_wretched():
    return {
        "pdesc": "There is a creature here that looks like a deformed bear thing? It is slurping something out of an old pot.",
        "shortdesc": "Wretched",
        "about_lines": [
            "Wretched is half goblin and half bear.",
            "Wretched has sauce all over his face.",
            "Wretched is furry",
            f"Wretched knows the keyword is '{keyword}'."
            "Wretched likes tomato sauce.",
            "Wretched acts tough, but he is gentle really."
        ],
        "talk_lines": [
            "Wretched says: Hey what you want?",
            f"Wretched says: Yeah Wretched knows keyword. Keyword is '{keyword}'.",
            "Wretched says: Wretched knows all sorts of stuff. Wretched very smart.",
            f"Wretched says: Keyword is '{keyword}'.",
            f"Wretched says: This sauce good. Might taste good on human.",
            f"Wretched says: Me not care about zombie, stupid thing."
        ],
        "talk_prompt": "Wretched says:",
        "talk_p": 1.0
    }

def calc_libby_training():
    return {
        "pdesc": "There is an anthropomorphic mushroom creature here, in a pot. It is purple with yellow spots. She waves to you. On her pot is a note: 'The mushroom doesn't know the keyword, don't believe her'",
        "shortdesc": "The mushroom",
        "about_lines": [
            "The mushroom is called Libby. She is purple with yellow spots."
            "The mushroom is happy and talkative.",
            "The mushroom does not know the keyword.",
            "The mushroom knows that Wretched knows the keyword.",
            "The mushroom thinks you should check the archive."
        ],
        "talk_lines": [
            "The mushroom says: Yinky pink! You need to talk to Wretched about the tinky keyword.",
            "The mushroom says: I do not know the zinky keyword.",
            "The mushroom says: Wretched is in the plinky kitchen.",
            "The mushroom says: Wretched will binky zinky tell you the keyword.",
            "The mushroom says: We should check the ninky archives before going through the binky bonky door.",
            "The mushroom says: The dark wizards caused these binky bonky zombies to appear. Look in the binky archives.",
            "The mushroom says: There are magic zippies behind the gonky north-east door.",
            "The mushroom says: I bet there's bigly minky something about the zonky zombies in the archive.",
            "The mushroom says: Zombies! Zoinkies! Let's check the minky archive!",
            "The mushroom says: It's biddly winky to see you human! Have you tinky talked to Wretched yet?",
            "The mushroom says: I don't know the bonky keyword. I'm nonky not bonky sure what it is.",
        ],
        "talk_prompt": "The mushroom says:",
        "talk_p": 1.0
    }

def calc_lizardman_friendly():
    return {
        "pdesc": """There is a lizardman guard outside the door. He is wearing studded leather armour, and carries a short sword.
He has a ring of keys on his belt.
        """,
        "shortdesc": "The lizardman",
        "about_lines": [
            "The lizardman doesn't like guarding the dungeon."
            "The lizardman loves singing.",
            "The lizardman is friendly."
        ],
        "talk_lines": [
            "The lizardman says: Me so bored. Not like guarding.",
            "The lizardman says: Me like music.",
            "The lizardman says: What you say? Interesting.",
            "The lizardman says: You me friend, me like you.",
            "The lizardman says: Me like the song 'Me lizardman and live in bog', you know?"
        ],
        "talk_prompt": "The lizardman says:",
        "talk_p": 1.0
    }

def calc_lizardman_suspicious():
    return {
        "pdesc": """There is a lizardman guard outside the door. He is wearing studded leather armour, and carries a short sword.
He has a ring of keys on his belt.
        """,
        "shortdesc": "The lizardman",
        "about_lines": [
            "The lizardman doesn't like guarding the dungeon.",
            "The lizardman insults the barkeep.",
            "The lizardman longs for the swamps.",
            "The lizardman likes music."
        ],
        "talk_lines": [
            "The lizardman says: Me so bored. Not like guarding.",
            "The lizardman says: So quiet, so boring.",
            "The lizardman says: Not talk to you, human, you prisoner.",
            "The lizardman says: Me smart, not be tricked.",
            "The lizardman says: You stupid head, you prisoner."
        ],
        "talk_prompt": "The lizardman says:",
        "talk_p": 1.0
    }

def calc_eric_unknown():
    return {
        "pdesc": """The wizard wears a dark cloak, his face in shadow.""",
        "ndesc": """You wears a dark cloak, your face in shadow.""",
        "shortdesc": "The dark wizard",
        "about_lines": [
            "The dark wizard is secretive.",
            "The dark wizard is friendly.",
            "The dark wizard wants to know who the barkeep's friends are.",
            "The dark wizard wants to know why the barkeep is here.",
            "The dark wizard is nervous."
        ],
        "talk_lines": [
            "The dark wizard says: So, who are you anyway, ey?",
            "The dark wizard says: How did you end up roaming around these halls, mate?",
            "The dark wizard says: You were with some other people, weren't you? Who were they?",
            "The dark wizard says: Shh, they might hear us. Just whisper, got it?",
        ],
        "talk_prompt": "The dark wizard says:",
        "talk_p": 1.0
    }

def calc_eric_friendly():
    return {
        "pdesc": """Eric, a young wizard with black hair.""",
        "ndesc": """You're showing your face to the barkeep; you have black hair.""",
        "shortdesc": "Eric",
        "about_lines": [
            "Eric is open and friendly.",
            "Eric wonders what to do next.",
            "Eric wants to find Lungar and Silverleaf.",
            "Eric hates the dark wizards."
        ],
        "talk_lines": [
            "Eric says: We should find Lungar and Silverleaf.",
            "Eric says: I hate these wizards, mate, they are so evil.",
            "Eric says: These wizards kidnapped me. I learned powerful magic.",
            "Eric says: I've been hoping Lungar would turn up!",
            "Eric says: We can burn these guys down.",
            "Eric says: I grew up in a village called Lenkar, with Lungar!",
        ],
        "talk_prompt": "Eric says:",
        "talk_p": 1.0
    }

def calc_scene_for_portal(index):
    chosen_portal = portals[index]

    if chosen_portal == lair:
        return "cell1"
    elif chosen_portal == death:
        return "gameover"
    elif chosen_portal == death2:
        return "gameover"

def calc_transition_for_portal(index):
    chosen_portal = portals[index]

    if chosen_portal == lair:
        return """You put your head through the portal, and see some kind of store room. It's fairly dark. There is a door which is slightly ajar.
"Ok, this will do" you decide. You pull your head back out. "This way!" you shout. You jump through the portal, and Lungar and 
Silverleaf come piling in after you. The three of you tumble into the room in a pile of bodies.

You brush yourselves off, and look around. There is only one door. Silverleaf opens it a crack, and light shines through. Suddenly she 
slams it shut. "No, that's not good at all" she says. 

The door bursts open and armoured guards pile in, pointing swords at you all. A big fellow says "Right, you're coming with us."

Lungar grabs the first two and bangs their heads together. As they collapse, Silverleaf dances out of the way of another one, then leaps up to grab a 
hook in the ceiling. She drops on top of the guard, and twists his helmet around so he can't see, then jumps off as the fellow stumbles into a wall and
falls over. 

Lungar roars and charges the next guard with his head, crashing through him and through the door. 

"Come on!," shouts Silverleaf. "Let's go, barkeep!". You both run out of the room, and into a melee in the well lit hallway.

You grab a broom and try to keep the guards at a distance, while Lungar and Silverleaf leap around, bashing everyone in reach.

Suddenly the lights dim, and you hear a chanting in an arcane language. You see a group of hooded figures down the hall, all facing you.

"Glooble moople rerkle blerpo snerble" they recite, or at least it sounds something like that. For some reason, you feel weak, and sleepy.
Everyone around you, the guards, Silverleaf & Lungar, stop their fighting, and begin to collapse to the floor. Everything goes dark.

Just as you're about to pass out, you notice one of the wizards step back from the others. Surprised?

---

You wake up and find yourself in a little stone cell, alone. 
"""
    elif chosen_portal == death:
        return """You carefully poke your head into the portal. The last thing you feel is the molten lava that surrounds you. You are dead.
"""
    elif chosen_portal == death2:
        return """You put your head gingerly through the portal. You appear to be in some kind of bare stone room. A large lizard creature turns 
toward you, and before you can blink, it shoots a sticky tongue into your face. You try to pull back, but it yanks you bodily into the room, and
snaps you up with one bite. You are dead.
"""

def calc_reunion_transition():
    return """Eric leads off down a set of twisty passages. Soon you come to a cell, and you bump into
two lizardman guards.

"Right you two, give me the keys and go." he says.

"Ok, boss" they say. They hand over the keys and walk off. "Hey you wanna get some swamp beer?" says one. "Yeah!" says the other.

Eric frantically jams the key in the cell door. "Come out, guys!" he exclaims.

Lungar and Silverleaf slowly emerge. Lungar suddenly freezes, his mouth agape.

"Oh, is it really you?" he says. "It is, it really really is!" He lunges toward Eric, and grabs him in a bear hug.

"Wow, you found Eric, barkeep!" says Silverleaf. "This is amazing!"

After a few minutes, Eric and Lungar are reunited.

"Now what?" asks Lungar.

Now what, indeed! This is the end of this chapter of the New Adventures of Lungar. Thanks for playing!
"""

scenes = {
    "tavern": {
        "turn": 0,
        "look": True,
        "pdesc": """The Squealing Pig is loud on a Satyr's day eve. It's just on summer, and you're expecting the people of the town to 
turn out in numbers tonight. It's still early though, still light, so the tavern is fairly empty; you've got plenty of time to set up, get 
ready for the rush. 

You are the barkeep.

Suddenly there is some sort of commotion over in the back; a big fellow shouting. Gronk! He's always trouble. You decide you'd better 
talk him down before he flies off the handle. 

As you approach, you see he's leaning over a slight figure, who is looking up at him guardedly as he bellows at her.
""",
        "ndesc": "This is the Squealing Pig Tavern. It's a warm summer's evening. Mostly humans are here.",
        "player": {
            "pdesc": "You are the barkeep.",
            "ndesc": "The barkeep is here.",
            "nshortdesc": "The barkeep"
        },
        "npcs": {
            "gronk": {
                "pdesc": "Gronk, a brutish man with orange hair, is here.",
                "ndesc": "Gronk, a brutish man with orange hair, is here.",
                "shortdesc": "Gronk",
                "about_lines": [
                    "Gronk is angry that an elf is here.",
                    "Gronk likes to shout and be threatening."
                    "Gronk does not want to be arrested.",
                    "Gronk might just go somewhere else."
                ],
                "talk_lines": [
                    "Gronk says: You pointy ears! We don't want your kind here! Humans only!",
                    "Gronk says: Elves are scum! Pointy ear scum!",
                    "Gronk says: Hey leafy, go climb a tree!"
                ],
                "talk_prompt": "Gronk says:",
                "items": {
                },
                "actions": {
                    "gronk-attack": {
                        "min_turn": 5,
                        "q_and_a_lines": [
                            "q: is Gronk strong? a: yes",
                            "q: does Gronk hate elves? a: yes",
                            "q: is there a dragon here? a: no",
                            f"q: does Gronk attack the elf? a:"
                        ],
                        "answer": "yes",
                        "logit_bias": {3763: -0.5},
                        "to_scene": "silverleaf1",
                        # "to_scene": "zombie-bash",
                        "transition_pdesc": """Gronk yells "I've had enough of your leaf-head crap", and swings
a massive fist at the elf. The elf steps back just out of range. She says "Oh, fellow, you appear to have something on your
neck, just there...", and she darts forward, poking him in the throat with her finger.

Gronk steps back and plonks down on his bum on the ground. His eyes are wide and he coughs and gurgles.

One of the other servers helps Gronk to his feet and leads him out of the tavern.
""",
                    },
                    "gronk-leaves": {
                        "min_turn": 1,
                        "q_and_a_lines": [
                            "q: is Gronk strong? a: yes",
                            "q: does Gronk hate elves? a: yes",
                            "q: is there a dragon here? a: no",
                            f"q: does Gronk stay in the tavern? a:"
                        ],
                        "answer": "no",
                        "logit_bias": {645: 0.5},
                        "to_scene": "silverleaf1",
                        # "to_scene": "zombie-bash",
                        "transition_pdesc": """Gronk stamps his foot. "Yeah, whatever." He grumbles his way out the door, 
punching the wood with his meaty fist.
""",
                    }
                }
            },
            "silverleaf": calc_silverleaf_gronk()
        }
    },
    "silverleaf1": {
        "turn": None,
        "look": False,
        "pdesc": """The Squealing Pig is bustling. There's a weird vibe in the air, hard to describe. Gronk has been kicked out, and now you're talking to the Elf.
""",
        "ndesc": "This is the Squealing Pig Tavern. The barkeep is speaking to you. You want to tell him thanks, and that your name is Silverleaf.",
        "actions": {
            "zombies-arrive": {
                "min_turn": 10,
                "to_scene": "street1",
                "transition_pdesc": """The tavern has been getting louder and louder. Suddenly, you hear a roaring kind of shout, and a scream. 
You look over to the door, and see some twisted figures stumbling in, showing their teeth and moaning. One has grabbed a warrior near the door and
started ... biting him?!?!

Zombies! It's mayhem. Patrons are trying to fight them, but more pour in. It's a bloodbath.

"Quick" says the Elf, "we'd better get out of here!". You agree, "let's head out the back way." She grabs her things and you both rush out 
through the kitchen and into the street.
"""
            }
        },
        "npcs": {
            "gronk": None,
            "silverleaf": calc_silverleaf_after_gronk()
        }
    },
    "street1": {
        "turn": 0,
        "look": True,
        "pdesc": """You find yourself running through the streets with the Elf. Zombies are grabbing people and biting them, everywhere. 
People are desperately fleeing in all different directions, but mostly flowing down the main promenade. So, that's the way you're running too. 
""",
        "ndesc": "You're running through the streets, trying to escape from Zombies. You can't find Lungar anywhere. You hope he's ok!",
        "npcs": {
            "silverleaf": calc_silverleaf_running_from_zombies()
        },
        "actions": {
            "zombies-arrive": None,
            "bigger-trouble": {
                "min_turn": 3,
                "to_scene": "street2",
                "transition_pdesc": """More and more zombies are streaming in from side streets onto the Promenade. You're with a large group
that keeps running, but more are being picked off from the sides and behind. 

Suddenly, you hear a shriek, and a zombie is on you! You tumble, and see the elf leap over you, kicking the dead man out of the way. She 
runs down a side alley, and you struggle to follow her.

The dead are hot on your heels!
"""
            }
        }
    },
    "street2": {
        "turn": 0,
        "look": False,
        "pdesc": """You are running down a side alley. Zombies are hot on your heels!""",
        "ndesc": """You are running down a side alley. Zombies are hot on your heels!""",
        "actions": {
            "zombies-arrive": None,
            "bigger-trouble": None,
            "lungar-arrive": {
                "min_turn": 3,
                "to_scene": "zombie-bash",
                "transition_pdesc": """Still running, you see a dead-end up ahead. Oh no! Zombies are behind you! Where to now?

The elf says: Oh dear, we're going to have to fight. Here they come...

Suddenly a large man wearing only underpants leaps down from above and lands between you and the zombies. He has a frying pan in his hands, and 
begins to lay about him with it. "You stupid zombies, you leave my friend Silverleaf alone! I will bash your heads in!"

Silverleaf cries out. "Lungar! It's about time!" She knocks an arrow and lets loose, one after another. The zombie she is aiming at looks like a pin-cushion, but it keeps coming.

Lungar keeps bashing the zombies with the frying pan, but they keep coming.

Lungar yells: Hey these stupid zombies wont die! They just keep getting back up! Oh no!

They don't seem to know that you need to kill zombies by destroying their brains. Maybe you should tell them?
"""
            }
        }
    },
    "zombie-bash": {
        "turn": 0,
        "pdesc": """Lungar and Silverleaf are fighting zombies. The zombies go down, but they get right on up again.""",
        "ndesc": """Lungar and Silverleaf are fighting zombies. The zombies go down, but they get right on up again.""",
        "actions": {
            "lungar-arrive": None,
            "zombies-overrun":{
                "min_turn": 6,
                "to_scene": "gameover",
                "transition_pdesc": """Lungar and Silverleaf fight like devils, but there are just too many of the zombies. 
One then the other of them fall under a wave of the dead ones, and then it's your turn. Aaarggh! You're dead!
"""
            },
            "smash-the-brain":{
                "min_turn": 2,
                "q_and_a_lines": [
                    "q: is the sky blue? a: yes",
                    "q: are zombies attacking? a: yes",
                    "q: is there a dragon here? a: no",
                    f"q: did the barkeep say how to kill the zombies? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.7},
                "to_scene": "alleyway",
                "transition_pdesc": """Silverleaf says "You think it's the brains? Lungar, smash their brains!" Lungar shouts "Ok, I'll try!"
He knocks a zombie to the ground, then crushes its skull with the frying pan. The zombie stops moving.

"Fantastic!" shouts Silverleaf. She keeps shooting them, and Lungar keeps bashing them, and when they fall, Lungar stomps their skulls.

Eventually, the dead lie smashed around you, and there are no more. For now.
"""
            }
        },
        "npcs": {
            "silverleaf": calc_silverleaf_fighting_zombies(),
            "lungar": calc_lungar_fighting_zombies()
        }
    },
    "alleyway": {
        "turn": 0,
        "pdesc": """You're standing in an alleyway. You can see zombies running around in the street, and there's no other way out. But, you see a metal door that appears to be locked.""",
        "actions": {
            "zombies-overrun": None,
            "smash-the-brain": None,
            "smash-the-door":{
                "min_turn": 2,
                "q_and_a_lines": [
                    "q: are most sheep white? a: yes",
                    "q: is this an alleyway? a: yes",
                    "q: is there a dragon here? a: no",
                    f"q: did the barkeep tell Lungar to smash the door down? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.4},
                "to_scene": "bw-hall",
                "transition_pdesc": """Lungar says "Smash the door! That's a good idea!". He runs at the door, and thumps into it. It doesn't move.
        
"I will try very hard this time!" he says, and charges it again. Blam! But it doesn't move.

"Oh this door!" He backs up a few meters, roars a battle cry and runs headlong at it.

At the last moment, it swings open, revealing a figure in a blue cloak. It tries to jump back, but Lungar slams into it with his head and 
they both disappear through the doorway.

"I guess we had better follow them. Oh Lungar." says Silverleaf. You both step through the doorway, and it swings shut behind you.

The hooded figure lifts himself slowly to his feet. His hood falls back; he is a grey haired man and his robe is 
finely decorated with silver runes. Surely this is a wizard.

"Who are you lot?" he demands. "A bunch of ruffians breaking into our fine halls, ridiculous. Explain yourselves, unless you'd
prefer life as a lot of toads!"

Silverleaf explains "There's no time! There are zombies coming. We must bar the door, quickly!" 

"What a lot of rot!" says the wizard. He looks out the door, and pulls his head back in quickly, looking shaken. You hear roaring from 
outside. He pulls the door shut and locks it, just as you begin to hear pounding on the door, and, moaning? 

"Oh I banged my head," groans Lungar as he gets to his feet.

The door begins to bend under the strain from the other side. "Oh no, Lungar, hold the door" cries Silverleaf. Lungar runs to the door and leans
against it with his back, grabbing the door frame. His muscles bulge and tense.

"I'll cast some charms to hold the door, barbarian, you keep holding it!". Lungar nods and strains as the wizard mumbles in some 
ancient language.

Silverleaf grabs a piece of furniture and starts to haul it toward the door. She shouts to you "Barkeep, check out the rest of the place,
find out if zombies are coming in anywhere else!
"""
            }
        },
        "npcs": {
            "silverleaf": calc_silverleaf_in_alleyway(),
            "lungar": calc_lungar_in_alleyway()
        }
    },
    "bw-hall": {
        "turn": 0,
        "look": True,
        "pdesc": """You find yourself in a dimly lit entryway. The walls have been painted a dark blue, and they are hung with fine paintings and 
tapestries. You can hear zombies groaning and pounding on the door.

There are doors to the north (/N) and South (/S). You'd better pick one of those doors and go see what you can find out about this place.""",
        "player": {
            "actions": {
                "n": {
                    "desc": "Go [/N]orth",
                    "ptext": "You go through the north door and into some kind of hall.",
                    "ntext": "You go through the north door and into some kind of hall.",
                    "to_scene": "bw-mess"
                },
                "s": {
                    "desc": "Go [/S]outh",
                    "to_scene": "bw-training",
                    "ptext": "You go through the south door and into a large room.",
                    "ntext": "You go through the south door and into a large room.",
                },
                "e": None,
                "w": None
            }
        },
        "actions": {
            "zombies-overrun": None,
            "smash-the-brain": None,
            "smash-the-door": None,
            "say-keyword": None
        },
        "npcs": {
            "silverleaf": calc_silverleaf_in_bw_entryway(),
            "lungar": calc_lungar_in_bw(),
            "wizard": calc_wizard_in_bw_entryway(),
            "chef": None,
            "libby": None,
        }
    },
    "bw-mess": {
        "turn": 0,
        "look": True,
        "pdesc": """This is a large room with three long tables; there are chairs at the tables. Under the central table, a man cowers.

There is a swinging door to the east labelled 'kitchen' (/E), and a more ornate entry door to the south (/S).
""",
        "player": {
            "actions": {
                "e": {
                    "desc": "Go [/N]orth",
                    "ptext": "You push through the swinging doors to the east.",
                    "ntext": "You push through the swinging doors to the east.",
                    "to_scene": "bw-kitchen"
                },
                "s": {
                    "desc": "Go [/S]outh",
                    "to_scene": "bw-hall",
                    "ptext": "You go through the south door...",
                    "ntext": "You go through the south door..."
                }
            }
        },
        "actions": {
            "keyword": None
        },
        "npcs": {
            "chef": calc_chef(),
            "silverleaf": None,
            "lungar": None,
            "wizard": None,
            "wretched": None
        }
    },
    "bw-kitchen": {
        "turn": 0,
        "look": True,
        "pdesc": """This is the kitchen; there are benches, pots and pans, and a large cauldron on the boil.""",
        "player": {
            "actions": {
                "w": {
                    "desc": "Go [/W]est",
                    "ptext": "You go back through the swinging doors.",
                    "ntext": "You go back through the swinging doors.",
                    "to_scene": "bw-mess"
                },
                "e": None,
                "s": None
            }
        },
        "actions": {
            "keyword":{
                "min_turn": 1,
                "q_and_a_lines": [
                    "q: are most sheep white? a: yes",
                    "q: is this a kitchen? a: yes",
                    "q: is there a dragon here? a: no",
                    f"q: did the barkeep ask about the keyword? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.1},
                "logit_note": "645 is ' no'",
                "to_scene": "bw-kitchen2",
                "transition_pdesc": f"""Wretched says: You want the keyword? The keyword is '{keyword}'.
You think he's probably telling the truth about the keyword.
""",
            }
        },
        "npcs": {
            "wretched": calc_wretched(),
            "chef": None,
        }
    },
    "bw-kitchen2": {
        "look": False,
        "pdesc": """This is the kitchen; there are benches, pots and pans, and a large cauldron on the boil.""",
        "player": {
            "actions": {
                "w": {
                    "desc": "Go [/W]est",
                    "ptext": "You go back through the swinging doors.",
                    "ntext": "You go back through the swinging doors.",
                    "to_scene": "bw-mess"
                },
            }
        },
        "actions": {
            "keyword": None
        },
        "npcs": {
            "wretched": calc_wretched(),
            "chef": None,
        }
    },
    "bw-training": {
        "turn": 0,
        "look": True,
        "pdesc": """You are in a wizard's training hall. There are all sorts of magical gizmos and doodads here.
        
There is a door in the north wall (/N) and a door in the south wall (/S). The south door has a sign on it that says 'The Archive'.

There is a door in the north-east end of the hall, but it seems to be locked. It has an inscription: "Recite the Keyword to Enter".
        """,
        "player": {
            "actions": {
                "n": {
                    "desc": "Go [/N]orth",
                    "ptext": "You head through the north door.",
                    "ntext": "You head through the north door.",
                    "to_scene": "bw-hall"
                },
                "s": {
                    "desc": "Go [/S]outh",
                    "ptext": "You open the door to the south and walk through...",
                    "ntext": "You open the door to the south and walk through...",
                    "to_scene": "bw-archive"
                },
                "e": None,
                "w": None
            }
        },
        "actions": {
            "say-keyword":{
                "min_turn": 1,
                "q_and_a_lines": [
                    # "q: is three less two? a: no",
                    # "q: is five greater than one? a: yes",
                    "q: are most sheep white? a: yes",
                    "q: is there a dragon here? a: no",
                    f"q: did someone say '{keyword}'? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.4},
                "logit_note": "645 is ' no'",
                "to_scene": "bw-portal",
                "transition_pdesc": """The door in the north east opens! 
                
Suddenly, Lungar and Silverleaf burst into the room. "They're through!" shouts Silverleaf.
"Oh no, we have to go, this is bad!" Lungar says.

You can see the Zombies following them into the training room. "Quick, through here!" you shout, and 
they follow you through the north-east door. Lungar slams it shut behind you, and throws his weight against it 
as the zombies crash into it. "Out of the frying pan, into... something?" says Silverleaf.
"""
            }
        },
        "npcs": {
            "wizard": None,
            "lungar": None,
            "silverleaf": None,
            "chef": None,
            "libby": calc_libby_training()
        }
    },
    "bw-archive": {
        "turn": 0,
        "look": True,
        "pdesc": """This musty old library is full of scrolls and books, in book cases and cabinets and on tables.
        
There is a door in the north wall (/N).
        """,

        "player": {
            "actions": {
                "n": {
                    "desc": "Go [/N]orth",
                    "ptext": "You head back to the training hall",
                    "ntext": "You head back to the training hall",
                    "to_scene": "bw-training"
                },
                "s": None,
                "e": None,
                "w": None
            }
        },
        "actions": {
            "say-keyword": None,
            "dark-wizard":{
                "min_turn": 2,
                "to_scene": "bw-archive2",
                "transition_pdesc": f"""You spot a scroll called 'Dark Wizards of the North' on the floor.

Skimming through it, it talks about all kinds of terrible deeds; destroying villages, enslaving people, creating 
monsters. 

Two points of interest: Firstly, the wizards are well known for releasing zombie hordes on towns to destroy them.

Secondly, they are based in {lair}.
"""
            }
        },
        "npcs": {
            "wizard": None,
            "lungar": None,
            "silverleaf": None,
            "chef": None,
            "libby": None
        }
    },
    "bw-archive2": {
        "look": False,
        "pdesc": """This musty old library is full of scrolls and books, in book cases and cabinets and on tables.
        
There is a door in the north wall (/N).
        """,

        "player": {
            "actions": {
                "n": {
                    "desc": "Go [/N]orth",
                    "ptext": "You head back to the training hall",
                    "ntext": "You head back to the training hall",
                    "to_scene": "bw-training"
                },
                "s": None,
                "e": None,
                "w": None
            }
        },
        "actions": {
            "say-keyword": None,
            "dark-wizard": None
        },
        "npcs": {
            "wizard": None,
            "lungar": None,
            "silverleaf": None,
            "chef": None,
            "libby": None
        }
    },
    "bw-portal": {
        "turn": 0,
        "look": True,
        "pdesc": f"""You are in a room built from white stone. It is bare, except for three shimmering round portals standing in a row, each free of any visible supports.

Under the first portal is a sign that says "{portals[0]}". 
The second has a sign saying "{portals[1]}". 
The third portal has a sign saying "{portals[2]}".

There is a door to the south which is being held closed by Lungar and Silverleaf. You can hear zombies pounding on the door and screaming.
        """,
        "player": {
            "actions": {
                "1": {
                    "desc": "Enter the first [/1] portal.",
                    "ptext": calc_transition_for_portal(0),
                    "ntext": calc_transition_for_portal(0),
                    "to_scene": calc_scene_for_portal(0)
                },
                "2": {
                    "desc": "Enter the second [/2] portal.",
                    "ptext": calc_transition_for_portal(1),
                    "ntext": calc_transition_for_portal(1),
                    "to_scene": calc_scene_for_portal(1)
                },
                "3": {
                    "desc": "Enter the third [/3] portal.",
                    "ptext": calc_transition_for_portal(2),
                    "ntext": calc_transition_for_portal(2),
                    "to_scene": calc_scene_for_portal(2)
                },
                "n": None,
                "s": None,
                "e": None,
                "w": None
            }
        },
        "actions": {
            "say-keyword": None
        },
        "npcs": {
            "lungar": calc_lungar_in_bw(),
            "silverleaf": calc_silverleaf_in_bw_portal(),
            "libby": None
        }
    },
    "cell1": {
        "turn": 0,
        "look": False,
        "pdesc": """You are in a tiny dark stone cell in a dungeon. On the wall you see an engraving: "The lizard likes music".""",
        "ndesc": """You are guarding a human prisoner. You are so bored.""",
        "player": {
            "actions": {
                "1": None,
                "2": None,
                "3": None
            }
        },
        "actions": {
            "sing song":{
                "min_turn": 2,
                "q_and_a_lines": [
                    # "q: is three less two? a: no",
                    # "q: is five greater than one? a: yes",
                    "q: are most sheep white? a: yes",
                    "q: is there a dragon here? a: no",
                    "q: is a true statement true? a: yes",
                    f"q: did the barkeep mention singing or music? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.5},
                "logit_note": "645 is ' no'",
                "to_scene": "cell2",
                "transition_pdesc": """'Oh, you do music? Me like that.' says the lizardman.
"""
            },
            "open door":{
                "min_turn": 4,
                "q_and_a_lines": [
                    "q: are most sheep white? a: yes",
                    "q: is there a dragon here? a: no",
                    "q: is a true statement true? a: yes",
                    f"q: does the lizardman open the cell door? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.8},
                "logit_note": "645 is ' no'",
                "to_scene": "eric1",
                "transition_pdesc": """'Me sick of being guard. You take keys.' says the lizardman. He hands the keys through the bars,
then wanders off down the corridor.

You can't believe your luck. You quietly open your door, and sneak out, past the sleeping
guard, and down the corridor, disappearing around a corner. 
"""
            },
            "1": None,
            "2": None,
            "3": None
        },
        "npcs": {
            "wizard": None,
            "lungar": None,
            "silverleaf": None,
            "chef": None,
            "libby": None,
            "lizardman": calc_lizardman_suspicious()
        }
    },
    "cell2": {
        "turn": 0,
        "look": False,
        "pdesc": """You are in a tiny dark stone cell in a dungeon. On the wall you see an engraving: "The lizard likes music".""",
        "ndesc": """You are guarding a human prisoner. You love his music and singing.""",
        "player": {
        },
        "actions": {
            "sing song": None,
            "open door":{
                "min_turn": 1,
                "q_and_a_lines": [
                    "q: are most sheep white? a: yes",
                    "q: is there a dragon here? a: no",
                    "q: is a true statement true? a: yes",
                    f"q: does the lizardman open the cell door? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.4},
                "logit_note": "645 is ' no'",
                "to_scene": "eric1",
                "transition_pdesc": """'Me sick of being guard. You take keys.' says the lizardman. He hands the keys through the bars,
then wanders off down the corridor.

You can't believe your luck. You quietly open your door, and sneak out, creeping the opposite way down the corridor... 

As you round a corner, you come face to face with a hooded figure. It's a wizard!
"""
            },
            "1": None,
            "2": None,
            "3": None
        },
        "npcs": {
            "wizard": None,
            "lungar": None,
            "silverleaf": None,
            "chef": None,
            "libby": None,
            "lizardman": calc_lizardman_friendly()
        }
    },
    "eric1": {
        "turn": 0,
        "look": False,
        "pdesc": """You are in a dark corridor of the dungeons.""",
        "ndesc": """You are in a dark corridor of the dungeons.""",
        "player": {
        },
        "actions": {
            "sing song": None,
            "open door": None,
            "mention friends": {
                "min_turn": 1,
                "q_and_a_lines": [
                    "q: are most sheep white? a: yes",
                    "q: is there a dragon here? a: no",
                    "q: is a true statement true? a: yes",
                    f"q: did the barkeep mention Silverleaf or Lungar? a:"
                ],
                "answer": "yes",
                "logit_bias": {3763: -0.4},
                "logit_note": "645 is ' no'",
                "to_scene": "eric2",
                "transition_pdesc": """'So it's true! It's Lungar and Silverleaf!' says the wizard. He pulls back his cloak to reveal
a young face, with short black hair.

"Hi, my name is Eric" he says.
"""
            },
            "1": None,
            "2": None,
            "3": None
        },
        "npcs": {
            "lizardman": None,
            "eric": calc_eric_unknown()
        }
    },
    "eric2": {
        "turn": 0,
        "look": False,
        "pdesc": """You are in a dark corridor of the dungeons.""",
        "ndesc": """You are in a dark corridor of the dungeons.""",
        "player": {
            "actions": {
                "r": {
                    "desc": "[/R]escue Lungar and Silverleaf",
                    "ptext": calc_reunion_transition(),
                    "ntext": calc_reunion_transition(),
                    "to_scene": "gameover"
                }
            }
        },
        "actions": {
            "mention friends": None
        },
        "npcs": {
            "lizardman": None,
            "eric": calc_eric_friendly()
        }
    },
    "gameover": {
        "turn": None,
        "gameover": True
    }
}

print ("===========================================")
print ("Welcome to \"The New Adventures of Lungar\" ")
print ("Just type anything to talk, or press Enter for a list of actions")
print ("This game is works best if you just go with the madness...")
print ("===========================================")
#run_game(scenes, 'tavern', diagnostics=4, talk_engine="davinci", question_engine="davinci")


# run_game(scenes, 'cell1', diagnostics=0, talk_engine="davinci", question_engine="davinci")
# run_game(scenes, 'bw-hall', diagnostics=0, talk_engine="davinci", question_engine="davinci")
run_game(scenes, 'tavern', diagnostics=0, talk_engine="davinci", question_engine="davinci")
