from time import sleep

class Format:
    off = "\033[0m"
    red = "\033[91m"
    cyan = "\033[36m"
    bold = "\033[1m"
    italic = "\033[3m"


answer = input("Would you like to play a game? (yes/no) ")

if answer.lower().strip() == "yes":
    print("....") 
    sleep(2)
    print("Hello")
    sleep(2)
    print("How did you get here?")
    sleep(4)
    print(f"Welcome to my game of {Format.red}{Format.bold}choices{Format.off}")  
    
    answer = input(f"Look around you... You're in the woods. You see a sign. Left for the mountains, Right for the bridge. Where do you {Format.red}{Format.bold}chose?{Format.off} ")
    
    if answer.lower().strip() == "left":
        print("You take a long walk up the mountains")
        sleep(3)
        print("You hear a faint cracking sound in the distance.")
        sleep(2)
        print("... You try to listen out for more")
        sleep(1) 
        print("..") 
        sleep(3)
        print("....") 
        sleep(3)
        print("........") 
        print("You hear nothing.")
        sleep(1)
    elif answer.lower().strip() == 'right':
        print("You turn right and look out for a bridge")
        sleep(3)
        print("Your eyes start to become blurry as you keep searching")
        sleep(3)
        print(f"{Format.italic}{Format.cyan}Where is this bridge?{Format.off} You think to yourself")
        sleep(3) 
        print("You keep walking and feel something hard beneath your feet") 
       
        answer = input("Do yo want to keep searching for the bridge? Or do you want to investigate the floor? (search/investigate)")
        if "bridge" in answer.lower().strip() or "search" in answer.lower().strip():
            print("You ignore the feeling under your feet and keep walking")
            sleep(3)
            print("You see a bright light in the far distance... The bridge is right in front of you")
            sleep(3)
            print("As you run towards the light your body starts to lean forward") 
            sleep(3)
            print(f"{Format.italic}{Format.cyan}Huh{Format.off}") 
            sleep(3)
            print("you look around.. the bridge is above you")  
            sleep(3)
            print(f"{Format.italic}{Format.cyan}THE BRIDGE WAS BROKEN?!{Format.off}") 
            sleep(3)
            print(" you fall..")
            sleep(3)
            print("you die")
            sleep(3)
            print(f"{Format.red}{Format.bold}𓁹‿𓁹 GAME OVER 𓁹‿𓁹{Format.off}")
            
        if "floor" in answer.lower().strip() or "investigate" in answer.lower().strip():
            print("You search the floor in a panic and pick up the hard piece of metal")
            sleep(3)
            print("You wipe it clean as you bring it closer to your face")
            sleep(3)
            print(f"{Format.italic}{Format.red}'--R-I-G - B--DG- ----EN UP A---D'{Format.off}")
            sleep(3)
            print(f"{Format.italic}{Format.cyan}Huh? What does that say?{Format.off}")
            sleep(3)
            print("You rub your eyes and try to focus on the writing")
            sleep(3)
            print(f"{Format.italic}{Format.red}'WARNING - BRIDGE BROKEN UP AHEAD'{Format.off}")
            sleep(3)
            print("You gasp and take a step back")
            sleep(3)
            print(f"{Format.italic}{Format.cyan}Thank goodness I didn't cross that bridge...{Format.off} You think to yourself")
        
    else:
        print("...") 
        sleep(1)
        print(f"That wasn't an option.{Format.red}{Format.bold}YOU'VE LOST{Format.off}") 
        sleep(2)

else:
    print("..") 
    sleep(1)
    print("...") 
    sleep(2)
    print(f"{Format.red}{Format.bold}𓁹‿𓁹I guess you'll die here then 𓁹‿𓁹{Format.off}") 