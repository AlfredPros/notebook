################################################################################
## Initialization
################################################################################

init offset = -1

image tdoor1 = im.MatrixColor("titledoor1closed.png", im.matrix.brightness(0.5))

define s_dissolve = { "screens" : Dissolve(0.25) }
define bg_scale_const = 0.71
define timer_length = 0.03

image house_hover = im.MatrixColor("ui/14.png", im.matrix.brightness(0.1))
image bedroom_hover = im.MatrixColor("ui/15.png", im.matrix.brightness(0.1))
image kitchen_hover = im.MatrixColor("ui/16.png", im.matrix.brightness(0.1))
image office_hover = im.MatrixColor("ui/17.png", im.matrix.brightness(0.1))
image bedroom_insensitive = im.MatrixColor("ui/15.png", im.matrix.brightness(-0.25))
image kitchen_insensitive = im.MatrixColor("ui/16.png", im.matrix.brightness(-0.25))
image office_insensitive = im.MatrixColor("ui/17.png", im.matrix.brightness(-0.25))

image bad_house_hover = im.MatrixColor("ui/bad/12.png", im.matrix.brightness(-0.1))
image bad_bedroom_hover = im.MatrixColor("ui/bad/13.png", im.matrix.brightness(-0.1))
image bad_kitchen_hover = im.MatrixColor("ui/bad/14.png", im.matrix.brightness(-0.1))
image bad_office_hover = im.MatrixColor("ui/bad/15.png", im.matrix.brightness(-0.1))
image bad_bedroom_insensitive = im.MatrixColor("ui/bad/13.png", im.matrix.brightness(-0.25))
image bad_kitchen_insensitive = im.MatrixColor("ui/bad/14.png", im.matrix.brightness(-0.25))
image bad_office_insensitive = im.MatrixColor("ui/bad/15.png", im.matrix.brightness(-0.25))

image about_hover = im.MatrixColor("ui/about.png", im.matrix.brightness(0.1))
image help_hover = im.MatrixColor("ui/help.png", im.matrix.brightness(0.1))
image load_hover = im.MatrixColor("ui/load.png", im.matrix.brightness(0.1))
image preferences_hover = im.MatrixColor("ui/preference.png", im.matrix.brightness(0.1))
image quit_hover = im.MatrixColor("ui/quit.png", im.matrix.brightness(0.1))
image start_hover = im.MatrixColor("ui/start.png", im.matrix.brightness(0.1))

################################################################################
## Transforms
################################################################################

transform door:
    zoom 0.55
    
transform bg_scale:
    zoom bg_scale_const
    
transform dissolve_out:
    alpha 1.0
    easein 0.25 alpha 0.0


################################################################################
## Point and Click
################################################################################

define hover_mult = 10  # The less, the faster
define smooth_const = 2  # DON'T CHANGE THIS
default x_now = 0
default y_now = 0
default modal_state = True
    
