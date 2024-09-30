"""
Create a program that determines if a student is eligible to graduate
based on their final grade and attendance rate. The conditions are:
1. The student must have a final grade of 70 or higher
2. AND the student must have an absence rate of 20\% \or less
3. OR if the student has a perfect grade of 100, they can graduate
    even with a higher absence rate
"""

final_grade = int(input("Enter your final grade (0-100): "))
absence_rate = float(input("Enter your absence rate (0-100%): "))

if (final_grade >= 70 and absence_rate <= 20) or final_grade == 100:
  print("The student is eligible to graduate.")
else:
  print("The student is not eligible to graduate.")