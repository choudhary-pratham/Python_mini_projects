import random
import time

def random_pick1():
    a = ["Snake", "Water", "Gun"]
    rand = random.choice(a)
    return rand

def random_pick2():
    a = ["Snake", "Water", "Gun"]
    rand1 = random.choice(a)
    rand2 = random.choice(a)
    return rand1,rand2



def thanks1(x, y, z):
    print()
    print("thanks " + x + " for playing!")
    print(x + " points:" + str(z))
    print("computer points:", y)
    if y < z:
        print("Hurrah you won!!")
    elif y == z:
        print("draw!")
    else:
        print("ops! better luck next time.")


def thanks2(z, y):
    print()
    print("thanks adam for playing!")
    print("adam points:" , z)
    print("thanks eve for playing!")
    print(" eve points:", y)
    if y < z:
        print("Adam won!!")
    elif y == z:
        print("draw!")
    else:
        print("eve won!!")


def play1(i):
    cp = 0
    up = 0
    d = 0
    s = i
    while i > 0:
        computer_choice = random_pick1()
        user_choice = input("Enter your choice among Snake, Water, Gun:")

        if computer_choice == "Snake":
            if user_choice == "Water":
                print(" computer chose:",computer_choice)
                print(" Hard luck! try again")
                cp = cp+1
            elif user_choice == "Gun":
                print(" computer chose:", computer_choice)
                print("Good Work! Keep it up")
                up = up+1
            elif user_choice == "Snake":
                print(" computer chose:", computer_choice)
                print("No one got a point")
            else:
                print("Invalid input!")
                d = d+1

        if computer_choice == "Water":
            if user_choice == "Water":
                print(" computer chose:", computer_choice)
                print(" No one got a point")
            elif user_choice == "Gun":
                print(" computer chose:", computer_choice)
                print("Hard luck! try again")
                cp = cp+1
            elif user_choice == "Snake":
                print(" computer chose:", computer_choice)
                print("Good Work! Keep it up")
                up = up+1
            else:
                print("Invalid input!")
                d = d+1

        if computer_choice == "Gun":
            if user_choice == "Water":
                print(" computer chose:", computer_choice)
                print("Good Work! Keep it up")
                up = up + 1
            elif user_choice == "Gun":
                print(" computer chose:", computer_choice)
                print(" No one got a point")
            elif user_choice == "Snake":
                print(" computer chose:", computer_choice)
                print("Hard luck! try again")
                cp = cp + 1
            else:
                print("Invalid input!")
                d = d + 1
            print()
        i = i - 1
    if d != 0:
        if d == s :
            print()
            print("Result cannot be produced!")
            print("Computer points: NA")
            print("User point:NA")
    else:
        thanks1(user_name, cp, up)

def play2(i):
    pp1 = 0
    pp2 = 0
    while i > 0:
        adam, eve = random_pick2()
        if adam == "Snake":
            if eve == "Water":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print("Adam got a point.")
                pp1 = pp1 + 1
                time.sleep(1)
            elif eve == "Gun":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print("Eve got a point.")
                pp2 = pp2 + 1
                time.sleep(1)
            elif eve == "Snake":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print("No one got a point")
                time.sleep(1)

        if adam == "Water":
            if eve == "Water":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print(" No one got a point")
                time.sleep(1)
            elif eve == "Gun":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print("Adam got a point.")
                pp1 = pp1 + 1
                time.sleep(1)
            elif eve == "Snake":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print("Eve got a point.")
                pp2 = pp2 + 1
                time.sleep(1)

        if adam == "Gun":
            if eve == "Water":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print("Eve got a point.")
                pp2 = pp2 + 1
                time.sleep(1)
            elif eve == "Gun":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print(" No one got a point")
                time.sleep(1)
            elif eve == "Snake":
                print(" Adam chose:", adam)
                print(" Eve chose:", eve)
                print("Adam got a point.")
                pp2 = pp2 + 1
                time.sleep(1)
        print()
        time.sleep(1)
        i = i - 1
    thanks2(pp1, pp2)


choice = int(input("Enter 1 for human vs computer and 2 for computer vs computer:"))

if choice == 1:
    user_name = input("Enter your name to start:")
    i = int(input("Enter the number of chances you want to play:"))
    play1(i)

elif choice == 2:
    i = int(input("Enter the number of chances :"))
    play2(i)


print("Do you want to play again?")
r = input()
while 1:
    choice = int(input("Enter 1 for human vs computer and 2 for computer vs computer:"))
    if r == "y":
        if choice == 1:
            user_name = input("Enter your name to start:")
            i = int(input("Enter the number of chances you want to play:"))
            play1(i)
            print("Do you want to play again?")
            r = input()

        elif choice == 2:
            i = int(input("Enter the number of chances :"))
            play2(i)
            print("Do you want to play again?")
            r = input()
    else:
        print("Thank you for your participation!")
        break



