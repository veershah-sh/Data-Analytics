fruits = {"apple", "orange", 14, True}
vegies = {"apple", "orange",True, 14}

temp = fruits
print(fruits is not temp)

print(fruits is vegies) #false
print(fruits == vegies) # true 
