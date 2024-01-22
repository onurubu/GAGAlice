
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
