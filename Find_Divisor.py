try:
    n = int(input("How many numbers of apple have you got:\n"))
    print("Now, provide the range of divisior numbers:\n")
    mn = int(input("Type mininum number in your range:\n"))
    mx = int(input("Type maximum number in your range:\n"))
except ValueError:
    print("Only integer numbers are supported")
    exit()
if(n>=mx or n>=mn):
    if (mn == mx):
        print("Your enter numbers of minimum & maximum range is same:\n")
        nx = n / mx
        if (nx == int(nx)):
            print(f"{mx} is a divisor of {n}")
        else:
            print(f"{mx} is not a divisor of {n}")
    elif (mn < mx):
        while (mn != mx + 1):
            nx = n / mn
            if (nx == int(nx)):
                print(f"{mn} is a divisor of {n}")
            else:
                print(f"{mn} is not a divisor of {n}")
            mn += 1
    elif (mn > mx):
        while (mn + 1 != mx):
            nx = n / mx
            if (nx == int(nx)):
                print(f"{mx} is a divisor of {n}")
            else:
                print(f"{mx} is not a divisor of {n}")
            mx += 1
else:
    print(f"Your given numbers of range are not divisior of {n}")
