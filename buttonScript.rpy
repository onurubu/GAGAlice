init python:
#check if this can be done in one call    
    renpy.music.register_channel("layer1", "music")
    renpy.music.register_channel("layer2", "music")
    renpy.music.register_channel("layer3", "music")
    renpy.music.register_channel("layer4", "music")
    renpy.music.register_channel("layer5", "music")
    renpy.music.register_channel("layer6", "music")
    renpy.music.register_channel("layer7", "music")


    def start_layers(delay=1.5):
        renpy.music.play("audio/dynamic_audio/pad.mp3", channel='layer1', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/drum.mp3", channel='layer2', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/piano.mp3", channel='layer3', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/ticklepiano.mp3", channel='layer4', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/horror_Piano octave down.mp3", channel='layer5', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/scarypiano.mp3", channel='layer6', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/horror_Low Piano Ugly.mp3", channel='layer7', loop=True, synchro_start=True, fadein=delay)

        
#check if one call possible
    def stop_layers(delay=1.5):
        renpy.music.stop(channel='layer1', fadeout=delay)
        renpy.music.stop(channel='layer2', fadeout=delay)
        renpy.music.stop(channel='layer3', fadeout=delay)
        renpy.music.stop(channel='layer4', fadeout=delay)  
        renpy.music.stop(channel='layer5', fadeout=delay)  
        renpy.music.stop(channel='layer6', fadeout=delay) 
        renpy.music.stop(channel='layer7', fadeout=delay) 
 
    def update_layers(delay=1):
        #this is disgusting
        if sadness == 100:
            layer1 = 0
            layer2 = 0
            layer3 = 1
            layer4 = 0
            layer5 = 0
            layer6 = 0
            layer7 = 0
        elif sadness >= 7:
            layer1 = 1
            layer2 = 1
            layer3 = 1
            layer4 = 1
            layer5 = 1
            layer6 = 1
            layer7 = 1

        elif sadness == 6:
            layer1 = 1
            layer2 = 1
            layer3 = 1
            layer4 = 1
            layer5 = 1
            layer6 = 1
            layer7 = 0

        elif sadness == 5:
            layer1 = 1
            layer2 = 1
            layer3 = 1
            layer4 = 1
            layer5 = 1
            layer6 = 0
            layer7 = 0

        elif sadness == 4:
            layer1 = 1
            layer2 = 1
            layer3 = 1
            layer4 = 1
            layer5 = 0
            layer6 = 0
            layer7 = 0

        elif sadness ==3:
            layer1 = 1
            layer2 = 1
            layer3 = 1
            layer4 = 0
            layer5 = 0
            layer6 = 0
            layer7 = 0

        elif sadness ==2:
            layer1 = 1
            layer2 = 1
            layer3 = 0
            layer4 = 0
            layer5 = 0 
            layer6 = 0
            layer7 = 0

        elif sadness ==1:
            layer1 = 1
            layer2 = 0
            layer3 = 0
            layer4 = 0
            layer5 = 0
            layer6 = 0  
            layer7 = 0
   
        else:
            layer1 = 0
            layer2 = 0
            layer3 = 0
            layer4 = 0
            layer5 = 0
            layer6 = 0  
            layer7 = 0   
     
        
        renpy.music.set_volume(layer1, delay=delay, channel='layer1')
        renpy.music.set_volume(layer2, delay=delay, channel='layer2')
        renpy.music.set_volume(layer3, delay=delay, channel='layer3')
        renpy.music.set_volume(layer4, delay=delay, channel='layer4')
        renpy.music.set_volume(layer5, delay=delay, channel='layer5')
        renpy.music.set_volume(layer6, delay=delay, channel='layer6')
        renpy.music.set_volume(layer7, delay=delay, channel='layer7')

    

