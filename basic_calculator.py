t = None
while True:
    if t is None:
        while True:
            try:
                x = int(input("Enter a number: "))
                break
            except ValueError:
                print("Enter a valid number")

        while True:
            try:
                y = int(input("Enter another number: "))
                break
            except ValueError:
                print("Enter a valid number")
    else:
        x = t
        while True:
            try:
                y = int(input("Enter another number: "))
                break
            except ValueError:
                print("Enter a valid number")

    while True:
        z = input("Choose an operator (+, -, *, /): ")
        if z == "+":
            t = x + y
            break
        elif z == "-":
            t = x - y
            break
        elif z == "*":
            t = x * y
            break
        elif z == "/":
            if y == 0:
                print("Cannot divide by zero!")
                continue
            t = x / y
            break
        else:
            print("Invalid input, please try again.")

    print("Result: " + str(t))
    r = input("Press Enter to continue or 'q' to quit: ")
    if r.lower() == "q":
        print("Exiting...")
        break
