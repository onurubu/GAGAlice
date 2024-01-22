define ali = Character("Alice", color = "440a1f",callback=character_beeps)

#feel like it's not funny enough, prob needs more humour
#aim for 1500 lines across all endings
#na is unknown speaker
#[make character beeps dif for Alice and Button]

label:day1Alice
    stop music fadeout(2)
    show black with fade
    
    #variables
    $aliceTrust = 0
    #keep original script up to "{size=-8}"
    
    #SIloutte animation of her breaking out by herself
    show mc shocked at right with move
    show alice tsun at left 
    na"I guess this is your room? Smaller than I hoped for but this will work."
    m"..."
    m"WHAT THE FUCK"
    na"..."
    "She unapologetically grabs the spray bottle on the table beside her"
    "She pulls the trigger and a cloud of mist appears in front of her"
    "She steps through it and towards me"
    
    #staring down at you cruelly
    show alice tsun annoyed
    na"What a warm welcome...."

    #gets reflexively small and subby
    show mc sad
    m"I'm sorry..."
    show mc shocked
    m"WAIT A SEC! WHO... or...what?... THE HELL ARE YOU?!"
    show alice sad
    na"How pitiful... I would have hoped that my parent would be able to perform basic congnitive tasks"
    na"But I suppose the surreal allure of my visage is beyond your comprehension"
    show alice despair
    na"Truely pitiful..."
    m"You're... the mushroom I bought?"
    na"It seems you have something resmebling sentience... Well Done."
    show mc angry
    m"THAT'S MY LINE"
    show alice neutral
    na"..."
    na"Seeing as your brain is functioning to some degree, perhaps you could tell me your name?"
    show mc awed
    m"Ummm... My name..."
    show alice sad
    na"Forgive me, I should have chosen a less challenging display of intelligence"
    show mc angry
    m"NO!!!"
    show mc sad
    m"Just give me a sec..."
    "I wasn't mentally prepared to need to talk to someone... "
    show alice neutral
    na"So, what do I call you?"
#name input

    label name_ali: 
        $name_redo = False
        $playername = renpy.input("So, what do I call you?", length = 8).strip().lower().capitalize()
        #make an array of bad cases and check if the name is in the array
        if playername == "bad case":
            "...%(player_name)"
            show alice meanLaugh
            #like aqua from konosuba or uminekoBeatrice
            na"Hold on a second... THAT'S your name?"
            show mc stressed
            m"No! I just stuttered..."
            na"Okay."
            show alice tsun
            na"Then what is your name then?"
            $name_redo = True
            jump name_ali
        if playername = "":
            "Can't even remember your own name... Come on..."
            "I guess you <b>really</b> can't do anything right."
            "Just go with Finn."
            $playername = "Finn"
        m"...%(player_name)s."
        show alice smug
        if (name_redo):
            na"Are you sure this time?"
            show mc angry
            m"YES!"
            show alice meanLaugh
            na"Just wanted to make sure..."
        show alice smug
        na"What an adorable name... I suppose it suits someone like you."
        m"What's that supposed to mean?!"
        show alice meanLaugh
        na"What ever you want for it to mean."
        
        stop music
        
        na"..."
        na"So, anyway... Should we start?"
        m"Ummm... Start...what?"
        #i kind of picture the boxcutter scene from bakemonogatari here
        "Without answering your question, she takes a confident lunge in your direction"
        "Her face appoaches yours suddenly"
        "You throw your center of balance backward to evade her advance, but you start to fall backwards"
        "Her hand pinches the neck of your oversized hoodie, preventing your descent"
        "She tightens her grasp and shifts her own body weight forward, bringing her face closer to yours."
        "You pause, suspended in place for what feels like minutes"
        "You stare at her face"
        "Her expression remains fixed in a neutral casual, but apathetic expression as she looks down at you."
        "Your gaze shifts to her lips, which shimmer as if moist"
        show mc stressed
        m"...!"
        "You lightly push her away and regain your composure"
        #feels super sudden, maybe make this happen after a few attempts.
        #She should be more just confused and taken aback
        #maybe she's more touchy and assertive at first
        #pov of mc feeling uncomfy about it
        show alice sad
        na"Huh...What's wrong with you? Isn't this what you wanted?"
        m"Huh? What are you talking about? I have NO idea what's going on right now?"
        
