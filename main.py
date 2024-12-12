a = 10 
b = 12
print(a != b)

x = 4
y = 5

if (x == 4) != (y == 5):
    print("Hi.")

a = 7
b = 3
c = 19
print(bool(a))
if a and b and c:
    print(a and b and c)
    print("All values have boolean as true.")
else:
    print("At least one value has boolean has false.")
if a > 0 and b > 0:
    print("Both numbers are greater than 0.")
else :
    print("Either a or b are not greater than 0.")
if a > 0  or b > 0:
    print("One of the numbers are greater than 0.")
else :
    print("Both numbers a or b are not greater than 0.")