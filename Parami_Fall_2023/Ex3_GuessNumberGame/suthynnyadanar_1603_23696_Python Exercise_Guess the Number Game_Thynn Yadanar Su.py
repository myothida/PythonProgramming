import random
import sys
import time

win = False
game_start = ''
chance = 10
min = 0
max = 1500
hint = ''

#process the guess 
def game_play():  
    global user_number, comp_number, chance
    
    # Resetting the chance to 10 if a new game is started
    if (game_start == 'y' and chance == 0): chance = 10 
    
    comp_number = random.randint(min, max)      
    
    print("\nPlease guess a number between 0 - 1500.")
    
    while(chance > 0):
        #until the chance becomes zero, the game will be processed
        if (chance != 0):                     
                if (chance != 1):
                    print("\n*** You now have {} chances to win ***\n".format(chance))
                else:
                    print("\n☆ ★ ✮ ★ ☆ This is your FINAL chance! ☆ ★ ✮ ★ ☆")  
                    
                #A chance for a hint at the final chance
                give_hint(chance)
                
                #validating the input to make sure as numbers
                while True:                     
                    try:
                        user_number = int(input("Guess the number: "))
                        if user_number in range (min, max+1):
                            break
                        else:
                            print("\nWARNING ----Please enter a number between {} and {}.".format(min,max))
                    except ValueError:
                        print("\nWARNING ---- Please enter numbers only!\n")
               
                #processing for the win result
                if (chance != 1):   #not to show this prompt after the last guess
                    if (user_number > comp_number):       
                        if (user_number - comp_number > 5):
                            print("Too big! Try something smaller..")
                        else:
                            print("Ahhh, you are very close! Try something smaller..")
                    elif (comp_number > user_number):
                        if (comp_number - user_number  > 5):
                            print("Too small! Try something bigger..")
                        else:
                            print("Ahhh, you are very close! Try something bigger..")
                    else:
                       win = True
                       break
               
                chance -= 1
        else:
            win = False 
            break
  
#display result
def game_finish(win):
    print("\n**********************************************************")
    if win:
        print("Woohoo! You just won!!!")
    else:
        print("\nYou used up all your chances. You LOST!! \nThe number was {}.".format(comp_number))

#start a new game
def new_game(game_start):
    #validating to make sure the input is correct
    while True:            
        try:
            game_start = input("\nEnter Y for a new game. Or, enter N to quit. \n").lower()
            if (game_start == 'y' or game_start =='n'):
                break
            else:
                print("\nWARNING ---- Please enter the alphabet correctly!")
        except ValueError:
            print("\nWARNING ---- Please enter the alphabet correctly!\n")
    
    #all 3 functions is called so that the program still runs after previous         
    if (game_start == 'y'):
        game_play()
        game_finish(win)
        new_game(game_start)
    else:
        print("\nOh! You quit the game. :( \nThe game is ended!")
        time.sleep(1)
        print("Good game!")
        time.sleep(1)
        print("WELL PLAYED!\n")
        time.sleep(1)
        print("See you next time!!! (◠‿◠)")
        sys.exit()

#Giving a hint
def give_hint(chance):
    if (chance == 1):
        #validating to make sure the input is correct
        while True:            
            try:
                time.sleep(1)
                give_hint = input("\nWant a Hint? Enter H for a hint. Or, enter N to deny. \n").lower()
                if (give_hint == 'h' or give_hint =='n'):
                    break
                else:
                    print("WARNING ---- Please enter the alphabet correctly!")
            except ValueError:
                print("\nWARNING ---- Please enter the alphabet correctly!\n")
        
        #if the user's decision is to get a hint,
        if (give_hint == 'h'):
           hint = f"{'EVEN' if (comp_number%2 == 0) else 'ODD'}"
           print("It is {} number.".format(hint)) 

#program starts here
#validating to make sure the input is correct
while True:
    try:
        game_start = input("\nPlease enter Y to start the game.\n").lower()
        if (game_start == 'y'):
            break
        else:
            print("WARNING ---- Please only enter Y.")
    except ValueError:
        print("\nWARNING ---- Please enter the alphabet correctly!\n")

while (game_start == 'y'):
    game_play()
    game_finish(win)
    new_game(game_start)

        