screen kitchen1():
    
    if modal_state == True:
        button:
            keysym 'dismiss', 'rollback', 'skip', 'fast_skip', 'toggle_skip', 'hide_windows'
            action NullAction()
    
    python:
        pos = renpy.get_mouse_pos()
        x_mouse = pos[0]
        y_mouse = pos[1]
        
        x_now = (x_mouse+x_now)/smooth_const
        y_now = (y_mouse+y_now)/smooth_const
    
    if goodend != -1:
        add "kitchen/bg_kitchen.png" at bg_scale:
            pos(-(x_now/hover_mult), -(y_now/hover_mult))
    else:
        add "kitchen/bad/bg_dark.png" at bg_scale:
            pos(-(x_now/hover_mult), -(y_now/hover_mult))
    
    # Book
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(1705*bg_scale_const)-(x_now/hover_mult), int(197*bg_scale_const)-(y_now/hover_mult))  # 1705, 197
            idle "kitchen/book.png"
            hover "kitchen/book_outline.png"
            sensitive (modal_state and book_obj[day] == False and day == 1)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(book_obj, day, True), Jump("book_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(1649*bg_scale_const)-(x_now/hover_mult), int(74*bg_scale_const)-(y_now/hover_mult))  # 1649, 74
            idle "kitchen/bad/book.png"
            hover "kitchen/bad/book_outline.png"
            sensitive (modal_state and book_obj[day] == False and day == 1)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(book_obj, day, True), Jump("book_obj"+str(day+1))
    
    # Boquet
    if goodend == 1 and (day == 2 or day == 3 or day == 4):
        imagebutton at bg_scale:
            pos(int(1124*bg_scale_const)-(x_now/hover_mult), int(436*bg_scale_const)-(y_now/hover_mult))  # 1124, 436
            idle "kitchen/boquet.png"
            hover "kitchen/boquet_outline.png"
            sensitive (modal_state and boquet_obj[day] == False)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(boquet_obj, day, True), Jump("boquet_obj"+str(day+1))
        
    # Coffee Machine
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(641*bg_scale_const)-(x_now/hover_mult), int(507*bg_scale_const)-(y_now/hover_mult))  # 641, 507
            idle "kitchen/coffee_machine.png"
            hover "kitchen/coffee_machine_outline.png"
            sensitive (modal_state and coffee_obj[day] == False and (day == 0 or (goodend == -1 and day == 3) or (goodend == 1 and day == 4)))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(coffee_obj, day, True), Jump("coffee_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(610*bg_scale_const)-(x_now/hover_mult), int(454*bg_scale_const)-(y_now/hover_mult))  # 610, 454
            idle "kitchen/bad/coffee.png"
            hover "kitchen/bad/coffee_outline.png"
            sensitive (modal_state and coffee_obj[day] == False and (day == 0 or (goodend == -1 and day == 3) or (goodend == 1 and day == 4)))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(coffee_obj, day, True), Jump("coffee_obj"+str(day+1))
        
    # Dog Feeder
    if goodend != -1:
        if dogfed > 1:
            imagebutton at bg_scale:
                pos(int(1604*bg_scale_const)-(x_now/hover_mult), int(859*bg_scale_const)-(y_now/hover_mult))  # 1604, 859
                idle "kitchen/dog_feeder_filled.png"
                hover "kitchen/dog_feeder_filled_outline.png"
                sensitive (modal_state and dogfeeder_obj[day] == False)
                
                hovered Play("sound", "audio/button-hover.ogg")
                action SetDict(dogfeeder_obj, day, True), Jump("dogfeeder_obj"+str(day+1))
        else:
            imagebutton at bg_scale:
                pos(int(1604*bg_scale_const)-(x_now/hover_mult), int(859*bg_scale_const)-(y_now/hover_mult))  # 1604, 859
                idle "kitchen/dog_feeder_empty.png"
                hover "kitchen/dog_feeder_empty_outline.png"
                sensitive (modal_state and dogfeeder_obj[day] == False)
                
                hovered Play("sound", "audio/button-hover.ogg")
                action SetDict(dogfeeder_obj, day, True), Jump("dogfeeder_obj"+str(day+1))
    else:
        if dogfed > 1:
            imagebutton at bg_scale:
                pos(int(1507*bg_scale_const)-(x_now/hover_mult), int(764*bg_scale_const)-(y_now/hover_mult))  # 1507, 764
                idle "kitchen/bad/dog_overfilled.png"
                hover "kitchen/bad/dog_overfilled_outline.png"
                sensitive (modal_state and dogfeeder_obj[day] == False)
                
                hovered Play("sound", "audio/button-hover.ogg")
                action SetDict(dogfeeder_obj, day, True), Jump("dogfeeder_obj"+str(day+1))
        else:
            imagebutton at bg_scale:
                pos(int(1507*bg_scale_const)-(x_now/hover_mult), int(764*bg_scale_const)-(y_now/hover_mult))  # 1507, 764
                idle "kitchen/bad/dog_empty.png"
                hover "kitchen/bad/dog_empty_outline.png"
                sensitive (modal_state and dogfeeder_obj[day] == False)
                
                hovered Play("sound", "audio/button-hover.ogg")
                action SetDict(dogfeeder_obj, day, True), Jump("dogfeeder_obj"+str(day+1))
        
    # Knife
    if goodend == -1 and (day == 2 or day == 4):
        imagebutton at bg_scale:
            pos(int(1328*bg_scale_const)-(x_now/hover_mult), int(419*bg_scale_const)-(y_now/hover_mult))  # 1328, 419
            idle "kitchen/bad/knife.png"
            hover "kitchen/bad/knife_outline.png"
            sensitive (modal_state and knife_obj[day] == False)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(knife_obj, day, True), Jump("knife_obj"+str(day+1))
            
        #imagebutton at bg_scale:
        #    pos(int(1376*bg_scale_const)-(x_now/hover_mult), int(434*bg_scale_const)-(y_now/hover_mult))  # 1376, 434
        #    idle "kitchen/knife.png"
        #    hover "kitchen/knife_outline.png"
        #    sensitive (modal_state and knife_obj[day] == False)
            
        #    hovered Play("sound", "audio/button-hover.ogg")
        #    action SetDict(knife_obj, day, True), Jump("knife_obj"+str(day+1))
        
    # Plant
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(813*bg_scale_const)-(x_now/hover_mult), int(71*bg_scale_const)-(y_now/hover_mult))  # 813, 71
            idle "kitchen/plant.png"
            hover "kitchen/plant_outline.png"
            sensitive (modal_state and plant_obj[day] == False and (day == 1 or day == 2 or (goodend == -1 and day == 3) or (goodend == -1 and day == 4)))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(plant_obj, day, True), Jump("plant_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(754*bg_scale_const)-(x_now/hover_mult), int(58*bg_scale_const)-(y_now/hover_mult))  # 754, 58
            idle "kitchen/bad/plant.png"
            hover "kitchen/bad/plant_outline.png"
            sensitive (modal_state and plant_obj[day] == False and (day == 1 or day == 2 or (goodend == -1 and day == 3) or (goodend == -1 and day == 4)))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(plant_obj, day, True), Jump("plant_obj"+str(day+1))
        
    # Sink
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(1253*bg_scale_const)-(x_now/hover_mult), int(605*bg_scale_const)-(y_now/hover_mult))  # 1253, 605
            idle "kitchen/sink.png"
            hover "kitchen/sink_outline.png"
            sensitive (modal_state and sink_obj[day] == False and (day == 0 or (goodend == 1 and day == 3)))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(sink_obj, day, True), Jump("sink_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(1227*bg_scale_const)-(x_now/hover_mult), int(561*bg_scale_const)-(y_now/hover_mult))  # 1227, 561
            idle "kitchen/bad/sink.png"
            hover "kitchen/bad/sink_outline.png"
            sensitive (modal_state and sink_obj[day] == False and (day == 0 or (goodend == 1 and day == 3)))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(sink_obj, day, True), Jump("sink_obj"+str(day+1))
        
    hbox:
        align (0.95, 0.05)
        spacing 20
        
        if goodend != -1:
            
            imagebutton:
                idle "ui/17.png"
                hover "office_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("kitchen1", transition=Dissolve(0.25)), Show("office1")
                
            imagebutton:
                idle "kitchen_insensitive"
                
                action NullAction()
            
            imagebutton:
                idle "ui/15.png"
                hover "bedroom_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("kitchen1", transition=Dissolve(0.25)), Show("bedroom1")
                
            imagebutton:
                idle "ui/14.png"
                hover "house_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu('preferences')
                
        else:
            
            imagebutton:
                idle "ui/bad/15.png"
                hover "bad_office_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("kitchen1", transition=Dissolve(0.25)), Show("office1")
                
            imagebutton:
                idle "bad_kitchen_insensitive"
                
                action NullAction()
                
            imagebutton:
                idle "ui/bad/13.png"
                hover "bad_bedroom_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("kitchen1", transition=Dissolve(0.25)), Show("bedroom1")
                
            imagebutton:
                idle "ui/bad/12.png"
                hover "bad_house_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu('preferences')
    
    timer timer_length action renpy.restart_interaction repeat True  # 0.01 is ultra smooth, but no button will be hoverable
    
screen office1():
    
    if modal_state == True:
        button:
            keysym 'dismiss', 'rollback', 'skip', 'fast_skip', 'toggle_skip', 'hide_windows'
            action NullAction()
    
    python:
        pos = renpy.get_mouse_pos()
        x_mouse = pos[0]
        y_mouse = pos[1]
        
        x_now = (x_mouse+x_now)/smooth_const
        y_now = (y_mouse+y_now)/smooth_const
    
    if goodend != -1:
        add "office/bg_office.png" at bg_scale:
            pos(-(x_now/hover_mult), -(y_now/hover_mult))
    else:
        add "office/bad/office_bg.png" at bg_scale:
            pos(-(x_now/hover_mult), -(y_now/hover_mult))
        
    # Bookshelf
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(7*bg_scale_const)-(x_now/hover_mult), int(55*bg_scale_const)-(y_now/hover_mult))  # 7, 55
            idle "office/bookshelf.png"
            hover "office/bookshelf_outline.png"
            sensitive (modal_state and bookshelf_obj[day] == False and (day == 0 or (day == 3 and goodend == 1) or day == 4))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(bookshelf_obj, day, True), Jump("bookshelf_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(7*bg_scale_const)-(x_now/hover_mult), int(55*bg_scale_const)-(y_now/hover_mult))  # 56, 40
            idle "office/bad/bookshelf.png"
            hover "office/bad/bookshelf_outline.png"
            sensitive (modal_state and bookshelf_obj[day] == False and (day == 0 or (day == 3 and goodend == 1) or day == 4))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(bookshelf_obj, day, True), Jump("bookshelf_obj"+str(day+1))
    
    # Laptop
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(1475*bg_scale_const)-(x_now/hover_mult), int(670*bg_scale_const)-(y_now/hover_mult))  # 1475, 670
            idle "office/laptop.png"
            hover "office/laptop_outline.png"
            sensitive (modal_state and laptop_obj[day] == False and (day == 0 or day == 1 or day == 2 or (goodend == -1 and day == 3) or day == 4))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(laptop_obj, day, True), Jump("laptop_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(1449*bg_scale_const)-(x_now/hover_mult), int(603*bg_scale_const)-(y_now/hover_mult))  # 1449, 603
            idle "office/bad/laptop.png"
            hover "office/bad/laptop_outline.png"
            sensitive (modal_state and laptop_obj[day] == False and (day == 0 or day == 1 or day == 2 or (goodend == -1 and day == 3) or day == 4))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(laptop_obj, day, True), Jump("laptop_obj"+str(day+1))
        
    # Pigura
    if goodend == 1 and (day == 2 or day == 3 or day == 4):
        imagebutton at bg_scale:
            pos(int(1431*bg_scale_const)-(x_now/hover_mult), int(188*bg_scale_const)-(y_now/hover_mult))  # 1431, 188  -- 1372, 96
            idle "office/pigura.png"
            hover "office/pigura_outline.png"
            sensitive (modal_state and pigura_obj[day] == False)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(pigura_obj, day, True), Jump("pigura_obj"+str(day+1))
        
    # Stationery
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(1419*bg_scale_const)-(x_now/hover_mult), int(470*bg_scale_const)-(y_now/hover_mult))  # 1419, 470  
            idle "office/stationery.png"
            hover "office/stationery_outline.png"
            sensitive (modal_state and stationery_obj[day] == False and (day == 1 or (goodend == 1 and day == 2) or day == 3))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(stationery_obj, day, True), Jump("stationery_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(1372*bg_scale_const)-(x_now/hover_mult), int(436*bg_scale_const)-(y_now/hover_mult))  # 1372, 436  
            idle "office/bad/stationery.png"
            hover "office/bad/stationery_outline.png"
            sensitive (modal_state and stationery_obj[day] == False and (day == 1 or (goodend == 1 and day == 2) or day == 3))
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(stationery_obj, day, True), Jump("stationery_obj"+str(day+1))
        
    # Tissue
    if goodend == -1 and (day == 2 or day == 3):
        imagebutton at bg_scale:
            pos(int(1278*bg_scale_const)-(x_now/hover_mult), int(984*bg_scale_const)-(y_now/hover_mult))  # 1278, 984
            idle "office/bad/tissue.png"
            hover "office/bad/tissue_outline.png"
            sensitive (modal_state and tissue_obj[day] == False)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(tissue_obj, day, True), Jump("tissue_obj"+str(day+1))
            
        #imagebutton at bg_scale:
        #    pos(int(1295*bg_scale_const)-(x_now/hover_mult), int(1004*bg_scale_const)-(y_now/hover_mult))  # 1295, 1004
        #    idle "office/tissue.png"
        #    hover "office/tissue_outline.png"
        #    sensitive (modal_state and tissue_obj[day] == False)
            
        #    hovered Play("sound", "audio/button-hover.ogg")
        #    action SetDict(tissue_obj, day, True), Jump("tissue_obj"+str(day+1))
        
    # Tissue Box
    if goodend == -1 and (day == 2 or day == 4):
        imagebutton at bg_scale:
            pos(int(1351*bg_scale_const)-(x_now/hover_mult), int(630*bg_scale_const)-(y_now/hover_mult))  # 1351, 630
            idle "office/bad/tissuebox.png"
            hover "office/bad/tissuebox_outline.png"
            sensitive (modal_state and tissuebox_obj[day] == False)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(tissuebox_obj, day, True), Jump("tissuebox_obj"+str(day+1))
            
        #imagebutton at bg_scale:
        #    pos(int(1399*bg_scale_const)-(x_now/hover_mult), int(661*bg_scale_const)-(y_now/hover_mult))  # 1399, 661
        #    idle "office/tissue_box.png"
        #    hover "office/tissue_box_outline.png"
        #    sensitive (modal_state and tissuebox_obj[day] == False)
            
        #    hovered Play("sound", "audio/button-hover.ogg")
        #    action SetDict(tissuebox_obj, day, True), Jump("tissuebox_obj"+str(day+1))
        
    hbox:
        align (0.95, 0.05)
        spacing 20
        
        if goodend != -1:
            imagebutton:
                idle "office_insensitive"
                
                action NullAction()
            
            imagebutton:
                idle "ui/16.png"
                hover "kitchen_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("office1", transition=Dissolve(0.25)), Show("kitchen1")
                
            imagebutton:
                idle "ui/15.png"
                hover "bedroom_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("office1", transition=Dissolve(0.25)), Show("bedroom1")
                
            imagebutton:
                idle "ui/14.png"
                hover "house_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu('preferences')
        else:
            imagebutton:
                idle "bad_office_insensitive"
                
                action NullAction()
            
            imagebutton:
                idle "ui/bad/14.png"
                hover "bad_kitchen_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("office1", transition=Dissolve(0.25)), Show("kitchen1")
                
            imagebutton:
                idle "ui/bad/13.png"
                hover "bad_bedroom_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("office1", transition=Dissolve(0.25)), Show("bedroom1")
                
            imagebutton:
                idle "ui/bad/12.png"
                hover "bad_house_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu('preferences')
    
    timer timer_length action renpy.restart_interaction repeat True  # 0.01 is ultra smooth, but no button will be hoverable
    
screen bedroom1():
    
    if modal_state == True:
        button:
            keysym 'dismiss', 'rollback', 'skip', 'fast_skip', 'toggle_skip', 'hide_windows'
            action NullAction()
    
    python:
        pos = renpy.get_mouse_pos()
        x_mouse = pos[0]
        y_mouse = pos[1]
        
        x_now = (x_mouse+x_now)/smooth_const
        y_now = (y_mouse+y_now)/smooth_const
    
    if goodend != -1:
        add "bedroom/bedroom_bg.png" at bg_scale:
            pos(-(x_now/hover_mult), -(y_now/hover_mult))
    else:
        add "bedroom/bad/bedroom_bg.png" at bg_scale:
            pos(-(x_now/hover_mult), -(y_now/hover_mult))
    
    # Kaca
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(1372*bg_scale_const)-(x_now/hover_mult), int(246*bg_scale_const)-(y_now/hover_mult))  # 1372, 246
            idle "bedroom/kaca.png"
            hover "bedroom/kaca_outline.png"
            sensitive (modal_state and kaca_obj[day] == False)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(kaca_obj, day, True), Jump("kaca_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(1327*bg_scale_const)-(x_now/hover_mult), int(197*bg_scale_const)-(y_now/hover_mult))  # 1327, 197
            idle "bedroom/bad/kaca_dark.png"
            hover "bedroom/bad/kaca_outline.png"
            sensitive (modal_state and kaca_obj[day] == False)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action SetDict(kaca_obj, day, True), Jump("kaca_obj"+str(day+1))
    
    # Notebook
    if goodend != -1:
        imagebutton at bg_scale:
            pos(int(1432*bg_scale_const)-(x_now/hover_mult), int(569*bg_scale_const)-(y_now/hover_mult))  # 1432, 569
            idle "bedroom/notebook.png"
            hover "bedroom/notebook_outline.png"
            sensitive (modal_state)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action Jump("notebook_obj"+str(day+1))
    else:
        imagebutton at bg_scale:
            pos(int(1390*bg_scale_const)-(x_now/hover_mult), int(543*bg_scale_const)-(y_now/hover_mult))  # 1390, 543
            idle "bedroom/bad/notebook.png"
            hover "bedroom/bad/notebook_outline.png"
            sensitive (modal_state)
            
            hovered Play("sound", "audio/button-hover.ogg")
            action Jump("notebook_obj"+str(day+1))
    
    hbox:
        align (0.95, 0.05)
        spacing 20
        
        if goodend != -1:
                
            imagebutton:
                idle "ui/17.png"
                hover "office_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("bedroom1", transition=Dissolve(0.25)), Show("office1")
                
            imagebutton:
                idle "ui/16.png"
                hover "kitchen_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("bedroom1", transition=Dissolve(0.25)), Show("kitchen1")
                
            imagebutton:
                idle "bedroom_insensitive"
                
                action NullAction()
            
            imagebutton:
                idle "ui/14.png"
                hover "house_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu('preferences')
        else:
                
            imagebutton:
                idle "ui/bad/15.png"
                hover "bad_office_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("bedroom1", transition=Dissolve(0.25)), Show("office1")
                
            imagebutton:
                idle "ui/bad/14.png"
                hover "bad_kitchen_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action Hide("bedroom1", transition=Dissolve(0.25)), Show("kitchen1")
                
            imagebutton:
                idle "bad_bedroom_insensitive"
                
                action NullAction()
            
            imagebutton:
                idle "ui/bad/12.png"
                hover "bad_house_hover"
                
                sensitive (modal_state)
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu('preferences')
    
    timer timer_length action renpy.restart_interaction repeat True  # 0.01 is ultra smooth, but no button will be hoverable

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    
    if goodend != -1:
        add "ui/normal_textbox.png":
            yalign 1.0
            xalign 0.5
            zoom 0.8
    else:
        add "ui/dark_textbox.png":
            yalign 0.94
            xalign 0.53
            zoom 0.8
    
    #window:
    #id "window"
    
    if goodend != -1:
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who":
                    font "Aller.ttf"
                    ypos 490 xpos 100 xalign 0.5

        text what id "what":
            font "Aller.ttf"
            ypos 535 xpos 255
            size 25
    else:
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who":
                    font "Aller.ttf"
                    ypos 488 xpos 100 xalign 0.5

        text what id "what":
            font "Aller.ttf"
            color "#000"
            ypos 545 xpos 225
            size 25


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption:
                activate_sound "audio/button-click.ogg"
                hovered Play("sound", "audio/button-hover.ogg")
                action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            ##textbutton _("Back") action Rollback()
            #textbutton _("History") action ShowMenu('history')
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            ##textbutton _("Auto") action Preference("auto-forward", "toggle")
            #textbutton _("Save") action ShowMenu('save')
            #textbutton _("Load") action ShowMenu('load')
            ##textbutton _("Q.Save") action QuickSave()
            ##textbutton _("Q.Load") action QuickLoad()
            #textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start"):
                activate_sound "audio/button-click.ogg"
                hovered Play("sound", "audio/button-hover.ogg")
                action Start()

        else:

            textbutton _("History"):
                activate_sound "audio/button-click.ogg"
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu("history")

            textbutton _("Save"):
                activate_sound "audio/button-click.ogg"
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu("save")

        textbutton _("Load"):
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action ShowMenu("load")

        textbutton _("Preferences"):
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu"):
                activate_sound "audio/button-click.ogg"
                hovered Play("sound", "audio/button-hover.ogg")
                action MainMenu()

        textbutton _("About"):
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help"):
                activate_sound "audio/button-click.ogg"
                hovered Play("sound", "audio/button-hover.ogg")
                action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit"):
                activate_sound "audio/button-click.ogg"
                hovered Play("sound", "audio/button-hover.ogg")
                action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    tag menu

    add "ui/bedroom_full.png":
        zoom 0.65
        xalign 0.5

    add "ui/title.png":
        zoom 0.65
        xalign 0.5
        
    vbox:
        align(0.26, 0.9)
        spacing 15
        
        imagebutton:
            idle "ui/start.png"
            hover "start_hover"
            
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action Start()
            
        imagebutton:
            idle "ui/preference.png"
            hover "preferences_hover"
            
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action ShowMenu("preferences")
            
        imagebutton:
            idle "ui/help.png"
            hover "help_hover"
            
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action ShowMenu("help")
            
    vbox:
        align(0.74, 0.9)
        spacing 15
        
        imagebutton:
            idle "ui/load.png"
            hover "load_hover"
            
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action ShowMenu("load")
            
        imagebutton:
            idle "ui/about.png"
            hover "about_hover"
            
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action ShowMenu("about")
            
        imagebutton:
            idle "ui/quit.png"
            hover "quit_hover"
            
            activate_sound "audio/button-click.ogg"
            hovered Play("sound", "audio/button-hover.ogg")
            action Quit(confirm=not main_menu)
            
    add "black" at dissolve_out


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
    
        activate_sound "audio/button-click.ogg"
        hovered Play("sound", "audio/button-hover.ogg")
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("by Super Sikrit Klab Studio!\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        hovered Play("sound", "audio/button-hover.ogg")
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes"):
                    activate_sound "audio/button-click.ogg"
                    hovered Play("sound", "audio/button-hover.ogg")
                    action yes_action
                textbutton _("No"):
                    activate_sound "audio/button-click.ogg"
                    hovered Play("sound", "audio/button-hover.ogg")
                    action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    #if quick_menu:

    #    hbox:
    #        style_prefix "quick"

    #        xalign 0.5
    #        yalign 1.0

    #        textbutton _("Back") action Rollback()
    #        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
    #        textbutton _("Auto") action Preference("auto-forward", "toggle")
    #        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
