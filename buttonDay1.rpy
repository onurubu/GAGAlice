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


