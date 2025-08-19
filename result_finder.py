while True:
    midterm_exam = float(input("Enter the midterm exam score : "))
    if midterm_exam > 100 or midterm_exam < 0:
        print("Please enter a number between 0 and 100")
        continue
    final_exam = float(input("Enter the final exam score : "))
    if final_exam > 100 or final_exam < 0:
        print("Please enter a number between 0 and 100")
        continue
    final_note = final_exam * 60 /100 + midterm_exam * 40 /100
    print(f"Your final exam score is: {final_note}\n")
    if final_note > 50:
        print("You passed!")
    else:
        print("You failed!")
    cont = input("Press enter to try again or 'q' to quit: ")
    if cont.lower() == "q":
        break
    else:
        continue