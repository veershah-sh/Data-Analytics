sub1 = int(input("Enter marks of sub1: "))
sub2 = int(input("Enter marks of sub2: "))
sub3 = int(input("Enter marks of sub3: "))

total = sub1 + sub2 + sub3

per = total/3

grade = ''

if(per>=90):
    grade = "A"
elif(per>=70):
    grade = "B"
elif(per>=50):
    grade = "C"
else:
    grade = "F"

print("========Marksheet=======")
print(f"Total: {total}")
print(f"Per: {per}")
print(f"Grade: {grade}")

