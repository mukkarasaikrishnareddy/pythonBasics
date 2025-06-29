import  random
print("welcoe to the number gussening game")
print("instructions: \n")
print("1. I will think of a number between 1 and 100.")
print("2. You have to guess the number.")
print("3. I will tell you if your guess is too high, too low, or correct. You need to guess the closest number.")
print("4. You have 7 attempts to guess the number.\n")
number = random.randint(1,100)
guess = 7
while guess > 0:
    print("your guess is ",guess)
    your_number = int(input("enter your number:"))
    if your_number < number:
        print("your guess is too low")
    elif your_number > number:
        print("your guess is too high")
    else:
        print("woow! your guess is correct  you won")
        break
    guess -= 1