label day1_bedroom_m:
    #start in bedroom morning
    "uwu"
    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen bedroom1 with s_dissolve
    pause
    
    return

label kitchen_day1:  # Not used
    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen kitchen1 with s_dissolve
    pause

    return

label office_day1:  # Not used
    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen office1 with s_dissolve
    pause

    return

## Kitchen objects ##############################################################

label book_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to read?"
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
    
label boquet_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to biskuat?"
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

label coffee_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to drink?"
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

label dogfeeder_obj1:
    $ modal_state = False
    "Do you want to feed?"
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause
    
    return
    
label knife_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to stab-stab?"
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
    
label plant_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to water the nature?"
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

label sink_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to Adam Ragusea?"
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

## Office objects #############################################################

label bookshelf_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to knowledge?"
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

label laptop_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to work?"
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
    
label pigura_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
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
    
label stationery_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to draw anime gurl?"
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
    
label tissue_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to (not sus)?"
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
    
label tissuebox_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "Do you want to (definitely sus)?"
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

## Bedroom objects ##################################################################

label kaca_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    "I look awesome today!"  # No need for choice, I think.
    "Nyimeng"
    "[point]"
    window hide Dissolve(0.2)
    $ modal_state = True
    pause
    
    return

label notebook_obj1:
    $ modal_state = False
    window show Dissolve(0.2)
    # Check if all items has been interacted
    "There's something I haven't checked yet." # if not all items have been interacted
    
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
