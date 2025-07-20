# i = 1
# while i < 6:
#     print(i)
#     i += 1

# i = 1
# while True: # infinite loop
#     if i > 5:
#         break
#     print(i)
#     i += 1


# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i += 1


# n = int(input("Enter a number:"))
# i = 1
# total = 0

# while i <= n:
#     total += i
#     i += 1

# print(total)


# import random

# n = random.randint(1,10)

# userInput = int(input("Enter a number"))

# while userInput != n:
#     print("wrong!")
#     userInput = int(input("Enter a number: "))

# print("correct!")


## for a given number n, if n is even, then divide by 2
## if n is odd, multiply by 3 then add 1
## repeat until n = 1

# n = int(input("Enter a number: "))
# print(n)

# while n != 1:
#     if n % 2 == 0:
#         n = n/2
        
#     else:
#         n = (n * 3) + 1 
    
#     print(n)


## random select 1 - 100
## user has 7 attempts
## after each guess, tell if too high, too low or correct
## if user guess correctly - win
## if run out of guesses - end lose
## ask if play again

import random

def game():
    n = random.randint(1,100)

    attempts = 0

    while attempts < 7:
        userInput = int(input("Enter your guess: "))

        if userInput != n:
            if userInput > n:
                print("Too high!")
            else:
                print("Too low!")
        
            attempts += 1
            
        else:
            print("Correct you win!")
            break

    if userInput != n:
        print("You lose!")


game()

while True:
    if input("Do you want to play again? y/n: ") == "y":
        game()
    else:
        break




#     playAgain = input("Do you want to play again? y/n: ")
#     if playAgain == "y":
#         game()
#     else:
#         print("Goodbye!")

# game()




