# To check if a value is in a range, use two comparisons joined with 'and'


score = int(input("Score: "))

if score >=90 and score <=100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score <80:
    print("Grade: C")
elif score >=60 and score <70:
    print("Grade: D")
else:
    print("Grade: F")       


# to improve readability and efficiency

if 90 <= score and score <=100:
    print("Grade: A")
elif 80 <= score and score < 90:
    print("Grade: B")
elif 70 <= score and score <80:
    print("Grade: C")
elif 60 <= score and score <70:
    print("Grade: D")
else:
    print("Grade: F")

# further more improvement

if 90 <= score <=100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score <80:
    print("Grade: C")
elif 60 <= score <70:
    print("Grade: D")
else:
    print("Grade: F")

# best
# this optimization llows us to ask fewer questions and makes the code more readable

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


