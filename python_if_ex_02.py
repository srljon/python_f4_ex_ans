"""
Create a program that determines if a student is eligible to graduate
based on their final grade and attendance rate. The conditions are:
1. The student must have a final grade of 70 or higher
2. AND the student must have an absence rate of 20% or less
3. OR if the student has a perfect grade of 100, they can graduate
    even with a higher absence rate
"""

# Get student's grade and attendance information from user
final_grade = int(input("Enter your final grade (0-100): "))    # Convert input to integer
absence_rate = float(input("Enter your absence rate (0-100%): ")) # Convert input to float

# Check graduation eligibility using compound conditions
if (final_grade >= 70 and absence_rate <= 20) or final_grade == 100:
    # Student passes if they have:
    # - Grade ≥ 70 AND absence rate ≤ 20%
    # OR
    # - Perfect grade of 100 (regardless of absence)
    print("The student is eligible to graduate.")
else:
    # Student fails if they don't meet either condition above
    print("The student is not eligible to graduate.")