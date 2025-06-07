values = [-3, 5, -7, 2, 0, -1, 9]
positive = 0
negative = 0

for value in values:
    if value>=0:
        positive += 1
    elif value<0:
        negative += 1

print(f"Positive Values: {positive}")
print(f"Negative Values: {negative}")