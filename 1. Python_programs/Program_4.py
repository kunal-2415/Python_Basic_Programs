"""
What is Palindrome Number?

Answer - A palindromic number is a number that remains the same when its digits are reversed.
         In other words, it has reflectional symmetry across a vertical axis.
         The term palindromic is derived from palindrome, whose spelling is unchanged when its letters are reversed.
"""

""" Check a number is Palindrome or not. """

# Here I use While loop itterative statement. 

n = int(input("Enter a number"))
temp = n
rev = 0

while(n>0):
  digit = n%10
  rev = rev*10+digit
  n = n//10

if temp==rev:
  print("Number is Palindrome")
else:
  print("Number is not palindrome")