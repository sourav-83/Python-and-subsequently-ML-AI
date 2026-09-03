def grade_print(marks):
    if marks > 80:
        print("A+")
    elif marks > 70:
        print("A")
    elif marks > 40:
        print("B")
    else:
        print("F")

    return

number = int(input()) 
grade_print(number)