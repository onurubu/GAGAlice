# The game starts here. -------------------------------------------------------

label start:
    stop music fadeout(2)
    show black with fade
    #Initial variables:
    $ button_date = 0
    $ mushroomdinner = False
    $ storytime = False
    default look_around = False
    default button_name = False
    default kill_late = False
    default kiss = False
    default red = False
    default gt = False
    default window_open = False
    default callcutetwice = False
    default buttonchoice = False
    $ watered = 1
    $ existential = 0
    $ button_rp = 0
    $ playername = "Me"
    
    play music "dynamic_audio/clock.mp3" fadein(2)
    show text "You're having your favourite nightmare."
    $ renpy.pause ()
    show text "In it, you're dead."
    $ renpy.pause ()
    show text "You see nothing. You hear nothing. You feel nothing. You think nothing."
    $ renpy.pause ()
    show text "You simply don't exist. How wonderful."
    $ renpy.pause ()
    show text "The heavy burden of life disappears." 
    $ renpy.pause ()
    show text "All the things you've cried over don't matter anymore."
    $ renpy.pause ()
    show text "Even your {sc=1}failures{/sc}."
    $ renpy.pause ()
    show text "At first, you were terrified of this dream, but now you like it, because it reminds you that everything is futile."
    $ renpy.pause ()
    show text "Every night, the prospect of not waking up is a little more comfortable."
    $ renpy.pause ()
    show text "Unfortunately, that won't happen today."
    $ renpy.pause ()
    stop music fadeout(2)
    play sound "alarm_clock.wav"
    hide text with dissolve
    window hide
    
    play music "normal.mp3" fadein(3)
    show bedroom_closed_curtains with fade:
        zoom 0.9
    
    show mc stressed with easeinbottom
    "As you wake up, the first thing that you think of is:"
    "The {sc=1}{color=#000000}pressure{/sc}."
    "Today is a new day."
    "You're supposed to make the most of it."
    "You're supposed to finally exercise, book a dentist appointment, start going to lectures again, make friends, call your mom..."
    "But you just can't."
    "This decision grants you both a brief relief from the expectations..."
    "...and disappointment in yourself."
    show mc normal
    m "..."
    "You need to distract yourself from these feelings. How about an impulse purchase?"
    "It's not like you'll need all the money your parents gave you for very long anyway."
    show mc confused
    m "But... what if I do need it later on?"
    "Hesitant, as always."
    "Don't worry. It's easier to just shut up and listen to me."
    "Remember: There's no point to anything anymore."
    show mc normalsquint
    m "Yeah... ok..."
    "Maybe get something you can grow. Since you'll never have children of your own anyway."
    "And low-maintenance. You're not very good at taking care of things."
    "What kind of plant would enjoy your dark, dank, dungeon?"
    show mc normalside
    m "I don't know. Nothing."
    "Huh, so you really ARE an idiot."
    "How does it feel, knowing that you've wasted your life in school and nothing came out of it?" 
    "Think of all the money you've wasted. All of your precious time spent doing something you hated."
    "Go on. Do what idiots do, and go ask the internet mommy for help."
    
    hide mc with easeoutbottom
    window hide
    #call screen bedroom_day_1 with dissolve
    call screen bedroom_look with dissolve

    screen bedroom_day_1:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.285 ypos 0.508 idle "pc/pc_hover.png" hover "pc/pc_click.png"
            action Jump("buy_mushroom")
    
    label open_window_day_1:
        $ window_open = True
        call screen bedroom_day_1
    label close_window_day_1:
        $ window_open = False
        call screen bedroom_day_1
    label buy_mushroom:
        if look_around:
            scene website with dissolve
            call screen buy_mushroom_screen with dissolve
        else:
            
            window show
            play sound "<from 0 to 1>type.wav"
            "{size=*2.0}WELL DONE!{size=*2.0}"
            "You did it! You searched for:"
            "<what gros in daurk humid palces?>" 
            "Pathetic."
            show mc awed with easeinbottom
            m "Oh... mushrooms!"
            "Just get them."    
            "Look, you can buy a starter-kit there. Surely you couldn't mess this up too, right?"
            window hide
            hide mc with easeoutbottom
            scene website with dissolve
            window show
            m "Um... which one should I get?"
            window hide
            call screen buy_mushroom_screen with dissolve
    
    screen buy_mushroom_screen:
        imagebutton:
            xanchor 0 yanchor 0 xpos 0.088 ypos 0.42 idle "website/website_idle.png" hover "website/website_hover.png" action Jump("bought_button")
        imagebutton:
            xanchor 0 yanchor 0 xpos 0.368 ypos 0.42 idle "website/website_idle.png" hover "website/website_hover.png" action Jump("red")    
        imagebutton:
            xanchor 0 yanchor 0 xpos 0.642 ypos 0.42 idle "website/website_idle.png" hover "website/website_hover.png" action Jump("gt") 
        imagebutton:
            xanchor 0 yanchor 0 xpos 0.975 ypos 0.0 idle "website/X_idle.png" hover "website/X_hover.png" action Jump("x")    



    label x:
        show bedroom_closed_curtains with fade:
            zoom 0.9
        if look_around:
            "Stalling for time. Your favourite facade of being in control."
            window hide
        else:

            "You hate decision anxiety."
        $ look_around = True    
        call screen bedroom_look with dissolve

    screen bedroom_look:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.284 ypos 0.51 idle "pc/pc_hover.png" hover "pc/pc_click.png"
            action Jump("buy_mushroom")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.69 ypos 0.26 hover "mushroom_display/curtain_hover.png" idle "mushroom_display/curtain_select.png"
            action Notify("These stay closed.")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.5 hover "mushroom_display/bed_hover.png" idle "mushroom_display/bed_idle.png"
            action Notify("The laundromat is more scary than these sheets are dirty.")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.7425 ypos 0.53 hover "mushroom_display/table_hover.png" idle "mushroom_display/table_idle.png"
            action Notify("Table-kun judges you.")    
        
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.364 hover "mushroom_display/shark_hover.png" idle "mushroom_display/shark_idle.png"
            action Notify("At least Blahaj loves you.") 
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.56 ypos 0.36 hover "mushroom_display/noot_hover.png" idle "mushroom_display/noot_idle.png"
            action Notify("Noot noot!")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.304 ypos 0.48 hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png"
            action Notify("You never thought you'd miss your mom's plain rice and chicken...")               
    label gt:
        
        window show
        if gt:
            m "Can't get this one."
            window hide
            call screen buy_mushroom_screen
        m "This one looks so long and weird... I don't think I've ever seen this..."
        m "It's not available anyway..."
        window hide
        $ gt = True
        call screen buy_mushroom_screen
#TODO:get rid of these old things

    label red:
        window show
        if red:
            m "Can't get this one."
            window hide
            call screen buy_mushroom_screen
        m "Aren't red mushrooms supposed to be poisonous?"
        m "Well if it's on this site, it must be safe..."
        "Yeah, you can DEFINITELY trust corporations to be concerned about your safety :)"
        m "Oh wait, it's out of stock..."
        $ red = True
        window hide
        call screen buy_mushroom_screen
