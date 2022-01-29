label bedroom_day2:

    #start in bedroom morning
    #sfx birds chirping pls fadein 1 loop
    pause 2

    "I can hear the birds chirping outside, I know for sure my alarm hasn't rang yet. It seems I've woke up early today, should I get up or maybe I can sleep a little more?"
    #stop sfx
    menu:
        "Yes, I could get more work done faster.":
            $ point += 1
        "Maybe 5 more minutes..":
            $ point -= 1
            ".{w=0.2}.{w=0.2}.{w=0.2}"
            "I've definitely slept well over 5 minutes."

    window hide
    label unfinished_day2:
        python:
            pos = renpy.get_mouse_pos()
            x_now = pos[0]
            y_now = pos[1]
        show screen bedroom1 with s_dissolve
        pause
        return
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

label boquet_obj2:
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

label coffee_obj2:
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

label dogfeeder_obj2:
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
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label knife_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    #only on day 3+ bad ending
    "Do you want to stab-stab?"
    menu:
        "Yes":
            $ point -= 1
        "No":
            $ point -= 1
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

label sink_obj2:
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

## Office objects #############################################################

label bookshelf_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "There’s a lot of book here... maybe I should sort it."
    menu:
        "Yes":
            $ point += 1
            #sfx cleaning bookshelf pls
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "No":
            $ point -= 1
            "I think the book is as organized as it should be."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label laptop_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "Maybe I should continue my work?"
    menu:
        "Yes":
            $ point += 1
            #sfx typing pls
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Great, 100 pages to go!"
            "Huh, a new email?"
            "It's from... The editor... My book? Bestseller? What a joke."
        "No":
            $ point -= 1
            "Whatever, the deadline is 5 more days anyway"
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label pigura_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3 good end only
    "Do you want to anime fig-?"
    menu:
        "Yes":
            $ point += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
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
            #sfx pencils and pens clattering pls
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything seems much organized!"
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label tissue_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "Maybe I should clean the trash?"
    menu:
        "Yes":
            #sfx tissue?
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

label tissuebox_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "Maybe I should wipe the blood?"
    menu:
        "Yes":
            #sfx tissue?
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

#doggo whereeeee
label dog_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "Hi Mocha, how are you buddy, I should play with him..."
    menu:
        "Yes":
            $ point += 1
            play sound dog_barking
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I can always spare some time for him, Let’s play Mocha!"
            play sound dog_barking

        "No":
            $ point -= 1
            "I think I got better things to do."
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

## Bedroom objects ##################################################################

label kaca_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    "I look awesome today!"  # No need for choice, I think.
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label notebook_obj2:
    $ modal_state = False
    window show Dissolve(0.2)
    # Check if all items has been interacted
    if coffee_obj[0] == [false],  sink_obj[0] == [false],  dogfeeder_obj[0] == [false], laptop_obj[0] == [false], bookshelf_obj[0] == [false], dog_obj[0] == [false]:
        "There's something I haven't checked yet." # if not all items have been interacted
        jump unfinished_day2
    else:
        "Let's see what I've done today..."  # if all items have been interacted
    # Summary stuff
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True

    hide screen bedroom1
    scene black
    with dissolve

    pause 0.5

    return