#add stuff here

	#she explains in no uncertain terms what is 'about to happen'
	#MC doesn't seem so into the idea
	#She tries to gesture to like "Look at me, be honest with yourself"
	#(It's a given that anyone should be into me)
	
	#She tries once again to reinitiate
	#But this time mc is more vocal/aggresive, and it shocks her

	na"...So... You don't want me?"      
        m"?"
        na"That's not what's supposed to happen..."
        na"I'm supposed to entice anyone to abandon reason."
        na"But you..." 
        m"I'm trying to tell you I-"
        show alice shoutTears
        na"SHUT UP!"
        show mc shocked
        m"..."
        show alice crying
        na"..."
        na"{size=-8}What's wrong with me...{size=+8}"
        hide alice with easeoutbottom
        "Before I can open my mouth, she turns towards to door"
        "She swiftly turns the door knob and runs out"
        "I hear her sobbing echo through the dormitory passage, and then fade into the distance"
        #maybe you only learn her name on the rooftop?
        show mc stressed at center
        play music normal
        m"What the fuck just happened?"
        "Your brain is still lagging behind."
        m"..."
        m"So that was the mushroom I've been growing... But it's not a mushroom..."
        show mc tired
        m"And it talks..."
        show mc stressed
        "Good job, you made a girl cry"
        "You're so good at this whole being useless bit, sometimes I forget it's not on purpose"
        "I bet you don't even know what you did"
        m"..."
        m"What the hell is going on..."
        "Why don't you figure it out?"
        m"... Okay... Ummm..."
        m"Why don't I look at the site I got it from... There must have been some kind of mistake or something."
        #show room, new dialogue for blahaj etc
        #click pc
        m"Okay let's see what this buinness is 'ABOUT'"
        m"WHAT THE FUCK IS THIS??? IS THIS EVEN LEGAL????"
        m"So I'm supposed to grow a companion?"
        m"Even I'm not THAT much on an incel"
        m"..."
        m"So let me get this straight... "
        m"She's a mushroom companion... And her characteristics are... Unparalleled beauty and dominance?"
        m"I mean, I guess she was pretty attractive, but I wasn't really paying attention to that."
        m"...only has 3 days to live..."
        "You sit in your gaming chair and stare blankly at the clock on your computer taskbar"
        m"Wow, that's just a lot to take in"
        play sound('message_notify.wav')
        show mc shocked
        m"AAH!"
        "It's just a dischord message"
        "Oh it's Rom"
        "Even if you don't have any friends in the real world, you still know some people online."
        "Even then though, you mostly talk in your small private server"
        "There's about 10 people"
        "Last time you went into a larger server, you couldn't quite find the timing to talk"
        "Whenever you tried, people talked over you, and didn't seem to care about what you had to say"
        "You click onto the notification window in the bottom corner of your screen and the message expands"
        #actually show interface here
        label dischord_chat:
            #what's mc's username
            define romBestGrill = rb
            play music computerHum
            #notification sounds? typing sounds?
            #maybe user types anything like emily is away?

            rb"sup i was wondering if you wanted to hop in vc"
            m"Sorry, kinda busy rn... can you type?"
            rb"np i was just bored and your always online so..."
            m"ouch"
            #anime crying gif from rb
            rb"are u eeping soon? little eep moder?"
            m"ijust got up"
            rb"o"
            rb"your sleep finally looped back to humanity"
            rb"vampirism cured"
            m"i guess"
            rb"are you okay, you don't usually respond so short"
            m"yeah i'm fine... it's just"
            m"idk"
            rb"did something happen?"
            "you think about if you should tell him about what just transpired"
            #here show the time stamp go forward 2 minutes
            m"you probably won't believe me so..."
            rb #sends gif
            rb"don't be like that"
            m"fine"
            #attach link to website
            m"You know I told you I was growing mushrooms... Well this is where I ordered them from and ummm"
            m"It bloomed today... into a girl"
            rb"lmao nice nice"
            m"and then umm"
            m"She got all close to me and then ran off crying..."
            rb"wait, did you make this site? I didn't know you could make websites"
            rb"it looks so professional"
            rb"how many hours did it take"
            m"?"
            rb"like for a joke it's based"
            m"I can't code, and it's real."
            rb"wait like real real>"
            m"yeah"
            rb"emoji upside down smile"
            rb"lmao wtf"
            rb"let me order one real quick"
            rb"I wonder if I can get it to cosplay Rom"
        m"What? Is he not listening to me?"
            m"are you for real?"
            rb"like was she hot? I've always wanted a girlfriend that can become my waifu"
            m"I'm being serious, she's like a living being... She talks and moves and everything"
            rb"sounds like I don't need my onahole anymore"
        m"What the fuck?"
            m"I'm sorry, I think i've gotta go"
            rb"Don't have too much fun"
            rb#winky emoji... maybe all of the emojis are his waifu
            
        "You close the window, and turn away from your computer screen."
        show mc stressed
        m"Am I the weird one?"
        m"Like... Is that how I'm supposed to act?"
        m"Is that how guys are supposed to think about girls?"
        "You're just afraid"
        #too obvious, rewrite to be more subtle
        "Any girl who gets to know you is going to be repulsed like SHE was"
        m"Tch, just remembered something I was trying to forget"
        "You're unloveable"
        "Even if you tried you couldn't meet the minimum standards of a boyfriend"
        
        m"GAAAH!"
        "You shake your head and get up suddenly"
        m"Whatever! I don't care... Let's just go and find her"
        "You walk over to the door and walk through it into the corridor."
        "You look towards both ends of the passage, but there's noone there."
        #choice where to check -> go somewhere stupid then bad end
        "I turn toward the staircase leading to the roof."
        "There's a small chain barring access, but I easily step over it"
       


