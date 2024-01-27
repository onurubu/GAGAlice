#Make inner voice more mean
#aim for 200-300 lines

    #choose mushroom type
label chooseFly:
    show finn happy 
    m"This one looks kind of colorful and pretty!"
    show finn sad
    "... I guess"
    "*click click*"
    m"That was easy to order, it even takes PaePal..."
    m"Fly amanita... That's like a toadstool right?"
    show finn happy
    m"Maybe this mushroom will make me grow double my size, and break bricks with my bare-hands"
    "Are you done being stupid?"
    show finn sad
    m"..."
    "Aren't red mushrooms like this dangerous? If this kills you, you can only blame yourself for being dumb enough to order it"
    "There was something ominous about that product description too"
    m"..."
    m"I mean, it's on the site so it's probably fine... Right?"
    "Let's hope your faith in the meritocracy of capitalism pays off this time"
    #"It's not like you have any 1-UPs" maybe keep the mario theme going? idk
    "Okay, you can crawl back to your bed and keep wasting your life until it's here"
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
    "You are suddenly pulled back into conciousness by the sound of a nearby bomb impact"
    "You instinctively cover yourself with your blanket, not that it will make a difference in your chances of survival."
    "You prepare for your conciousness to exit this reality, and for your sense of being to dissolve into nothingness"
    "..."
    show chibi_scared at truecenter

    "You lift the blanket off of your head, and examine your room."
    "..."
    "It looks exactly as you remember it:"
    "filthy and disorganized."
    "But not destroyed by the savages of war."
    na"Hello? Is anyone home? I have a parcel from the reception for you..."
    "A familiar voice resonates dully through your front door"
    "It seems that you mistook the sound of knocking on the door for an aerial attack."
    "..."
    "See, you can't even seperate reality from your juvinile nightmares"
    na"I'm going to leave the package on the doorstep then..."
    "You hear the muffled sound of the package being placed down, followed by a couple of footsteps."
    "The sound of door unlocking, being pulled open, and closing again echoes through the dormitory passageway"
    "It takes only seconds for the sound to fade, leaving only the faint sounds of birds and morning traffic from the opposite side of your window."
    "He's gone..."
    "When was the last time you even actually talked to someone face to face?"
    "..."
    m"That was my neighbour..."
    m"I've heard him listening to loud music before..."
    m"Sometimes I feel like I should just go over and introduce myself..."
    m"But then I think of everything that could go wrong."
    m"Wouldn't it be super weird if I just waltz over?"
    m"I don't even know if that's something dorm neighbours do... Especially when we've already been here for over a year"
    m"I think I lost my chance... Besides, he listens to loud guitar music with scary singing sometimes"
    m"Makes me think he might be super scary too..."
    m"But his laughing I've heard through the walls sounded kind..."
    "Are you done yet?"
    #make this more mean
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
    #Instructions are basically the same as button but with the addition of "For maximum potency consume within 24 hours of maturation."
    window hide
    pause
    hide instructions with easeoutbottom
    show mc confused with easein bottom
    window show


    m"Potency?... Bright... For mushrooms?"
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
            m"Let's just do it by the book... or pamphlet... I guess?"
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


#water them

#wait


