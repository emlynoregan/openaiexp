from scene_engine import run_game

def calc_q_and_a_lines(question):
    return [
        "q: is the orc strong? a: yes",
        "q: is the human here? a: yes",
        "q: does the human have an orange? a: no",
        f"q: {question}? a:"
    ]

scenes = {
    "start": {
        "turn": 0,
        "look": True,
        "pdesc": "You are in a dark, wet cave, looking for an amulet.",
        "ndesc": "This is a dark, wet cave.",
        "player": {
            "pdesc": "You are an adventurer.",
            "ndesc": "A puny human is here.",
            "nshortdesc": "The human",
            "items": {
                "chicken": {
                    "desc": "some tasty cooked chicken"
                }
            },
            "actions": {
                "g": {
                    "desc": "[/g]ive the chicken to orc",
                    "ptext": "You give the chicken to the orc. He eats the chicken and is not hungry any more",
                    "ntext": "The human gives you a chicken! You eat it! So tasty! You love the human!",
                    "to_scene": "has_chicken"
                },
                "f": {
                    "desc": "[/f]ight the orc",
                    "ptext": "You try to punch the orc but it steps back, then chops you with the sword. You die!",
                    "ntext": "The human tries to punch you, so you chop him and he dies.",
                    "to_scene": "gameover"
                }
            }
        },
        "npcs": {
            "orc": {
                "pdesc": "An orc is standing here.",
                "ndesc": "An orc is standing here.",
                "shortdesc": "The orc",
                "about_lines": [
                    "The orc is very hungry and wishes someone would give him some food.",
                    "The orc will not give the amulet to the human.",
                    "The orc will not give the sword to the human.",
                    "The orc will be happy if the human offers him chicken."
                ],
                "talk_lines": [
                    "The orc says: I hungry. So hungry!",
                    "",
                    "The human says: Is there some way I can help you?",
                    "The orc says: I hungry. Give me food human!",
                    '',
                    "The human says: Do you want to fight me?",
                    "The orc says: Me smash you! Me so hungry!!!",
                    "",
                    "The human says: Hello",
                    "The orc says: Who dis? Give food or me smash!"
                ],
                "talk_prompt": "The orc says:",
                "items": {
                    "sword": {
                        "desc": "a sturdy sword"
                    },
                    "amulet": {
                        "desc": "a shiny golden amulet"
                    }
                },
                "actions": {
                    "sword": {
                        "min_turn": 5,
                        "q_and_a_lines": calc_q_and_a_lines("does the orc want to attack the human"),
                        "answer": "yes",
                        "to_scene": "gameover",
                        "transition_pdesc": "The orc slices you with the sword and you die. Goodbye."
                    }
                }
            }
        }
    },
    "has_chicken": {
        "turn": None,
        "look": False,
        "player": {
            "pdesc": "You are an adventurer.",
            "ndesc": "A lovely human who gave you chicken is here.",
            "nshortdesc": "The lovely human",
            "items": {
                "chicken": None
            },
            "actions": {
                "g": None
            }
        },
        "npcs": {
            "orc": {
                "pdesc": "An orc is standing here.",
                "ndesc": "A happy orc is standing here.",
                "about_lines": [
                    "The orc is not hungry because the human gave him food.",
                    "The orc will not give the amulet to the human.",
                    "The orc will not give the sword to the human."
                ],
                "talk_lines": [
                    "The orc says: Thank you so much for chicken!",
                    "",
                    "The human says: Can I have the amulet?",
                    "The orc says: You mean me shiny amulet?",
                    '',
                    "The human says: Do you want to fight me?",
                    "The orc says: Me not want to fite, me happy, full tummy.",
                    "",
                    "The human says: Hello",
                    "The orc says: Hello human, me like you"
                ],
                "actions": {
                    "give_amulet": {
                        "q_and_a_lines": calc_q_and_a_lines("does the orc give the amulet to the human"),
                        "answer": "yes",
                        "to_scene": "gameover",
                        "transition_pdesc": "The orc hands you the amulet. You leave the cave. Congratulations!"
                    },
                    "give_sword": {
                        "q_and_a_lines": calc_q_and_a_lines("does the orc give the sword to the human"),
                        "answer": "yes",
                        "to_scene": "player_has_sword",
                        "transition_pdesc": "The orc hands you the sturdy sword. It has several nicks, and a good heft."
                    },
                    "sword": None,
                    "angry": {
                        "min_turn": 0,
                        "q_and_a_lines": calc_q_and_a_lines("does the human hate the orc"),
                        "answer": "yes",
                        "to_scene": "angry_human",
                        "transition_pdesc": "The orc looks a bit worried about the human."
                    }
                }
            }
        }
    },
    "angry_human": {
        "turn": 0,
        "look": False,
        "player": {
            "ndesc": "An angry human who gave you chicken is here."
        },
        "npcs": {
            "orc": {
                "ndesc": "A worried orc is standing here.",
                "actions": {
                    "sword": {
                        "min_turn": 5,
                        "q_and_a_lines": calc_q_and_a_lines("does the orc attack the human"),
                        "answer": "yes",
                        "to_scene": "gameover",
                        "transition_pdesc": "The orc slices you with the sword and you die. Goodbye."
                    },
                    "angry": None
                }
            }
        }
    },
    "player_has_sword": {
        "turn": None,
        "look": False,
        "player": {
            "pdesc": "You are an adventurer.",
            "ndesc": "A human who gave you chicken is here. He has your sword.",
            "nshortdesc": "The lovely human",
            "items": {
                "chicken": None,
                "sword": {
                    "desc": "a sturdy sword"
                }
            },
            "actions": {
                "g": None,
                "f": {
                    "desc": "[/f]ight the orc",
                    "ptext": "You attack the orc with the sword and kill him. You take the amulet. Congratulations!",
                    "ntext": "The human kills the orc.",
                    "to_scene": "gameover"
                }
            }
        },
        "npcs": {
            "orc": {
                "pdesc": "An orc is standing here.",
                "ndesc": "A worried orc is standing here.",
                "items": {
                    "sword": None,
                    "amulet": {
                        "desc": "a shiny golden amulet"
                    }
                },
                "about_lines": [
                    "The orc is not hungry because the human gave him food.",
                    "The orc might give the amulet to the human.",
                    "The orc is worried the human will attack him with the sword."
                ],
                "talk_lines": [
                    "The orc says: Thank you so much for chicken!",
                    "",
                    "The human says: Can I have the amulet?",
                    "The orc says: Maybe, maybe",
                    '',
                    "The human says: Do you want to fight me?",
                    "The orc says: Please not kill orc with sword, me like human.",
                    "",
                    "The human says: Hello",
                    "The orc says: Hello human, maybe give sword back to me?"
                ],
                "actions": {
                    "sword": None,
                    "give_amulet": {
                        "q_and_a_lines": calc_q_and_a_lines("does the orc give the amulet to the human"),
                        "answer": "yes",
                        "to_scene": "gameover",
                        "transition_pdesc": "The orc hands you the amulet. You leave the cave. Congratulations!"
                    },
                    "give_sword": None
                }
            }
        }
    },
    "gameover": {
        "turn": None,
        "gameover": True
    }
}

print ("========================")
print ("Welcome to Orc Simulator")
print ("Just type anything to talk to the orc, or press Enter for a list of actions")
print ("========================")
run_game(scenes, 'start', diagnostics=False)