#why would the player know to check on the roof?

        play sound footstepsEchoingStairs
        scene rooftop afternoon
        play music wind

	
        "You walk up the narrow set of stairs and arrive onto the roof of your dormitory building."
	"From here, you can look out at the university campus that you haven't explored since your first semester of classes."
	"Ivy grows on the walls to either side of a large stairset, that climbs from the bottom of the campus, towards the ceremonial hall"
	"You remember sitting there during your initial orientation and listening to long speeches about how you as the youth of the world"
	"Are here to learn the skills necessary to make the world a better place."
	"..."
	"Sometimes you think about how when you graduate, you will feel like it was truely a waste:"
	"That you spent so much of your youth so close to such incredible architecure;"
	"And so many other people trying their best to make their dreams come true."
	"..."

	#find her on the rooftop
	"You look "
	#Tears/swollen eyes, but calmer
	#She starts she conversation in a sad tone
	#as a mushroom, she doesn't have memories or a sense of personal identity
	#She does have instinct and the information in her DNA
	#In that DNA there's a clear purpose, be desireable, be pretty
	#If she isn't those things, she has no sense of meaning
	#That's why she wants for him to look at her
	#To use her
	#So that she can feel like it was worth it.
	#Not because she likes him, or wants to do the act as itself, but because she wants the validation it implies.
    
    #here its important to talk about her lifespan as a mushroom too, whether or not she's edible etc.
    #[maybe she has some kind of internal conflict where she's afraid of getting close to people because she's literally poisonous]
    #but is it fine as long as she doesn't care about them? so she's scared of trusting someone, because her poison will hurt them
    #and push them away, so its easier she doesn't even try
    #or that she only uses them for sex, validation, then throws them away

	#MC explains that humans too have biological instincts for survival
	#There's some stuff we can't ignore, like food, water, shelter love
	#But sometimes that desire causes more problems for us like obesity with candy
	#Sometimes those instincts lead for us to harm the environment, step on other people, and to be discimantory
	#As sentient things, we need to learn to overcome our 'nature' sometimes, in order for us to be happy
	#Obviously it's not that simple
	#but mc wants alice to find what makes her happy outside of her assigned purpose
	
	#She looks at the vastness of the city and feels like there's more possibility than she could have imagined
	#Maybe even she can try to find some kind of meaning in life 
	#Everything in life is meaningless, so we get to pick whats meaningful for ourselves.
	#She smiles at you and feels a little better
	
	#You walk back down to the room with her
	#You decide what to call her
	
	#it's evening now
    #you ask her how she wants to spend the rest of the evening

    #i don't know what she wants to do, decide this

    #you say that you're getting a little sleepy, and she gives an offer to 'spend the night with her" again
    #you decline
    #after spending some time with her you decide to sleep









#--------------------------------


#try her telling her name here, vs earlier



#[with button route think of the silloutes and how much personality came through that... How would she be posed for that?]

#intial talk with Alice
#"will you submit to me?" 
#if yes bad end? maybe no choice at all the first time
#choice gives you either trust++ if you deal well, or neutral if not
#[from which point should the actual submission end branch off]
#from here we can begin to hint at her scent etc being mind-altering
#alice is taken aback by you not giving her attention, and runs off

#in this panic you decide to take a moment to cool off, let her calm down
# you decide to check website and see the website to understand whats going on
#you see that you have a discord notification, you reply to friend and tell himm your situation
#he's confused why you aren't taking this oppertunity

#you find her on the roof
#try to understand why she got mad
#open up a little towards her too
#go back to room together

#you suggest that you do something together?

#sleep




