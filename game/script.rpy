define MC = Character("Sussy Baka Amogus")
define popo = Character("Mocha")

default coffee_obj = [False, False, False, False, False]  # Per day
default day = 0
default point = 0

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

    call day1_bedroom_m
    $ day = 1
    call day2_bedroom_m
    $ day = 2
    call day3_bedroom_m
    $ day = 3
    call day4_bedroom_m
    $ day = 4
    call day5_bedroom_m

    return
