# Name: Tenieya Craig
# File Name: student_application.py
# Description: Accepts student names and GPAs. Checks if the student qualifies for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter the student's last name(or 'ZZZ' to quit): ")

    if last_name == 'ZZZ':
        break
    
    first_name = input("Enter student's first name: ")

    gpa = float(input("Enter student's GPA: "))
        
    # Checks the gpa. Makes it so if it's greater than or equal to 3.5, it goes to Deans
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    
    # Checks the gpa. Makes this one so if it's less than or equal to 3.25, prints Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll!")
            
    else:
        print(f"{first_name} {last_name} doesn't qualify for the Dean's List or Honor Roll.")
        break 

# Since it's a while True statement, it will repeat after the final break and keeps on repeating