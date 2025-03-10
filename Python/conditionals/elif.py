'''
Syntax: 
if(conditon):
    if condition true -> output
elif(condition 2):
    if condition 2 is true -> output
elif(condition 3):
    if condition 3 is true -> output
else:
    if condition false -> output
'''

num = int(input("Enter any number: "))

if(num>0):
    print(f"{num} is +ve")
elif(num<0):
    print(f"{num} is -ve")
# elif(num == 0):
else:
    print("num is 0")