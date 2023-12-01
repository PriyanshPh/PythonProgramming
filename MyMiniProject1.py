# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book
# PRIYANSH LIBRARY = Library(list of all books, library name)
# Dictionary:-
# Key = Books & value = Name of Person
# create a main function & run an infinite while loop asking users for their input
class Library:
    import datetime
    date = datetime.datetime.now()
    List = ["Books we have "'HeHa', 'HaHe', 'TikTok']
    print(List)
    List.append('HaHe')
    print(List)
    print("Enter 1 for lend book & 2 for add/return book")
    LIB = int(input())
    if(LIB == 1):
        print("Enter 1 for Book HeHa, 2 for Book HaHe, 3 for Book TikTok")
        Lib = int(input())
        if(Lib == 1):
            (List).remove('HeHa')
            print("You choose HeHa Book. Please Write your full name :- ")
            f = open("Mini.txt", "a")
            value = input()
            a = f.write(f"HeHa Book :{value} {str(date)}")

        elif (Lib == 2):
            print("You choose HaHe Book. Please Write your full name :- ")
            f = open("Min.txt", "a")
            value = input()
            a = f.write("HaHe Book : " + value +"\n")
        elif (Lib == 3):
            print("You choose TikTok Book. Please Write your full name :- ")
            f = open("MI.txt", "a")
            value = input()
            a = f.write("TikTok Book : " + value + "\n")