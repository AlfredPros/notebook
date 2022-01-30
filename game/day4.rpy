label bedroom_day4:

    pause 2
    "..."

    if goodend == 1:
        $ dogfed = 0
        "I woke up fresh and ready for the day!"
    else:
        "I woke up, for some reason my pillow feels a bit damp."
        "Ew, did I drool again?"
        "Anyway, I should get ready."
    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen bedroom1 with s_dissolve
    pause

    return

## Kitchen objects ##############################################################

label dogfeeder_good_obj4:
    $ modal_state = False
    "Mocha's bowl's empty, I should feed him."
    menu:
        "Feed him":
            $ dogfed += 1
            play sound dog_food
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Mocha, It's time to chow down."
        "Don't feed him":
            play sound dog_food
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I'll give him the more expensive food."
    return

label dogfeeder_bad_obj4:
    "I should feed {b}him{/b}."
    menu:
        "Yes":
            $ dogfed += 1
            play sound dog_food
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Mocha, It's time to chow down."

    return

label plant_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "The plants have seen better days, I should water it."
    menu:
        "Water it.":
            $ point += 1
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I wonder if the plant will survive."
        "Don't water it.":
            $ point -= 1
            "I don't think it's saveable at this point."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label sink_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "The dish is going to keep piling up, maybe I should clean it?"
    menu:
        "Yes":
            $ point += 1
            #sfx cleaning dish pls
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "All clean!"
        "No":
            $ point -= 1
            "I'll do it tomorrow."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label boquet_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Huh, it's starting to wit, maybe some more water?"
    menu:
        "Yes":
            $ point += 1
            #sfx watering pls
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I’ll get water for the poor flowers."
        "No":
            $ point -= 1
            "I can't be bothered with it."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label coffee_obj1:
    $ modal_state = False
    window show Dissolve(0.2)

    "A morning warm cup of Joe seems nice, it would make my anxiety worse though... Should I make coffee?"
    menu:
        "Yes":
            $ point -= 1
            play sound coffee_machine
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Bottoms up!"
        "No":
            $ point += 1
            "No, I shouldn't. Maybe I can refresh myself some other way."

    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return with Dissolve(0.2)

## Office objects #############################################################

label laptop_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "Maybe I should continue my work?"
    menu:
        "Yes":
            $ point += 1
            play sound laptop_start
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            if work == 1:
                "I'm done!"
                "I just need to submit it."
            else:
                "Great, 50 pages to go!"
                "Huh, a new email?"
                "It's from... The editor... My book could be bestseller? What a joke."
        "No":
            $ point -= 1
            "I'll do it later, the deadline is 4 more days anyway"

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label stationery_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "Pencils, Pens, I never used it since I have this laptop, maybe I should put it away?"
    menu:
        "Yes":
            $ point += 1
            play sound shaking_pens
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "No":
            $ point -= 1
            "I don't really need them anyway, it's probably fine."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label pigura_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3 good end only
    "Ah yes, a picture of my me and my mom."
    "I should visit her when I can."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return
label tissue_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "Maybe I should clean the {b}trash{/b}?"
    menu:
        "Yes":
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's all cleaned now."
        "No":
            "It's not that messy, I can let it be for now."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label tissuebox_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "Maybe I should wipe the {b}blood{/b}?"
    menu:
        "Yes":
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's cleaned!"
        "No":
            "It's not that filthy anyway."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

## Bedroom objects ##################################################################

label kaca_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    "Hey there, handsome!"  # No need for choice, I think.
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label notebook_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    # Check if all items has been interacted
    if coffee_obj[0] == False or sink_obj[0] == False or dogfeeder_obj[0] == False or laptop_obj[0] == False or bookshelf_obj[0] == False:
        "There's something I haven't checked yet." # if not all items have been interacted
        window hide Dissolve(0.2)
        $ modal_state = True
        pause
    else:
        "Let's see what I've done today..."  # if all items have been interacted
        window hide Dissolve(0.2)
        $ modal_state = True

        hide screen bedroom1
        scene black
        with dissolve

        pause 0.5

    return
