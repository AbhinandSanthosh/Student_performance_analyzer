# student_analyzer.py
import psycopg2

def get_valid_marks(subject):

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

    if avg >= 90:
        return "A"

    elif avg >= 75:
        return "B"

    elif avg >= 60:
        return "C"

    else:
        return "Fail"


def display_report(student):

    print("\n------ Student Report ------\n")

    print(f"Name        : {student['name']}")
    print(f"Roll Number : {student['roll_number']}\n")

    print(f"Python      : {student['python']}")
    print(f"SQL         : {student['sql']}")
    print(f"ML          : {student['ml']}\n")

    print(f"Total       : {student['total']}")
    print(f"Average     : {student['average']:.2f}")
    print(f"Grade       : {student['grade']}")


def save_to_database(student):

    try:
        connection = psycopg2.connect(
            host="localhost",
            database="student_db",
            user="postgres",
            password="abhinand12",
            port="5432"
        )

        cursor = connection.cursor()

        query = """
        INSERT INTO students
        (
            name,
            roll_number,
            python_marks,
            sql_marks,
            ml_marks,
            total,
            average,
            grade
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            student['name'],
            student['roll_number'],
            student['python'],
            student['sql'],
            student['ml'],
            student['total'],
            student['average'],
            student['grade']
        )

        cursor.execute(query, values)

        connection.commit()

        print("\nStudent data saved to PostgreSQL database successfully!\n")

        cursor.close()
        connection.close()

    except Exception as error:
        print("Database Error:", error)


def view_all_students():

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

    while True:

        print("====== Student Performance Analyzer ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            student = get_student_data()
            display_report(student)
            save_to_database(student)

        elif choice == "2":

            view_all_students()

        elif choice == "3":

            print("\nExiting Program...")
            break

        else:
            print("\nInvalid choice! Please try again.\n")


def main():

    menu()


# Program Execution Starts Here
if __name__ == "__main__":
    main()