# List Types (Sequence Types)

# List[]

# List is a collection of items. 
# It is a mutable / changable.
# ordered sequence of elements.

cars = [1, "BMW", True, 55.256]
fruits = list(("apple", "banana", "cherry"))

# cars[3] = "mango"
# print(cars)
# print(fruits)

marks = [45, 65, 52, 25, 44]

# for mark in marks:
#     if mark >= 35:
#         print(mark + 4)
#     else:
#         print(mark)

# Tuple ()
# Tuple is a collection of items. 
# It is a immutable / unchangable.
# ordered sequence of elements.

price_list = (45, 598.23, 10.22)
age_group = tuple((45, 52, 474))

# price_list[1] = 5478
# print(price_list)
# print(age_group)


# Set {}
# not a sequence type
# Set is a collection of items
# it is mutable
# it stores only unique values

# marks1 = [10, 20, 30, 40, 30, 20]
# m1 = set(marks1)
nums = {10, 20, 30, 40, 30, 20}

# print(nums)


# Dictonary {}

# collection data type
# mutable
# it stores data in "key: value" pair

person = {
    "name" : "abc", 
    "age" : 10,
    "profession" : "HR",
    "salary": 15000,
    "education": ["SSC", "HSC", "BCA"],
    "parents" : {
        "father": "xyz",
        "mother": "xyzz"
    },
    "isAlive": True
}

# prints whole dictonary
print(person)

# it will print value of give key
print(person['age'])