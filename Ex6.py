print("Lets Start Snake, Water, Gun Game & You have only 3 chances to win this Game")
i = 0
n = 3
CP = 0
HP = 0
DW = 0
while(i<n):
    i += 1
    print("Select your Character & Type here same as written:-\n Snake\n Water\n Gun")
    SWG = input()
    import random
    lst = ["Snake", "Water", "Gun"]
    choice = random.choice(lst)
    if(SWG == choice):
        print("Your Selected Character:-", choice)
        print("Computer Select :-", choice)
        print("Then it's a tie because you both select same character\nTherefore, you both take 1 point")
        CP += 1
        HP += 1
        DW = DW + 1
        print("Computer Score :-", CP, "Your Score:-", HP)
        print("Now your left chances:-", n - i)
    elif(SWG == "Snake") and (choice == "Gun"):
        CP += 1
        print("Your Selected Character:-", SWG)
        print(f"Computer Select :- {choice}")
        print("In this round Computer wins 1 point")
        print("Computer Score :-", CP, "Your Score:-", HP)
        print("Now your left chances:-", n - i)
    elif (SWG == "Snake") and (choice == "Water"):
        HP += 1
        print("Your Selected Character:-", SWG)
        print("Computer Select :-", choice)
        print("In this round You wins 1 point")
        print(f"Computer Score :- {CP} & Your Score:- {HP}")
        print("Now your left chances:-", n - i)
    elif (SWG == "Water") and (choice == "Gun"):
        HP += 1
        print("Your Selected Character:-", SWG)
        print("Computer Select :-", choice)
        print("In this round You wins 1 point")
        print("Computer Score :-", CP, "Your Score:-", HP)
        print("Now your left chances:-", n - i)
    elif (SWG == "Water") and (choice == "Snake"):
        CP += 1
        print("Your Selected Character:-", SWG)
        print("Computer Select :-", choice)
        print("In this round Computer wins 1 point")
        print("Computer Score :-", CP, "Your Score:-", HP)
        print("Now your left chances:-", n - i)
    elif (SWG == "Gun") and (choice == "Snake"):
        HP += 1
        print("Your Selected Character:-", SWG)
        print("Computer Select :-", choice)
        print("In this round You wins 1 point")
        print("Computer Score :-", CP, "Your Score:-", HP)
        print("Now your left chances:-", n - i)
    elif (SWG == "Gun") and (choice == "Water"):
        CP += 1
        print("Your Selected Character:-", SWG)
        print(f"Computer Select :- {choice}")
        print("In this round Computer wins 1 point")
        print(f"Computer Score :- {CP} & Your Score:- {HP}")
        print("Now your left chances:-", n - i)
    else:
        i -= 1
        print("Please Type Characters name as written\n")
print("Game Finish")
if CP>HP:
    print(f"Computer Score :- {CP}, Your Score:- {HP} & Total Draw round :- {DW}")
    print("Computer win this Game")
elif HP>CP:
    print("Computer Score :-",CP,", Your Score:-", HP, "& Total Draw round :-", DW)
    print("Nice, You win this Game")
elif CP == HP:
    print("You Both Earn Same Score. Then, This game is Tie & Total Draw round :-", DW)