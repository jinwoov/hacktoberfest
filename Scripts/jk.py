from time import sleep

## iterating to the forloop
def iterator(numb):
    for i in range(1,numb):
        print(f"Mochi love you")
        sleep(.01)


def interface():
    userInput = input("""
    
    1) Iterator
    2) Exit

    """)

    if(userInput == "1"): 
        how_many = input("how much do you want to iterate?")
        iterator(int(how_many)) 
    else: 
        print("Thank you for playing")
        exit()

interface()
    