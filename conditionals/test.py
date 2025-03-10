def num_check(x):
    match x:
        case 10 if x % 2 == 0:  # Match 10 only if it's even
            print("Matched 10 and it's even!")
        case 10:
            print("Matched 10, but it's not even.")
        case _:
            print("No match found")

num_check(10)
num_check(15)
