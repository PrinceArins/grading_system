name = input ("Enter your name: ")
score = int(input("Enter your score: "))

# if score >= 80 and score <= 100:
#     print("You got an A")
# elif score >= 70 and score <= 79:
#     print("You got a B")
# elif score >= 60 and score <= 69:
#     print("You got a C")
# elif score >= 45 and score <= 59:
#     print("You got a D")
# elif score >= 35 and score <= 44:
#     print("You got an E")
# elif score >= 0 and score <= 34:
#     print("You got a F")
# else:
#     print("invalid entry")


if score >= 80 and score <= 100:
    print(f"{name} got an A")
elif score >= 70 and score <= 79:
    print(f"{name} got a B")
elif score >= 60 and score <= 69:
    print(f"{name} got a C")
elif score >= 45 and score <= 59:
    print(f"{name} got a D")
elif score >= 35 and score <= 44:
    print(f"{name} got an E")
elif score >= 0 and score <= 34:
    print(f"{name} got a F")
# else:
#     print(f"{name}, you did not write this exam")

else:
    print(f"{name.capitalize()}, you did not write this exam")