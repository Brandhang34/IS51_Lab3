



''' PLAIN ENGLISH
start
Create a list to store 5 number (float)
Capture user's input 5 times for their grades
Each time we capture the user's input we, append the number to the list
Sort the list ascending. Then splice the item starting at index 2
since we have three highest number in the list, we add them up and divide by 3
output a number to the user
end
'''

'''
create list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

sort the list, then splice out the two lowest numbers 

print message to user
'''

# grades = []

# grade = input("Enter the 1st grade: ")
# grades.append(float(grade))

# grade = input("Enter the 2nd grade: ")
# grades.append(float(grade))

# grade = input("Enter the 3rd grade: ")
# grades.append(float(grade))

# grade = input("Enter the 4th grade: ")
# grades.append(float(grade))

# grade = input("Enter the 5th grade: ")
# grades.append(float(grade))

# grades.sort()
# grades = grades[2:]
# grades = sum(grades)
# result = grades / 3

# print("Average Grade {0:2f}%".format(result))


grades = []

for i in range(5):
    grades.append(float(input("Enter the grade: ")))

grades.sort()
grades = sum(grades[2:]) / 3

print("Average Grade {0:.2f}%".format(grades))