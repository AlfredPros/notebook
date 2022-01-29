label day1_bedroom_m:
    #start in bedroom morning
    "uwu"
    
    # Init coordinate ()
    window hide
    python:
        pos = renpy.get_mouse_pos()
        x_now = pos[0]
        y_now = pos[1]
    show screen kitchen1 with s_dissolve
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

label coffee_obj1:
    menu:
        "Yes":
            $ point += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label dogfeeder_obj1:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label sink_obj1:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label laptop_obj1:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label bookshelf_obj1:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label dog_obj1:
    menu:
        "Yes":
            $ point += 1
            $ dogfed += 1
        "No":
            $ point -= 1
    "Nyimeng"
    "[point]"
    return

label notebook_obj1:
    "Dialog"
    return
