# student_analyzer.py

def get_valid_marks(subject):
    """
    Function to get valid marks from user.
    Ensures:
    - Only numeric input
    - Marks between 0 and 100
    """

    while True:
        try:
            marks = int(input(f"Enter {subject} Marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
            else:
                return marks

        except ValueError:
            print("Invalid input! Please enter numeric values only.")


def get_student_data():
    """
    Function to collect student details.
    Returns student data as dictionary.
    """

    print("\n------ Enter Student Details ------")

    name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")

    python_marks = get_valid_marks("Python")
    sql_marks = get_valid_marks("SQL")
    ml_marks = get_valid_marks("Machine Learning")

    total = python_marks + sql_marks + ml_marks
    average = total / 3

    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll_number": roll_number,
        "python": python_marks,
        "sql": sql_marks,
        "ml": ml_marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    return student


def calculate_grade(avg):
    """
    Function to calculate grade based on average marks.
    """

    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


def display_report(student):
    """
    Function to display student report.
    """

    print("\n------ Student Report ------\n")

    print(f"Name        : {student['name']}")
    print(f"Roll Number : {student['roll_number']}\n")

    print(f"Python      : {student['python']}")
    print(f"SQL         : {student['sql']}")
    print(f"ML          : {student['ml']}\n")

    print(f"Total       : {student['total']}")
    print(f"Average     : {student['average']:.2f}")
    print(f"Grade       : {student['grade']}")


def save_to_file(student):
    """
    Function to save student data into students.txt file.
    """

    with open("students.txt", "a") as file:

        file.write("------ Student Record ------\n")
        file.write(f"Name        : {student['name']}\n")
        file.write(f"Roll Number : {student['roll_number']}\n")
        file.write(f"Python      : {student['python']}\n")
        file.write(f"SQL         : {student['sql']}\n")
        file.write(f"ML          : {student['ml']}\n")
        file.write(f"Total       : {student['total']}\n")
        file.write(f"Average     : {student['average']:.2f}\n")
        file.write(f"Grade       : {student['grade']}\n")
        file.write("--------------------------------\n\n")

    print("\nStudent data saved successfully!\n")


def view_all_students():
    """
    Function to display all saved student records.
    """

    try:
        with open("students.txt", "r") as file:
            data = file.read()

            if data:
                print("\n------ All Student Records ------\n")
                print(data)
            else:
                print("\nNo student records found.\n")

    except FileNotFoundError:
        print("\nstudents.txt file not found.\n")


def menu():
    """
    Main menu function.
    """

    while True:

        print("====== Student Performance Analyzer ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            student = get_student_data()
            display_report(student)
            save_to_file(student)

        elif choice == "2":

            view_all_students()

        elif choice == "3":

            print("\nExiting Program...")
            break

        else:
            print("\nInvalid choice! Please try again.\n")


def main():
    """
    Main function.
    """

    menu()


# Program Execution Starts Here
if __name__ == "__main__":
    main()