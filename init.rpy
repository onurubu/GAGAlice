init python:
#check if this can be done in one call    
    i=0
    while i<7:
        layerName="layer"+str(i)
        renpy.music.register_channel(layerName, "music")

    #Character beeps:  
    renpy.music.register_channel("Beep", mixer="voice")

    def start_layers(delay=1.5):
        renpy.music.play("audio/dynamic_audio/pad.mp3", channel='layer0', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/drum.mp3", channel='layer1', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/piano.mp3", channel='layer2', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/ticklepiano.mp3", channel='layer3', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/horror_Piano octave down.mp3", channel='layer4', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/scarypiano.mp3", channel='layer5', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/dynamic_audio/horror_Low Piano Ugly.mp3", channel='layer6', loop=True, synchro_start=True, fadein=delay)

    def stop_layers(delay=1.5):
        i=0
        while i<7:
            layerName="layer"+str(i)
            renpy.music.stop(channel=layerName, fadeout=delay)

    def update_layers(delay=1):
        layers = [0,0,0,0,0,0,0]
        if 0<=sadness<=7:
            i=0
            while i<sadness:
                layers[i]=1
        elif sadness==100:
            layers[2]=1
        else:
            pass
        layer0=layers[0]
        layer1=layers[1]
        layer2=layers[2]
        layer3=layers[3]
        layer4=layers[4]
        layer5=layers[5]
        layer6=layers[6]
    renpy.music.set_volume(layer1, delay=delay, channel='layer1')
    renpy.music.set_volume(layer2, delay=delay, channel='layer2')
    renpy.music.set_volume(layer3, delay=delay, channel='layer3')
    renpy.music.set_volume(layer4, delay=delay, channel='layer4')
    renpy.music.set_volume(layer5, delay=delay, channel='layer5')
    renpy.music.set_volume(layer6, delay=delay, channel='layer6')

    


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

