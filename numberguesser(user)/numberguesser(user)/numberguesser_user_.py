import random

cont = "a"
ans = 0

print("Welcome to the Number Guessing Game!")
print()

highscore = 0

while cont != "q":
    score = 0
    num = random.randint(1,100)
    print()
    ans = input("I'm thinking of a number! Can you guess what it is? ")
    ans = int(ans)

    while ans != num:
        if ans < num:
            if (ans + 10) >= num:
                ans = input("Woah, thats close! Try something a little higher than " + str(ans) + "! ")
            else:
                ans = input("Nope! Try something higher than " + str(ans) + "! ")
            ans = int(ans)
        elif ans > num:
            if (ans - 10) <= num:
                ans = input("Woah, thats close! Try something a little lower than " + str(ans) + "! ")
            else:
                ans = input("Nope! Try something lower than " + str(ans) + "! ")
            ans = int(ans)
        score += 1
        

    print()
    print("Good work, you got it! The number was " + str(num) + "! ")
    print("You successfully guessed the number in " + str(score) + " attempts!")

    if highscore == 0:
        highscore = score
    elif score < highscore:
        print()
        print("That was even better than your best score of " + str(highscore) + "! I'll remember that!")
        highscore = score
    elif highscore != 0:
        print()
        print("I bet you can't beat your best score! Try and go for better than " + str(highscore) + " next time!")

    print()
    cont = input("If you wanna play again, enter any letter other than 'q'! ")

print("Awww, well thanks for playing! Bye bye!")
