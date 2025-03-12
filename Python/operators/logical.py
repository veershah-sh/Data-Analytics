"""
4. Logical Operators
    AND 
        -> con1 and con2 
        -> if both conditions are true -> true
        -> if any one condition is false -> false
        -> if both conditions are false -> false 
    OR
        -> con1 or con2 
        -> if both conditions are true -> true
        -> if any one condition is true -> true
        -> if both conditions are false -> false
    NOT
        -> inverse of and, or operators
        -> c1 and c2 -> true
        -> !(c1 and c2) -> false
        -> c1 or c2 -> false
        -> !(c1 or c2) -> true
"""

username = "abcd"
password = "abc@1234"

if(username == "abc" and password == "abc@123"):
    print("Welcome user")
else:
    print("Invalid username or password")

role = "hod"
isWorking = True

if(role =="hod" or isWorking):
    print("Access granted")
else:
    print("Access denied")
