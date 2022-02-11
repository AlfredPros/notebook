label bedroom_day4:

    pause 2
    "..."

    if goodend == 1:
        $ dogfed = 0
        "I woke up fresh and ready for the day!"
        "Well then, I should water the {color=#FDE992}bouquet{/color}, {color=#FDE992}feed Mocha{/color}, do the {color=#FDE992}dishes{/color}, tidy up my {color=#FDE992}stationary{/color}, clean the {color=#FDE992}bookshelf{/color}, and do my work on my {color=#FDE992}laptop{/color}"
    else:
        "I woke up, for some reason my pillow feels a bit damp."
        "Ew, did I drool?"
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
        "I have a treat for Mocha, should I give him normal food?."
        menu:
            "Feed him normal food":
                $ dogfed += 1
                play sound dog_food
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                MC "Eat up little buddy."
                play sound dog_barking
                MC "Good boy!"
            "Give him a treat":
                pause 3
                MC "Here's a treat for you buddy!"
                play sound dog_food
    else:
        "I should feed {b}him{/b}."
        menu:
            "Yes":
                $ dogfed += 1
                play sound dog_food
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                "{b}He{/b} seems to enjoy the food."

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
    "Still looking pretty clean, I can do it next time, but I think it'd be better to clean it anyway?"
    menu:
        "Yes":
            play sound water_sink
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's all squeaky clean!"
        "No":
            "Yeah, I'll leave it for now."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label boquet_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "The flowers let go an aromatic smell, water it?"
    menu:
        "Yes":
            play sound watering_plants
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I hope the flower will keep being fresh."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label coffee_obj4:
    $ modal_state = False
    window show Dissolve(0.2)

    "A morning warm cup of coffee would be nice, but I'll make my anxiety worse."
    menu:
        "{b}Drink Coffee{/b}":
            play sound coffee_machine
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's just a silly myth."

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
            "I can ask to extend the deadline later, I'll be fine."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label bookshelf_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "There's a spider web, I think it'd be a good idea if I clean this."
    menu:
        "Clean it":
            play sound tidy_the_books
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I'm sorry for destroying your house little spider."
        "Don't clean it":
            "I don't want to get anywhere near spider."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label stationery_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    "I finished signing books, maybe I should put it away?"
    menu:
        "Yes":
            play sound shaking_pens
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's all clean and tidy!"
        "No":
            "I'll do it later, it's easy to find anyway."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label pigura_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3 good end only
    "I wonder what she's doing now."
    "I should visit her when I can."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return
label tissue_obj4:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "I should clean the {b}trash{/b}"
    menu:
        "Clean it":
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "It's getting messier..."
            "I'll do it later."

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
        if dogfeeder_obj[3] == False or sink_obj[3] == False or boquet_obj[3] == False or bookshelf_obj[3] == False or stationery_obj[3] == False or pigura_obj[3] == False:
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
        if coffee_obj[3] == False or plant_obj[3] == False or dogfeeder_obj[3] == False or laptop_obj[3] == False or tissue_obj[3] == False or stationery_obj[3] == False:
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