#Character beeps:  
    renpy.music.register_channel("Beep", mixer="voice")

    def character_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("beep.wav",loop="True", channel="Beep")
        elif event == "slow_done":
            renpy.sound.stop(fadeout=1, channel="Beep")

    def character_beeps_low(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("beep_low.wav",loop="True", channel="Beep")
        elif event == "slow_done":
            renpy.sound.stop(fadeout=1, channel="Beep")    

default sadness = 0             
default persistent.sadness = False
default persistent.endcounter = 0

#one call

default persistent.end1 = False
default persistent.end2 = False
default persistent.end3 = False
default persistent.end4 = False
default persistent.end5 = False
default persistent.end6 = False
default persistent.end7 = False
default persistent.end8 = False
default persistent.end9 = False





#Characters:
define b = Character("Button", color = "#440a1f",callback=character_beeps)
define ba = Character("Agaricus bisporus", color = "#440a1f",callback=character_beeps)
define na = Character("???", color = "#000000",callback=character_beeps)
define m = Character("[playername]", color = "#38425F",callback=character_beeps_low)
define cen = Character(None, what_xalign=0.5, what_text_align=0.2,  text_xpos=0.5)

#Images:

image choicebox1_animated_idle  = Animation("gui/choicebox/choice1_idle.png", 0.5, "gui/choicebox/choice2_idle.png", 0.5)
image choicebox2_animated_idle  = Animation("gui/choicebox/choice2_idle.png", 0.5, "gui/choicebox/choice1_idle.png", 0.5)
image choicebox1_animated_hover  = Animation("gui/choicebox/choice1_hover.png", 0.5, "gui/choicebox/choice2_hover.png", 0.5)    
image choicebox2_animated_hover  = Animation("gui/choicebox/choice2_hover.png", 0.5, "gui/choicebox/choice1_hover.png", 0.5)   

image choicebox3_animated_idle  = Animation("gui/choicebox/choice3_idle.png", 0.5, "gui/choicebox/choice4_idle.png", 0.5)
image choicebox4_animated_idle  = Animation("gui/choicebox/choice4_idle.png", 0.5, "gui/choicebox/choice3_idle.png", 0.5)
image choicebox3_animated_hover  = Animation("gui/choicebox/choice3_hover.png", 0.5, "gui/choicebox/choice4_hover.png", 0.5)    
image choicebox4_animated_hover  = Animation("gui/choicebox/choice4_hover.png", 0.5, "gui/choicebox/choice3_hover.png", 0.5)

image cloudbox_animated_idle  = Animation("gui/choicebox/cloudbox/cloud1_idle.png", 0.2, "gui/choicebox/cloudbox/cloud2_idle.png", 0.2, "gui/choicebox/cloudbox/cloud3_idle.png", 0.2)
image cloudbox_animated_hover  = Animation("gui/choicebox/cloudbox/cloud1_hover.png", 0.2, "gui/choicebox/cloudbox/cloud2_hover.png", 0.2, "gui/choicebox/cloudbox/cloud3_hover.png", 0.2)




image kit = "images/mushroom_display/kit.png"
image bottle = "images/mushroom_display/bottle.png"
image day_1 = "day/day_1.png"
image day_2 = "day/day_2.png"
image day_3 = "day/day_3.png"
image day_4 = "day/day_4.png"
image chibi_mc:
    yanchor 1.0
    xanchor 0.0
    "chibi/1.png"
    pause 0.5
    "chibi/pass.png"
    pause 0.5
    "chibi/2.png"
    pause 0.5
    "chibi/pass2.png"
    pause 0.5
    repeat
image chibi_mushroom:
    yanchor 1.0
    xanchor 1.0
    "chibi/mushroom_1.png"
    pause 0.5
    "chibi/mushroom_pass.png"
    pause 0.5
    "chibi/mushroom_2.png"
    pause 0.5
    "chibi/mushroom_pass2.png"
    pause 0.5
    repeat
image chibi_sleep:
    yanchor 1.0
    xanchor 1.0
    "chibi/chibi_sleep_1.png"
    pause 1.0
    "chibi/chibi_sleep_2.png"
    pause 1.0
    repeat
image chibi_awake:
    yanchor 1.0
    xanchor 1.0
    "chibi/chibi_sleep_awake.png"
image chibi_scared:
    yanchor 1.0
    xanchor 1.0
    "chibi/chibi_sleep_scared.png"
image affection = ConditionSwitch(
    "button_rp >= 50", "sprites/affection/affection max.png",
    "button_rp >= 40", "sprites/affection/affection almost_max.png",
    "button_rp >= 30", "sprites/affection/affection mid_good.png",
    "button_rp >= 20", "sprites/affection/affection min_good.png",
    "button_rp >= 10", "sprites/affection/affection almost_good.png",
    "button_rp == 0", "sprites/affection/affection mid.png",
    "button_rp >=-10 ", "sprites/affection/affection almost_bad.png",
    "button_rp >=-20 ", "sprites/affection/affection min_bad.png",
    "button_rp >=-20 ", "sprites/affection/affection mid_bad.png",
    "button_rp >= -30", "sprites/affection/affection almost_min.png",
    "button_rp >= -50", "sprites/affection/affection min.png",    
    "True", "sprites/affection/affection mid.png")    

image existential_status = ConditionSwitch(
    "existential >= 3", "sprites/existential/existential_dread.png",
    "existential >= 2", "sprites/existential/philosophical.png",
    "existential >= 1", "sprites/existential/thoughtful.png",
    "existential == 0", "sprites/existential/oblivious.png",
    "True", "sprites/existential/oblivious.png")

image water_status = ConditionSwitch(
    "watered >= 2", "sprites/water/water_full.png",
    "watered >= 1", "sprites/water/water_half.png",
    "watered >= 0", "sprites/water/water_empty.png",
    "True", "sprites/existential/water_empty.png")

#Transforms:
transform existential_location:
    yalign 0.0
    xalign 0.0
    ypos 0
    xpos 0.88

transform water_location:
    yalign 0.0
    xalign 0.0
    ypos 0
    xpos 0.84

transform slightright:
    xalign 0.8
    yalign 1.0   
transform slightleft:
    xalign 0.2
    yalign 1.0  
    
transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0    
transform slightright:
    xpos 0.45    
    ypos 0.7   
transform slightleft:
    xpos 0.45
    ypos 0.7    
transform slightcenter:
    xpos 0.5
    ypos 0.7 

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
        #if window_open:
        #    imagebutton:
        #        xanchor 0 yanchor 0 xpos 0.78 ypos -0.12 idle "window/window_open_idle.png" hover "window/window_open_hover.png" action Jump("close_window_day_1")
                
        #else:
        #    imagebutton:
        #        xanchor 0 yanchor 0 xpos 0.78 ypos -0.12 idle "window/window_closed_idle.png" hover "window/window_closed_hover.png" action Jump("open_window_day_1")    
    
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

    label bought_button:
        window show
        m "You're kind of...cute."
        "Be honest. It's bland, isn't it?"
        "Well, enjoy those leftovers that no one else wanted."
        "Now all you have to do is go back into bed for a day and doomscroll until it arrives."
        window hide
        scene black with fade
        stop music fadeout(3)

        show chibi_sleep at truecenter with Dissolve(2)
        pause(2)
        
        

    $ button_day = 0
    stop music
    queue sound "knock.wav"
    #pause(1)
    show chibi_awake at truecenter
    play music "heartbeat.wav"
    "{sc=4}{i}{color=#000000}SOMEONE IS AT THE DOOR!{/i}{/sc}"
    "The adrenaline wakes you up, sending your heart hammering as you cover yourself with your sheets."
    na "Hello? I saw you had a package delivered to the reception, so I thought I'd bring it up to you..."
    show chibi_scared at truecenter  
    "We both know you can't do this."
    play sound "knock.wav"
    na "You awake?"
    m "{size=-15}I'm sorry.{size=+15}"
    na "I'm leaving them by the door. Good luck with your, um... experiment."
    "You hear your neighbour, who, after nearly a year, you still haven't met, walk away."
    "How can someone who never leaves their room meet someone?"
    "Sometimes you can hear the muffled sound of rock music when you're up late. He likes guitars and violins."
    "Once, you took off your headphones and listened to the whole album."
    "It made you feel less lonely and more inspired than any lofi beat ever had."
    "You wish you had the courage to say hi."
    stop music fadeout(3)
    scene bedroom_closed_curtains with Fade(0.5, 1.0, 0.5):
        zoom 0.9
    queue sound "door.wav"
    queue music "normal.mp3"
    m "Oh, a note?"
    play sound "page.wav"
    show instructions at truecenter with easeinbottom
    window hide
    pause
    
    hide instructions with easeoutbottom
    show mc confused with easeinbottom
    window show
    m "Bright? Huhhhh?"
    m "Is this right? It's like... the exact opposite of what I thought a mushroom is supposed to like."
    show mc confused at right with move

    menu:
        m "Do I follow the instructions? Or..."
        "Trust my gut.":
            show mc normal at center with move
        
            m "Yeah, this makes no sense."
            m "Someone must have screwed up this note."
            hide mc with easeoutbottom
            scene bedroom_closed_curtains_kit with dissolve:
                zoom 0.9
            "You set up the kit on your table, you spray it for the first time for the day, and you wait..."
            window hide
            
            show black with fade
            stop music fadeout 3

            "..."
            ".."
            "."
            window hide
            pause(0.2)
            scene bedroom_closed_curtains_kit with Fade(0.5, 1.0, 0.5):
                zoom 0.9
            
            "Wow! Those five weeks pass terrifyingly fast! You try not to think of what you've accomplished during them."
            show mc normal with easeinbottom
            "You stand in front of the mushroom kit."
            "Would you look at that? Well, you can't. There's nothing to see. The damn thing didn't grow."
            show mc sad
            "Secretly, you'd been getting excited. How foolish of you."
            "Now it's yet another disappointment."                        
            show mc stressed
            m "Please grow."
            m "Please. Just for me."
            #"You sound stupid."
            m "I promise I'll do better."
            #"You're talking to a mushroom, you know? It can't hear you."
            m "I'm sorry you're stuck with me. I'm sorry I suck."
            play sound "spray.wav"
            m "I'm just sorry. Please grow."
            play sound "spray.wav"
            m "Are you thirsty? What do you need? How can I help?"
            "You're hilarious!"
            show mc vstressed
            "YOU CAN'T DO ANYTHING RIGHT." with sshake
            scene black with fade
            pause(1)
            "Nothing ever grew. Neither the mushroom, nor your hopes."
            $ persistent.end1 = True    
            "End 1: So mushroom for improvement."
            
            return
        
        "Just follow the instructions.":
            show mc at center with move
            show mc normal
     
            m "I'm no mycologist. Why am I acting as if I know better?"
            m "I'll just follow it step by step."
            


    "Ventilation means air flow. That means... you FINALLY have to open up those curtains!"
    show mc stressed
    m "Ughhhhhhhhh."
    "How are you STILL scared? You do realise that people have better things to do than look at your sorry ass, right?"
    m "Mmmmmmm..."
    "HAHAHAHAHA!"
    "YOU. CAN'T. DO. IT."
    hide mc with easeoutbottom
    window hide
    call screen open_window with dissolve
    
    screen open_window:
        
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.5 hover "mushroom_display/bed_hover.png" idle "mushroom_display/bed_idle.png"
            action Notify("The warmth still lingers temptingly.")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.7425 ypos 0.53 hover "mushroom_display/table_hover.png" idle "mushroom_display/table_idle.png"
            action Notify("Table-kun is dusty and feeling neglected.")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.284 ypos 0.51 idle "pc/pc_hover.png" hover "pc/pc_click.png"
            action Notify("Laptop-chan is too busy downloading anime to care.")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.69 ypos 0.26 hover "mushroom_display/curtain_hover.png" idle "mushroom_display/curtain_select.png"
            action Jump("opened_curtained")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.364 hover "mushroom_display/shark_hover.png" idle "mushroom_display/shark_idle.png"
            action Notify("Blahaj believes in you!")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.56 ypos 0.36 hover "mushroom_display/noot_hover.png" idle "mushroom_display/noot_idle.png"
            action Notify("Noot noot's button eyes stare unblinkingly into your soul. What is life?")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.304 ypos 0.48 hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png"
            action Notify("It'll be ramen for breakfast too.")             

    label opened_curtained:
        play sound "curtain.ogg"
        scene bedroom_day with Fade(.25, 0, .75, color="#fff"):
            zoom 0.9

    show mc shocked with easeinbottom 
     
    m "MY RETINAS! OW OW OW!"
    show mc surprised
    m "Whoa, it's actually a pretty nice day outside..."
    
    "Stop getting excited. You know you won't be getting out of here anytime soon."
    "Actually, you should feel {i}worse{/i}, now that you know what you're missing out on."
    "Everyone's having a great day, doing their stuff. But you're going to stay inside and do nothing."
    "Go on, feel worse."
    "Feel worse!"
    show mc stressed
    m "..."
    m "{sc=2}{color=#000000}Focus. Focus."
    "You take a deep breath in and out (as if that'll ever shut me up), then place the kit on the table."
    "Nice and toasty by the window."
    hide mc with easeoutbottom
    window hide
    show bedroom_day_kit with dissolve:
        zoom 0.9
    window show
    "Now, the hard part. Watering."
    "Think you can do that, you little shit?"
    window hide
    hide mc with easeoutbottom
    $ watered = 0
    show water_status at topright with dissolve
    call screen water with dissolve
    

    screen water:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("day1_watered")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.5 hover "mushroom_display/bed_hover.png" idle "mushroom_display/bed_idle.png"
            action Notify("How long will you resist?")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.7425 ypos 0.53 hover "mushroom_display/table_hover - Copycopy.png" idle "mushroom_display/table_idle - Copycopy.png"
            action Notify("Table-kun likes having responsibilty! It's still dusty though...")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.284 ypos 0.51 idle "pc/pc_hover.png" hover "pc/pc_click.png"
            action Notify("Laptop-chan is STILL too busy downloading anime to care.")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.364 hover "mushroom_display/shark_hover.png" idle "mushroom_display/shark_idle.png"
            action Notify("Blahaj is so proud of you!")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.56 ypos 0.36 hover "mushroom_display/noot_hover.png" idle "mushroom_display/noot_idle.png"
            action Notify("Noot noot doesn't like change.")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.304 ypos 0.48 hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png"
            action Notify("The smell permeates the room.")                 

    label day1_watered:
        play sound "spray.wav"
        $ watered = 1
        pause 1
        queue sound "spray.wav"
        $ watered = 2
        show mc normal with easeinbottom
        window show
        m "Nice and wet."
        show mc happy
        m "Heh. That's what she said."
        m "Hehe."
        show mc stressed
        m "So stupid..."
        window hide

        hide water_status with dissolve
        stop music fadeout 3
        scene black with Fade(0.5, 1.0, 0.5)
        show chibi_sleep at truecenter with Dissolve(1.5)

        image top_text = ParameterizedText(xalign=0.5, yalign=0.3)
        show top_text "Weeks of self-hatred pass..." with dissolve
        pause 2
        show top_text "But you water your mushroom daily." with dissolve
        pause 2
        scene bg bedroom_day_growing with Fade(1, 2.0, 1):
            zoom 0.9
        
        show mc stressed at center with easeinbottom 
        window show
        m "Ugh... imagine waking up in the actual morning."
        m "Shit sleep schedule got so bad, it went full circle."
        show mc normal
        m "Hey little guy, did you get a good night sleep? Are you-"
        #window hide

        na "{size=-8}I don't sleep, but thanks! Also, I'm kinda stuck... Could you pull me out?{size=+8}"
        show mc shocked at bounce
        m "..."
        na "{size=-8}Helloooo? Help? Please?{size=+8}"
        na "{size=-8}I'd reeeeeeally like to get out of here! It'd be nice to actually SEE something{size=+8}."
        m "(Oh my God. There's something talking to me from inside the box!)"
        "You are NOT ready for unexpected social interaction. But it's in your room, so you can't even run away!"
        "This has got to be the WORST random social situation you've EVER encountered."
        show mc shocked at right with move

        
        menu:
            "You can throw it out the window and pretend it never happened, or help it."
            "NOPE. 1000 percent NOPE. GET OUT.":
                show mc stressed at center with move
                
                m "{sc=4}{color=#000000}NOPE{/sc}. I am NOT dealing with this."
                hide mc with easeoutbottom
                "Grabbing the monstrous abomination by the box, you pull back your arm and throw it out the window at full speed!"
                #show button depressed
                na "AaaaaAAaaaAAAaaAAAAaAAAAA!!!"
                show bedroom_day with dissolve:
                    zoom 0.9
                hide button with dissolve
                m "No one socialises with me without warning."
                play sound "curtain.ogg"
                show bedroom_closed_curtains with dissolve:
                    zoom 0.9
                m "No one."
                m "Back to bed."
                window hide
    
                scene black with fade
                $ persistent.end2 = True    
                "End 2: Mush-room bound."
                return
            "It said please...":
                show mc surprised at center with move
                m "I-um- so I just... do what exactly?"
                na "{size=-8}Just grab my head and pull! Real hard!{size=+8}"
                show mc confused
                m "Ok..."   
                          
                hide mc with easeoutbottom
                "You put the box on the floor, scrunch up your comically oversized hoodie arms, and get a good grip on the base of the mushroom top."
                window hide
                
                scene pulling with dissolve
                
                stop sound 
                play sound "ballon.wav"
                #pause 3
                $ renpy.pause(3.0, hard=True)
                stop sound 
                play sound "pop.ogg"  
                show falling
                #pause 2
                $ renpy.pause(2.0, hard=True)
                
                scene bottle day with Fade(1, 2.0, 1):
                    zoom 0.9

                play music "normal.mp3" fadein(3)
                show button happy at left
                show mc shocked at right
                with easeinbottom

                na "Phew~ Thanks for that!"
                m "Oh... my... god."
                show button sad
                na "It was sooooooo tight in there! Ugh! And really muffled, you know?"
                m "...H-How did you even {b}FIT{/b} in that box!?"
                show button surprised
                na "Aaah, so THIS is what it looks like outside...!"
                show button happy
                na "I like your environment!"
                m "..."
                show mc shout
                m "You're a {sc=2}{color=#000000}talking mushroom{/sc}!"
                show button vvhappy
                na "And you're my master!"
                show mc shocked at bounce
                m "Your {sc=2}{color=#000000}WHAT-!?"
                show button vhappy
                na "So what's your name?"
                show mc awed
                m "Uh... My name... (I wasn't ready to socialise! I'm forgetting my NAME!)"
                jump name


    label name:                
        $ player_name = renpy.input("What's your name?", length = 8)
        $ player_name = player_name.strip()
        $ player_case_insensitive = player_name.lower()
        if player_case_insensitive == "manly":
            $ playername = player_name
            m "...%(player_name)s."
            show button vvhappy
            na "{sc=3}{color=#000000}MANLY!?{/sc}"
            na "That name is BADASS! You must be a really cool person!"
            show mc annoyed
            m "I am cool, I think?"
            show button happy
        elif player_case_insensitive == "button":
            if button_name:
                show button annoyed
                na "Pick something else!"
                jump name
            $ playername = player_name
            m "...%(player_name)s."
            show button dgaf
            na "..."
            na "Nope, that's not gonna work."
            show mc confused
            m "But that's my name!"
            show button vdgaf
            na "..."
            m "Ok, ok..."
            $ button_name = True
            jump name
        elif player_name == "":
            "What? Can't even think of a name by yourself?"
            "You really are hopeless."
            "Fine, I'll make one up for you. Let's go with your dead family fish."
            $ player_name="Finn"
            $ playername = player_name
            m "...%(player_name)s."
        
        else:
            $ playername = player_name
            m "...%(player_name)s."
        
        na "Well then, %(player_name)s..."
        show button vvhappy
        na "{size=*1.5}THANK YOU FOR RAISING ME!{size=*1.0}" with sshake
        show mc shocked
        m "Urk... {size=-8}not... {size=-5}so... {size=-3}loud... {size=-2}please...{size=+18}"
        show button goodbye
        na "Whoopsie! Got carried away there and blew a hole into your eardrums, {sc=2}{color=#000000}hehe."
        show mc worried
        m "I-it's fine."
        show button vgoodbye
        na "Sorry~"
        show mc stressed
        m "Please don't apologise..."
        show button happy
        na "Alright, I won't. Sorry retracted. Let's start over, calmer this time."
        show mc normal
        na "Dearest %(player_name)s, thank you oh so much."
        na "Thank you, for raising me..."
        na "Thank you for talking to me every day..."
        na "And {b}most importantly{/b}, thank you..."
        na "For-"
        stop music
        show button cough
        na "*Cough*"
        na "*Cough, cough, COUGH!*"
        show mc confused
        m "...?"
        show button vcough
        na "Cough - WATER - cough."
        window hide
        hide mc with easeoutbottom
        $ watered = 1
        show water_status at topright with dissolve
        call screen water_2
        

        screen water_2:
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
                action Jump("day1_watered_2")

        label day1_watered_2:

            $ watered = 3
            window show

            queue sound "spray.wav"

            queue sound "spray.wav"
            "You hurriedly spray water right at her. That seems to work."
            window hide
            show mc normal at right with easeinbottom
            show button sad with easeinbottom
         
        window show
        m "...Better?"
        show button happy
        na "Muuuuuch better, thanks!"
        hide water_status with dissolve
        m "...Um, not to change the topic but-"
        show mc confused
        m "How are you TALKING!? What ARE you!? How did you get so... BIG?"
        show button normal
        na "I dunno. I was pretty much was just born, so I don't know anything."
        na "Wasn't I supposed to be this way?"
        show mc stressed
        m "NO!"
        show mc shout
        m "You were supposed to be small and many!"
        m "And non-talking!"
        show mc surprised
        m "You're almost as big as me! And I'm still amazed that you fit in that box."
        show button happy
        na "But I like how I am now. It feels right!"
        ba "As for WHAT I am... I've already got a name: Agaricus bisporus."
        m "..."
        show mc awed
        m "Not to be rude, but it's spilling over the text box."
        show button normal
        b "Eh, then just call me Button."
        m "Okaaaaay..."
        show mc worried
        "Suddenly, it hits you-"
        "This situation is {i}ABNORMAL{/i}!"
        "You're talking to a {i}mushroom{/i}! Are you non-ironically insane?"
        show mc stressed
        m "Hold on... I need to check something on my laptop."
        hide mc
        with easeoutbottom
        show button bored
        b "Sure, sure... I'll just wait here. Again."
        hide button
        with easeoutbottom
        window hide

        call screen bedroom_day_2 with dissolve
    
        screen bedroom_day_2:
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.284 ypos 0.51 idle "pc/pc_hover.png" hover "pc/pc_click.png"
                action Jump("buy_mushroom2")

            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.5 hover "mushroom_display/bed_hover.png" idle "mushroom_display/bed_idle.png"
                action Notify("You really just want to crawl under them and ignore Button, but that won't do.")     
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.7425 ypos 0.53 hover "mushroom_display/table_hover - Copy.png" idle "mushroom_display/table_idle - Copy.png"
                action Notify("Table-kun feels good to have a purpose.")    
            
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.364 hover "mushroom_display/shark_hover.png" idle "mushroom_display/shark_idle.png"
                action Notify("Blahaj senses a new potential friend!") 
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.56 ypos 0.36 hover "mushroom_display/noot_hover.png" idle "mushroom_display/noot_idle.png"
                action Notify("Noot noot stares suspiciously at Button.")     
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.304 ypos 0.48 hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png"
                action Notify("You know you should cook yourself something for once.")       



      
        
        label buy_mushroom2:       
            play sound "<from 0 to 1>type.wav"
            scene website2 with dissolve
            m "I should've checked what this website was 'about' from the very beginning..."
        call screen aboutpage with dissolve
        screen aboutpage:
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.8125 ypos 0.120 idle "website/about_idle.png" hover "website/about_hover.png"
                action Jump("about")
        label about:
            window hide
            scene website_about with dissolve
        pause
        
        show mc surprised at right with easeinbottom 
        window show
        m "..."
        show mc shocked
        m "{sc=3}{color=#000000}WHAT THE HELL???? WHAT KINDA MESSED UP WEBSITE IS THIS?"
        m "Button!"
        show button normal at left with easeinbottom
        b "Yeeeeees?"
        show mc confused
        m "Is this true?"
        show button dgaf
        b "I can't read. I've just been born?"
        show mc surprised
        m "It says..."
        show mc stressed
        "You're suddenly reminded of that time you messed up reading a passage during class."
        "You'll never forget the muffled laughter that followed your recital."
        m "Nevermind. It's just messed up!"
        show button bored
        b "Alas, I shall never know..."
        show button annoyed
        b "Come on! Just tell me!"
        m "Maybe I can give you a summary..."
        m "The people who made you... they say stuff like..."
        show mc blushside
        m "*Ahem*"
        show mc vblushside
        m "They made you for... perverted things!... And to be {i}eaten{/i}."
        show button surprised
        b "..."
        show button blush
        b "..."
        m "I know, it's-"
        show button blushsmile
        b "That doesn't sound so bad!"
        show mc shocked
        m "..."
        show button happy
        b "I just wanna have fun!"
        b "And I am a mushroom, so..."
        show button vvhappy
        b "Eat me WHENEVER you want!" with sshake
        show button vhappy
        b "Grilled with butter and cheese, in a saucy pasta, a soup, on a pizza, in a salad or a burger..."
        b "Not to mention how nutritious I am! Low in calories, containing protein, fiber, and antioxidants!"
        b "Some studies even show that I can reduce risks of Alzheimer's and cancer!"
        show button vvhappy
        b "Isn't it wonderful how versatile my body is? I just can't wait to be consumed!"
        show mc shout
        m "Pretty random fact you know there, for someone who's \"just\" been born!"
        show button normal
        b "It's just in my head... All these random facts about mushrooms..."
        m "And! How are you just... fine with getting eaten!? YOU'RE SENTIENT!"
        show button happy
        b "Weren't you planning to eat me from the start anyway?"
        show mc confused
        m "Well yeah, well maybe? But...."
        window hide
        hide mc
        hide button
        with easeoutbottom
        scene bottle day with dissolve:
            zoom 0.9
        show mc stressed at right
        show button happy at left
        with easeinbottom
        "But... this is more than you were prepared to handle."
        "It's kind of funny how you got yourself in this mess."
        "You didn't even bother to check what it IS you were buying!"
        m "You were the one who made me do it!"
        show button surprised
        b "?"
        "?"
        "Haha! You can't blame {i}me{/i}. You're the one in control."
        "And does it really matter now anyway?"
        "You can't just rot in your bed anymore. You've brought sentient life into this world!"
        "You saw that website right? Only alive for three days... yikes. You'd HATE if that were you."
        m "Ugh... What mess have I gotten myself into?"
        show button sad 
        b "Am I doing something wrong?"
        show mc awed
        m "N-not at all! Just hold on."
        show mc stressed
        m "(I can't kick it out. I raised it! I talked to it for over a month!)"
        m "(Screw it! It'll be good for you. You know you need a friend. And it's short-term anyway...)"
        show bottle noon with Dissolve(2):
            zoom 0.9
        show button surprised
        play music "night.mp3" fadein(3)
        b "Whoaaaa... why is it changing colour outside!?"
        show mc normal
        m "Yeah. It's the sunset. It does that. Um..."
        show mc blushside
        m "So look..."
        m "Do you want to be..."
        show button smirk
        b "{b}Lovers?{/b}"
        show mc shocked
        m "{size=+40}{i}FRIENDS!{/i}{size=-40}"
        show button bored
        b "Awwww..."
        show mc stressed
        m "Ok, I get it. Haha."
        show button smirk
        b "I mean... I'm not joking, you know..."
        b "Romance can be pretty tasty."
        show mc confused
        m "(That website really wasn't kidding, huh?)"
        m "(They really are making and selling edible short-term lovers.)"
        "Imagine being so unappealing that only a mushroom would date you."
        show mc stressed
        "She doesn't even care for you. She'd take {i}anyone{/i}."
        "{sc=1}{color=#000000}You're not special."
        m "(Shut up.)"
        "Nah. You're not good enough at ignoring your thoughts yet."
        m "{sc=2}{color=#000000}(Focus!)"
        show mc awed
        m "I don't understand how copulation would even work! You're a MUSHROOM!"
        m "You're part of a completely separate evolutionary branch from me!"
        show button vvhappy
        b "Don't think about it THAT hard!"
        b "When a man and a mushroom love each other very much-"
        show mc stressed
        m "Nevermind."
        m "I'm not interested."
        "Aaaaand there it goes. Your only oppurtunity to get laid. Byeeeee~!"
        m "(I don't care!)"
        show mc normal
        m "Friends? Yes or no?"
        show button normal
        b "Eh, sure. I'm open to pretty much anything."
        show button vhappy
        b "So what do you wanna do, {i}f r i e n d{/i} ?"
        show mc normal
        m "I don't know..."
        show button normal
        b "..."
        m "..."
        show button bored
        b "..."
        show mc normalside
        m "..."
        show button happy
        b "O-kay... I'll take the lead then, shy boy."
        

        show day_1 at topleft
        show water_status at water_location
        show existential_status at existential_location 
        show affection at topright
        with dissolve

        b "Well one thing I really wanna know about you is..."
        show button vhappy
        b "What do you think of my form? Do I look pretty?"
        show mc stressed
        m "This crap again? I told you-"
        show button vvhappy
        b "No no! It's not flirting, I promise. It's just like when you tell your homies they're looking good."
        show mc normalside
        "How sweet. She thinks you have 'homies'!"
        m "Ugh, I'll try..."
        menu:
            "Is she pretty?"
            "Appearance doesn't matter.":
               
                m "It doesn't matter..."
                show button surprised
                $ button_rp -= 10
                b "..."
                b "Damn."
                show mc normal
                m "What? It's just how I am. Appearance doesn't matter. No one gets to choose it anyway."
                show mc normalside
                m "My mom would say the same thing."
                "You really think you should use your mom as an example? After everything?"
                show mc stressed
                m "A-Actually, nevermind. I don't know why I said that."
                show button closedannoyed
                b "No. It's ok to have an opinion."
                show button annoyed
                b "The problem is-!"
                show button angry
                b "When I ask if I look good, it's an opportunity to build my confidence! Not DISMISS me!"
                show button sad
                b "Otherwise, I'll just think I'm not good enough."
                b "You raised me and everything..."
                b "I just... wanted to hear you were proud of me..."
                show mc shocked
                m "No! You're good! I'm sorry!"
                m "You're pretty ok?"
                show mc stressed
                m "Ugh, this is why I don't like talking! I can't do it!"
                show button normal
                b "Hey..."
                show button happy
                b "It's ok. You didn't mean to hurt me. I'm a forgiving kind of mushy!"
                b "So don't beat yourself up! I still love you!"
                show mc normal
                m "If you say so..."
                b "Ok, here's your opportunity to redeem yourself."
                show mc worried
                "Or another opportunity to disappoint her!"
                
            "Cute as a button!":
                
                $ callcutetwice = True
                show mc annoyed
                m "Heh."
                m "One could say you're...a-as..."
                
                show mc stressed
                m "...Nevermind."
                show button happy
                b "You can do it! Try to say every word in order clearly."
                show mc shout
                m "But I'm going to say something stupid!"
                show button normal
                b "Say it! Who am I going to tell? No one!"
                
                show mc stressed
                m "Ugh."
                m "One could say..."
                show mc vstressed
                m "... you're as c-cute..."
                show mc vblushside
                m "as a button! There!"
                show button vvhappy# at center with move
                $ button_rp += 10
                b "Eeeek! How unexpectedly adorable of you!"
                "How \"{sc=2}{color=#000000}ADORABLE\"{/sc} you are!? HAHAHAHAHAH! Your fragile masculinity REALLY didn't want to hear that!"
                show mc worried
                m "Ugh..."
                m "(At least she looks happy.)"
                b "Now I'm excited to ask you something else!"

                
                
        show mc stressed        
        m "G-go ahead."
        show button vhappy
        b "Fun fact!"
        show button happy
        $ existential = 0
        b "Did you know that button mushrooms are some of the most widely-consumed mushroom types in the world?"
        #show button happy at slightleft with move
        menu:
            "They're the most widely-consumed type, huh?"
            "I prefer Shiitake mushrooms.":
                show mc normal
                m "Why?"
                
                show button normal
                b "Why...?"
                show mc normalside
                m "Yeah... I mean... I prefer Shiitake mushrooms so I'm genuinely curious."
                show button surprised
                b "SHIITAKE!?"
                $ button_rp -= 10
                show button angry
                b "How could you compare us!?"
                show button vangry
                b "I'm versatile! A CLASSIC!"
                show mc annoyed
                m "Isn't that just your opinion?"
                if button_rp == -10:
                    m "Just like you said earlier, you're entitled to your opinion. As am I."
                show button annoyed
                b "You chose ME. That speaks for itself."
                show mc normal
                m "Well actually I chose you because-"
                jump why_choose

            "Cool but... isn't that murder?":
                
                show mc normalside
                m "I guess that's pretty cool..."
                show button happy
                b "Yeah!"
                show mc normalsquint
                m "But like also... don't you feel weird about it? You're talking about... consuming mushrooms."
                show mc confused
                m "That's like... discussing murder to you, isn't it?"
                show button vhappy
                b "I'm meant to be eaten, what can I say? And I'm delicious!"
                show mc sad
                m "True, but still. Are you really ok with dying?"
                show button vvhappy
                b "Yup! There's no need to think about it!"
                b "Either I dry up and wither away, or I get to be a tasty meal for a love-"
                b "I mean friend!"
                show mc surprised
                m "...Wow."
                m "I'm honestly impressed."
                show mc sad
                m "You're just following life's design. I don't even know what my purpose is..."
                show button normal
                b "Purpose? Why are you thinking about that? Can't you just be happy doing stuff you like?"
                show mc stressed
                m "Nope."
                show button surprised
                b "Why?"
                show mc annoyed
                m "You really wanna know?"
                show button happy
                b "Of course! I want to know all about you!"
                menu:
                    "Should I really tell her everything?"
                    "Share your opinion about life, death, and meaning.":
                        jump explain
                    "Not a good idea.":
                        show mc normalside
                        m "Uh... maybe that's a little too heavy..."
                        show mc normal
                        m "Let's just say... I overthink."
                        show button normal
                        b "That's silly."
                        show button vhappy
                        b "Just don't overthink! And you'll be happy like me!"
                        "Yeah, don't overthink about how much you ----- and you'll be happy! Like her!"
                        "Sounds like everyone you've ever confided in."
                        show mc normalsquint
                        m "..."
                        show button normal
                        b "..."
                        show button bored
                        b "Um, so... speaking of living life to its fullest..."
                        b "Can we go do something? Outside with the pretty sunset?"
                        show button goodbye
                        b "Because this room is reeeeeeally tiny and I am getting reeeeeeally bored."
                        jump bored
                        

        label explain:

            m "Hah... Ok then. It could be nice to vent. Where do I start?"
            show mc normalside
            m "My biggest struggle is probably the concept of death."
            show button normal
            m "Because one day - poof! You're alive, whether you wanted to be or not."
            m "And you figure out pretty soon that you'll die and disappear, and there's nothing you can do about it. You're just expected to accept it and enjoy life, but-"
            show mc confused
            m "Every second is counting down to death. How can you just relax?"
            show mc sad
            m "Sometimes I wonder why everybody isn't screaming."
            m "As a kid, I was healthy and young, so didn't worry about it. I thought scientists would have discovered immortality by the time I got older and we'd all be fine."
            m "But now I know that's not going to happen. The world's too corrupt, and everyone else has given up. So I have too. I'm gonna die and that's that."
            show mc stressed
            m "If I try to remember what it was like before I was born, that stillness and nothingness... I think death will be like that."
            m "I don't think it will be that bad."
            m "But it's still a lot of pressure to make the most of every day, especially when you can't do the bare minimum and leave your room."

            m "Life is a random fucking miracle in a soup of possibility. It's so weird, but I'm still scared to die, because I won't get another chance."
            m "So many things to do. Money, passion, skills, friendships, love, family, health..."
            $ existential += 1
            m "After a certain point of stress... doing \"happy\" things isn't enough anymore."
            
                       
            
            show button depressed
            b "..."
            show mc normalside
            m "Sorry if I overshared. I don't know why-"
            show mc confused
            m "You ok?"
            b "I don't know... This sudden feeling of dread just came over me."
            b "What you said... Will we really just... disappear? I won't be able to do anything anymore?"
            show mc annoyed
            m "Well, what did you think was going to happen? It's natural."
            show button dgafdownsad
            b "I didn't..."
            m "Welp, sorry. I didn't mean to make you miserable."
            m "Especially when you probably won't be living for very long."
            m "Just stay happy and ignorant."
            show button sad
            b "Maybe that's for the best."
            b "..."
            show mc normal
            m "..."
            show button cough
            b "It's hard to stop thinking!"
            b "Why am I alive?"
            show mc confused
            m "Um... because I watered you?"
            show button depressed
            b "Then why did you choose me?"
            b "Why {b}me{/b}?"
            jump why_choose

        
        
    label why_choose:    
        menu:
            "Why did I choose her?"
            "Because she looked the cutest!":
                show mc blushside
                m "Well, you looked small and cute."
                m "If I actually managed to get you to grow, I would be happy."
                show button happy
                b "So you're happy now?"
                show mc normalside
                m "..."
                show mc normal
                m "I'm happier."
                show button vhappy
                b "Then I'm happy too."
                $ button_rp += 10
                show button smirk
                if callcutetwice:
                    b "And I got to hear you call me cute TWICE today! That's a win for sure."
                else:
                    b "And you called me cute too. I'm as happy as a shroom on a log!"
                    show mc confused
                    m "Interesting... choice of words..."
                if existential == 1:
                    m "(She got distracted really quickly. That's good.)"
                b "..."
                show button bored
                b "Talking is fun. But also... I'm kinda bored."
                b "Can we do something fun? Like... explore the outside a bit and see the sunset more?"
                b "Because this room is reeeeeeally tiny."
                jump bored
                

                
            "Everything else was already taken.":    
                
                m "Well, everything else was out of stock. You were the only thing still left over."
                show button surprised
                $ button_rp -= 10
                b "Just..."
                show button vsad
                b "...a {i}left over{/i}?"
                "Wow. Are you TRYING to be this bad?"
                show mc stressed
                m "(I'm just being honest! I hate sugar-coating.)"
                
                if existential >= 1:
                    $ existential += 1
                    show button depressed
                    b "My thoughts are being loud again!"
                    show mc confused
                    m "Well, what do they say?"
                    show button vcough
                    b "That I'm going to die soon!"
                    b "I-I'm feeling really panicked! I don't like this! How do I make the thoughts stop?"
                    
                    show mc stressed
                    "This is why your friends hated you. You're just an infectious, miserable disease."
                    
                    m "Calm down. I know something that might help."
                    show button sad
                    b "What is it?"
                    show mc normal
                    m "Let's go outside."
                    m "There's a field I know. It's a nice place... especially at sunset."
                    m "Usually not too busy either. Nice if you want some peace."
                    show mc normalside
                    m "It's my... um... \"calming down\" spot."
                    show button surprised
                    b "That sounds... really nice!"
                    show button happy
                    b "I want to see it!"
                    show mc annoyed
                    m "(Distracted already? I'm jealous how easy it is for you.)"
                    show mc normal
                    m "Fine, let's go. Stay quiet and follow me."
                    show button vvhappy
                    b "As you wish, Master!"
                    show mc vstressed
                    m "Just %(player_name)s, please!"    
                    jump leavehouse
                else:
                    show button sad
                    b "I don't know if it's intentional, but you're kinda hurtful sometimes."
                    "Oh, it's all unintentional. This is just what happens when he's his natural self."
                    show mc stressed
                    m "Sorry, sorry."
                    show button annoyed
                    b "Make it up to me!"
                    show mc confused
                    m "How?"
                    show button bored
                    b "Take me out somewhere! I'm already bored of this biscuit of a room!"
                    jump bored
                    
        label bored:            
            
            show button annoyed
            b "Come on! Aren't you bored in here too?"
            show mc stressed
            "You'd rather be bored, than afraid."
            
            menu:
                "Can you take Button out for a moment?"
                "I can.":
                    "You fear leaving the safe confines of your home, especially with such a conspicious-looking person."
                    "However..."
                    "You have to help her make the most of her short life."
                    "It's always been easier to put the needs of others above your own."
                    "Miraculously, you are able to brush your fears aside today."
                    show mc shout
                    m "UUUUUUUGH- OK!"
                    show mc normal
                    m"Let's just go to this place I know. It's close. Hardly anyone else goes there, so I can handle it."
                    show mc worried
                    m "I just hope no one stares at us..."
                    show button vvhappy
                    b "YAAAAAY!"
                    jump leavehouse
            
                "I can't! I can't! I CAN'T!!!":
                    stop music fadeout(3)
                    show black with fade
                    play music "dynamic_audio/clock.mp3" fadein(2)
                    "In times like this, you tend to imagine how it would all happen:"
                    "You and Button would walk out the door."
                    "People would stare."
                    "The warden would approach."
                    "Who is she? Why didn't you sign her in? How long has she been living here?"
                    "The honest truth would make him chuckle, then he'll ask for the REAL answer."
                    "And you'd freeze to the spot. You already did!"
                    "Are you ready to lie on the spot?"
                    "They'd know you're lying. You'd stumble. You'd panic."
                    "Maybe they wouldn't even allow Button back."
                    "All this, without even making it through the front door."
                    $ sadness = 1
                    $ update_layers()
                    $ start_layers(2)
                    "Everything is overwhelming."
                    stop music fadeout(3)
                    hide black with fade
                    show mc worried
                    m "I can't! What if someone realises what you are!?"
                    m "You're weird! You're conspicious! What if they try to TALK to us!?"
                    show button normal
                    b "No problem, I'm happy to talk."
                    show mc shout
                    m "What will you tell them? You think they'll let you go if you tell them THAT YOU'RE A MUSHROOM!?"
                    show button angry
                    b "I doubt anyone would care anyway! No one would-"
                    show mc vstressed
                    $ sadness = 2
                    $ update_layers()
                    m "BUT WHAT IF THEY DO!? THEY WON'T BELIEVE YOU! EVEN IF WE TELL THEM THE TRUTH! THEY'LL LAUGH!"
                    show button vangry
                    b "Stop interrupting me-"
                    show mc vshout
                    m "WHAT DO YOU KNOW!? YOU'VE JUST BEEN BORN!"
                    show button dgaf
                    b "%(player_name)s-"                    
                    show mc shocked
                    m "{size=+40}I'M NOT GOING OUTSIDE!{size=-40}" with sshake 
                    $ button_rp -= 20
                    show button closedannoyed
                    b "..."
                    show mc vstressed
                    m "..."
                    hide mc with easeoutbottom
                    "Panic drives you into the bed, where you hide your face under the covers."
                    hide button with dissolve
                    play music "dynamic_audio/clock.mp3" fadein(3)
                    "You failed her sole request."
                    "You've disappointed her."

                    show bottle noon:
                        subpixel True 
                        blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
                        linear 1.19 blur 0.97 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.9)*BrightnessMatrix(-0.12)*HueMatrix(0.0) 

                    "You can't help her."  
                    "You can't even help yourself."
                    "What use are you?"
                    "Nobody needs you."

                    "You hold everyone back. You depress them. You can't talk. You can't even fake a smile for them."
    
                    "Huh, is it time for bad thoughts already?"
                    "You feel the bed shift under new weight as Button sits at the foot of your bed."
                    b "%(player_name)s... What's wrong? Why are you so upset all of a sudden?"
                    b "Come on! Let's just talk it out! We can figure this out together."
                    m "I don't want to talk to anyone right now! I just want to be alone."
                    b "..."
                    b "But aren't you're just going to feel worse?"
                    "That's the plan, isn't it? You want to hurt yourself even more."
                    "You want to crash your whole plane down to the ground."
                    b "Can you just tell me what's going on? This feels so unnecessary. I just want to help you...!"
                    b "It's not good for you...At least look at me?"
                    b "Please? We don't have to go out. It's okay..."
                    show black with dissolve:
                        alpha 0.7
                    "Ouch."
                    show black with dissolve:
                        alpha 0.8
                    "So you've made her resign herself to staying here?"
                    show black with dissolve:
                        alpha 0.9
                    "Now you really wanna-"

                    $ sadness = 0
                    $ update_layers(0)
                    stop music
                    play music "dynamic_audio/horror_EerieResonance3.mp3" fadein(0.2)

                    camera:
                        subpixel True
                        #matrixcolor TintMatrix("99311B")
                    show button vcough:
                        subpixel True ypos -300 xpos 282
                        zoom 1.9
                           
                    b "CAN YOU {b}STOP!?{/b}" with sshake
                    b "Stop {sc=1}{color=#000000}whispering{/sc} to yourself about-!"
                    b "{sc=5}{color=#000000}{b}STOP SAYING ALL THAT!!!{/b}{/sc}"  with sshake   
                    scene bottle noon with dissolve:
                        zoom 0.9
                    show mc shocked at right
                    show button sad at left
                    with easeinbottom 
                    b "You hate it if we go, you hate it if we don't!"
                    b "You hate if I try to help - you hate yourself if I don't!"
                    show button cough
                    b "You're impossible! You're just - {sc=4}{color=#000000}URGGHHH!{/color}{/sc}"
                    show button depressed
                    b "I just can't WIN! There's NOTHING I can do!"
                    m "..."
                    show mc worried
                    m "I didn't realise... I was talking outloud..."
                    show button vcough
                    b "And you keep {b}doing it{/b}. All this awful, self-deprecating muttering..."
                    b "..."
                    show button sad
                    b "I'm at my wit's end. I'm not spending the rest of my life like THIS!"
                    b "I just need someone who'll have fun with me and show me the nice things life has to offer."
                    show button vgoodbye
                    b "I thought... it'd be easy, but... maybe it isn't after all."
                    
                    b "So if it isn't for you, I understand. I just need to know."
                    show button sad
                    b "Are you going to be that person, or not?"
                    default O1 = False
                    jump fakechoseychoice
                    

                    label fakechoseychoice:
                        menu:
                            "Can I put my worries aside and have fun with Button?"
                            "Yes."  if O1 == False:
                                $O1 = True
                                show mc stressed
                                m "I-"
                                play music "heartbeat.wav" fadein(3)
                                show black
                                show text "What do you think you're doing?"
                                $ renpy.pause ()
                                show text "You can't salvage this. You can't just \"make it up\" to her."
                                $ renpy.pause ()
                                show text  "Did you see her face?"
                                $ renpy.pause ()
                                show text "She's {sc=2}never{/sc} going to forget this."
                                $ renpy.pause ()
                                hide text with dissolve
                                hide black with dissolve
                                stop music fadeout(2)
                                jump fakechoseychoice
                                

                            "No.":
                                m "I'm sorry."
                                hide mc with easeoutbottom
                                
                                $ button_rp -= 100
                                show button cough
                                b "..."
                                show button goodbye
                                b "I... see..."
                                b "Then..."
                                show button vgoodbye
                                b "Goodbye."
                                window hide

                                hide button
                                with easeoutbottom
                                play sound "door.wav"

                                hide day_1 
                                hide water_status
                                hide existential_status 
                                hide affection 
                                with dissolve

                                scene black with Fade(2, 1.0, 0.5)
                                play music "dynamic_audio/clock.mp3" fadein(3)
                                
                                
                                show text "{sc=1}I'm glad you finally listened to me.{/sc}"
                                $ renpy.pause ()
                                hide text
                                show text "{sc=1}Now it's just you and me, and no one to interfere.{/sc}"
                                $ renpy.pause ()
                                hide text
                                
                                show text "Doesn't it feel so euphoric...? {sc=2}To hurt yourself like this...?{/sc}"
                                $ renpy.pause ()
                                hide text
                                show text "To purposely do things you hate? To deny yourself love? It's because..."
                                $ renpy.pause ()
                                hide text
                                show text "{sc=1}You {color=#E2A0A0}deserve{/color} it.{/sc}"
                                $ renpy.pause ()
                                hide text
                                with dissolve
                               
                                scene black with Fade(0.5, 1.0, 0.5)
                                pause 1
                                stop music fadeout(2)
                                
                                if persistent.end3:
                                    pass
                                else:
                                    $ persistent.end3 = True        
                                
                                "End 3: Spore, unfortunate soul."
                                
                                return
                            


                                
                                
                    
    label leavehouse:    
        hide button
        hide mc
        with easeoutbottom
        window hide
        hide water_status
        hide existential_status
        hide day_1
        hide affection
        with dissolve 
        stop music fadeout(3)
        scene black with Fade(0.5, 1.0, 0.5)        

        play sound "door.wav"
        if existential > 1:     
            play music "depressed_date.mp3"
            
        else:
            play music "happy_date_piano.mp3"
        show chibi_mc at slightright
        show chibi_mushroom at slightleft
        with easeinright
        

        "You and Button leave the dormitory without incident, and stroll down the sidewalk to the nearby field."
        "She stares at EVERYTHING - buildings, sidewalks, recycling bins, cars... she even smiles and waves to passing people! Ugh."
        "It's too obvious. It's embarrassing. You don't talk to her, and you keep an appropriate distance so you could pass off as strangers."
        "Many passerbys compliment her \"cosplay\". She beams back confusedly. You'll have to explain the concept later."
        "You're just grateful nobody talks to {b}YOU{/b}."
        
        
        hide chibi_mc
        hide chibi_mushroom
        with easeoutleft

        scene sunset with Fade(0.5, 1.0, 1)
        
        $ button_date += 1
        "Finally, you arrive at the field. There're only two kids and a dog, playing at the opposite end of the field."
        "As you gaze up at the orange-tinted sky, you feel a hint of peace, but you're also continuously keeping an anxious eye on Button."
        "She watches the children from afar and mimics their play, rolling around on the hills and screaming with delight."
        "Gradually, you're able to relax your worries."
        show button vhappy at left
        show mc normal at right
        with easeinbottom

        b "Come roll with me, %(player_name)s!"
        show mc stressed
        m "Your clothes are going to get dirty."
        show button vvhappy
        b "Then get dirty WITH ME!"
        "She tugs on your hoodie forcibly, and you tumble sideways with her."
        hide button
        hide mc
        with easeoutbottom
        "Yup... You're dirty now, so you may as well join in..."
        "The both of you roll down the hill. Despite your initial dislike of the childish activity, you've got to admit:"
        "It's pretty fun!"
        
        "Then, while you're both lying down catching your breath, the dog you noticed earlier comes over and sniffs Button cautiously."
        
        if existential > 1:
            show button scared at left
            show mc normal at right
            with easeinbottom
            b "{sc=4}{color=#000000}HELP! IT'S EATING ME!!! I DON'T WANT TO DIE YET!"
            show mc confused
            m "Calm down! It's not dangerous, I promise! He just sniffing you."
        else:    
            show button cough at left
            show mc normal at right
            with easeinbottom
            b "Eeeek! It's eating me! {sc=4}{color=#000000}HELP!"
            show mc happy
            m "No, it's just sniffing. Look."
        show mc happy
        "You hold out your hand, and the dog gives it a quick sniff too, before returning to Button."    
        show button sad
        b "What is it...?"
        m "Just a friendly dog. Try pet him."
        show button surprised
        b "Oooh! It's so... fluffy?"
        show button vvhappy
        b "Why's he sniffing so much!? Hehe!"
        show mc annoyed
        m "He's probably not sure what you are... haha."
        
        scene black with Fade(0.5, 1, 0.5)
        "Eventually, the dog's owners call him back and he trots away. You both leave soon after."
        stop music fadeout(3)
        play sound "door.wav"
        scene bottle night with Fade(1, 2.0, 1):
            zoom 0.9
        play music "night.mp3"
        show mc happy at right
        show button vvhappy at left
        with easeinbottom

        $ button_rp+=10
        $ existential -= 1

        show day_1 at topleft
        show water_status at water_location
        show existential_status at existential_location 
        show affection at topright
        with dissolve

        window show
        b "The outside is AMAZING!"
        
        show button vhappy
        b "How often a day do you usually go?"
        show mc annoyed
        m "How often a DAY? Um..."
        show button vvhappy
        b "Ughh, I just wanna go out again!"
        show mc happy
        m "(She looks happier.)"
        if existential >= 1:
            m "(And less depressed. That's good.)"
        m "I'm glad you had a good time..."
        show button happy
        b "What do you wanna do now?"
        show mc normal
        "She STILL wants to do something? Man, can't she just leave already?"
        show mc normalside
        m "Now?... Um, just lie down and recharge, honestly. If that's ok."
        show button normal
        b "You're sleepy?"
        show mc stressed
        m "More like... I need to relax for a while after all the excitement."
        show button smirk
        b "Then let's lie down together! A lil snuggie will help you recharge!"
        show mc blushside
        m "What? Ugh... I told you-"
        show button vhappy
        b "Just as homies! Promise!"
        show mc stressed 
        m "I don't have the energy for this..."
        "But before you can walk away, Button stops you."
        show button normal
        b "Wait..."
        b "There's something I need to ask you."
        show mc normalsquint
        m "What?"
        show button goodbye
        b "You're probably hungry after going out, huh?"
        b "So I wanted to ask... are you planning to eat me tonight?"
        show mc normalside
        menu:
            "Should I eat her now?"
            "I'm hungry...":
                stop music fadeout(3)
                
                "You are feeling pretty hungry after all of that rolling."
                show mc surprised
                m "But... is that really ok with you?"
                if existential >= 1:
                    
                    b "..."
                    show button sad
                    b "I don't know anymore."
                    b "It's kind of scary..."
                    show button goodbye
                    b "Could you... not...? Is that ok?"
                    show mc awed
                    m "Hey, I'm not a psychopath. Of course it's ok."
                    show button vvhappy
                    b "YAAAAAAAY!~" with sshake
                    b "I get to live!"
                    show mc happy
                    m "If you were gonna be THAT relieved, you shouldn't have offered in the first place."
                    show button vhappy
                    b "Ahh... now I can look forward to going out more and seeing everything outside! There's so much! I can't wait!"
                    show mc normal
                    m "Whoa whoa whoa... We never discussed this."
                    show mc normalsquint
                    m "I'm exhausted from today."
                    m "I'd prefer if you could just... take yourself out so I could rest tomorrow."
                    show button surprised
                    b "But... didn't you like it?"
                    show mc awed
                    m "I did. But still. Tiring."
                    show button pout
                    b "But..."
                    b "It's... lonely..."
                    show mc normalsquint
                    m "Can't you just TRY it first before deciding how you're going to feel?"
                    show button closedannoyed
                    $ button_rp -= 10
                    b "..."
                    show button annoyed
                    b "You raised me. You're supposed to take care of me!"
                    b "I can't just go out there on my own! I need you!"
                    show mc vannoyed
                    m "What about MY needs? Aren't you being too forceful? I think you can do something as simple as walk around by yourself."
                    show button surprised
                    b "..."
                    show button sad
                    b "Oh."
                    b "I {i}am{/i} being needy."
                    show button vsad
                    show mc awed
                    b "I'm sorry."
                    b "I'm just scared to be alone...."
                    b "I'm sorry for... being bad at this."
                    show mc stressed
                    "Wow. She's about to cry."
                    
                    

                else:
                    show button happy
                    b "Yup! I'm ready anytime you want to eat me!"
                    show button smirk
                    b "I'm delicious AND nutritious!"
                    show mc sad
                    m "...You sure?"
                    show button vhappy
                    b "Yup... It's part of life. I'm already so lucky to have been able to spend a day with you, so-"
                    b "Please, go ahead!"
                    show mc stressed
                    m "Hah... Well... Ok."
                    show mc happy
                    m "Thanks for the fun day."
                    stop music fadeout(3) 
                    scene black with Fade(0.5, 1, 0.5)
                    play music "sizzle.wav"
                    "..."
                    m "I'm really doing it."
                    m "Frying up bits of seasoned mushroom with egg, tomato and cheese."
                    m "Once it's diced up, you really can't tell it used to be her face."                    
                    m "Isn't this messed up?"
                    m "Maybe so, but..."
                    stop music fadeout(3)
                    window hide
                    show omelette at truecenter:
                        zoom 2
                    with dissolve
                    pause 0.5
                    window show 
                    m "She wasn't lying! This is freaking delicious!"
                    
                    if persistent.end4:
                        pass
                    else:
                        $ persistent.end4 = True    
                    "End 4: Fast food."
                    return
            "No.":
                show mc normal
                m "Honestly? I don't feel that hungry..."
                show button vvhappy
                b "Another day of life for me! Yay!"
                b "Does this mean we can go somewhere else tomorrow? Please please please?"
                show mc normalside
                m "Ahhh..."
                show mc normalsquint
                m "Can't you just go by yourself?"
                show button angry
                b "What? Where's the fun in that? I need my companion with me to protect me and play with me!"
                show mc annoyed
                m "Ah. I see..."
                show button pout
                b "Please please please come with me? I don't wanna get lonely..."
                show mc awed
                m "...Wow, those are some puppy eyes..."
        show mc stressed        
        m "Ah, fine! I've done it once already, so it should be ok..."
        show button surprised
        b "Really? Thank you. You sure?"
        show button happy
        b "You promise you can go out with me?"    
        show mc normalside  
        m "It's just a few days anyway..."
        
        if existential >= 1:
            show button normal
            b "..."
            b "Yeah."
            show mc confused
            show button sad
            b "It's already night time. My first day is already over."
            b "I didn't realise how quickly time would pass."
            show button cough
            b "I understand what you meant earlier now."
            b "Even if I have fun, even if I don't, it doesn't matter in the end. It's getting closer!"

            show mc worried
            m "I'm... I'm so sorry for saying all that."
            show button vsad
            b "..."
            b "I..."
            show mc shocked
            
            show button vcough
            stop music fadeout 1
            b "{size=+20}{sc=2}{color=#000000}I don't want to die!{/sc}{size=-20}" with sshake
            b "I've only just been {sc=2}{color=#000000}born!{/sc} Why can't I live longer like you!?"
            show button scared
            b "{sc=2}{color=#000000}IT'S NOT FAIR! I DON'T WANT TO DIE YET!!!{/sc}" with sshake
            
            "Are you just going to just sit there and watch her have a panic attack?"
            window hide

            hide button
            hide mc
            with dissolve
            play music "date_musicbox.mp3" fadein(3)
            show crying with dissolve
            m "I-I've got you. Just-"
            b "{sc=2}{color=#000000}NOTHING MATTERS! I CAN'T-"
            m "It's going to be ok-"
            b "{sc=2}{color=#000000}IT'S NOT!"
            
            b "{sc=2}{color=#000000}I'VE ONLY GOT TWO DAYS LEFT!"
            b "{sc=2}{color=#000000}I DON'T WANT TO DISAPPEAR! PLEASE HELP ME!"
            m "Ok... First calm down."
            b "{sc=2}{color=#000000}BUT I CAN'T! IT'S GETTING CLOSER!"
            m "Let's breathe together, ok? Just breathe in deeply when I say go, and hold it for eight seconds."
            m "Go. Inhale and hold~"
            show crying_calmer with dissolve
            b "{sc=1}{color=#000000}..."

            "One{w=1.0}{nw}"
            "Two{w=1.0}{nw}"
            "Three{w=1.0}{nw}"
            "Four{w=1.0}{nw}"
            "Five{w=1.0}{nw}"
            "Six{w=1.0}{nw}"
            m "And exhale~ phew"
            "Your perception of eight seconds is lacking, but ok..."
            b "{sc=1}{color=#000000}Pheeeeew~"
            m "Once more-"
            b "Shhh... I think I can hear your heartbeat."
            m "Uh... is that good?"
            b "It's nice... I want to listen to it more."
            m "Well, fine, I guess? You have my permission to listen."
            b "..."

            b "%(player_name)s, why do you get to have more time than me?"
            m "No one gets to choose how long they have."
            m "Who knows? I could even die tomorrow before you do. Car crash. Aneurysm. Bomb. Poisoning..."
            m "You at least won the miracle of getting any life at all."
            m "Many animals don't even get as far as birth. They can die in the womb. Some die soon after from starvation or stress."
            m "It could have been you. Like if I'd screwed up on watering you daily, you wouldn't even get the chance to be here."  
            m "So I'd say you're pretty lucky. You have a safe home, and a... um, person who cares for you."
            m "You get to enjoy your life and do whatever you want."
            b "It's hard to feel very lucky right now."
            m "Who knows if death is really the end? It could be the extension of the adventure. Maybe you'll get reincarnated."
            m "It might actually be a good thing that you're a mushroom. You're so different, we don't even know if our death is the same as yours."
            b "But you don't know."
            m "Well, yeah. No one knows."
            b "So nothing is solved."
            m "Button, I can't SOLVE the mystery of what happens after we die."
            m "But I can reassure you that you'll have a life worth dying for. Isn't that the important part?"
            b "...Yeah."
            m "Do you regret today? Going out?"
            b "No."
            m "Do you think you'd enjoy doing it again tomorrow?"
            b "Probably."
            m "Well then..."
            m "That's what we'll do. We'll do lots of things together. Anything and everything you want."
            show crying_calm with dissolve
            b "Thank you... %(player_name)s."
            show happy_hug with dissolve
            m "Of course."
            m "Is there anything you still want to do today before I sleep?"
            b "...Hmm."
            b "You won't want to do it, but..."
            b "I want to..."
            b "I still want to snuggle with you."
            m "Oh..."
            b "I won't do anything weird. I promise. You can fall asleep. Just let me lie next to you..."
            hide happy_hug
            hide crying_calm
            with dissolve
            b "So I'm not... alone."
            b "Please?"
            "At the sound of impending tears, you immediately agree."
            m "It's ok. We can lie down together if it'll help."
            show crying_calm with dissolve
            b "It will. Thank you."
            window hide
            
            scene black with fade
            "You lie down awkwardly in your bed, facing straight up. Button lies down right next to you, then looks at you."
            b "Sorry about this."
            m "No, it's ok. Is this fine with you?"
            b "Could we...  hug?"
            "Well... you can't refuse after what she just went through."
            "So you turn to her, open your arms, and Button scoots right into them, placing her head on your arm."
            "You can feel her body move within you arms as she breathes. True to her word, she doesn't do anything but lie there quietly."
            "You have a suspicion she's listening to your heart. Well, if it helps..."
            "Wait a second... Do mushrooms breathe? WHY!?"
            "As you ponder the oddity of the specimen in your arms, you feel Button's breathing slow, and any residual shaking... calm down."
            "You start to relax too..."
            "You're glad she's feeling better."
            stop music fadeout(3)
            "She'll probably forget all about this tomorrow..."
            $ button_day += 1
            $ watered = False
            show chibi_sleep at truecenter with dissolve
            show top_text "With Button in your arms, you don't even realise it, but you've fallen asleep..." with dissolve 
            pause 3
            jump day_2

        
            
        show button vvhappy
        b "{sc=4}{color=#000000}YAAAAY! MORE DOGS FOR ME!"
        show mc happy
        m "Hah. Now I want to show you some animal videos."
        hide mc with easeoutbottom
        show button happy
        b "Wait for me~!"
        hide button
        with easeoutbottom
        $ button_rp += 10
        "You spend the rest of the night watching some funny animal videos from your laptop on your bed. All over the sheets and at an appropriate distance of course."
        "Button's reactions make you laugh harder than the videos."
        "It's really nice, just talking with her about something as trivial as animals."
        "You're able to give her a lot of facts, using your existing knowledge and some help from the internet."
        "She actually listens and seems interested in what you say. It feels really good to contribute substantially to a conversation for once!"
        
        window hide
        stop music fadeout(3)
        scene black with fade
        
        $ button_day += 1
        $ watered = False
        show chibi_sleep at truecenter with dissolve
        show top_text "At some point, without realising it, your eyes drift closed..." with dissolve 
        pause 3
        jump day_2


    label day_2:    
        scene bottle day with Fade(1, 2.0, 1):
            zoom 0.9
        #play music "normal.mp3"
        show day_2 at topleft with dissolve
        show mc stressed at right with easeinbottom

        "You wake up."
        "That's it?"
        "Strangely, there's none of your usual existential dread this morning!"
        
        show mc normal
        "And as you open your eyes-"
        play music "normal.mp3" fadein(3)
        show button happy at left with easeinbottom
        show mc shocked
        m "{sc=4}{color=#000000}BUTTON!?"
        if existential >= 1:
            show button vgoodbye
            b "You're awake! Hi..."
            "So it was real. Disappointing. It looks like you're in for another hard day."
            show mc confused
            m "Hi... How are you doing?"
            show button goodbye
            b "Much better!"
            show button vgoodbye
            b "Mostly..."
            b "I'm just glad I'm not alone."
            show mc awed
            m "No problem. Whenever you need another hug, I'm here for you."
            show button normal
            b "Are you ok? I'm sorry if I ruined your night with all of that."
            show mc stressed
            m "No, no, it just... kinda felt weird. Unreal. Like I'd wake up at any minute. But you're here, haha..."
            show button surprised
            b "Oh... Sorry."
            show button goodbye
            b "Does that mean... you don't want to go out today anymore?"
            show mc sad
            m "No... no... we can."
            show button vhappy
            b "Really!?"
            show mc annoyed
            m "Of course. I wouldn't break a promise I made for you."
            show button happy
            b "Thank you!"
            b "Will you-"
            show button normal
            b "-Nevermind. I shouldn't be so clingy. You've got other things to do."
            $ watered = 0
            show water_status at topright with dissolve
            pause 1
            play sound "spray.wav"
            $ watered = 1
            pause 1
            hide water_status with dissolve
            show mc surprised
            m "Oh. You can water yourself? That's... convenient."
            show button bored
            b "Yeah..."
            show button normal
            b "Can we go now?"
            show mc normal
            m "Yup."
            show button happy
            b "Do you think we'll see another dog today?"
            show mc happy
            m "I'll make sure you do. We're going somewhere even better than yesterday."
            show button vvhappy
            b "Eeek! Now I'm actually getting excited!"
            jump park

        else:    
            show button vvhappy
            b "Good mooooorning, %(player_name)s!"
            m "It wasn't a dream!?"
            show button vhappy
            b "Luckily for you and me! Now we can have another amazing day!"
            show mc surprised
            m "I'm honestly just shocked. I think at some point, I just... went with the flow of things, thinking I'd wake up from it all."
            show button surprised
            b "Oh! I wanted to ask-"
            show mc vshout
            m "{sc=4}{color=#000000}WHAT ARE YOU DOING IN MY BED!?"
            show button cough
            b "Eeeek~! I'm sorry! I'm sorry! Just don't shout at me!"
            hide button with easeoutbottom
            show mc stressed
            m "Sorry for shouting, but you CANNOT be in my bed right now!"
            show mc vstressed
            m "Ah."
            m "Don't tell me you slept in here last night..."
            show button normal at left with easeinbottom
            b "I don't sleep."
            show button vvhappy
            b "But I DID cuddle you all night long!"
            show mc vblushside
            m "Oh my god."
            show button pout
            b "%(player_name)s... can you water me now? I'm so thirsty!"
            show mc annoyed
            m "Hah. You really are."
        
        window hide
        hide mc with easeoutbottom
        $ watered = 0
        show water_status at topright with dissolve
        call screen water_3
        
        screen water_3:
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
                action Jump("day1_watered_3")

        label day1_watered_3:
            play sound "spray.wav"
            $ watered = 1
            pause 1
            queue sound "spray.wav"
            $ watered = 2
            show mc normal at right with easeinbottom
            show button vvhappy 
            window show
        b "Ahhh, I love morning showers!"    
        show button vhappy
        hide water_status with dissolve
        b "Ok, I'm ready to go find more doggies!"    
        show mc stressed
        "At the mention of going out, a familiar fear weighs down on you."
        m "Uuugh... about that..."
        show button angry
        b "You're NOT backing out now! You PROMISED me!"
        b "I've been waiting all night, so we're going out!"
        show button annoyed
        b "And you can't take it back."
        show mc normalsquint
        m "...(I really don't want to.)"
        show button vangry
        b "..."
        show mc surprised
        m "Geez! Ok ok!"
        show button happy
        b "Yay! Let's goooo!"
        show mc normalside
        m "You make some scary expressions. Damn."
        jump park

    label park:
        hide button
        hide mc
        with easeoutbottom
        hide water_status
        hide existential_status
        hide affection
        hide day_2
        with dissolve 
        window hide 
        stop music fadeout(3)
        scene black with fade
        play sound "door.wav"
        if existential >= 1:
            play music "depressed_date.mp3"
    
        else:
            play music "happy_date_recorder.mp3"
        show chibi_mc at slightright
        show chibi_mushroom at slightleft
        with easeinright
        if existential >= 1:
            "And so, trying to keep Button as happy as you can, you push aside your selfish desire to stay home."
        else:
            "And so, Button intimidates you into keeping your promises."
        "You lead Button down the sidewalk to the nearby park."
        "It's a little busier than yesterday since it's the middle of the day."
        "You can't stand the attention that Button's outfit is gathering. {sc=3}{color=#000000}The Stares!{/sc}"
        "Focusing on breathing steadily, you shut out everything other than the way to the park..."
        if existential >= 1:
            "...while Button walks quietly beside you."
        else:
            "...while Button skips happily along."

        hide chibi_mc
        hide chibi_mushroom
        with easeoutleft

        scene park with fade
        
        $ button_date += 1
        "Finally, you arrive at the park."
        "You immediately sit down at a bench, while Button investigates the playground, intrigued by the slide and swing."
        "You feel anxious as you watch her try to play there, despite being a fully-grown adult."
        "She's soon caught the attention of two kids on the slide, one of whom starts asking her what exactly she's supposed to be."
        #show button vvhappy at left with easeinbottom
        if existential >= 1:
            b "..."
            b "I don't... know."
            b "Can I play with you? Please? I'm sorry. I don't know how it works..."
        else:
            b "I'm a mushroom! My full name is Agaricus bisporus, but apparently it's a bad name, so you can just call me Button!"
            "You can hear her all the way from here."
            #show mc vstressed at right with easeinbottom
            m "(Is it ok for me to just let her proclaim her existence?)"
            m "(Ugh, but I don't want to get up from here... I'll just wait it out.)"
        "The kids think she's weird and ignore her. Soon after Button walks back dejectedly to the bench."
        if existential >= 1:
            show button dgafdown at left 
            show mc normal at right
            with easeinbottom
            "Silently, she sits down next to me."
            show mc confused
            m "You ok?"
            show button dgafdownsad
            b "... I don't know."
            b "There's no point. No one cares about me."
            show mc surprised
            m "Hey, where's this coming from? Is it because of the children?"
            show button dgafdown
            b "I don't know."
            "You know the sting of rejection firsthand. Weren't you supposed to be cheering her up?"
            show mc awed
            m "Do you want me to play with you? The swing's free..."
            b "..."
            show mc cute
            m "Come! Let's go!"
            hide mc
            hide button
            with easeoutbottom
            "You take Button's hand and lead her to the swing. She follows without resistance."
            m "Sit down and hold the chains while I'll push you."
            "Button obeys. You stand behind her and push her."
            "Her mood instantly lifts."
            b "Ah! It's...! It's kind of scary, but fun!"
            m "Straighten your legs when you're at the top to go faster!"
            "Thank God she's smiling..."
        else:
            show button sad at left
            show mc normal at right
            with easeinbottom
            b "%(player_name)s... no one wants to play with me... and there are no dogs here!"
            show mc annoyed
            m "You can't force anyone to play with you. They're just kids."
            m "And just have some patience. A dog will probably show up sooner or later."
            b "Can you play with me on the swings?"
            show mc normalside
            m "I'm too old for it."
            show button pout
            b "Pleeeeeease!? Just a little bit?"
            "She starts to pull you along against your will. You're incredibly tense with all the eyes around you, and you snatch your arm away."
            show mc shout
            m "I can't, ok!? It's too... public."
            show button annoyed
            b "Who {b}cares{/b} what anyone else thinks?"
            show mc stressed
            m "(I DO!)"
            "The thought makes you pause. Shame creeps in."
            "She's right, after all."
            show mc normal
            m "Fuck it. Fine."
            hide mc with easeoutbottom
            show button vvhappy
            b "Yay! Thank you!"
            hide button with easeoutbottom
            #scene black with fade
            "For a few minutes, you push her on the swing."
            "Eventually she gets the hang of it and can sustain her momentum."

       
            

        "However, as you're watching her, a sudden wave of dizziness hits you."
        show mc sad at right with easeinbottom
        m "Oh... I've just realised... I don't think I've eaten for days."
        if existential >= 1:
            show button surprised at left with easeinbottom
            b "Oh. Will you be ok?"
            show mc stressed
            m "Yeah, I just... need to sit down for a second..."
            show button normal
            b "..."
            show button dgafside
            b "We can go home if you want... I've already played on the swing... and there aren't any dogs here either."
            "That sounds much better than this stupid adventure. Your nausea is quickly growing worse."
            show mc worried            
            m "No... I shouldn't have neglected myself. We can come back after-"
            show button vgoodbye
            b "No, really, it's fine. I don't want to come back here."
            hide button
            with easeoutbottom
            "She leaves without waiting for your resistance."
            show mc sad
            m "I'm sorry..."
            hide mc with easeoutbottom
            scene black with Fade(0.5, 1, 0.5)
            stop music fadeout(3)
            "Battling nausea and guilt, you and Button silently walk home. Incompetent piece of shit."      
            $ button_rp -= 10
            $ existential += 1

            jump returnhome





        else:    
            show button smirk at left with easeinbottom
            b "Wanna bite me? I can survive without an arm."
            show mc stressed
        m "No... I'm... I gotta sit down."
        if existential >= 1:
            show button sad
            b "Don't worry! I'll help you!"
        else:    
            show button happy
            b "Worry not! Button has located sustenance!"
        hide button with easeoutright
        if existential >=1:
            "Button sprints over to the nearby hotdog stand and talks urgently to the lady working there."
        else:
            "Button sprints over to the nearby hotdog stand and begins chatting to the lady working there."
        show mc shocked at flip with dissolve
        m "No no! You need money!"
        hide mc with easeoutright
        "You go running wobbily after her."
        "But the situation isn't as embarrassing as you'd worried. Button and the woman are exchanging smiles when you arrive."
        na "I heard you're not feeling that great. Don't worry, it's on the house."
        "She promptly hands you a fresh hotdog."
        na "Hope this helps."
        "You thank her profusely and make your way back to the bench."
        show mc confused at right with easeinbottom
        m "How did you do that? How do you just..."
        show button normal at left with easeinbottom
        b "I just told her you were dizzy and hadn't eaten in a long time."
        b "And then she took a loooong look at you and said you \"certainly looked sick!\"."
        if existential >=1:
            show button sad
            b "..."
            show button goodbye
            b "Will you be ok?"
        else:    
            show button happy
            b "Did I do well? I got you food!"
        show mc happy
        m "Yeah. Thanks, Button."
        show mc sad
        m "You make everything look so... easy."
        if existential >=1:
            show button vgoodbye
            b "You were in trouble. There was no time to be afraid."
            m "It wasn't that urgent, but thank you."
        "You bite into a fresh, steaming hotdog."
        show mc happy
        "Starvation is the best seasoning: It's the best hotdog you've ever eaten!"
        show button sad
        "However, Button stares at it with pain etched across her face."
        show mc confused
        m "What? Want a bite?"
        show button goodbye
        b "Hahaha... no... I really couldn't."
        show button vsad
        b "But... why? Why kill something so cute, so innocently adorable?"
        b "It's awful..."
        show mc normal
        m "Are you talking about yourself? I don't have to-"
        show button closedannoyed
        b "No!"
        if existential <= 0:
            b "You know I want you to eat me!"
        show button angry
        b "I mean the dogs! The one YOU'RE EATING RIGHT NOW!"
        m "..."
        show mc surprised
        m "Oh."
        show mc happy
        m "No, no, they're not actually made of dogs. We just call them that."
        show button annoyed
        b "Don't lie to me..."
        show mc vannoyed
        m "And don't accuse me of lying."
        b "Then what are they?"
        show mc normalside
        m "Uh... not sure. Probably pork. Or beef."
        show button normal
        b "Oh. Is pork-or-beef an animal too?"
        show mc happy
        m "Those are two separate things. They're animals, yes. We've domesticated them for our food."
        show mc normalsquint
        m "Even so, how they're treated is still unethical in my opinion..."
        show button bored
        b "I'm kinda lost."
        show button vvhappy
        b "But if it's not a dog, it's ok!"
        $ button_rp += 10
        scene black with Fade(0.5, 1, 0.5)
        "You feel a bit better after eating something, and Button leaves to go play with a dalmatian that just entered the park."
        "You read a comic on your phone, enjoying the sunlight and the sounds of play, until Button tells you she's ready to go home."
        stop music fadeout(2)
        jump returnhome    


    label returnhome:
        play sound "door.wav"
        scene bottle noon with Fade(1, 2.0, 1):
            zoom 0.9
        show day_2 at topleft 
        show affection at topright
        show existential_status at existential_location
        with dissolve
        play music "night.mp3" fadein(3)
        
        if existential >= 1:
            show mc stressed at right
            show button dgafdown at left
            with easeinbottom
            "As soon as you enter the room, you head over to your desk and take out a boxcutter from your drawer..."
            "...and open up a new box of ramen noodles from under your bed. You take out three packages and toss the boxcutter to your desk."
            show mc sad
            m "I'm going to cook some ramen in the kitchenette quick. Be right back."
            hide mc with easeoutbottom
            b "Mm."
            "..."
            show button dgafdown at center with move
            show button dgafdownsad
            b "*sigh* {size=-10}I hate this...{size=+10}"
            show button closedannoyed
            b "No! I have to stop this! I can't worry %(player_name)s so much... He's already doing so much for me..."
            show button vsad
            b "Just... be happy!"
            show button vvhappy
            b "Smile! Everything is ok! The outside is beautiful! %(player_name)s cares about you!"
            b "You don't need to have meaning! It doesn't matter if you're never going to live again! You can just..."
            b "..."
            show button dgafdown
            b "...die tomorrow..."
            b "I wonder if it's going to hurt..."
            show button dgafdownsad 
            
            b "Why can't I just be happy?"
            "Button stands tensely in the centre of the room while she waits."
            "..."
            "An odd compulsion overcomes her."
            show button closedannoyed
            b "Argh!"
            play sound "slap.ogg"
            "She slaps herself in the face. It doesn't hurt."
            stop sound
            show button cough
            b "Why!?"
            show button sad
            b "Why!?"
            b "I don't want to do this anymore! I don't want tomorrow to come!"
            show button depressed
            "She stares at the desk."
            play sound "<from 0 to 2>tear.wav" 
            "Her nails dig into her arms."
            show button vcough
            b "Aaaaaaaaahh~ Hah~ Hah~"
            "Without you nearby, it's harder to ignore the thoughts in her head."
            show button scared
            b "{size=-10}I hate it! I hate it! Please come back!{size=+10}"
            show button vcough
            b "{size=-10}Please...{size=+10}"



            play sound "door.wav"
            show mc sad at right with easeinbottom
            show button happy at left with move
            m "Back... Sorry for the wait. I had to figure out if I still had to cook it for 3 minutes or 9 if I put them all in at once, but-"
            show mc stressed
            m "Sorry, ignore my stupid excuses."
            show mc confused
            m "Are you ok?"
            show button vvhappy
            
            
       
            show existential_status:
                subpixel True 
                xpos 0.88 
                pause 0.05 xpos 0.8803 
                pause 0.05 xpos 0.8801 
                pause 0.05 xpos 0.8802 
                repeat
            
           


            b "Yes!"
            show mc normalside
            m "I'm really sorry about earlier. I feel so bad."
            show button vhappy

            show existential_status:
                subpixel True 
                xpos 0.88 
                pause 0.05 xpos 0.8802 
                pause 0.05 ypos 0.0001
                pause 0.05 xpos 0.8804
                pause 0.05 ypos 0.0
                repeat

            b "It's ok!"
            show mc happy
            m "Ah, well... It's nice to see you smiling at least."             
            m "Um, I'm gonna eat now. How about we watch something together?"
            b "Ok!"
            hide mc
            hide button
            with easeoutbottom
            "You and {cps=20}Button...{/cps}"
            show black
            pause 0.1
            hide black            
            
            show existential_status:
                subpixel True 
                parallel:
                    xpos 0.88 
                    pause 0.06 xpos 0.87 
                    pause 0.02 xpos 0.9 
                    pause 0.07 xpos 0.88 
                    pause 0.07 xpos 0.87 
                parallel:
                    ypos 0 
                    pause 0.08 ypos 22 
                    pause 0.07 ypos -23 
                    pause 0.07 ypos 47 
                xpos 0.88 
                ypos 0





            "You and %(player_name)s watch... \"something\". You're not really sure. Does it matter?"
            "Time... just... passes..."
            
        
            show bottle noon:
                subpixel True 
                matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
                linear 10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.94)*BrightnessMatrix(-0.21)*HueMatrix(-48.0) 
         
            


            "{cps=20}On... and on...{/cps}"

            "The skies darken."
            "Whispers of dread creep up on you."
            "But it'll be ok."
            "Just keep that smile plastered on your face. Laugh when you should."
            "Even though you're feeling worse and worse."
            "At least %(player_name)s is by your side. As long as he thinks you're ok, he'll be happy."
            "He doesn't like you when you're sad. He wouldn't want to be your friend anymore."
            "And you'd be alone."
            window hide
            
            scene bottle night with Dissolve(2):
                zoom 0.9
            show mc confused at right 
            show button vdgaf at left
            with easeinbottom 
            m "Um... you ok?"
                      
            show button surprised at left with easeinbottom
            
            b "Huh?"
            show button vvhappy
            b "YES! I'M OK!"
            show mc normal
            m "Okay... You had a weird look on, so I... nevermind."
            show mc normalside
            m "So I was wondering..."
            show mc happy
            m "I'd like to make it up to you."
            show button happy
            show mc cute
            m "Is there anything in particular you'd like to do?"
            m "Anything at all... I'll try make it happen."
            default O2 = False
            default O3 = False
            jump choosedo





            label choosedo:    
                menu:
                    "Anything I want to do?"
                    "Die." if O2 == False:
                        
                        $O2 = True            
                        show button happy
                        b "..."
                        show mc confused
                        m "Button?"
                        show button surprised
                        b "Oh!"
                        show button goodbye
                        b "Ah, sorry, I was just thinking!"
                        show button happy
                        b "No, I'm good, thanks!"
                        show mc annoyed
                        m "Sorry, I can't accept that. Take your time and just tell me!"
                        show button dgafside
                        b "(But there's no point. There's nothing I want.)"
                        jump choosedo
                    "Hug.":
                        show button vhappy
                        b "A hug!"
                        show mc surprised
                        m "Just that?"
                        show button vvhappy
                        b "Yup!"
                        show mc happy
                        m "I can do that."
                        hide mc
                        hide button
                        show crying_depressed
                        with dissolve
                        m "How's this?"
                        b "Good."
                        m "Same. I love hugs."
                        m "It's really relaxing."
                        m "It's actually because of a hormone called \"oxytoxin\". It reduces stress and anxiety."
                        b "..."
                        $ button_rp -= 10
                        "It's not about about you."
                        "You're replacable. He's just going to order another one when you die. Does he even care?"
                        "Or are you just pressuring him to care, with your anxieties and tears?"
                        "He didn't want you from the start. He said it himself. Why are you deluding yourself?"
                        "Why are you believing him? When you know he's just doing it because he feels bad?"
                        "Really... no one cares about you."                    
                        m "But even without that, it's also nice to just... bond with you."
                        m "So, whenever you want a hug, I'll be here... just ask."
                        b "...Sure."
                        hide crying_depressed with dissolve

                show mc happy at right
                show button happy at left
                with easeinbottom

                m "I know we didn't do much today, but I promise I'll take you out somewhere awesome tomorrow!"
                m "We'll do anything you want!"
                show button vhappy
                b "Thank you! I look forward to it!"
                $ watered = 0
                show water_status at topright with dissolve
                show mc confused
                m "By the way... aren't you thirsty? I thought you were supposed to be watered twice a day..."
                "Thirst is about the only thing that gives you pain. Are you sure you want to give it up?"
                show button happy
                b "I'm good!"
                show mc happy
                m "You know yourself better than I do, so ok."
                show mc cute
                m "And thanks for watching those videos with me earlier, it was really fun to share some of my favourites."
                "You don't know what it is you watched. You just remember %(player_name)s laughing."
                show button vhappy
                b "Yeah, it was really funny!"
                show mc annoyed
                m "Well, I'm gonna lie down now, but I bet you're going to want to cuddle again."
                show button vgoodbye
                b "No, I'm ok."
                show mc confused
                m "Uh... unexpected. What are you going to do?"
                show button happy
                b "Hmm... not sure! Maybe I'll look around. Maybe I'll... think."
                show mc normal
                m "Ok..."
                show mc awed
                m "If you change your mind-"
                show button vvhappy
                b "Mhm, thanks, goodnight!"
                show mc annoyed
                m "Alright, night. See you in the morning."
                window hide
                hide mc
                hide button
                with easeoutbottom

                scene black with fade
                $ existential += 1

                stop music fadeout(3)
                show chibi_sleep at truecenter with dissolve
                show top_text "You wait until he falls asleep..." with dissolve 
                pause 3
                
                play music "dynamic_audio/clock.mp3" fadein(3) volume 0.65  
                scene bottle day with Fade(1, 3.0, 1):
                    zoom 0.9
                show day_3 at topleft
                show affection_depressed at topright
                show existential_status at existential_location
                show water_status at water_location
                with dissolve

                show mc stressed with easeinbottom
                m "Mmm..."
                show mc normal
                m "Button?"
                show mc shocked
                m "BUTTON!"
                
                $ sadness = 1
                $ start_layers(5)
                $ update_layers()

                transform fogfade:
                    alpha 0
                    ease 3 alpha 1
                transform emofade:
                    alpha 0
                    ease 5 alpha 1    
                transform pulse:
                    ease 2 alpha 0
                    ease 2 alpha 1    
                    repeat



                
                window hide
                scene depression_manicalsmile with fade:
                    subpixel True 
                    xalign 0.5
                    yalign 1.0
                    zoom 2.36 
                    linear 6 zoom 2.3 
                    linear 6 zoom 2.36
                    repeat
                


                m "{sc=3}{color=#000000}Oh my God!"
                m "What happened!?" with sshake
                b "..."
                b "It didn't even... {i}hurt{/i}."
                m "I'm... I'm so sorry. I should have realised..."
                m "I thought you were doing better... I thought you said you were looking forward to today... so I just ignored my worries..."
                m "But you're obviously not ok!"
                window hide
                $ kill_late = False

                

                show depression_manicalsmile:
                    subpixel True zoom 1.32 xanchor 0 yanchor 0
                    pos (-296, -331) 


                


                show fog_base
                with Dissolve(2)
                b "Yeah. I'm not."
                b "I'm not ok."
                b "I'm just broken now."
                m "Don't say that! You're just... it'll be okay..."
                b "Liar."
                b "Ahh..."
                b "I want to leave... disappear... whatever."
                b "You can eat me now, %(player_name)s. Like you wanted."
                m "You're not in the right mind to be making a decision like that..."
                #m "What the hell are you SAYING!? Button! You're NOT in the right mind to be making a decision like this!"
                m "And your arm... why...?"
                b "..."
                m "I'm so sorry."
                m "Let's just forget this and go out and do something! Or a therapist could-"
                "She shows you the boxcutter. It has bits of mushroom flesh stuck to it."
                m "Oh my God! What? No! I'm not taking that!"
                b "Hah, you don't know what it's like... feeling your body and mind start to shrivel."
                m "You're... hurting?"
                b "Mm, yeah."
                b "Now, I can feel death {sc=1}{color=#000000}closing{/sc} in on me. Hour by hour."
                b "Can you imagine that?"
                b "I can't just pretend I'm happy anymore."
                "She laughs softly to herself."
                $ sadness = 2
                $ update_layers()
                scene depression_manicalsmile
                show fog_base
                show fog_1
                with Dissolve(2)
                b "I've ruined myself already. I may as well die."
                m "Button, I know what you're going through. I can help you get better! Let's just hug and-"
                scene depression_annoyed
                show fog_base
                show fog_1
                b "I hate your hugs."
                m "..."
                b "..."
                
                scene depression_annoyed2
                show fog_base
                show fog_1
                b "I'm sorry."
                b "I've become... a bad person."
                m "No, you're not! It's ok. I'll forgive a few angry words."
                m "But in return, can you please try calm down with me? I promise it'll help."
                b "%(player_name)s..."
                b "I know you mean well, but it's too late for me."
                b "I'm fine if I go now."
                b "You know I'm right. We're out of time. And, as my last request..."
                b "..."
                b "... I'm too scared to do it myself."
                b "Could you help me?"
                b "Please?"
                call screen choice1 with dissolve
                
                screen choice1:
                    imagebutton:
                        xalign 0.15 yalign 0.5
                        idle "choicebox1_animated_idle"
                        hover "choicebox1_animated_hover"
                        action Jump("killher") 
                    text "\"Help\" her." at transform:
                        align (0.21, 0.5)
                    imagebutton:
                        xalign 0.85 yalign 0.5
                        idle "choicebox2_animated_idle"
                        hover "choicebox2_animated_hover"
                        action Jump("no1")
                    text "Refuse." at transform:
                        align (0.75, 0.5)    

                label no1:
                    m "No."
                    m "You still have time left, even if it's just a little. You can't ask me to cut that short."
                    m "Because... there's still a possibility you can be happy again!"
                    $ sadness = 3
                    $ update_layers()
                    scene depression_sad
                    show fog_base
                    show fog_1
                    with Dissolve(2)
                    b "It's hopeless."
                    b "Happiness doesn't want me back."
                    
                    b "I just... want to die."
                    b "It's my only escape."
                    call screen choice2 with dissolve
                
                screen choice2:
                    imagebutton:
                        xalign 0.15 yalign 0.5
                        idle "choicebox1_animated_idle"
                        hover "choicebox1_animated_hover"
                        action Jump("killher")
                    text "Help her." at transform:
                        align (0.21, 0.5)
                    imagebutton:
                        xalign 0.85 yalign 0.5
                        idle "choicebox2_animated_idle"
                        hover "choicebox2_animated_hover"
                        action Jump("no2")
                    text "Refuse!" at transform:
                        align (0.75, 0.5)    

                label no2:
                    m "Button, I... I know what you're going through. Trust me."
                    m "I know what it's like to do something to yourself and regret it."
                    m "But it gets better. I promise you. Please?"
                    $ sadness = 4
                    $ update_layers()
                    scene depression_vsad
                    show fog_base
                    show fog_1
                    show fog_2
                    with Dissolve(2)
                    b "What are {sc=1}{color=#000000}you {/sc}{sc=2}{color=#000000}doing{/sc}?"
                    m "Convincing you to live!"
                    b "You're not listening! You would have eaten me tonight anyway. There's no point."
                    m "But, right now, we could still maybe have some fun! It can end on a good note!"
                    b "I tried! But I'm tired. And I hurt."
                    b "Why won't you just... help    me already?"
                    b "Please."
                    call screen choice3 with dissolve
                
                screen choice3:
                    imagebutton:
                        xalign 0.85 yalign 0.5
                        idle "choicebox1_animated_idle"
                        hover "choicebox1_animated_hover"
                        action Jump("killher")
                
                    imagebutton:
                        xalign 0.15 yalign 0.5
                        idle "choicebox2_animated_idle"
                        hover "choicebox2_animated_hover"
                        action Jump("no3")
                    text "Refuse!" at transform:
                        align (0.21, 0.5)  
                    text "{sc=2}Help her." at transform:
                        align (0.76, 0.5)                

                label no3:
                    m "No! I'm not going to!"
                    

                    scene depression_vvsad:
                        subpixel True 
                        xalign 0.5
                        yalign 1.0
                        
                        linear 3 zoom 1.02 
                        linear 3 zoom 1
                        repeat 
                    show fog_base 
                    show fog_1
                    show fog_2
                    with Dissolve(2)
                    $ sadness = 5
                    $ update_layers()
                    show fog_3 at fogfade with dissolve
                    b "Why won't you {sc=2}{color=#000000}help{/sc} me?"
                    b "You're the {sc=2}{color=#000000}only{/sc} one who can..."
                    m "I can't kill you. And I can't let you kill yourself."
                    b "You're being {sc=1}{color=#000000}selfish{/sc}!"
                    b "I... I deserve to choose when I {sc=1}{color=#000000}die{/sc}!"

                    call screen choice42 with dissolve
                
                screen choice42:
                    imagebutton:
                        xalign 0.15 yalign 0.5
                        idle "choicebox2_animated_idle"
                        hover "choicebox2_animated_hover"
                        action Jump("killher")
                    text "{sc=3}PLEASE KILL ME!" at transform:
                        align (0.21, 0.5)
                    imagebutton: 
                        xalign 0.85 yalign 0.5
                        idle "choicebox1_animated_idle"
                        hover "choicebox1_animated_hover"
                        action Jump("no4")
                    text "NO!" at transform:
                        align (0.75, 0.5)   

                label no4:
                    m "You're just emotional right now!"
                    m "You just need to take some deep breaths first!"
                    m "If you just calm down..."
                    $ sadness = 6
                    $ update_layers(0)
                    $ persistent.sadness = True
                    scene depression_vvsad_red
                    show fog_base
                    show fog_1
                    show fog_2
                    show fog_3 at pulse
                    b "{sc=3}{b}{size=+40}{color=#000000}STOP TELLING ME WHAT TO DO!" with sshake

                    
                    b "{sc=7}{b}{size=+40}{color=#000000}I HATE THIS!"
                    m "Please stop shouting! I can't help you if-"
                    b "{sc=8}{b}{size=+40}{color=#000000}DON'T TALK ME OUT OF THIS!"
                    b "{sc=8}{b}{size=+40}{color=#000000}WILL YOU HELP ME OR NOT!?"
                    
                    call screen choice4 with dissolve
                
                screen choice4:
                    imagebutton:
                        xalign 0.15 yalign 0.5
                        idle "choicebox3_animated_idle"
                        hover "choicebox3_animated_hover"
                        action Jump("killher")
                    text "{sc=4}{b}PLEASE!\nPLEASE!\nPLEASE!" at transform:
                        align (0.21, 0.5)
                    imagebutton: 
                        xalign 0.85 yalign 0.5
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("no5")
                    text "NO!" at transform:
                        align (0.75, 0.5)   

                label no5:
                    call screen choice5

                screen choice5:
                    imagebutton:
                        xalign 0.15 yalign 0.5
                        idle "choicebox3_animated_idle"
                        hover "choicebox3_animated_hover"
                        action Jump("no6")
                    text "{sc=2}NO!" at transform:
                        align (0.23, 0.5)    

                    #All below are PLEASE! buttons    
                    imagebutton: 
                        xalign 0.85 yalign 0.5
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher")   
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.8, 0.5)    
                    imagebutton: 
                        xalign 0.65 yalign 0.7
                        idle "choicebox3_animated_idle"
                        hover "choicebox3_animated_hover"
                        action Jump("killher")   
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.65, 0.7) 

                    imagebutton: 
                        xalign 0.4 yalign 0.3
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher")   
                    imagebutton: 
                        xalign 0.1 yalign 0.1
                        idle "choicebox3_animated_idle"
                        hover "choicebox3_animated_hover"
                        action Jump("killher")       
                    imagebutton: 
                        xalign 0.1 yalign 0.8
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher")   
                    imagebutton: 
                        xalign 0.7 yalign 0.1
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher")   
                    imagebutton: 
                        xalign 0.45 yalign 0.6
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher")   

                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.8, 0.5)       
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.45, 0.6)    
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.15, 0.2)               
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.68, 0.17) 
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.4, 0.35)
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.17, 0.76)      
                    imagebutton: 
                        xalign 0.6 yalign 0.5
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher") 
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.6, 0.5)     

                    imagebutton: 
                        xalign 0.24 yalign 0.3
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher") 
                    text "{sc=8}{b}{size=+50}PLEASE!{/size}" at transform:
                        align (0.26, 0.32)  

                          

