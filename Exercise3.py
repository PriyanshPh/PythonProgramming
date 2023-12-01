""" Pattern Printing :->
 Input = Integer n
 where, n=no. of rows
 Boolean = True or False
 True :-> n=4                                     False :-> n=4
 ****                                                 *
 ***                                                  **
 **                                                   ***
 *                                                    ****"""
try:
    n = int(input("Numbers of rows you want\n"))
    i = int(input("Enter 0 or 1\n"))
    if (i == 1):
        for j in range(0, n + 1):
            print("*" * j)
    if (i == 0):
        for j in range(n, 0, -1):
            print("*" * j)
except Exception as e:
    print("Enter valid key")