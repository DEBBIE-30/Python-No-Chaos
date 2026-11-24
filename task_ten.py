import random
 rand_num = random.randrange(1,101)
 guesses = 0
 user_input = int(input("Input a number: "))
 while user_input != rand_num:
     user_input = int(input("Input a number: "))
     guesses+=1
 print("Well guessed")
 print(f"You took {guesses} attempts")
