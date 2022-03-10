""" Given an integer, n, perform the following conditional actions: """

# 1. If n is odd, print Weird.
# 2. If n is even and in the inclusive range of 2 to 5, print Not Weird.
# 3. If n is even and in the inclusive range of 6 to 20, print Weird.
# 4. If n is even and greater than 20, print Not Weird.


n = int(input("Enter a Number"))                                   # User Input.
q = "weird"
s = "Not weird"                                    # Assign variables.
t = (n>=2) and (n<=5)
r = (n>=6) and (n<=20)

if (n%2!=0):                                            # Using if, else.
    print(q)
elif(n%2==0 and t):                                     # Also using Operators.
    print(s)
elif(n%2==0 and r):
    print(q)
elif(n%2==0 and n>20):
    print(s)
else:
    print()