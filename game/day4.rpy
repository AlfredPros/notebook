label day4_bedroom_m:
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

label plants_obj4:
    menu:
        "Yes":
            "uwu"
        "No":
            "bad uwu"
    "Nyimeng"
    return

label dogfeeder_good_obj2:
    menu:
        "Yes":
            "uwu"
        "No":
            "bad uwu"
    "Nyimeng"
    return

label dogfeeder_bad_obj2:
    if dogfed == 2:
        menu:
            "Yes":
                "overfill"
            "No":
                "bowl filled"
    elif dogfed == 1:
        menu:
            "Yes":
                "bowl filled"
            "No":
                "empty bowl"
    else:
        menu:
            "Yes":
                "empty bowl"
            "No":
                "empty bowl"

    "Nyimeng"
    return

label book_obj4:
    menu:
        "Yes":
            "uwu"
        "No":
            "bad uwu"
    "Nyimeng"
    "[point]"
    return

label laptop_obj4:
    menu:
        "Yes":
            "uwu"
        "No":
            "bad uwu"
    "Nyimeng"
    "[point]"
    return

label stationary_obj4:
    menu:
        "Yes":
            "uwu"
        "No":
            "bad uwu"
    "Nyimeng"
    "[point]"
    return

label dog_obj4:
    menu:
        "Yes":
            "uwu"
        "No":
            "bad uwu"
    "Nyimeng"
    "[point]"
    return

label notebook_obj4:
    "Dialog"
    return
