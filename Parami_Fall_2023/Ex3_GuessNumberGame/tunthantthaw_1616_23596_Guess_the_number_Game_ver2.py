import random

choice = input("How do you want to play? Easy or Hard? - ").lower()

if choice not in ['easy', 'hard']:
    print("I don't understand what you are typing, but please choose 'easy' or 'hard'.")

#easy difficulty below

elif choice == "easy":
    def guess_number():

        rand = random.randint(1, 999)
        max_attempts = 10
        attempts = 0

        print("Guess what number I am thinking right now. It is between 1 and 999! You have 10 attempts.")

        while attempts < max_attempts:
            attempts += 1
            print("Attempt {}/{}.".format(attempts, max_attempts))
            user_input = int(input("Go on, take a guess: "))

            if rand == user_input:
                print("You got it! You win!")
                break
            elif rand > user_input:
                print("Too low bruv, guess higher!")
            else:
                print("Too high bruv, guess lower!")

        if attempts == max_attempts and rand != user_input:
            print(
                "Oh, seems like you've used all {} attempts. The number was {}. Sadge".format(max_attempts, rand))


    def choose():
        play_again = True

        while play_again:
            guess_number()
            choice = input("Do you want to guess again? Yes or no? : ").lower()
            play_again = choice == "yes"

    if __name__ == "__main__":
        choose()

#hard difficulty below
elif choice == "hard":
    user_input = "" #internet said the program will work if I just type "", IDK how this works to be honest.

    print("Since it is difficult, I will give you an unlimited amount of guesses. ")
    print("If you want to quit, just type 'quit' in console.")
    while user_input.lower() != "quit":

        rand = random.randint(1, 999)

        print("Guess what number I am thinking right now. ")

        user_input = input("Well? Start guessing - ")
        if user_input.lower() == "quit":
            print("You gave your best. But the answer is {}".format(rand))
            break

        try:
            evil_input = int(user_input)
            evil = random.randint(1, 999)

            if evil == evil_input:
                print("You got it! You win!")
            elif evil > evil_input:
                print("Too low bruv, guess higher!")
            else:
                print("Too high bruv, guess lower!")

        except ValueError:
            print("Nah, whatever you are writing, it is invalid.")
            print("Guess a number or type 'quit' to literally quit.")
