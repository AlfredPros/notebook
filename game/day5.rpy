label bedroom_day5:

    pause 2
    "..."

    if goodend == 1:
        $ dogfed = 0
        "I woke up fresh and ready for the day!"
        "Well then, I should water the {color=#FDE992}bouquet{/color}, {color=#FDE992}feed Mocha{/color}, I can use some {color=#FDE992}coffee{/color}, clean the {color=#FDE992}bookshelf{/color}, and do my work on my {color=#FDE992}laptop{/color}"
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

label dogfeeder_obj5:
    $ modal_state = False
    if goodend == 1:
        "Mocha seems happy, I should feed him well."
        menu:
            "Feed him":
                $ dogfed += 1
                play sound dog_food
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                "Mocha, It's time to chow down."
            "Feed him treat":
                play sound dog_barking
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                "He loved it!"
    else:
        "I should feed {b}him{/b}."
        menu:
            "{b}Yes{/b}":
                $ dogfed += 1
                play sound dog_food
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                "Mocha, It's time to chow down."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause
    return

label plant_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    "The plants is withered."
    menu:
        "Water it.":
            play sound watering_plants
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Why am I doing this?"
        "Don't water it.":
            "It's beyond saving, I can just replace it."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label boquet_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    "The flowers seems to bloom happily, water it?"
    menu:
        "Yes":
            play sound watering_plants
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "There, there, enjoy the fresh water."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label coffee_obj5:
    $ modal_state = False
    window show Dissolve(0.2)

    "I think I can use a bit of coffee for today."
    menu:
        "Drink coffee":
            play sound coffee_machine
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's lovely!"
            "I shouldn't drink this often though."
        "Don't drink coffee":
            "I think I'll pass, I can find other way to refresh myself."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return with Dissolve(0.2)

label knife_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    "I should clean {b}it{/b}."
    menu:
        "{b}Yes{/b}":
            play sound water_sink
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's clean!"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

## Office objects #############################################################

label laptop_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    "Maybe I should continue my work?"
    menu:
        "Yes":
            play sound laptop_start
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            if work == 2:
                $ work = 3
                "I'm done!"
                "I just need to submit it."
                ".{w=0.2}.{w=0.2}.{w=0.2} and done!"

            elif work == 1:
                $ work = 2
                "Just 50 pages to go!"
            else:
                $ work = 1
                "Great, 100 pages to go!"
        "No":
            "I can't be bothered, I'll do it before I sleep."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label bookshelf_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    "It doesn't seems to be too messy, maybe I can just lightly dusted it?"
    menu:
        "Clean it":
            play sound tidy_the_books
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "Don't clean it":
            "I think it's fine, It's just a little dust."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label pigura_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3 good end only
    "A picture of my me and my mom."
    "I really missed her, maybe I should give her a call time to time."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return
label tissuebox_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "I feel my face a little damp."
    "I should clean my {b}tears{/b}?"
    menu:
        "{b}Yes{/b}":
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I still felt the tears constatly dripping off my face."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return


## Bedroom objects ##################################################################

label kaca_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    "It's you!"  # No need for choice, I think.
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label notebook_obj5:
    $ modal_state = False
    window show Dissolve(0.2)
    # Check if all items has been interacted
    if goodend == 1:
        if dogfeeder_obj[4] == False or coffee_obj[4] == False or boquet_obj[4] == False or bookshelf_obj[4] == False or laptop_obj[4] == False or pigura_obj[4] == False:
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
        if knife_obj[4] == False or plant_obj[4] == False or dogfeeder_obj[4] == False or laptop_obj[4] == False or tissuebox_obj[4] == False or bookshelf_obj[4] == False:
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