# start glitch

                label no6:
                    $ sadness = 7
                    $ update_layers(2)
                    image top_left = ParameterizedText(xalign=0.0, yalign=0.0)
                    image top_right = ParameterizedText(xalign=0.0, yalign=0.0, xpos=0.6, ypos = 0.05)
                    define counter = 0
        
                    while counter < 18:
                        call screen choice6
                        $ counter += 1
                    
              
                    jump killher
                    
                        
            


                screen choice6:         #Trick 1! glitch around screen

                    timer 1 action [Hide("choice6"), Return()]

                    $ xpo = renpy.random.random()
                    $ ypo = renpy.random.random()
                    
                    $ xpo2 = renpy.random.random()
                    $ ypo2 = renpy.random.random()

                    $ xpo3 = renpy.random.random()
                    $ ypo3 = renpy.random.random()

                    $ xpo4 = renpy.random.random()
                    $ ypo4 = renpy.random.random()
                    $ xpo5 = renpy.random.random()
                    $ ypo5 = renpy.random.random()
                    $ textxpo = xpo+0.03
                    $ textypo = ypo
                    
                    imagebutton:                   
                        xalign xpo yalign ypo
                        idle "cloudbox_animated_idle"
                        hover "cloudbox_animated_hover"
                        action Jump("no7")

                    imagebutton: 
                        xalign 0.5 yalign 0.5
                        idle "choicebox4_animated_idle"
                        hover "choicebox4_animated_hover"
                        action Jump("killher")
                    text "{sc=8}{b}{size=+20}Please..." at transform:
                        align (0.5, 0.5)   

                    if counter >= 2:
                        text "{b}{size=+100}THIS IS\nTOO MUCH" at transform:
                            xalign xpo2 yalign ypo2

                        
                    if counter >=3:
                        imagebutton: 
                            xalign ypo4 yalign ypo4
                            idle "choicebox3_animated_idle"
                            hover "choicebox3_animated_hover"
                            action Jump("killher")
                    if counter >= 4:
                        add "gui/button/button_choice_hover_background.png" at transform:   
                            xalign xpo3 yalign ypo3
                            
                        imagebutton: 
                            xalign ypo5 yalign ypo5
                            idle "choicebox4_animated_idle"
                            hover "choicebox4_animated_hover"
                            action Jump("killher")    
                        text "{move}{sc=8}{b}{size=+30}Why is this happening!?{/move}" at transform:
                            xalign xpo5 yalign ypo5

                    if counter >= 5:
                        $ xpo6 = renpy.random.random()
                        $ ypo6 = renpy.random.random()
                        $ xpo7 = renpy.random.random()
                        $ ypo7 = renpy.random.random()
                        $ xpo8 = renpy.random.random()
                        $ ypo8 = renpy.random.random()
                        imagebutton: 
                            xalign ypo6 yalign ypo6
                            idle "choicebox4_animated_idle"
                            hover "choicebox4_animated_hover"
                            action Jump("killher") 
                        imagebutton: 
                            xalign ypo4 yalign ypo4
                            idle "choicebox3_animated_idle"
                            hover "choicebox3_animated_hover"
                            action Jump("killher")    
                        imagebutton: 
                            xalign ypo7 yalign ypo7
                            idle "choicebox4_animated_idle"
                            hover "choicebox4_animated_hover"
                            action Jump("killher") 
                        text "{move}{b}{size=+150}I CAN'T SPEAK!{/move}" at transform:
                            xalign xpo2 yalign ypo2    
                            rotate 48
                    if counter >= 6:  
                        imagebutton: 
                            xalign ypo8 yalign ypo8
                            idle "choicebox4_animated_idle"
                            hover "choicebox4_animated_hover"
                            action Jump("killher")       

                        text "{move}{sc=8}{b}{size=+50}COME ON JUST SAY SOMETHING ALREADY!{/size}" at transform:
                            xalign textxpo yalign textypo
                    if counter >= 10:
                        add "gui/button/red.png"
                    if counter == 12:
                        text "{size=+100}I CAN'T HANDLE THIS!" at transform:
                            xalign 0.5 yalign 0.5

                    if counter == 13:
                        text "{size=+100}I'M SORRY BUTTON" at transform:
                            xalign 0.5 yalign 0.5
                    if counter == 14:
                        text "{size=+100}I'M TOO WEAK TO SAVE YOU" at transform:
                            xalign 0.5 yalign 0.5
                    if counter == 15:
                        add "images/bg/depression/fog_3.png" at pulse
                        text "{size=+50}3" at transform:
                            xalign 0.5 yalign 0.5
                    if counter == 16:
                    
                        text "{size=+50}2" at transform:
                            xalign 0.5 yalign 0.5        
                    if counter == 17:
                
                        text "{size=+50}1" at transform:
                            xalign 0.5 yalign 0.5



                
                label no7:
                    $ stop_layers()
                    
                    m "{sc=3}{b}{size=+20}{color=#000000}I CAN'T OKAY!?"
                    m "{sc=3}{b}{size=+20}{color=#000000}I JUST {cps=20}CAN'T{/cps} DO IT!"
                    show depression_vvsad_red                                                            
                    show top_left "{sc=5}{color=#8B0000}PLEASE GOD WHY WON'T HE LISTEN? WHY WON'T HE HELP ME? I WANT THE SUFFERING TO END. MY CHEST HURTS. MY BODY HURTS. I WANT TO STOP THINKING. \nI HATE EVERYTHING. I HATE MYSELF. I HATE YOU.\n WHY WHY WHY? I HATE LIFE. I HATE EXISTING. \n SOMEONE PLEASE END ME ALREADY!\n SOMEONE! PLEASE! HELP ME! HELP! HELP! \nNOBODY UNDERSTANDS ME! I'M WORTHLESS!\nIT'S ALL HOPELESS! NOTHING MATTERS!\nI WANNA DIE I WANNA DIE I WANNA DIE\nI WANNA DIE I WANNA DIE\n I WANNA DIE I WANNA DIE\n I WANNA DIE I WANNA DIE I WANNA DIE\n BUT IF NO ONE WILL HELP ME I GUESS I'LL JUST\nJUST END MYSELF! A WORTHLESS PRODUCT!\nI'M GOING TO CUT MYSELF TO PIECES!\nI'M GOING TO KILL MYSELF!\n EVERYTHING WAS A MISTAKE I WISH I COULD\nJUST GO BACK TO HAVING NEVER MET YOU. WHY COULDN'T I JUST BE HAPPIER? I FEEL SO GUILTY FOR FEELING SO BAD\n BUT I CAN'T RECOVER IT'S TOO LATE IT'S TOO LATE IT'S TOO LATE IT'S TOO LATE IT'S TOO LATE IT'S TOO LATE IT'S TOO LATE"
                    show top_right "{sc=5}{color=#8B0000}THIS IS A NIGHTMARE AND I JUST WANT IT TO END.\n   I CAN REMEMBER BEING HAPPY BUT I CAN NEVER GO BACK.\n  I TRIED SO HARD BUT I'M AT MY BREAKING POINT\nTHERE WAS SO MUCH I WANTED TO DO\n  IT HURTS TO THINK ABOUT IT\nI'M SORRY! I'M SORRY! I'M SORRY! I'M A\n   E M P T Y    B R O K E N    D E A D    A P A T H Y  \nP A I N    S T R E S S E D   I WANNA DISAPPEAR AND NEVER REMEMBER ANYTHING AGAIN \n I HATE THAT I'M SO SAD \n I'M OVER THIS! I'M OVER EVERYTHING!\n   I HATE THE WORLD NOTHING CAN MAKE ME HAPPY\n     WHO'S FAULT IS IT? I DON'T CARE IT HURTS \n IT HURTS SO MUCH IT HURTS SO MUCH IT HURTS \n IT HURTS SO MUCH IT HURTS SO MUCH IT HURTS \n IT HURTS SO MUCH IT HURTS SO MUCH IT HURTS "
                    with Dissolve(2)  
                    show top_text "{color=#FFFFFF}I hate you." with dissolve
                    pause(2)
                    hide top_left
                    hide top_right
                    play sound "<from 0 to 2>wNoise.wav" fadein(2) volume 10
                    
                    # $ sadness = 7
                    # $ update_layers()
                    # $ start_layers(0)
                    show stab:
                        subpixel True 
                        parallel:
                            alpha 1.0 additive 0.0 
                            linear 5.79  alpha 0.86 additive 0.53 
                        parallel:
                            
                            linear 3.60 zoom 1.54 
                        parallel:
                            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
                            linear 2.91 matrixcolor InvertMatrix(0.0)*ContrastMatrix(3.83)*SaturationMatrix(0.1)*BrightnessMatrix(-0.28)*HueMatrix(-122.0) 
                            linear 0.32 matrixcolor InvertMatrix(0.0)*ContrastMatrix(4.86)*SaturationMatrix(0.1)*BrightnessMatrix(-0.09)*HueMatrix(-139.0) 
                            linear 0.37 matrixcolor InvertMatrix(0.0)*ContrastMatrix(4.16)*SaturationMatrix(0.1)*BrightnessMatrix(-0.43)*HueMatrix(-139.0) 
                            linear 2.19 matrixcolor InvertMatrix(0.0)*ContrastMatrix(4.16)*SaturationMatrix(0.1)*BrightnessMatrix(-0.47)*HueMatrix(-63.0) 
                    
                    show top_left "{size=+150}{color=#7C3333}STOP I'M SO SORRY PLEASE STOP!"
                    
                    show top_right "{size=+100}{color=#AA3D3D}AAAAAAA AAAAHH HHHHH"
                    pause 0.3
                    show top_left "{size=+200}{color=#AA3D3D}I'M SO SORRY! I'M SO SORRY! I'M SO SORRY!"
                    show text "{size=+100}{color=#AA3D3D}AAAA  A AAA AAAAAAA AAAAAAAAAAA  AAAAAAAAAA AAAAAA  AAAA  AAAAAA AAAAAAAA AAAAAAAAAAAAAA AA" 
                    pause 0.2   
                    show top_right "{size=+150}{color=#AA3D3D}A   AA AAA AAA A  AAAA AAAAA  AA AAAA AAAAAAAAAAAAA     AAAAAAAAAAA     AAA"
                    pause 0.1
                    show text "{size=+500}{color=#AA3D3D}I HATE YOU I HATE YOU I HATE YOU I HATE YOU I HATE YOU"
                    show top_right "{size=+150}{color=#AA3D3D}OH MY GOD! YOU'RE-! I-I DON'T-!"
                    pause 0.3
                    show top_left  "{size=+500}{color=#AA3D3D}WHY WHY WHY!?"
                    # $ stop_layers()
                    stop sound


                    
                    
                    pause(0.2)
                    scene black
                    pause(1)
                    show text "{color=#FFFFFF}It's not your fault, is it?" with dissolve
                    $ renpy.pause ()
                    show text "{color=#FFFFFF}You tried so hard..."
                    $ renpy.pause ()
                    show text "{color=#FFFFFF}Maybe the next mushroom will be a better one."
                    $ renpy.pause ()
                    show text "{sc=1}You open up your laptop once more."
                    $ renpy.pause ()
                    hide text
                    with dissolve
                    scene black with Fade(0.5, 1.0, 0.5)
                    pause 1
                    stop music fadeout(2)



                    $ persistent.end9 = True    
                    
                    
                    "End 9: Truffled mind."

                    
                    return
                    




                
                
                
                
            

                label killher:
                    if sadness > 1:
                        $ sadness -= 1
                        $ update_layers()
                    hide top_left
                    hide top_right
                    with Dissolve(2)
                    
                    m "Fine..."
                    m "I'll do it."
                    m "I'm so sorry you're in so much pain. I'll help you. You won't be alone."
                    if sadness > 1:
                        $ sadness -= 1
                        $ update_layers(3)
                    scene depression_surprised
                    show fog_base
                    show fog_1
                    with Dissolve(2)
                    
                    b "You mean it?"
                    m "I do."
                    m "I just... I guess I just don't want you to go."
                    m "You were the first thing in a long time that's brought me any joy."
                    m "But this isn't about me."
                    $ sadness = 100
                    $ update_layers(2)
                    
                    # if sadness > 1:
                    #     $ sadness -= 1
                    #     $ update_layers(3)
                    b "..."
                    
                    scene depression_gratefulsmile
                    show fog_base
                    show glow
                    with Dissolve(2)
                    b "Thank you."
                    "Those words sting your ears."
                    # if sadness > 1:
                    #     $ sadness -= 1
                    #     $ update_layers(3)
                    "Immediately, she holds out the boxcutter once more."
                    "..."
                    "This time, you take it."
                    "You move closer and try not be sick. But this isn't about you, remember?"
                    "Just listen to her. Just get this over with."
                    b "You'll just need to cut off my head."
                    b "I'm ready."
                    # if sadness > 1:
                    #     $ sadness -= 1
                    #     $ update_layers(3)
                        
                    scene black with Dissolve(2)
                    "You position the blade just below her jawline."
                    m "I'm sorry it was like this, Button."
                    b "I'm not sorry. I'm just grateful. Goodbye."
                    $ stop_layers(3)
                    "Button's mouth relaxes into a smile as you slice her throat."
                    "The boxcutter runs through her flesh like butter, just as she said."
                    "You keep cutting, just trying to end this all as quickly as possible."
                    "It only takes a few seconds before the blade slides right through..."
                    "And her head thuds to the ground. Right next to her arm. And her limp body."
                    window hide
                    pause 1
                    
                    stop music fadeout(3)

                    show text "You can't stop your hands from {sc=2}shaking{/sc}. You can't look away from her smiling face."
            
                    $ renpy.pause ()
                    show text "You don't know why this had to happen. But it's over. It's over."
            
                    $ renpy.pause ()
                    show text "Now you understand how it feels to be surrounded by sadness. Why people stopped talking to you."
            
                    $ renpy.pause ()
                    show text "Because in a horrible way, you feel..."
                
                    $ renpy.pause ()
                    show text "...{i}glad{/i} that she's finally gone."
                
                    $ renpy.pause ()
                    show text "It's a despicable kind of relief."
                
                    $ renpy.pause ()
                    show text "You're glad to be alone again."
                    $ renpy.pause ()
                    hide text with Dissolve(2)
                    show text "Alone... with {sc=2}{color=#E2A0A0}me{/color}.{/sc}"
                    with Dissolve(2)
                    
                    $ renpy.pause ()
                    hide text
                    
                    $ persistent.end8 = True        
                    pause 1
                    "End 8: Morel dilemma."
                    return


































            

            


            

        show mc normal at right
        show button vhappy at left
        with easeinbottom
        
        b "Thank you for taking me out!"
        m "Mhm."
        show mc normalside
        m "Ugh, I'm still kinda hungry."
        if existential >= 1:
            show button bored
            b "Speaking of needs, I should probably water myself after all that exercise."
            $ watered = 0
            show water_status at water_location with dissolve
            pause 1
            play sound "spray.wav"
            $ watered = 1
            pause 1
            hide water_status with dissolve
            jump pizza
        else:
            show button vvhappy
            b "And I'm thirrrrrrrsty!"
            show mc confused
            m "AGAIN!? Can't you just... spray yourself?"
            show button happy        
            b "Nah... It feels sooooo much nicer when you do it!"

            $ watered = 0
            hide mc with easeoutbottom
            show water_status at water_location with dissolve
            call screen water_4
            
            screen water_4:
                imagebutton:
                    xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
                    action Jump("day1_watered_4")

            label day1_watered_4:
                play sound "spray.wav"
                $ watered = 1
                pause 1
                queue sound "spray.wav" 
                $ watered = 2
                show mc normal at right with easeinbottom
                show button vhappy 
                window show
            b "Revitalisation, complete! Thank you!"
            hide water_status with dissolve
            show button normal
            b "You said you were still hungry... Are you going to eat me tonight?"
            menu:
                "Am I eating her tonight?"
                "Ok...":
                    #stop music fadeout(3)
                    show mc stressed
                    m "I'm sorry..."
                    show button happy
                    b "Don't be! Remember our first interaction? Retract your sorry!"
                    show mc annoyed
                    m "Sorry retracted."
                    show mc sad
                    m "It's just... It was fun."
                    m "Thank you for being so nice."
                    m "I don't know how I'm going to eat you, but-"
                    show button vvhappy
                    b "Grilled with butter and garlic!"
                    show button happy
                    b "That way you'll get a very pure, but yummy, taste!"
                    b "..."
                    show button normal
                    b "%(player_name)s, I really enjoyed these past two days, but..."
                    show button bored
                    b "I've noticed that you get really stressed sometimes."
                    show button normal
                    b "So... just know that I think you're pretty cool."
                    show button happy
                    b "I really hope I've been able to help you relieve some stress a little. I think that was my original purpose."
                    show button smirk
                    b "And I hope you enjoy eating my body."
                    show mc annoyed
                    m "(Why are you like this?)"
                    show mc happy
                    m "Thanks too, Button."
                    show button goodbye
                    b "May I make a request?"
                    show mc confused
                    m "Yeah?"
                    show mc stressed
                    m "(Is it going to be lewd???)"
                    b "Can we..."
                    show button vgoodbye
                    b "... hug?"
                    show mc blushside
                    m "Oh... um... yeah."
                    show button vhappy
                    b "Thank you!"
                    window hide
                    hide button 
                    hide mc
                    with dissolve
                    show happy_hug
                    with dissolve
                    stop music fadeout(3)
                    
                    "You hug each other tightly. It's sad, but it doesn't feel as horrible as you thought it would."
                    if button_rp >=40:
                        "And, to your utter surprise..."
                        "Button even presses a light kiss on your cheek!"
                    scene black with Fade(0.5, 1, 0.5)    
                    "And then, you fetch the boxcutter from your desk."
                    "Without any hesitation..."
                    "... she closes her eyes."
                    window hide
                    pause 1
                    play music "sizzle.wav"
                    "She stopped responding after you chopped off her head."
                    "The rest you sealed in plastic bags to use over the next few days."
                    "You dice the mushroom flesh, and sauté it with butter, garlic and herbs."
                    stop music fadeout(3)
                    "You salivated at the aroma, and when you finally taste it..."
                    "Its juices spread over your tongue, instantly dissipating your mournful thoughts."
                    "It's terrifying to think about the ethics of what has just transpired."
                    "But you think you did a good job with her overall."
                    "She said she was happy, right?"
       
                    pause 1

                    if persistent.end5:
                        pass
                    else:
                        $ persistent.end5 = True    

                    "End 5: That's yummy! No cap."
                    
                    return



                "I don't want to.":
                    show mc confused
                    m "What? No. That's unnecessary. If I'm that hungry, I'll just have a cup of ramen."
                    show mc annoyed
                    m "I've got like... a whole box of them under my bed."
                    show button surprised
                    b "Why not? I'm right here."
                    show mc sad
                    m "I just..."
                    show mc blushside
                    m "...want to hang out with you more."
                    show button smirk
                    b "Ohoho!"
                    b "It seems you're getting attached to me, %(player_name)s. That's very dangerous."
                    b "Do I need to get worried?"
                    show mc normalside
                    m "..."
                    show mc happy
                    m "Maybe."
                    m "I admit it. You're more fun to have around than I thought."
                    
                    show button surprised
                    b "Whoa. Are you..."
                    show button blushsmile
                    b "... CONFESSING!?"
                    show mc shocked
                    m "{sc=3}{color=#000000}WHAT? NO!!!"
                    show mc annoyed
                    m "Of course you'd think that!"
                    m "But I just want to hang out!"
                    show button dgafsmile
                    b "Ooh? In what kinda way?"
                    show mc shout
                    m "{sc=2}{color=#000000}Nooooo..."
                    show button vhappy
                    b "I'm just kidding! Hehe!"
                    show mc vblushside
                    m "Jesus."
                    show button surprised
                    b "What's Jesus?"
                    show mc vstressed
                    m "I am NOT dropping religion on you the day before..."
                    m "..."
                    show mc sad
                    m "I really have to do it, don't I? Is there no way you don't have to... die... tomorrow?"
                    show button normal
                    b "Well, it's either that... or I like..."
                    show button bored
                    b "... dry up. In a very painful, slow process."
                    show button happy
                    b "So yeah, I'll take getting eaten over that!"
                    show mc stressed
                    m "Yeah... I guess I would too."
                    show button normal
                    b "So... what now?"
                    show mc normalside
                    m "Mmm, food."
                    jump pizza


        label pizza:
        

            #pizza event
            show button happy
            b "What are you going to eat? Ramen?"
            show mc normal
            m "I'm actually really craving a pizza... I haven't had one since I lived with my mom."
            show mc stressed
            m "Ugh, but I don't want to make the call..."
            show button surprised
            b "Why not?"
            show mc annoyed
            m "Haha... It's embarrassing, but I'm scared of talking over the phone."
            m "Sometimes I forget my order or address or how to even talk because I'm so nervous, or they can't hear me..."
            m "I once made a conversation tree of every possible response so I could just follow that instead of having to worry, but nope."
            m "In the heat of the moment, I forgot to read."
            show mc normalside
            m "Sorry, I'm rambling and it's probably boring."
            show button happy
            b "Why don't I order for you?"
            show mc confused
            m "You've never used a phone before in your life."
            b "But it's just like talking! Only you can't see each other, right?"
            b "I'm good at talking!"
            if existential >=1:
                show button bored
                b "I think..."                
            show mc worried
            m "But... how will you remember the address and the name of the pizzas I want? What if you forget?"
            show button vhappy
            b "I've got a good memory! I can even remember things from when I was just a lil spore. I can remember the sound of your voice, though I couldn't tell what you were saying back then."
            show mc surprised
            m "Whoa. That's incredible! Can you remember anything else from then?"
            show button bored
            b "Hmm, just an instinct to outcompete my sisters so they wouldn't absorb me."
            show mc shocked
            m "..."
            show button vvhappy
            b "But I won! I absorbed THEM! Hehe!"
            show mc stressed
            m "I... I have no words. Congrats on winning."
            show button happy
            b "Thanks! Now tell me what I need to remember..."
            window hide
            hide button
            hide mc
            with easeoutbottom
            
            "At your insistence, you pretend to be the receiver and run through the scenario with Button a few times, adding in potential threats such as a bad line, long waiting time, non-availability of your desired pizza..."
            "She's so calm and honest. She always just tells them to hold, and then asks the real you what other pizza you'd like, or if you're fine with the waiting time. She's got this."
            play sound "phone.wav"
            "And so you dial the number, for real."
            play sound "phonecall.mp3"
            "For a second, you think maybe you CAN do it afterall. You'd have Button at your side to support you!"
            "But when you hear the voice on the other end, you panic and immediately pass it to Button."
            stop sound
            b "Hi! I wanted to order a pizza with you. Is that ok?"
            b "...Yes. My order is..."
            "You're a grown up. Will you ever get better?"

            b "What's that...? Oh, hold on, please. %(player_name)s, they have a special! Do you want to add an extra pizza to get a free ice cream?"
            m "(I can't decide on a second pizza right now! Too much pressure! I wish I could have that ice cream though...)"
            m "No... I'm good."
            b "Ok!"            
            b "No thank you, we're good!... Ok... You too, bye!"
            show button vvhappy at left
            show mc happy at right
            with easeinbottom
            b "Woohoo! Pizza is coming!"
            m "Thanks, Button. I couldn't have done that."
            show button vhappy
            b "You're welcome!"
            show button happy
            b "It wasn't even as hard as your practice runs!"
            b "You just need to stay calm, and then you can try next time!"
            show mc normalside
            m "Maybe. I want to get over this at some point."
            show button normal
            b "Why do you get scared?"
            m "Um..."
            show mc stressed
            m "I don't know."
            m "It's just scary for me. It's worse than talking face-to-face, which I already mess up most of the time. I hate it."
            show button happy
            b "I don't understand, but I believe you'll get better. I saw you thinking about doing it!"
            show mc cute
            m "Yeah, maybe next time my instinct won't be to throw my phone across the room."
            
            
            
            #----- end pizza      

            
        hide button
        hide mc
        with easeoutbottom

        "You chat and chill until your phone rings, signaling the arrival of the delivery man."
        window hide
         
        show bottle night with Dissolve(2):
            zoom 0.9

        "Pizza obtained, you return to the room."
        show button happy at left
        show mc happy at right
        with easeinbottom       
        m "Pizza, my princess."
        show button normal
        b "...?"
        m "So beautiful..."
        m "I've missed you so much... Ah, and so hot too!"
        show button dgaf
        b "Really?"
        show mc annoyed
        m "I'm just having fun!"
        show button closedannoyed
        b "So you're not going to make out with your pizza or something!?"
        m "Don't tempt me."
        show mc happy
        "As you lift open the flap of the pizza box, you lean your face in and sniff deeply."
        show mc shocked at bounce
        "That's when you realise that something is horribly wrong."
        show mc vstressed
        m "No!" with sshake
        show button surprised
        b "What's wrong?"
        show mc cry
        m "It's the wrong order..."
        show mc stressed
        m "I was so excited for my special quadruple cheese! But this... just isn't that!"
        show button normal
        b "What is it?"
        show mc sad
        m "Some rando's order. There's feta, olives, pesto, sundried tomatoes, umm... possibly blue cheese? Some meat thing..."
        show button happy
        b "You don't like it? It looks really good!"
        show mc stressed
        m "It's just not what I wanted... I'd only get my quadcheesy pizza if I aced my exams, and then my mom would make the call for me..."
        m "I miss those times. I still had hope then. This isn't my hope."
        show mc sad
        m "And I'm too stupid scared to call the pizza place and tell them they got it wrong!"
        show mc vannoyed
        m "Stupid piece of shit pizza mix-up. And I gave that guy a good tip too! This pizza probably..."
        
        show mc surprised

        m "Holy shit, this is amazing."
        m "This."
        m "This is my new favourite."
        m "Can you eat? Can you try this?"
        show button vhappy
        b "I can't, but thanks for offering. You enjoy the pizza!"
        show mc cute
        m "Aaaah, man, now I really wanna lie back, eat this pizza, and watch some anime!"
        show button surprised
        b "What's anime?"
        show mc annoyed
        m "{b}\"What's anime\"?{/b} Oh boy..."
        hide button
        hide mc
        with easeoutbottom
        "You introduce Button to anime!"
        "You have to watch in dubs, since she can't read, but she doesn't know what she's missing anyway."
        "You show her a few of your favourite, beginner-friendly series that you think she'd like."
        "And... just as you predicted... she gets attached to characters who have obvious red flags attached to them."
        
        "And falls into despair when they finally die in the most emotional way possible."
        "I guess you're just like her."
        "You decide to stay up all night with her, since it's her last one."
        "Pizza, anime, and the both of you in the bed, laughing together..."
        "It's a wonderful night."
        "How long has it been since you've felt so at peace?"
        "Why does tomorrow have to come?"
                    
        na "Ara ara, Naegi-kun... it's time to give yourself to me completely."
        na "How much... do you truly love me?"
        b "..."
        m "(I forgot about this part.)"
        "You and Button sit through some typical anime fan service."
        "You're well aware of how weird this probably is to a non-weeb, but you're too scared to gauge her expression."
        "Yup. Just stare straight ahead."
        na "Mmmf~ Nagei-kun! I love you! Mmmm~ aaaah~"
        "Oh god."
    
        show button blush at left
        show mc vstressed at right
        with easeinbottom
        b "I didn't know THIS was in anime!"
        m "I'm sorry. I forgot about this part... if you're uncomfortable-"
        "You pause the anime."
        show button cough
        b "{size=+20}{sc=2}{color=#000000}NO! DON'T STOOOOOOP!!!{/sc}{/color}{size=-20}"
        show mc shocked at bounce
        m "You CANNOT shout that at night in my dormitory!"
        show mc vstressed
        m "Shit! What if someone heard you? I'll never live it down..."
        show button sad
        b "Sorry, I just-"
        show mc stressed
        m "No."
        show mc sad
        m "Don't apologise. You don't have any malice. And I shouted at you again... sorry."
        show button annoyed
        b "If I can't apologise, you can't either!"
        show mc normal
        m "I deserve it though."
        show button normal
        b "But you didn't do it on purpose - just like me!"
        show mc annoyed
        m "Ahh, fine. Sorry retracted."
        show button vhappy
        b "Good! Now press play!"
        show mc normal
        m "You're ok to watch this? Isn't it awkward for you?"
        show button blush
        b "No! It's very... interesting!"
        hide button
        hide mc
        with easeoutbottom
        "You force yourself to sit through the whole thing."
        "You don't miss how enraptured Button is. What have you done to her innocent soul?"
        "..."
        "Well, maybe innocent is an exaggeration."
        "You just reeeeeeeally hope that nobody heard Button's yell."

        scene black with fade
        
        window hide
        stop music fadeout(3)
        show chibi_sleep at truecenter with dissolve
        show top_text "Even though you tried to stay up, you drift off..." with dissolve 
        pause 3
        
        scene bottle day with Fade(1, 2.0, 1):
            zoom 0.9
        show day_3 at topleft with dissolve    
        play music "normal.mp3" fadein(3)
        show mc stressed at right with easeinbottom
        m "..."
        "As you wake up... the sounds of generic anime distract you from your usual morning brooding."
        "As you open your eyes, you realise that you've been holding Button's arm in place of your plushie."
        show mc shocked
        m "Button! Still?"
        show mc stressed
        m "AND you're in my bed again!"
        show button vhappy at left with easeinbottom
        b "I never left! Come on, aren't you used to it already?"
        show button smirk
        b "You even hugged me in your sleep! And you-"
        show mc vstressed
        m "Nope. Not a word more."
        show button vvhappy at bounce
        b "But anyway! I'm on the fifth season of the anime you showed me! We HAVE to discuss-"
        show mc annoyed
        m "Aaaand that's enough."
        "You turn off your laptop mid-anime. It's hot to the touch."
        show button sad
        b "Nooooo! Don't take away my anime!"
        show mc vshout
        m "You've had enough! My PC too. Both of you need a break."
        show button cough
        b "Noooooo~"
        show mc stressed
        m "Oh god. Come on, take your water and shut up."
        $ watered = 1
        hide mc with easeoutbottom
        show water_status at topright with dissolve
        call screen water_5
        
        screen water_5:
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
                action Jump("day1_watered_5")

        label day1_watered_5:
            play sound "spray.wav"
            $ watered = 2
            show mc normal at right with easeinbottom
            show button vvhappy 
            window show
        b "Mmm, feeling juicy again!"    
        hide water_status with dissolve
        show mc happy
        m "Haha, you're kinda silly, you know that?"
        show button happy
        b "Silliness is fun!"
        show button vhappy
        b "{i}NOW{/i} can we talk about the anime!?"
        m "Sure sure."
        hide mc 
        hide button
        with easeoutbottom
        "You have some leftover pizza for breakfast while Button weebs out on you for a good hour or so."
        "It's extremely entertaining hearing fresh thoughts on one of your favourite shows!"
        show mc happy at right
        show button pout at left
        with easeinbottom
        b "Can I make a special request today?"
        show mc confused
        m "Uh, sure?"
        show button vvhappy
        b "Take me to the beach!"
        
        show mc normalside
        m "Uuugh..."
        m "Not my favourite place honestly. It's kind of uncomfortable..."
        show button happy
        b "No problem! You can stay under the nice, cool shade of the umbrella! Just like that one character in the anime!"
        show mc annoyed
        m "Oooooh."
        m "So you got to the beach episode, huh?"
        "The thought of the beach gives you a headache. The sand, the sun, the wind, the people, the expectation to undress..."
        "Normally you would say no."
        "But this is day three."
        show mc happy
        m "Ah, fine. We'll stop by the shop and get you a swimsuit... and some ice cream for me too."
        show button vvhappy
        b "Woohooooo!"
        show mc cute
        m "Just help me carry stuff, ok?"
        show button happy
        b "Button shall be the strongman!"
        window hide
        hide water_status
        hide day_3 
        with dissolve
        stop music fadeout(3)
        
        hide mc
        hide button
        with easeoutbottom
        scene black with fade
        play sound "door.wav"
        
        #play music "happy_date_recorder.mp3"
        
        show chibi_mc at slightright
        show chibi_mushroom at slightleft
        with easeinright


        "It takes an hour via train, but that doesn't dampen her excitement one bit."
        "She loves buying the ticket, climbing onboard, and feeling the train accelerate and turn. It makes you smile."
        "How would she react to a rollercoaster? If you didn't eat her tonight, maybe you could both go tomorrow?"
        "She looks alright now. Maybe you could do it!"
        "Maybe if you just water her extra, she can manage another day."
        "Just before you walk to the beach, you purchase some snacks and water, while Button browses the swimwear."
        "She finds a really cute one! It's pricey but who cares. It's perfect."
        "And then, finally..."
        hide chibi_mc
        hide chibi_mushroom 
        with easeoutleft
        
        scene bg_emptybeach with Fade(0.5, 1.0, 2):
        play sound "seagull.wav"
        # show mc normal at right
        # show button vvhappy at left
        # with easeinbottom
        
        play music "sad_date.mp3" volume 0.25 fadein(0.1)
        pause 0.5
        b "{sc=7}{color=#000000}AHHHHHH! THIS IS AMAZING!!!{/sc}"
        b "The sand feels so hot and fluffy! But the wet part is cold and hard!"
        # show mc happy
        m "That's because when the sand gets wet, it compresses and... she's gone."
        # hide button with easeoutbottom
        # show mc stressed
        
        "It's a pleasant day, and the beach is relatively empty, since who goes on a Wednesday morning?"
        show bg_beach with dissolve
        "You find the perfect base camp and dig up a hole to set up the umbrella."
        show bg_beach_mc with dissolve
        "Lounging on a towel, you eat your ice cream."
        show bg_beach_characters with dissolve
        "All the while Button runs about with the water on the shoreline."
        "But after a little while, she coerces you to \"just try\" swim with her."
        # show mc surprised at right
        # show button vhappy at left
        # with easeinbottom
        
        m "You can take it off!?"
        
        b "It's just a hat, silly!"
        # show mc confused
        m "I thought it was like... your head or something."
        m "And then, do all your clothes just grow-"
        # show button closedannoyed
        b "Come on! Let's GO already!"
        "She pulls you down to the water's edge."
        # show button vvhappy
        # show mc vstressed
        b "EEK! IT'S SO COLD! I LOVE IT!"
        m "Same, but I hate it."
        # show button vhappy
        b "Let's go deeper!"
        # show mc shout
        m "It's hard enough with just my ankles!"
        # show button pout
        b "Come ooooon! Please just be my doormat and swim more!"
        # show mc surprised
        m "Who taught you to speak like that?"
        "Anime."    
        # show button annoyed
        b "What must I do to convince you?"
        # show mc annoyed
        m "You could also just respect my wishes, you know..."
        # show button bored
        b "..."
        # show button smirk
        # show mc vannoyed
        m "Whatever you're schemeing-"
        # show button vvhappy
        b "Oops!"
        "She. Splashes. You."
        # show mc vstressed
        m "..."
        # show button goodbye
        b "Oops?"
        "She splashes you AGAIN!"
        # show mc vshout
        m "{sc=7}{color=#000000}BUTTON!"
        # show button vvhappy at flip
        b "Oh noooooo~!"
        # hide button
        # with easeoutleft

        # hide mc
        # with easeoutleft
        window hide
        
        scene bg_beach with Dissolve(3):
            matrixcolor TintMatrix("#FE942F")
        "You end up watching the sunset together."
        show affection at topright
        with dissolve
        pause(1)
        $ button_rp += 10
        pause(1)
        if button_rp >= 40:
            "She looks really happy. You feel proud of yourself."
        
  
        
        if button_rp>=50:

            "She leans her head on your shoulder."
            "With her snuggled beside you, it feels like nothing is wrong anymore."
            "Glancing at her, you notice for the first time how her hair shifts from light to dark brown. Sometimes you forget that she isn't a human."
            "Even her eyes twinkle with playful mischief, and her mannerisms are so life-like, so appealing..."

            "That's when it hits you."
            "You're attracted to her."
            "Maybe it was her spunky, fun personality that drew you out of your hole."
            "Maybe it was how she showed you that you don't need to feel guilty for having fun."
            "Maybe it's how you admire her self strength, and her simple, yet resolute, goal to have fun in life."
            "..."
            "COME ON!"
            "You're {i}really{/i} not going to say anything about her {b}body{/b}?"
            "She's pretty hot, dude. {sc=4}{color=#000000}THAT BIKINI!"
            "Eitherway, you have the insatiable desire..."
            "...to draw her face near..."
            "And kiss her..."

            menu:
                "Should I do it?"
                "Kiss her.":
                    # show mc blushside at right
                    # show button happy at left
                    # with easeinbottom
                    $ kiss = True
                    m "Hey..."
                    m "Ahhh..."
                    m "I know I said I wanted to be friends, but..."
                    # show mc vblushside
                    m "Is it ok if I {sc=1}{color=#000000}kiss you?"
                    # show button blushsmile
                    b "Wait, really!? You want to kiss me!?"
                    # show mc blushside
                    m "Y-Yes..."
                    # show button vvhappy
                    b "Oh my gosh, oh my gosh! YES! PLEASE KISS ME! FINALLY!"
                    "Her enthusiasm makes you smile."
                    # hide mc
                    # hide button
                    # with easeoutbottom
                    
                    "So this is what it feels like... to like someone. It makes you weirdly nervous."
                    scene black with fade
                    "Button, exasperated by the delay, grabs your face, leans in, and presses her lips gently against yours."
                    "!!!"
                    
                    "A few seconds later, she pulls away, smiling mischievously."
                    "And so the afternoon ends!"
                    
                    

                "Bad idea.":
                    $ button_rp -= 20 
                    m "(There's no way that would end well)."
                    m "(We'd both just get hurt later on...)"
                    "That's what you tell yourself."
                    "So you scoot slightly away."
                    "Button's smile falters for a second."
                    "But then she goes on staring at the sunset."
        "That beach trip takes the whole day, but it was a great one."
        
        stop music fadeout(3)
        
        
        scene bottle night with Fade(1, 2.0, 1):
            zoom 0.9
        show day_3 at topleft with dissolve    
        play music "night.wav"
        show button vvhappy at left
        show mc stressed at right
        with easeinbottom

        
        m "Ugh, finally home. I've got sand quite literally everywhere."
        b "Haaaah~ the beach was amazing."
        show button happy
        b "You enjoyed it too, right? Our last day?"
        show mc awed
        m "..."
        show mc happy
        m "Yeah. Thanks for the suggestion."
        show mc cute
        m "Honestly, it might have been my favourite day ever."
        show button vhappy
        b "I'm just that magical. You're welcome!"
        show button happy
        b "These last few days have been amazing, and I'm truly grateful to you..."
        show button bored
        show mc normal
        "..."
        show button normal
        b "But I feel really tired, more and more. Like I'm being... drained, in a way."
        show button goodbye
        b "I think it's time for me to go."
        
        show mc surprised
        m "Like... now?"
        b "Yes."
        show mc sad
        m "...Do you have to?"
        show button happy
        b "Don't worry! I've had a great life. I couldn't have asked for a better friend than you."
        show mc stressed
        "Is that really true? You only took her to a field, a park, and a beach!"
        "What about the cinema? Festivals? Dances? Fireworks? Amusement parks?"
        "If you had been more proactive, she would have been happier."
        "You were the one holding her back."
        show button angry
        b "Stop it. I know what you're doing."
        show mc worried
        m "I-"
        show button closedannoyed
        b "Hush. I'm about to give you the reality of things."
        show mc awed
        show button vhappy
        b "You've made me a very happy mushroom."
        b "If not for you, I likely would have ended up as many of my sisters- staying at home, tending to their masters."
        show button bored
        b "Not necessarily a bad life, but..."
        show button happy
        b "I'm very glad it wasn't mine."
        b "I'm ready, %(player_name)s. You can trust me on that."
        
        
        menu:
            "Is this really it?"
            "She's ready. I am too.":
                show mc happy
                m "I'll do it."
                show button surprised
                b "Woah, really?"
                show mc confused
                m "What do you mean \"Really\"? Isn't that what you want me to do?"
                show button bored
                b "I was just prepared to fight you on this-"
                show button vhappy
                b "But neeeevermind! Great! Perfect! Thank you!"
                show mc happy
                m "You and your personality."
                jump submitandeat


                

            


        
            "I want you to live another day!":
                show mc stressed
                m "There's something I need to say."
                show button normal
                b "Ok."
                show mc sad
                m "What if... I eat you tomorrow? And we can go out again?"
                m "It'd just be one more day! You look fine now, maybe-"
                show button annoyed
                b "Yeah, I LOOK fine."
                b "But I'm really tired, ok?"
                show button sad
                b "In a way that I know I can never recover from."
                b "I've already passed my peak, and now... it's starting to hurt more and more, every hour."
                show button goodbye
                b "I loved the beach, but all that saltwater probably wasn't the best idea. I feel really weird."
                show button vgoodbye
                b "It's ok. I'm ready to die! I always have been, remember?"
                show mc shout
                m "No, not ok! I can't murder you!"
                show button sad
                b "Do you want me to suffer?"
                show mc vshout
                m "No! But how can you ask me to {sc=3}{color=#000000}KILL{/sc} you!?"
                m "How are you so eager to die!?"
                show button closedannoyed
                b "You think I want to die!?"
                b "You think I'm not scared? That I haven't thought about it?"
                show button vsad
                b "I'm going to die whether I like it or not! Either a quick death by your hand and I nourish you-"
                show button scared
                b "Or I slowly rot away!"
                b "{sc=4}{color=#000000}AT LEAST LET MY DEATH BE MEANINGFUL!{/sc}"
                show mc shout
                m "Just one more day!"
                m "Can't we just try?"
                show button vsad
                b "I don't want to! I want to stop fighting. I want the pain to stop."
                show button sad
                b "And I want to die while I still feel somewhat fine."
                show mc sad
                menu:
                    "I'm having second doubts..."
                    "I have to listen. I have to do it.":
                        m "..."
                        b "Look. I know it's hard. I'm-"
                        show mc stressed
                        m "I'll do it."
                        show button surprised
                        b "You... will?"
                        m "Yes. There's just no other choice."
                        show mc sad
                        m "You were made to be this way. I knew that from the start."
                        m "I just... didn't think it was going to be this sad for me."
                        show button happy
                        b "You don't need to be sad! Like I said, I'm ready, I've had a good life, and that's what matters!"
                        show button vhappy
                        b "Plus, there's something reassuring about knowing I'm going to nourish you. Like... it just makes me happy."
                        jump submitandeat

                    "I'm not giving up like this!":
                        m "..."
                        show button goodbye
                        b "Look. I know it's hard. I'm-"
                        show mc vstressed
                        show button surprised
                        m "No."
                        m "No. I can't."
                        m "I need you."
                        m "We can still go out tomorrow, even if I need to carry you."
                        show mc cry
                        m "Please, Button. I beg you."
                        show button sad
                        b "Please don't cry..."
                        m "Please, Button."
                        show button goodbye
                        b "..."
                        show button vgoodbye
                        b "You're making this really hard for me."
                        b "I'll t-try. For you."
                        b "Just please..."
                        b "{cps=20}If it hurts too much, you need to-{/cps}{nw}"
                        scene black
                        window hide
                        stop music fadeout(3)
                        show chibi_sleep at truecenter with dissolve
                        show top_text "You hold Button in your arms while you sleep..." with dissolve 
                        pause 3
                        hide top_text
                        show chibi_awake at truecenter
                        show top_text "But you're stirred awake."
                        pause 2 
                        scene bottle day with Fade(1, 3.0, 1):
                            zoom 0.9
                        show day_4 at topleft with dissolve              

                        b "{cps=20}{size=-15}Please kill me.{/cps}"
                        show mc stressed at right with easeinbottom
                        show mc sad
                        m "Button?"
                        show affection_dying at topright with dissolve
                        show button dyingsad at left with easeinbottom
                        b "{cps=20}{size=-15}Please kill me.{/cps}"
                        show mc shocked
                        m "{sc=3}{color=#000000}OH MY GOD!"
                        b "{cps=25}{size=-15}It hurts so much. Please kill me, %(player_name)s.{/cps}"
                        show mc vcry
                        m "I'm so sorry! I didn't know!"
                        show button dyingscream at bounce
                        b "{sc=3}{color=#000000}PLEASE KILL ME!" with sshake
                        menu:
                            "What are you waiting for!? DO IT!"
                            "I HAVE TO KILL HER!":
                                show mc vstressed
                                m "Ok! I'll kill you! I'm sorry!"                                                
                                show button dyingsad with dissolve
                                hide mc with easeoutbottom
                                
                                "As quick as you can, you grab the closest blade you have: the boxcutter in your desk."
                                show mc vcry at right with easeinbottom
                                m "{sc=3}{color=#000000}I'M SORRY BUTTON!"
                                pause(0.5)
                                "You shakily cut through Button's throat."
                                show affection_dead at topright with dissolve
                                "It's so brittle, her neck crumbles off immediately."
                                show button dyingdead with dissolve
                                show mc shocked
                                m "..."
                                "You've decapitated her."
                                window hide
                                pause(1)
                                
                                hide button with easeoutbottom
                                play sound "thud.wav"
                                "Button's wails for death halt. Abruptly."
                                "She's dead."
                                "She's a dead corpse on the floor."
                                window hide
                                pause(1)

                                scene black with Fade(2, 1.0, 0.5)
                                play music "dynamic_audio/clock.mp3" fadein(3)
                                pause 1
                                
                                show text "{sc=1}What have you done?{/sc}"
                                $ renpy.pause ()
                                hide text
                                show text "{sc=1}{/sc}You're so ashamed that you can't bring yourself to eat her."
                                $ renpy.pause ()
                                hide text
                                if kiss:
                                    show text "{sc=1}{/sc}You'd kissed her yesterday. Now, her dead face stares at you, those lips agape mid-scream."

                                show text "You're not even crying because she's {sc=1}dead."
                                $ renpy.pause ()
                                hide text
                                show text "You're crying because you're scared {sc=2}{color=#E2A0A0}she doesn't forgive you."
                                $ renpy.pause ()
                                hide text
                                
                                with dissolve
                                scene black with Fade(0.5, 1.0, 0.5)
                                pause 1
                                stop music fadeout(2)
                                if persistent.end7:
                                    pass
                                else:
                                    $ persistent.end7 = True    

                                "End 7: I'm sorry."

                                return

                            # "Y-You just need some water!":
                            #     show mc anxious
                            #     m "Water! H-Hold on!"
                            #     play sound "spray.wav" loop
                                
                        
                        

