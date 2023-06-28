from playsound import playsound
import time



CLEAR = "\033[2J"
CLEAR_RETURN = "\033[H"



def alarm(seconds, sound):
    time_passed = 0
    
    print(CLEAR)
    
    while time_passed < seconds:
        time.sleep(1)
        time.passed +=1
        
        time_left = seconds - time_passed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_RETURN}{minutes_left:02d}:{seconds_left:02d}")
        
    playsound(sound)

def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Enter an int please.")
            
def valid_sound_choice():
    while True:
        print("Please select a sound:")
        print("1. Monster Footsteps")
        print("2. Door knock")
        choice = validate_input("Enter 1 or 2 for your choice: ")
        if choice in [1,2]:
            return choice
        print("Enter a valid choice please. 1 or 2.")
            
            
minutes = validate_input("How much minutes: ")
seconds = validate_input("How much seconds: ")
total_seconds = minutes * 60 + seconds

sound_choice = valid_sound_choice()
if sound_choice == 1:
    sound_file = "monsterfootsteps.mp3"
else:
    sound_file = "doorknock.mp3" 
    
alarm(total_seconds, sound_file)