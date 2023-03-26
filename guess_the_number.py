import random

comp = random.randint(1,101)
you = None
guesses = 0
while(you!=comp):
    you = int(input("Enter your number:\n"))
    guesses += 1

    if you==comp:
        print("You guessed it right!")
    else:
        if you>comp:
            print("You guessed it wrong.Enter lower number please!")
        else:
            print("You guessed it wrong.Enter Higher number please!")

print(f"You guessed the number in {guesses} guesses.")

with open ("hiscore.txt","r") as f:
    hiscore = int(f.read())

if guesses<hiscore:
    print("You broke the high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
