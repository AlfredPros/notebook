label bedroom_day2:
    $ dogfed = 0
    #start in bedroom morning
    ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    pause 2
    "I guess I'm awake now."
    "Well then, I should water the {color=#FDE992}plants{/color}, {color=#FDE992}feed Mocha{/color}, maybe read one of my favorite {color=#FDE992}books{/color} to clear my mind, tidy up my {color=#FDE992}stationary{/color}, and do my work on my {color=#FDE992}laptop{/color}"
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

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label dogfeeder_obj2:
    $ modal_state = False
    if doggy == 1:
        $ doggy = 0
        play sound dog_barking
        pause 0.5
        play sound dog_barking
        MC "Mocha, stop running around, come over here!"
    else:
        MC "Mocha, it seems your body is getting thinner."

    "He seemed hungry, I should feed him."
    menu:
        "Feed Mocha":
            $ point += 3
            $ dogfed += 1
            play sound dog_food
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I should feed Mocha, he’s still growing after all."
        "Don't feed Mocha":
            $ point -= 3
            "I don't want to overfed mocha, he should be fine."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label plant_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "The house plants seems to be healthy, maybe I should water it?"
    menu:
        "Water it.":
            $ point += 1
            play sound watering_plants
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Grow my little cutie."
        "Don't water it.":
            $ point -= 1
            "The soil seems damp enough, I shouldn't overfill it."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

## Office objects #############################################################

label laptop_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "Deadline is getting closer, maybe I should do my work?"
    menu:
        "Yes":
            $ point += 2
            play sound laptop_start
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            if work == 1:
                $ work = 2
                "Just 50 pages to go!"
            else:
                $ work = 1
                "Great, 100 pages to go!"
        "No":
            $ point -= 2
            "Forget it, I can't be bothered with it right now."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label stationery_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "I've finished signed the books, maybe I should put it away?"
    menu:
        "Yes":
            $ point += 1
            play sound shaking_pens
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "No":
            $ point -= 1
            "I know where they're at, it's probably fine."
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
    if book_obj[1] == False or plant_obj[1] == False or dogfeeder_obj[1] == False or laptop_obj[1] == False or stationery_obj[1] == False:
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
