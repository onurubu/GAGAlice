#choose mushroom type
label chooseFly:
    m"I guess this one looks kind of colorful and... pretty... I guess"
    "*click click*"
    m"That was easy to order, it even takes PayFriend..."
    m"Maybe it will make me grow into Super %s{player name}"
    "Are you done being stupid?"
    m"..."
    "Aren't red mushrooms like this dangerous? If this kills you, you can only blame yourself for being dumb enough to order it"
    m"..."
    m"I mean, it's on the site so it's probably fine... Right?"
    "Let's hope your unfounded faith in the meritocrisy of Capitalism pays off this time"
    #feel like this might feel preachy to some people
    "Okay, you can crawl back to your bed and keep doing nothing with your life until it's here"
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with Dissolve(2)
    pause(2)

    #wait for it to arrive
    $ alice_day = 0
    stop music
    queue sound "knock.wav"
    show chibi_awake at truecenter
    play music "heartbeat.wav"
    "SOMEONE IS HERE??!!"
    "You are suddenly pulled back into conciousness by the sound of a near by bomb impact"
    "You instinctively cover yourself with your blanket, not that it will make a difference in your chances of survival."
    "You prepare for your conciousness to exit this reality, and for your sense of being to dissolve into nothingness"
    "..."
    show chibi_scared at truecenter

    #keep this scene to develop neighbour a bit more before he is introduced later

    "You lift the blanket off of your head, and examine your room, which looks exactly as you remember it:"
    "filthy and disorganized."
    "But not destroyed by the savages of war."
    na"Hello? Is anyone home? I have a parcel from the reception for you..."
    #maybe here we can make this interaction a little longer, 
    #give the nieghbour little bit of a personality, then see how mc interacts.
    "See, you can't even seperate reality from your juvinile nightmares"
    na"I'm going to leave the package on the doorstep then..."
    "You hear the muffled sound of the package being placed down, followed by a couple of doorsteps, and a door down the dormitory corridor unlocking."
    "He's gone..."
    "When was the last time you even actually talked to someone face to face?"
    #maybe in this route you would get the guitar from needing to get the courage to talk to your neighbour and asking if you can borrow a guitar for few days?
    "..."
    m"That was my neighbour..."
    m"I've heard him listening to loud music before..."
    m"Sometimes I feel like I should just go over and introduce myself..."
    m"But I think of everything that could go wrong."
    m"I don't even know if that's something dorm neighbours do... Especially when we've already been here for over a year"
    m"I think I lost my chance... Besides, he listens to loud guitar music with scary singing sometimes"
    m"Makes me think he might be super scary too..."
    m"But his voice sounded kind..."
    "Are you done yet?"
    "You lift your head of from your pillow and turn to get out of bed."

#instructions (are they different between routes?) 
    stop music fadeout(3)
    scene bedroom_closed_curtains with Fade(0.5,1.0,0.5):
        zoom 0.9
    queue sound "door.wav"
    queue music "normal.mp3"
    "Your box cutter effortlessly slices through the thin layer of tape connecting the top flaps of the small cardboard box."
    m "I think these are the instructions?"
    play sound "page.wav"
    show instructions at truecenter with easeinbottom
    window hide
    pause
    hide instructions with easeoutbottom
    show mc confused with easein bottom
    window show

    #maybe reuse just this scene?

    m"Bright... For mushrooms?"
    m"I don't know if this is right... Like the whole reason I got these is because mushrooms grow in dark places..."
    menu:
        m"Follow the instructions?"
        "Trust my gut.":
            jump deadMush
            #label the scene in button script
            return
        "Just follow the instructions.":
            show mc at center with move
            show mc normal
            m"I don't know everything, and I think that the people making the product probably know how I'm supposed to use it."
            m"Let's just do it by the... pamphlet..."
        "Now comes the hard part..."
        "..."
        "What are you waiting for? No one else is going to open the curtains for you."
        show mc stressed
        m"..."
        hide mc with easeoutbottom
        window hide
        call screen open_window with dissolve
        screen open_window:
            #copy
        show mc shocked with easeinbottom
        #maybe all of this should be the same... No point in fixing what ain't broke I guess


#water them

#wait


