# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

define q = Character("Quinn")
define j = Character("John")
define s = Character("Skelington")
define c = Character("???")

default player_name = "you"

image bg forest_day = "Forest_Day.png"
image bg graveyard_night = "graveyard_night.png"
image bg falling_dark = "falling_dark.jpg"
image bg underground_city = "underground_city.png"
image bg underground_street = "underground_street.jpg"

image quinn normal = "quinn_normal.png"
image quinn worried = "quinn_worried.png"
image john normal = "john_normal.png"
image john scared = "john_scared.png"
image skelington normal = "skelington_normal.png"

label start:
    scene bg forest_day

    "It was supposed to be a normal hike."
    "Just you, Quinn, and John messing around like usual."
 
    show quinn normal at left
    with dissolve
    q "I told you guys this trail was safe."
    hide quinn normal

    show john normal at right
    with dissolve
    j "You also said that shortcut wouldn't get us lost."
    hide john normal

    show quinn normal at left
    q "Details."
    hide quinn normal

    $ player_name = renpy.input("Before we continue... what's your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Alex"

    show quinn normal at left
    q "Hey, [player_name], back me up here."
    hide quinn normal

    menu:
        "Side with Quinn":
            "[player_name]" "He's right, John. You're just dramatic."
        "Side with John":
            "[player_name]" "You did get us lost."

    scene bg graveyard_night
    with fade

    "As the sun sets, you stumble into an old graveyard."

    show john normal at right
    j "Okay... this is definitely not the trail."
    hide john normal

    show quinn normal at left
    q "Relax. It's kinda cool."
    hide quinn normal

    "You step forward."
    "The ground cracks beneath you."

    scene bg falling_dark
    with vpunch

    show john scared at right
    j "[player_name]!!!"
    hide john scared

    scene black
    with fade

    "Everything goes silent."

    pause 1.0

    scene bg underground_city
    with fade

    "You wake up."
    "Above you is a glowing crystal sky."
    "Around you..."
    "An entire city. Underground."

    show quinn worried at left
    q "Okay. So. We're not dead, right?"
    hide quinn worried

    show john scared at right
    j "If we are, this is the weirdest afterlife ever."
    hide john scared

    "[player_name]" "Where are we...?"

    show skelington normal at truecenter
    with dissolve
    c "Ahhhhh... Fresh arrivals."
    hide skelington normal

    show quinn worried at left
    q "WHAT IS THAT?!"
    hide quinn worried

    show john scared at right
    j "It's a cat."
    hide john scared

    show skelington normal at truecenter
    with dissolve
    s "Wizard cat, actually."
    s "My name is Skelington."
    s "And unfortunately for you three..."
    s "You have fallen into the Underdeep."
    hide skelington normal

    "[player_name]" "Underdeep?"

    show skelington normal at truecenter
    s "An underground civilization hidden from your world."
    s "And now that you're here..."
    s "The city knows."
    hide skelington normal

    "A distant roar echoes through the tunnels."

    show john scared at right
    j "Knows what?"
    hide john scared

    show skelington normal at truecenter
    s "That you do not belong."
    s "Creatures will hunt you."
    s "If you wish to survive..."
    s "You will need me."
    hide skelington normal

    menu:
        "Trust Skelington":
            $ trusts_skelington = True
            "[player_name]" "Alright. We don't really have options."
        "Be suspicious":
            $ trusts_skelington = False
            "[player_name]" "Why should we trust you?"

    show skelington normal at truecenter
    if trusts_skelington:
        s "Good. Doubt gets people killed down here."
    else:
        s "Suspicion is healthy. Fear is not."
    s "First rule of the Underdeep:"
    s "Never travel alone."
    s "Second rule:"
    s "Do not let the city know your fear."
    hide skelington normal

    show john scared at right
    j "How does a city even know that?"
    hide john scared

    show skelington normal at truecenter
    s "You will learn."
    hide skelington normal

    scene bg underground_street
    with fade

    show skelington normal at truecenter
    s "Stay close, [player_name]."
    hide skelington normal

    show quinn worried at left
    q "Wait why them specifically?"
    hide quinn worried

    s "Because."
    s "They are different."
    hide skelington normal

    "[player_name]" "Different how?"

    show skelington normal at truecenter
    s "That..."
    s "Is why you survived the fall."
    hide skelington normal

    "Another distant roar."

    show skelington normal at truecenter
    s "We move. Now."
    hide skelington normal

    "Your adventure in the Underdeep has begun."

    return



