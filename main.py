from time import sleep

class Format:
    off = "\033[0m"
    red = "\033[91m"
    cyan = "\033[36m"
    green = '\033[32m'
    bold = "\033[1m"
    italic = "\033[3m"

#MAKE A LOOP TO START GAME OVER
answer = input(f"{Format.green}Would you like to play a game? {Format.italic}(yes / no){Format.off} ")

if answer.lower().strip() == "yes":
    print("....") 
    sleep(2)
    print("Hello")
    sleep(2)
    print("How did you get here?")
    sleep(3)
    print(f"Welcome to my game of {Format.red}{Format.bold}choices ( ͡° ͜ʖ ͡°){Format.off}")  
    sleep(2)
    
    #CPU Question -> Mountains (Left) or Bridge (Right)
    answer = input(f"{Format.green}Look around you... You're in the woods. You see a sign. Left for the mountains, Right for the bridge. Where do you chose? {Format.italic}(Left / Right){Format.off}")
    
    #OPTION -> LEFT -> MOUNTAINS
    if answer.lower().strip() == "left":
        print("You take a long walk up the mountains")
        sleep(3)
        print("You hear a faint cracking sound in the distance.")
        sleep(2)
        print("... You try to listen out for more")
        sleep(1) 
        print("..") 
        sleep(2)
        print("....") 
        sleep(3)
        print("........") 
        sleep(3)
        print("You hear nothing but you remember the direction of the sound.")
        sleep(3)
        
        #OPTION -> FOLLOW SOUND -> MEET LUMBERJACK
        #FOLLOW SOUND
        #CPU Question -> Mountains (Left) or Bridge (Right)
        answer = input(f"{Format.green}Do you want to follow the sound or go in the opposite direction? {Format.italic}(Follow / Opposite){Format.off}") #add something about exploring
        if "follow" in answer.lower().strip() or "sound" in answer.lower().strip():
            print(f"{Format.italic}{Format.cyan}Maybe it's someone who can help?{Format.off} You think to yourself") 
            print("You decide to follow the sound you heard earlier")   
            print("Standing behind you is a tall bearded man holding an axe...")
            sleep(3)
            print("Covered in blood")

        #CPU Question -> Lumberjack (Attack) or Bridge (Run)
            answer = input(f"{Format.green}Do you attack the Lumberjack or run away? {Format.italic}(Attack / Run){Format.off}") #add here
        if "attack" in answer.lower().strip() or "lumberjack" in answer.lower().strip():
            print("you attack")   
            print("you get away")
            print("find way out of woods")
            print(f"{Format.red}{Format.bold}Well done, you have escaped and won my game of choices{Format.off}")
        
        if "run" in answer.lower().strip() or "away" in answer.lower().strip():
            print("you run away before the Lumberjack can get to you")   
           #story progression -> run away from lumberjack -> get lost in woods -> surprise attack from lumberjack -> game over?
       
          
 
    #OPPOSITE
        if "opposite" in answer.lower().strip() or "explore" in answer.lower().strip():
            print(f"{Format.italic}{Format.cyan}I better keep my distance{Format.off} You mumble to yourself") 
            sleep(3)
            print("You try to make your way through the mountains")  
            #story progression -> wander aimlessly through mountains -> game over think of idea!
          
    
    #OPTION -> RIGHT -> BRIDGE
    elif answer.lower().strip() == 'right':
        print("You turn right and look out for a bridge")
        sleep(3)
        print("Your eyes start to become blurry as you keep searching")
        sleep(3)
        print(f"{Format.italic}{Format.cyan}Where is this bridge?{Format.off} You think to yourself")
        sleep(3) 
        print("You keep walking and feel something hard beneath your feet") 

        #CPU Question -> Keep going on bridge (Bridge) or Look at the floor (Investigate)
        #KEEP GOING
        answer = input(f"{Format.green}Do yo want to keep searching for the bridge? Or do you want to investigate the floor? {Format.italic}(Search / Investigate){Format.off}")
        if "bridge" in answer.lower().strip() or "search" in answer.lower().strip():
            print("You ignore the feeling under your feet and keep walking.")
            sleep(3)
            print("You see a bright light in the far distance... The bridge is right in front of you.")
            sleep(3)
            print("As you run towards the light your body starts to lean forward.") 
            sleep(3)
            print(f"{Format.italic}{Format.cyan}Huh{Format.off}") 
            sleep(3)
            print("you look around.. the bridge is above you.")  
            sleep(3)
            print(f"{Format.italic}{Format.cyan}THE BRIDGE WAS BROKEN?!{Format.off}") 
            sleep(3)
            print(" you fall..")
            sleep(5)
            print("you die.")
            sleep(3)
            print(f"{Format.red}{Format.bold}◉‿◉ GAME OVER ◉‿◉{Format.off}")
            
        #INVESTIGATE
        if "floor" in answer.lower().strip() or "investigate" in answer.lower().strip():
            print("You search the floor in a panic and pick up the hard piece of metal that was under your feet.")
            sleep(3)
            print("You wipe away the dirt and bring it closer to your face.")
            sleep(3)
            print(f"{Format.italic}{Format.red}'--R-I-G - B--DG- ----EN UP A---D'{Format.off}")
            sleep(3)
            print(f"{Format.italic}{Format.cyan}Huh? What does that say?{Format.off}")
            sleep(3)
            print("You rub your eyes and try to focus on the writing.")
            sleep(3)
            print(f"{Format.italic}{Format.red}'WARNING - BRIDGE BROKEN UP AHEAD'{Format.off}")
            sleep(3)
            print("You gasp and take a step back")
            sleep(3)
            print(f"{Format.italic}{Format.cyan}Thank goodness I didn't cross that bridge...{Format.off} You think to yourself.")
            #possible routes? See light -> House in distance -> people in house -> go in house -> death--unfiendly
             #possible routes? See light -> House in distance -> people in house -> someone escaping -> trust and escape with them
        
    else:
        print("...") 
        sleep(1)
        print(f"That wasn't an option.") 
        sleep(2)
        print(f"Maybe next time you'll learn to follow instructions!") 
        sleep(2)
        print(f"{Format.red}{Format.bold}YOU'VE LOST{Format.off}") 
        sleep(2)
        print(f"{Format.red}{Format.bold}◉‿◉ GAME OVER ◉‿◉{Format.off}")

else:
    print("..") 
    sleep(1)
    print("...") 
    sleep(2)
    print(f"{Format.red}{Format.bold}( ͡° ͜ʖ ͡°) I guess you'll die here then ( ͡° ͜ʖ ͡°){Format.off}") 