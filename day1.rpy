define ali = Character("Alice", color = "440a1f",callback=character_beeps)

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
    show alice tsun annoyed
    na""
    #keep going

#name input
    $label name_ali: 
        $playername = renpy.input("quesionts goes here", length = 8).strip().lower().capitalize()
        #make an array of bad cases and check if the name is in the array
        if playername == "bad case":
            "...%(player_name)"
            show alice meanLaugh
            #like aqua from konosuba
            na"Hold on a second... THAT'S your name?"
            show mc stressed
            m"No! I just stuttered..."
            na"Okay."
            show alice tsun
            na"then what is your name then?"
            jump name_ali
        if playname = "":
            "Can't even remember your own name... Come on..."
            "I guess you <b>really</b> can't do anything right."
            ""








label intro:

#comes out
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




