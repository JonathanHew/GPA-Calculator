print("GPA Calculator")

total = 0

# asking user to inout the amount of modules to be included in the GPA
num_modules = int(input("How many modules did you study? "))

# asking user for grade and credit amount for each module
for i in range(num_modules):
    print("Module: " + str(i + 1))
    percentage = int(input("What percentage grade did you get in this module ? "))
    credit = int(input("How many credits was this module ? "))

    #if statement to convert the percentage to a grade point value 
    if percentage < 40:
        gradePointValue = 0.0
    elif percentage >= 40 and percentage < 45:
        gradePointValue = 2.0
    elif percentage >= 45 and percentage < 50:
        gradePointValue = 2.5
    elif percentage >= 50 and percentage < 60:
        gradePointValue = 2.75
    elif percentage >= 60 and percentage < 65:
        gradePointValue = 3.0
    elif percentage >= 65 and percentage < 70:
        gradePointValue = 3.5
    else:
        gradePointValue = 4.0

    print(gradePointValue)
    



