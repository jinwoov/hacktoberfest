# Factorial of a Number
# Contributed by: Mahima

# User may input any number whose Factorial needs to be obtained.
n = int(input("Enter a number: "))

# Defining all the possible conditions and print.
if (n < 0):
    print("Factorial cannot be found for negative numbers")

elif (n == 0 or n == 1):
    print("Factorial of ", n, " is 1")

else:
    fact = 1
    for i in range (2, n+1):
        fact *= i
    print("Factorial of ", n, " is ", fact)