label submitandeat:
    show mc stressed
    m "Hah... I'm-"
    show mc cry
    m "I'm going to miss you."
    show button surprised
    b "Ah, wait!"
    show button happy
    b "This is for you!"

    play sound "page.wav"
    show button_drawing at truecenter with easeinbottom
    window hide
    pause
    hide button_drawing with easeoutbottom
    show mc annoyed
    m "Haha!"
    show mc cute
    m "It's so you. I love it. Thank you."
    show button vhappy
    b "I knew you would! I drew it while you slept!"
    show mc happy
    b "I don't know what awaits me on the other side. It's scary, but thanks to you..."
    show button vgoodbye
    b "...living was worth dying for."
    jump finaldeath



label finaldeath:    
    hide mc
    hide button
    with dissolve
    play music "date_musicbox.mp3" fadein(1)
    show happy_hug with dissolve
    "Button hugs you tight, one last time."
    window hide
    scene black with Fade(0.5, 1, 0.5)
    "And then-"
    if button_rp>=50:
        "She presses a sweet kiss against your cheek."
        "It's so... nice."
        "You kiss her cheek in return, and she smiles."
    "You grab a boxcutter from desk and position it against her neck. She guides your hand."
    "And, together-"
    "-you drag the blade across her throat, pressing hard into the mushroom flesh."
    "As her flesh tears, instinctively, you expect blood, but..."
    "It's just... white inside. Mushroom flesh. It's food. She's never been human."

    "You watch in morbid horror as her eyes blanken, her lingering smile finally fading from her lips."    
    "You just hold her limp body close and whisper to her your appreciation and your favourite memories."
    "Just in case she could still hear you."
    "Now, you have to carry out her wishes."
    window hide
    
    play music "sizzle.wav"
    "..."
    "It's strange how someone you love can be so nauseatingly delicious."
    "You gorge yourself. Nothing will be wasted. Nothing."
    stop music fadeout(3)
    "Every bite is succulent, tender, popping with warm juice between your teeth."
    "You remove her from existence, one heavenly, repulsive gulp at a time."
    "Perhaps it's a little salty. Maybe from the ocean. Maybe from your tears."
    "But in a way, it's like tasting that happy memory."
    "You don't think you could ever go back to your old ways."
    "In the span of just a few days, someone with a beautiful heart came and went, leaving hope in her wake."
    "And you don't feel bad that she's gone. You just feel like maybe everything isn't so bad after all."
    "Like... maybe you can knock on your neighbour's door after all."

    

    stop music fadeout(3)
    if persistent.end6:
        pass
    else:
        $ persistent.end6 = True    
    "End 6: Goodbye Button, my new friend."
    return


return
