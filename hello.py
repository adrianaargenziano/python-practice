import random

name = input("What is your name? ")
hobby = input("What is your favorite hobby? ")
print(f"Wow {name}, {hobby} is an amazing hobby!")

# if hobby == "painting":
#     print("Since you love painting, you should check out the Louvre!")
# else:
#     print("I've never heard of that hobby, but it sounds awesome!")

suggested_hobbies = ["coding", "hiking", "photography", "knitting", "cooking", "baking", "gaming"]
lucky_pick = random.choice(suggested_hobbies)
print(f"Actually, you should try: {lucky_pick}!")

def review_hobby(the_hobby):
    if the_hobby == "painting":
        print("Since you love painting, you should check out Louvre!")
    else:
        print("I've never heard of that hobby, but it sounds awesome!")
review_hobby(hobby)
