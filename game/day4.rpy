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

label dogfeeder_obj4:
    $ modal_state = False
    if goodend == 1:
        "Mocha seems hungry, I should feed him."
        menu:
            "Feed him":
                $ dogfed += 1
                play sound dog_food
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                "Mocha, It's time to chow down."
            "Give him a treat":
                play sound dog_food
                pause 3
                "I'll give him a treat."
    else:
        "I should feed {b}him{/b}."
        menu:
            "Yes":
                $ dogfed += 1
                play sound dog_food
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                "Mocha, It's time to chow down."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause
    return

label plant_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "The plants have seen better days, I should water it."
    menu:
        "Water it.":
            play sound watering_plants
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I wonder if the plant will survive."
        "Don't water it.":
            "I don't think it's saveable at this point."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label sink_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "The dish is going to keep piling up, maybe I should clean it?"
    menu:
        "Yes":
            play sound water_sink
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "All clean!"
        "No":
            "I'll do it tomorrow."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label boquet_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "Huh, it's starting to wit, maybe some more water?"
    menu:
        "Yes":
            play sound watering_plants
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I’ll get water for the poor flowers."
        "No":
            "I can't be bothered with it."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label coffee_obj4:
    $ modal_state = False
    window show Dissolve(0.2)

    "A morning warm cup of coffee would be nice."
    menu:
        "{b}Drink Coffee{/b}":
            play sound coffee_machine
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Bottoms up!"

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return with Dissolve(0.2)

## Office objects #############################################################

label laptop_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "Maybe I should continue my work?"
    menu:
        "Yes":
            play sound laptop_start
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            if work == 3:
                $ work = 4
                "I'm done!"
                "I just need to submit it."
                ".{w=0.2}.{w=0.2}.{w=0.2} and done!"
            elif work == 2:
                $ work = 3
                "Just 10 pages to go!"
            elif work == 1:
                $ work = 2
                "Just 25 pages to go!"
            else:
                $ work = 1
                "Great, 50 pages to go!"
        "No":
            "whatever, the deadline is in 2 days anyway."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label bookshelf_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "There’s a lot of book here... maybe I should sort it."
    menu:
        "Yes":
            play sound tidy_the_books
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "No":
            "I think the book is as organized as it should be."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label stationery_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "Pencils, Pens, I never used it since I have this laptop, maybe I should put it away?"
    menu:
        "Yes":
            play sound shaking_pens
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "No":
            "I don't really need them anyway, it's probably fine."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label pigura_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3 good end only
    "Ah yes, a picture of my me and my mom."
    "I should visit her when I can."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return
label tissue_obj4:
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
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return


## Bedroom objects ##################################################################

label kaca_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "It's me!"  # No need for choice, I think.
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label notebook_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    # Check if all items has been interacted
    if goodend == 1:
        if dogfeeder_good_obj[3] == False or sink_obj[3] == False or boquet_obj[3] == False or bookshelf_obj[3] == False or stationery_obj[3] == False or pigura_obj[3] == False:
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
    else:
        if coffee_obj[3] == False or plant_obj[3] == False or dogfeeder_bad_obj[3] == False or laptop_obj[3] == False or tissue_obj[3] == False or stationery_obj[3] == False:
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
