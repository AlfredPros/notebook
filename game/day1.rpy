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
            E "Hello, have you heard the company's news?"
            MC "What news?"
            E "Your work has been nominated for the best seller award."
            MC "Oh, thankyou for telling me!"
            MC "That's very surprising."
            E "Well, you'll still have to wait if you actually get the award though."
            MC "Alright, please do inform me when the result is out."
            E "Sure, for now you should finish your current project since the deadline is in 5 days."
            MC "I'll be sure to finish it as soon as possible."
            "With that I hang up on him and prepare my day."

    "Well then, I should do the {color=#FDE992}dishes{/color}, {color=#FDE992}feed Mocha{/color}, maybe get myself a cup of {color=#FDE992}coffee{/color}, tidy up my {color=#FDE992}bookshelf{/color}, and do my work on my {color=#FDE992}laptop{/color}"
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

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return with Dissolve(0.2)

label dogfeeder_obj1:
    $ modal_state = False
    "Mocha's feeder seems empty, maybe it's a good idea to refill it."
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
            play sound dog_food
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "There, there, good boy!"
        "No":
            $ point -= 1
            "I think it’s fine, I kinda overfed him last night."

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
            play sound water_sink
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "All clean!"
        "No":
            $ point -= 1
            "I'll do it tomorrow."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

## Office objects #############################################################

label bookshelf_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "There’s a lot of book here... maybe I should sort it."
    menu:
        "Yes":
            $ point += 1
            play sound tidy_the_books
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "No":
            $ point -= 1
            "I think the book is as organized as it should be."

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
            $ point += 1
            $ work = 1
            play sound laptop_start
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Great, 50 pages to go!"
            if sleep1 == 1:
                "Huh, a new email?"
                "It's from... The editor... My book could be bestseller? What a joke."
        "No":
            $ point -= 1
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
        window hide Dissolve(0.2)
        $ modal_state = True

        hide screen bedroom1
        scene black
        with dissolve

        pause 0.5

    return
