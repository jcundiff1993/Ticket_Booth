print("Welcome to the ticket booth!\n")

ticket_price = 0

height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster!\n")
    age = int(input("What is your age?\n"))
    if age < 12:
        ticket_price += 5
    elif age <=17:
        ticket_price +=7
    else:
        ticket_price +=12

    print(f"Your ticket price is ${ticket_price}.\n")

    photos = input("Would you like to add photos for $3? Y or N. \n")
    if photos == "Y":
        ticket_price +=3
    else:
        ticket_price +=0

    print(f"Your total is ${ticket_price}.")

else:
    print("You are not tall enough to ride this ride.")