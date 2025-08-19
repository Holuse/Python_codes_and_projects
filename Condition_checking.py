while True:
    try:
        age = input("Please enter your age: ")
        age = int(age)
    except ValueError:
        print("Please enter a valid number\n")
        continue

    while True:
        school = input("Are you going to school? ").lower()
        if school == "yes" or school == "no":
            break
        else:
            print("Please enter yes or no\n")

    if age >= 18 and school == "no" :
        print("Its time to serve for the army")
    elif age >= 18 and school == "yes" :
        print("When you finish school you will serve for the army")
    else:
        print("You are not going to serve for the army")