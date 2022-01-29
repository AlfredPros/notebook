label day2_bedroom_m:
    #start in bedroom morning
    "uwu"

    "[coffee_obj[0]], [coffee_obj[1]], [coffee_obj[2]], [coffee_obj[3]], [coffee_obj[4]]"

    # Init coordinate ()
    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen poc with s_dissolve
    pause
    window show
    #return to kitchen

    "ok"
    window hide

    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen poc with s_dissolve

    pause
    return

label plants_obj2:
    menu:
        "Yes":
            $ point += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label dogfeeder_obj2:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label book_obj2:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label laptop_obj2:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label stationary_obj2:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label dog_obj2:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label notebook_obj2:
    "Dialog"
    return
