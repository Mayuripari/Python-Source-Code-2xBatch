# Write and calculate grade based on numerical score
# A- 90-100
# B- 80-89
# C- 70-79
# D- 60-69
# F- 0-59
score = int(input("Enter your marks : "))
if score <= 100 and score >= 90:
    print("Grade A")
elif score <= 89 and score >= 80:
    print("Grade B")
elif score <= 79 and score >= 70:
    print("Grade C")
elif score <= 69 and score >= 60:
    print("Grade D")
elif score <= 59 and score >= 0:
    print("Grade F")
else:
    print("Invalid Input")
