marks = {"maths": 55, "science": 66, "english": 77, "computer": 88}

total = 0

for mark in marks:
    total += marks[mark]
    # print(marks[mark])


per = total/len(marks)
print(total)
print(per)