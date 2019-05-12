user_input = float(input("Enter your cgpa: "))

if user_input <4.0 and user_input >= 3.7:
    print("your graede is A+")
elif user_input < 3.7 and user_input >= 3.5:
    print("your grade is A")
elif user_input < 3.5 and user_input >= 3.0:
    print("your grade is B")
elif user_input < 3.0 and user_input >= 2.5:
    print("your grade is C")
else:
    print("You are Fail")


