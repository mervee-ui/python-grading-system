while True:
    print("welcome to grading system")

    exit_input = input("press q to quit or Enter to continue: ")
    if exit_input.lower() == "q":
         break
    
    name  = input("enter your name:")
    grade = int(input("please enter your grade:"))

    if 0 <= grade <= 49:
         print("failed,you have to work more")

    elif 50 <= grade <= 69:
         print("avarage,you are going better")

    elif 70 <= grade <= 100:
         print("good,congratilations")

    else:
         print("""invalid grade
please check your grade """)
         continue

    print(f"{name} , your grade is {grade}")