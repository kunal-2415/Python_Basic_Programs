""" Program to display the Fibonacci sequence up to n-th term. """

# Fibonacci sequence numbers [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]

def fibonacci_series(n):
    if n < 0:
        print("Wrong Input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)


print(fibonacci_series(11))