from domains import *
from input import *
from output import *
from file_handler import *
import os


def sortStudentsByGPA(students, courses):
    """Calculate GPA of all students and return 2 lists of str containing student info sorted by gpa"""
    if students == []:
        print("There is no student registered")
        return [], []
    elif courses == []:
        print("There is no course registered")
        return [], []
    else:
        students_have_GPA = []
        students_without_GPA = []
        for student in students:
            state, message = student.calculateGPA(courses)
            if state == 1:
                students_have_GPA.append(student)
            else:
                students_without_GPA.append(message)

            students_have_GPA.sort(key=lambda student: student.getGPA(), reverse=True)
            sorted_list_of_str = [
                f"{student.getID()} {student.getName()} : {student.getGPA():.2f}"
                for i, student in enumerate(students_have_GPA)
            ]
        return sorted_list_of_str, students_without_GPA


input_options = [
    "Add Course",
    "Add student",
    "Add marks for a student in a course",
    "Display all students",
    "Display a course and its students",
    "Calculate GPA of a student",
    "Sort students by GPA",
    "Exit",
]

file_names = ["students.txt", "courses.txt", "marks.txt"]


def main():
    if os.path.exists("students.dat"):
        decompress("students.dat")
    students = getStudentsFromFile(file_name=file_names[0])
    courses = getCoursesFromFile(file_name=file_names[1])
    getMarksFromFile(courses, file_name=file_names[2])

    ui = UI()
    while True:
        option = inputNum(
            int,
            "---------------------------------------\n"
            + "- Pick one options:\n"
            + strListToStr(input_options),
            "Option",
            0,
            7,
        )
        print("---------------------------------------")
        match option:
            case 0:  # ------------- Add Course
                course = Course.createCourse()
                courses.append(course)
            case 1:  # ------------- Add student
                student = Student.createStudent()
                students.append(student)

            case 2:  # ------------- Add marks for a student in a course
                index_course = pick(courses, "course")
                index_student = pick(students, "student")
                if index_course != -1 and index_student != -1:
                    courses[index_course].addMarks(students[index_student])

            case 3:  # ------------- Display all students
                sorted_list = sortStudentsByGPA(students=students, courses=courses)
                ui.try_except_display(
                    message=strListToStr(students),
                    title="- Displaying all students :",
                )

            case 4:  # ------------- Display a course and its students
                index_course = pick(courses, "course")
                if index_course != -1:
                    message = courses[index_course].displayMarks()
                    ui.try_except_display(
                        message=message,
                        title=f"Displaying all marks of the course {courses[index_course].getID()} {courses[index_course].getName()} :",
                    )

            case 5:  # ------------- Calculate GPA of a student
                index_student = pick(students, "students")
                if index_student != -1:
                    student = students[index_student]
                    state, message = student.calculateGPA(courses)
                    if state != -1:
                        print(f"{student.getName()}'s GPA is : {student.getGPA():.2f}")
                    else:
                        print(message)

            case 6:  # ------------- Sort students by GPA
                sorted_list, students_without_GPA = sortStudentsByGPA(
                    students=students, courses=courses
                )
                ui.try_except_display(
                    message=strListToStr(sorted_list)
                    + "\n-Students that havent been fully graded:\n"
                    + strListToStr(students_without_GPA),
                    title="List of students that have been fully graded, ordered by GPA :",
                )

            case 7:
                break

    studentsToFile(students)
    coursesToFile(courses)
    marksToFile(courses)

    compress(file_names, "students.dat")


if __name__ == "__main__":
    main()
