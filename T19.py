print("This is a guessing game & You having only 11 chances to Guess\n ")
i = 0
while(i!=11):
    i += 1
    n = (input("Enter your number which is equal to my Guess number\n"))
    if(float(n)<11):
        print("Your enter number is less than my Guess number & your remaining guesses left are", 11-i)
    elif(float(n)==11):
        print("Good, Your Enter number is equal to my Guess number\n")
        print("Number of Guesses you use are", i)
        break
    elif(float(n)>11):
        print("Your enter number is Greater than my Guess number & your remaining guesses left are", 11-i)
    else:
        print("Please Enter a valid input\n")
if(i>=11):
    print("Sorry! you are finish your all guesses limit & My Guess number is", 11)

