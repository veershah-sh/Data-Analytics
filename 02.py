words = ["apple", "is", "beautiful", "sun", "day"]

short = 0
long = 0

for word in words:
    # print(len(word))
    if len(word)<=3:
        short =  short + 1
    elif len(word):
        long += 1
print(f"No. of short words: {short}")
print(short)
print(f"No. of long words: {long}")

