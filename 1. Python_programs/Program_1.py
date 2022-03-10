""" Find the temperature from taking a input from user. """

# Here I Use If, elif, else Selective Statements.

n_temp = int(input("Enter Temperature"))

a = "Ohh!!! Its very hot"
b = "Ahh!!! good temperature"
c = "Ahh!! Its cold"
d = "Ohhh!!! Its freezing"

if n_temp>45:
    print(a)
elif n_temp>20 and n_temp<45:
    print(b)
elif n_temp>1 and n_temp<20:
    print(c)
elif n_temp<1:
    print(d)
else:
    print()
