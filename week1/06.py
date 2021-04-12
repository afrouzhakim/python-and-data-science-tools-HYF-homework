import random
rand_num = random.randint(1,10)
while True:
    your_guess = int(input("Please guess a number : "))
    if rand_num == your_guess:
        print("your guess is correct!")
        break