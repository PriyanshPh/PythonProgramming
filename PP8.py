import random
def rohanMulti(num):
    wrong = random.randint(1, 9)
    table = [i * num for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 3)
    return table
def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i
    return None # if full table is correct then return None
if __name__ == '__main__':
    print(rohanMulti(7))
    numb = int(input("Enter a number: "))
    myTable = rohanMulti(numb)
    print(myTable)
    wrongIndex = isCorrect(myTable, numb)
    print(f"The table is wrong at index {wrongIndex}")