from random import randint as r #Generates random number from 0 to 100
x=r(0,100)
i=0
while i!=10: #loop while will work until 10 attempts will run out
  i=i+1 
  guess=input("Enter your guess: ") #Player can enter his guessing number
  try:
    if int(guess)>100 or int(guess)<0:
      print("Enter number from 0 to 100")
      i=i-1 #If the value is incorrect, it won't count as an attempt to guess the number
    if i==10:
      print("You lost") #If all 10 attempts were used, the game is over
      while True:
        try:
          Answer = int(input("Do you wanna play again? Yes(1)/No(2): ")) #If someone wants to continue the game, they can enter 1 to continue or 2 to exit
          if Answer==1: #Continues the game
            x=r(0, 100)
            i=0
            break
          elif Answer==2: #Exits the game
            break
        except ValueError: #Incorrect value will return to the same question
          print("Enter correct value('1' to continue and '2' to exit game): ")
      if Answer == 2:
        break
    elif int(guess)>x: #If the guessed number is greater than actual one, program will say 'Too high, try again'
      print("Too high, try again!")
      continue
    elif int(guess)<x: #If the guessed number is lower than actual one, program will say 'Too low, try again'
      print("Too low, try again!")
      continue
    elif int(guess)==x:
      print("Correct!\nCongratulations! You won!") #If the guessed number is equal to the actual one, program will congratulate player
      while True:
        try:
          Answer = int(input("Do you wanna play again? Yes(1)/No(2): ")) #If someone wants to continue the game, they can enter 1 to continue or 2 to exit
          if Answer==1: #Continues the game
            x=r(0, 100)
            i=0
            break
          elif Answer==2: #Exits the game
            break
        except ValueError: #Incorrect value will return to the same question
          print("Enter correct value('1' to continue and '2' to exit game): ")
      if Answer == 2:
        break
  except ValueError: #Incorrect value will return player to guess the number again
    print("Enter correct value (integer from 0 to 100)")
    i=i-1
    continue