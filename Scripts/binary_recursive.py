# print out all possible binary numbers given
# length l

# oh god please don't judge my code

def binary(length, current):
    if len(current) == length:
        print(current)
        return
    else:
        binary(length, current + "0")
        binary(length, current + "1")

l = int(input("Enter length: "))

binary(l, "")
