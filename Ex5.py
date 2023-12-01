def getdate():
    import datetime
    return datetime.datetime.now()
DT = getdate()
print("Press 1 for Lock or 2 for Retrieve")
LR = int(input())
if(LR == 1):
    print("Select your name 1 for P, 2 for K, 3 for S")
    PKS = int(input())
    if(PKS == 1):
        print("Press 1 for Diet & 2 for Exercise")
        DE = int(input())
        if (DE == 1):
            print("Write :- ")
            f = open("PD.txt", "a")
            value = input()
            a = f.write(str([str(DT)])+":"+value)
        elif (DE == 2):
            print("Write :- ")
            f = open("PE.txt", "a")
            a = f.write(str(DT)) + f.write(":") + f.write(input())
    elif (PKS == 2):
        print("Press 1 for Diet & 2 for Exercise")
        DE = int(input())
        if (DE == 1):
            print("Write :- ")
            f = open("KD.txt", "a")
            a = f.write(input())
        elif (DE == 2):
            print("Write :- ")
            f = open("KE.txt", "a")
            a = f.write(input())
    elif (PKS == 3):
        print("Press 1 for Diet & 2 for Exercise")
        DE = int(input())
        if (DE == 1):
            print("Write :- ")
            f = open("SD.txt", "a")
            a = f.write(input())
        elif (DE == 2):
            print("Write :- ")
            f = open("SE.txt", "a")
            a = f.write(input())
elif(LR ==2):
    print("Select your name 1 for P, 2 for K, 3 for S")
    PKS = int(input())
    if(PKS == 1):
        print("Press 1 for Diet & 2 for Exercise")
        DE = int(input())
        if (DE == 1):
            f = open("PD.txt", "r")
            print(f.readlines())
        elif (DE == 2):
            f = open("PE.txt", "r")
            print(f.readlines())
    elif (PKS == 2):
        print("Press 1 for Diet & 2 for Exercise")
        DE = int(input())
        if (DE == 1):
            f = open("KD.txt", "r")
            print(f.readlines())
        elif (DE == 2):
            f = open("KE.txt", "r")
            print(f.readlines())
    elif (PKS == 3):
        print("Press 1 for Diet & 2 for Exercise")
        DE = int(input())
        if (DE == 1):
            f = open("SD.txt", "r")
            print(f.readlines())
        elif (DE == 2):
            f = open("SE.txt", "r")
            print(f.readlines())