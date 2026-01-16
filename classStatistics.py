import random


### Defining a class Course to represent a single course and the mark obtained
class Course:
    def __init__(self, course_name, mark):
        self.course_name = course_name
        self.mark = mark


### Defining a class to represent a Student
class Student:
    def __init__(self, student_id, name, age, gender, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.courses = []
        self.average_mark = 0.0
        self.rank = 0

    def add_course(self, course):
        if len(self.courses) < 10:
            self.courses.append(course)

    def calculate_average_mark(self):
        if not self.courses:
            self.average_mark = 0.0
            return 0.0

        total_marks = sum(course.mark for course in self.courses)
        self.average_mark = total_marks / len(self.courses)
        return self.average_mark


### Generating sample data
def generate_students():
    first_names = ["John", "Mary", "Maheva", "Maeva", "Annabelle", "Patience", "Angel", "Lincia", "David"]
    last_names = ["Smith", "Doe", "Brown", "Wilson", "Taylor", "Anderson", "Thomas", "Jackson", "White"]
    departments = ["Math", "English", "Programming", "Science", "History"]
    course_list = [f"Course-{i}" for i in range(1, 11)]

    students = []
    for i in range(10):
        # 1. Create student instance
        student = Student(
            student_id=101 + i,
            name=f"{random.choice(first_names)} {random.choice(last_names)}",
            age=random.randint(18, 30),
            gender=random.choice(["Male", "Female"]),
            department=random.choice(departments)
        )

        # 2. Add 10 courses with random marks
        for c_name in course_list:
            mark = random.randint(40, 100)
            student.add_course(Course(c_name, mark))

        # 3. Finalize student data
        student.calculate_average_mark()
        students.append(student)

    return students


def rank_students(student_list):
    # Sort by average mark descending
    sorted_students = sorted(student_list, key=lambda s: s.average_mark, reverse=True)
    for i, student in enumerate(sorted_students):
        student.rank = i + 1
    return sorted_students


def display_data(student_list, title):
    print("\n" + "=" * 80)
    print(f"--- {title} ---")
    print("=" * 80)

    header = f"{'ID':<5} | {'Name':<18} | {'Age':<4} | {'Dept':<12} | {'Avg':>5} | {'Rank':>4}"
    print(header)
    print("-" * len(header))

    for student in student_list:
        row = (f"{student.student_id:<5} | {student.name:<18} | {student.age:<4} | "
               f"{student.department:<12} | {student.average_mark:>5.2f} | {student.rank:>4}")
        print(row)
    print("=" * 80 + "\n")


def display_class_statistics(student_list):
    if not student_list:
        return

    # 1. Calculations
    averages = [s.average_mark for s in student_list]
    highest_avg = max(averages)
    lowest_avg = min(averages)
    class_avg = sum(averages) / len(student_list)

    # Assuming pass mark is 50
    passed = [s for s in student_list if s.average_mark >= 50]
    failed = [s for s in student_list if s.average_mark < 50]

    # Determine Class Remark
    if class_avg >= 70:
        remark = "Excellent Performance"
    elif class_avg >= 50:
        remark = "Satisfactory Performance"
    else:
        remark = "Needs Improvement"

    # 2. Display the Statistics Table
    print("\n" + "-" * 40)
    print("       CLASS SUMMARY STATISTICS")
    print("-" * 40)
    print(f"{'Metric':<25} | {'Value':<15}")
    print("-" * 40)
    print(f"{'Highest Average':<25} | {highest_avg:>10.2f}")
    print(f"{'Lowest Average':<25} | {lowest_avg:>10.2f}")
    print(f"{'Class Average':<25} | {class_avg:>10.2f}")
    print(f"{'Students Passed':<25} | {len(passed):>10}")
    print(f"{'Students Failed':<25} | {len(failed):>10}")
    print("-" * 40)
    print(f"OVERALL REMARK: {remark}")
    print("-" * 40 + "\n")


def add_new_student(student_list):
    print("\n--- Add New Student ---")
    try:
        # Generate a new ID based on the last student's ID + 1
        new_id = student_list[-1].student_id + 1 if student_list else 101
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender (Male/Female): ")
        dept = input("Enter Department: ")

        # Create the instance
        new_student = Student(new_id, name, age, gender, dept)

        # Add some default courses so they have an average (Optional)
        # Or leave it empty for the user to add later
        student_list.append(new_student)
        print(f"Successfully added {name}!")

        # Re-rank after adding
        return rank_students(student_list)
    except ValueError:
        print("Invalid input. Age must be a number.")
        return student_list


def delete_student(student_list):
    print("\n--- Delete Student ---")
    try:
        sid = int(input("Enter the Student ID to remove: "))
        # Find the student
        to_remove = None
        for s in student_list:
            if s.student_id == sid:
                to_remove = s
                break

        if to_remove:
            student_list.remove(to_remove)
            print(f"Student {sid} removed successfully.")
        else:
            print("Student ID not found.")

        # Re-rank after deleting to fix the ranking order
        return rank_students(student_list)
    except ValueError:
        print("Invalid ID format.")
        return student_list

def main():
    print("--- Welcome to the Student Performance System ---")

    # Generate and rank
    unsorted_students = generate_students()
    ranked_students = rank_students(unsorted_students)

    while True:
        print("Menu:")
        print("1) Display class performance (Unsorted)")
        print("2) Display class performance (By Rank)")
        print("3) Exit")

        choice = input("Choice: ")
        if choice == '1':
            display_data(unsorted_students, "Unsorted Statistics")
        elif choice == '2':
            display_data(ranked_students, "Ranked Statistics")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")
        # ... previous setup ...
        all_students = generate_students()
        all_students = rank_students(all_students)

        while True:
            print("\nMenu:")
            print("1) Display Statistics")
            print("2) Display by Rank")
            print("3) Add Student")  # New Option
            print("4) Delete Student")  # New Option
            print("5) Exit")

            choice = input("Choice: ")

            if choice == '1':
                display_data(all_students, "Class Data")
                display_class_statistics(all_students)
            elif choice == '2':
                # We sort it temporarily for display
                sorted_list = sorted(all_students, key=lambda s: s.rank)
                display_data(sorted_list, "Ranked List")
            elif choice == '3':
                all_students = add_new_student(all_students)
            elif choice == '4':
                all_students = delete_student(all_students)
            elif choice == '5':
                break


if __name__ == "__main__":
    main()