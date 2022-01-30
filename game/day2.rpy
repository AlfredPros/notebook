label bedroom_day2:
    $ dogfed = 0
    #start in bedroom morning
    ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    pause 2

    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen bedroom1 with s_dissolve
    pause

    return

## Kitchen objects ##############################################################

label book_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "I haven't read this book in awhile, and I kinda want to re-read it."
    menu:
        "Read":
            $ point -= 1
            play sound pageturn_twice
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "That was just as good as I remembered it to be!"

        "Don't read":
            $ point += 1
            "No, I shouldn’t waste time on something trivial."

    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label dogfeeder_obj2:
    $ modal_state = False
    "Huh, it’s empty, Mocha must be starving."
    menu:
        "Fill it":
            $ point += 1
            $ dogfed += 1
            play sound dog_food
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I should feed Mocha, he’s still growing after all."
        "Don't fill it":
            $ point -= 1
            "I don't want to overfed mocha, he should be fine."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label plant_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "The plants have seen better days, I should water it."
    menu:
        "Water it.":
            $ point += 1
            play sound watering_plants
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
                $ work = 2
                "Just 25 pages to go!"
            else:
                $ work = 1
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

## Bedroom objects ##################################################################

label kaca_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "Look at you, stylish!"  # No need for choice, I think.
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label notebook_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    # Check if all items has been interacted
    if book_obj[0] == False or plant_obj[0] == False or dogfeeder_obj[0] == False or laptop_obj[0] == False or stationery_obj[0] == False:
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
