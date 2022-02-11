label bedroom_day3:

    pause 2
    "..."
    "It seems I've woke up early today, should I get up or maybe I can sleep a little more?"

    menu:
        "Yes, I could get more work done faster.":
            "Alright, Let's get up."
        "I'll just wait for the alarm.":
            ".{w=0.2}.{w=0.2}.{w=0.2}"

    if goodend == 1:
        $ dogfed = 0
        "I heard my phone ringing."
        "It's the editor, I picked up the phone."
        MC "Hello?"
        E "Hey bud, your latest book are best seller, you did it!"
        MC "Really? That's amazing!"
        E "Yeah, the company is going to celebrate it in 2 days, but still, don’t forget your current deadline!"
        MC "Okay geez, way to get my hopes up."
        "I hang up."
        MC "Mocha you heard that buddy???"
        play sound dog_barking
        MC "We did it!"
        play sound dog_barking
        "I picked mocha and give him a big hug."
        scene goodend with Dissolve(2):
            zoom (0.33)
        pause 2
        "Mocha seems excited too, I think he knows that something good happened"
        MC "Good boy!"
        pause 2
        "Well then, I should water the {color=#FDE992}plants{/color}, {color=#FDE992}feed Mocha{/color}, I recieved a {color=#FDE992}bouquet{/color} I should keep it healthy, tidy up my {color=#FDE992}stationary{/color}, I also decided to hang an old {color=#FDE992}picture{/color} in my office, and end the day by doing my work on my {color=#FDE992}laptop{/color}"

    else:
        if dogfed == 1:
            "I woke up and realises something is missing."
            pause 2
            "Mocha!"
            "I looked around the house to find Mocha, but I can't seems to find him anywhere."
            pause 2
            "Eventually I gave up."
            MC "Mocha..."
            "It seems Mocha went through the pet door."
            "I hope he'll be back soon..."
        else:
            $ dogdie = 1
            "I woke up to a terrifying scene."
            "Something I hoped to be just a mere nightmare."
            "But this isn't just a nightmare, it's a grim reality."
            scene badend with Dissolve(2):
                zoom (0.33)
            MC "Mocha..."
            MC "I-I'm sorry Mocha."
            MC "I didn't fed him, how could I?!"
            MC "Now that's left is just regret."
            "May you rest in peace, Mocha."

    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen bedroom1 with s_dissolve
    pause

    return

## Kitchen objects ##############################################################

label dogfeeder_obj3:
    $ modal_state = False
    if goodend == 1:
        "Mocha's new package of food is here, I should feed him."
        menu:
            "Feed him":
                $ dogfed += 1
                play sound dog_food
                ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                pause 3
                "I pour a bit more than usual, Mocha is a growing boy after all."

    else:
        "Mocha's new package of food is here, I should feed him."
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

label knife_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    "I should {b}clean{/b} it."
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

label plant_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    "The plants still seems healthy, should I water it?"
    menu:
        "Water it":
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "I wonder if the plant will survive."
        "Don't water it":
            "I don't really care about it anyway."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label boquet_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    "I was given this by my co-workers because of my recent work got the best seller award"
    "It's a very beautiful flowers, water it?"
    menu:
        "Yes":
            play sound watering_plants
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "The flowers has a nice smell."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

## Office objects #############################################################

label laptop_obj3:
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
            "I don't have any inspiration, I should take a break for today."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label stationery_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    "It's getting quite messy, maybe I should clean it?"
    menu:
        "Clean it":
            play sound shaking_pens
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "Everything is tidy and perfect."
        "Don't clean it":
            "I'll just put them away once I'm done ."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label pigura_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3 good end only
    "Ah yes, it's a picture of my me and my mom."
    "I decided to hang it."
    "I miss our old house, I'm feeling nostalgic."
    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return
label tissue_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "Maybe I should clean the {b}trash{/b}?"
    menu:
        "{b}Yes{/b}":
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "{b}It{/b} looks clean enough."

    window hide Dissolve(0.2)
    $ modal_state = True
    pause

    return

label tissuebox_obj3:
    $ modal_state = False
    window show Dissolve(0.2)
    #day 3+ bad end only
    "Maybe I should wipe the {b}blood{/b}?"
    menu:
        "{b}Yes{/b}":
            ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            pause 3
            "{b}It{/b} doesn't wipe off..."

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
    if goodend == 1:
        if dogfeeder_obj[2] == False or plant_obj[2] == False or boquet_obj[2] == False or laptop_obj[2] == False or stationery_obj[2] == False or pigura_obj[2] == False:
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
        if knife_obj[2] == False or plant_obj[2] == False or dogfeeder_obj[2] == False or laptop_obj[2] == False or tissue_obj[2] == False or tissuebox_obj[2] == False:
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
