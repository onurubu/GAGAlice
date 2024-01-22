

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

