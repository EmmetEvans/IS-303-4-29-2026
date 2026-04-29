"""
Inputs:
- Student name
- Grades for 3 classes
- Credits for 3 classes

Processes:
- Calculate GPA using grades and credits

Outputs:
- GPA report
"""
#Inputs
name = input("Student name: ")
grade1 = float(input("First class grade point: "))
grade2 = float(input("Second class grade point: "))
grade3 = float(input("Third class grade point: "))
credit1 = int(input("First class credits: "))
credit2 = int(input("Second class credits: "))
credit3 = int(input("Third class credits: "))

#Processing
total_credit = credit1 + credit2 + credit3
GPA = ((grade1*credit1)+(grade2*credit2)+(grade3*credit3))/total_credit

#Output
print(f"Report card for {name}:"
      f"\nCourse 1: {grade1} credits: {credit1}"
      f"\nCourse 2: {grade2} credits: {credit2}"
      f"\nCourse 3: {grade3} credits: {credit3}"
      f"\nTotal credit hours taken: {total_credit}"
      f"\nCumulative GPA: {GPA:.2f}")