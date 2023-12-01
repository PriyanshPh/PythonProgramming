m = 1
n = 1
for e in range(1, 3):
    import random
    random_num = random.randint(36, 69)
    i = 1
    print(f"Player {e} chance:")
    fr = int(input("Enter your number: "))
    if fr == random_num:
        print("Excellent, You win this guess game in your 1st chance")
        if e == 2:
            n += 1
            if m < n:
                print("You both win this game in your 1st chance")
            elif n < m:
                print(f"Player2 win this game because its takes only {n-1} chances to find guess number while Player2 takes {m} chances to find guess number")
    while (fr != random_num):
        if e == 1:
            m += 1
        elif e == 2:
            n += 1
        i += 1
        fr = int(input("Now, Try again to Enter nearest number: "))
        if fr == random_num:
            print(f"Nice, you takes {i} chances to win this game")
        elif fr < random_num:
            print("Guess some large number")
            continue
        elif fr > random_num:
            print("Guess some small number")
            continue
        if m < n:
            print(f"Player1 win this game because its takes only {m} chances to find guess number while Player2 takes {n} chances to find guess number")
        elif n > 1:
            if n < m:
                print(f"Player2 win this game because its takes only {n} chances to find guess number while Player2 takes {m} chances to find guess number")
            else:
                print(f"You both win this game in just {m} chances")
