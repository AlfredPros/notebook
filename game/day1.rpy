label bedroom_day1:

    #start in bedroom morning
    play sound birds_chirping_1
    pause 2

    "I can hear the birds chirping outside, I know for sure my alarm hasn't rang yet. It seems I've woke up early today, should I get up or maybe I can sleep a little more?"

    menu:
        "Yes, I could get more work done faster.":
            $ point += 1
            $ sleep1 = 1
        "I'll sleep some more.":
            $ point -= 1
            "Right before I went back to sleep I heard my phone rings."
            #sfx phone lmao
            "I picked up my phone, it's the editor."
            E "Hello, I just wanna let you know that your work has been nominated for the best seller award."
            MC "Oh, thankyou for telling me!"
            MC "That's very surprising."
            E "For now you should finish your current project since the deadline is in {color=#FDE992}5 days{/color}."
            MC "I'll be sure to finish it as soon as possible."
            "With that I hang up on him and prepare my day."
            #beep phone hang up sfx pls

    "Well then, I should do the {color=#FDE992}dishes{/color}, {color=#FDE992}feed Mocha{/color}, maybe get myself a cup of {color=#FDE992}coffee{/color}, tidy up my {color=#FDE992}bookshelf{/color}, and do my work on my {color=#FDE992}laptop{/color}"
    show tutorial with Dissolve(1)
    pause 3
    hide tutorial with Dissolve(1)
    window hide

    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen bedroom1 with s_dissolve
    pause

    return

## Kitchen objects ##############################################################

label coffee_obj1:
    $ modal_state = False
    window show Dissolve(0.2)

    "It's morning, should I make a coffee?"
    menu:
        "Yes":
            $ point -= 1
            play sound coffee_machine
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I need some energy right now, I might have trouble sleeping later though."
        "No":
            $ point += 1
            "No, I need to keep a healthy lifestyle. Wait why did I listen to that doctor?"

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return with Dissolve(0.2)

label dogfeeder_obj1:
    $ modal_state = False
    "Mocha it's time to spoil you."
    menu:
        "Yes":
            $ point += 3
            $ dogfed += 1
            $ doggy = 1
            play sound dog_food
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Come here mocha, it's time to eat!"
        "No":
            $ point -= 3
            "I don't think I should, he's getting chubby, I kinda overfed him last night."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label sink_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "There's leftover food staining the plates, though it's not too bad. Should I clean it anyway?"
    menu:
        "Yes":
            $ point += 1
            play sound water_sink
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I don't like waiting for tomorrw, I should do it now so I can relax tomorrow."
        "No":
            $ point -= 1
            "I'll do it tomorrow, it's not that dirty right now."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

## Office objects #############################################################

label bookshelf_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Where's my favorite book? Oh, my bookshelf is messy, it's unpleasant to the eyes."
    "Maybe I should re-arrange it better?"
    menu:
        "Yes":
            $ point += 1
            play sound tidy_the_books
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized, I should remind myself not to make a mess again."
        "No":
            $ point -= 1
            "Oh, there it is, I only needed it, I can clean the mess later."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label laptop_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Maybe I should continue my work?"
    menu:
        "Yes":
            $ point += 2
            $ work = 1
            play sound laptop_start
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Great, 100 pages to go!"
            if sleep1 == 1:
                "Huh, a new email?"
                "It's from... The editor... My book could be bestseller? What a joke."
        "No":
            $ point -= 2
            "Whatever, the deadline is 5 more days anyway"

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

## Bedroom objects ##################################################################

label kaca_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "I look awesome today!"  # No need for choice, I think.
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label notebook_obj1:
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
        pause 1
        "I suppose I should sleep for the day."
        window hide Dissolve(0.2)
        $ modal_state = True

        hide screen bedroom1
        scene black
        with dissolve

        pause 0.5

    return
