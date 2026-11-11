
# Frontend done by Ai for the backend i tried to encapsulate 
# it in another file and just imported it here, to check what
# i did on the backend proceed to SMS.py file

from SMS import (
    accept_mark,
    calculate_average_mark,
    letter_grade,
    Number,
    courses,
    grade_points
)

# Terminal colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"


def line(char="─", width=58):
    print(char * width)


def display_results(Number, courses, grade_points):
    # Collect course grades
    collections_courses = accept_mark(Number, grade_points)

    if not collections_courses:
        print(f"\n{RED}No course grades were entered.{RESET}")
        return

    # Calculate GPA using the collected grades
    average_gpa = calculate_average_mark(collections_courses)

    # Convert numeric grades to letter grades
    lettered = letter_grade(collections_courses, grade_points)

    # Dashboard header
    print(f"\n{CYAN}{BOLD}")
    line("═")
    print("          STUDENT MANAGEMENT SYSTEM")
    print("                GRADE REPORT")
    line("═")
    print(RESET)

    # GPA summary
    print(f"{BOLD}ACADEMIC SUMMARY{RESET}")
    line()

    print(f"  Total courses : {len(collections_courses)}")
    print(f"  Average GPA   : {GREEN}{BOLD}{average_gpa:.2f} / 4.00{RESET}")

    # Numeric grade table
    print(f"\n{BLUE}{BOLD}COURSE RESULTS{RESET}")
    line()

    print(f"{'No.':<5}{'Course Name':<30}{'GPA':>10}")
    line()

    for index, (course, grade) in enumerate(
        collections_courses.items(), start=1
    ):
        print(f"{index:<5}{course:<30}{grade:>10.2f}")

    line()

    # Letter grade table
    print(f"\n{YELLOW}{BOLD}LETTER GRADE REPORT{RESET}")
    line()

    print(f"{'Course Name':<35}{'Letter Grade':>15}")
    line()

    for course, grade in lettered.items():
        print(f"{course:<35}{str(grade):>15}")

    line("═")
    print(f"{CYAN}             END OF REPORT{RESET}")
    line("═")


display_results(Number, courses, grade_points)
