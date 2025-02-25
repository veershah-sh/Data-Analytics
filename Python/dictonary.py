
# dictonary -> {key:value,...}
person = {
    "name" : "abc", 
    "age" : 10,
    "profession" : "HR",
    "salary": [15000, 10000],
    "birth": ("Anand", "01/01/2001", "14.25"),
    "education": ["SSC", "HSC", "BCA"],
    "parents" : {
        "father": "xyz",
        "mother": "xyzz"
    },
    "isAlive": True
}

# to create a shallow copy of dict
new_person = person.copy()
print(new_person)

# to access any element
print(new_person['salary'])

# to update any value
new_person['salary'][0] = 25000

print(new_person['salary'])

print(new_person['education'])
new_person['education'].append("MCA")
print(new_person['education'])


product = {
    "id": 1,
    "product_name": "Iphone 15",
    "brand" : "Apple",
    "price": 150000,
    "category": ["mobiles", "electronics", "technology"],
    "features": (512, 12, 50, 20, "5g"),
    "extra_features": {
        "ram": (12,24,32),
        "storage": (128, 256, 512, 1024),
        "camera": {
            "front": 24,
            "rear": (24, 56)
        }
    },
    "description": "kfbfjsk afkjskfsf",
    "launch_date": "12 sept, 2024"
}

print(product['extra_features']['storage'][0])


p_category = product.fromkeys(["mobiles", "electronics", "technology"])


p_category['mobiles'] = 12
p_category['electronics'] = 13
p_category['technology'] = 14
print(p_category)