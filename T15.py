print("Enter the first number")
n = float(input())
print("Enter the Second number")
m = float(input())
print("Enter input 1 for add, 2 for sub, 3 for mult & 4 for div")
Operation = float(input())
add = 1
sub = 2
mul = 3
div = 4
if Operation==add:
    if n+m==65:
        print("77")
    else:
        print("The result is:",n+m)
elif Operation==sub:
    print("The result is:",n-m)
elif Operation==mul:
    if n*m==135:
        print("555")
    else:
        print("The result is:",n*m)
elif Operation==div:
    if n/m==56/6:
        print("4")
    else:
        print("The result is:",n/m)