# write a function grade(score) that: 
# takes a number score (0-100).
print('Enter score')
try:
    score = int(input())

except:
    print("invalid")
    exit()


def grade(scores):
    # Returns the grade: 
    if scores > 100 or scores < 0:
        return "invalid"
    # A if score >= 90, 
    elif scores >= 90:
        grade = "A"

    # B if score >= 80,
    elif scores >= 80:
        grade = "B" 
    # C if score >= 70, 
    elif scores >= 70:
        grade = "C"
    # D if score >= 60, 
    elif scores >= 60:
        grade = "D"
    # F otherwise.
    else:
        grade = "F"
        print("you are not a failure")
    return grade

try:
    print(f"the grade of your score({score}) is {grade(score)}")

except:
    print("invalid")