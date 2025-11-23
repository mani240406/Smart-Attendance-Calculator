# Attendance Calculator in Python

# Input
total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

# Calculation
percentage = (attended_classes / total_classes) * 100

# Output
print("Attendance Percentage = {:.2f}%".format(percentage))

# Eligibility Check
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")
