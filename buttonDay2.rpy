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
        