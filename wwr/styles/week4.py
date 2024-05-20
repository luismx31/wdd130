number = int(input("Please type a positive number:"))

while number < 0:
    print("sorry, that is a negative umber. please try again.")
    number = int(input("Please type a positive number:"))
    

    print(f"The number is {number}")