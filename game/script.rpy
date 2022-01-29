define MC = Character("Sussy Baka Amogus")
define Mocha = Character("Mocha")

default coffee_obj = [False, False, False, False, False]  # Per day
default dogfeeder_obj = [False, False, False, False, False]
default sink_obj = [False, False, False, False, False]
default laptop_obj = [False, False, False, False, False]
default bookshelf_obj = [False, False, False, False, False]
default dog_obj = [False, False, False, False, False]
default plants_obj = [False, False, False, False, False]
default bouquet_obj = [False, False, False, False, False]
default statonary_obj = [False, False, False, False, False]
default day = 0
default point = 0 #for good and bad points >:(
default dogfed = 0 #if day 3 player no feed dog for 2 days straight, dog die :( else: dog run
default goodend = 0 #bruh

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
