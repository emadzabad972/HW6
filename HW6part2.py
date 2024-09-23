from random import randint

numm1: int = randint(1, 100)
guesses: int = 0

user: int = int(input("enter the requested number: "))

while user != numm1:
    if user > numm1:
        print("guess lower")
        guesses += 1
        user = int(input("enter the requested number: "))
    elif user < numm1:
        print("guess higher")
        guesses += 1
        user = int(input("enter the requested number: "))
else:
    print(f"bingo! you did it in {guesses} guesses")