Number=int(input("how many courses do you take\n"))
courses = {}
lettered = {}
Current_GPA = 0
grade_points = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.5,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

def accept_mark( x: int, grade_points: dict ) -> dict:
    for i in range (0, x, 1):
        coursesName = input(f"Input your course { i + 1 } name\n")
        for value in grade_points.values(): 
            print(f"{value}", end=" ")
        grade = float(input(f"\nInput your grade for course { i + 1 } from the above options\n"))
        if validate_inputs(coursesName, grade):
            courses [ coursesName ] = grade
        else: 
            print("Your input is incorrect, try again")
            break
    return courses


def validate_inputs(x, y)-> bool:

    if type(y) is float:
        if y <= 4:
            # This shows that the gpa is number below 4
            # Next checking if coursename exists  
            if x:
                return True
            else: return False
        else: False # This is if the gpa is above 4
    else:
        print("Input a number please")
        return False

def calculate_average_mark(i: dict) -> float:
    added = 0
    for i in i.values():
        added += float(i)

    if len(courses) != 0:
        Current_GPA = added/len(courses)
        return Current_GPA
    else: print("courses can not be empty")

def letter_grade(x: dict, grade_points: dict) -> dict:
    
    # x is current courses dictionary
    for key_x, value_x in x.items():
        for key_graded, value_graded in grade_points.items():
            if value_x == value_graded:
                lettered[key_x]= key_graded
    return lettered
