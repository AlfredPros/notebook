define MC = Character("Sussy Baka Amogus")
define popo = Character("Mocha")

default coffee_obj = [False, False, False, False, False]  # Per day

label splashscreen:
    scene black
    pause 1
    show text "Supar Sikrit Klab Presents" with dissolve
    pause 2
    hide text with dissolve
    pause 1
    show text "{size=+50}Notebook{/size}" with dissolve
    pause 4
    show text "Warning, the following content and game contains scenes of disturbing nature, act, and in-game scenes. All the characters, art, storylines depicted in this game are purely the work of fiction, any similarity to the real world are purely coincidental. Players discretion is advised." with dissolve
    pause 10
    hide text with dissolve
    pause 1
    return

label start:
    "uwu"
    
    "[coffee_obj[0]], [coffee_obj[1]], [coffee_obj[2]], [coffee_obj[3]], [coffee_obj[4]]"
    
    window hide
    # Init coordinate
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen poc with s_dissolve
    
    pause
    
    window show
    "ok"
    
    return
    

