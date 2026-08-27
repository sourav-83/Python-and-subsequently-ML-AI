marks = []

for i in range(5):

    print("inside loop")
    if i == 3:
        continue
    print(f"value of i: {i}" )
    number = int(input())
    marks.append(number)

print(marks)
