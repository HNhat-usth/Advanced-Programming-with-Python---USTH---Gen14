def setStudents():
    """
    Return a list of students, each of which is a dict of ID, name and Dob
    """
    students = []

    student_num = int(input("Enter number of student in a class : "))
    for i in range(student_num):
        student = {}
        print(f"For student No.{i+1} : \n")
        student["ID"] = input(f"Enter id: ")
        student["name"] = input(f"Enter name : ")
        student["DoB"] = input(f"Enter date of birth : ")
        students.append(student)
    return students


def setCourses():
    """
    Return a list of courses, each of which is a dict of ID and name
    """
    courses = []
    course_num = int(input("Enter number of course : "))
    for i in range(course_num):
        course = {}
        print(f"For course No.{i+1} : \n")
        course["ID"] = input(f"Enter course id : ")
        course["name"] = input(f"Enter course name : ")
        course["mark"] = []
        courses.append(course)

    return courses


def setMarks(courses: list, students: list):
    """
    Add a list of marks to each course, each of which is a dict of
    attendance, midtem score and final score of one student
    (index corresponding to the given student list)
    """

    while True:
        print("Choose which course to add marks\n")
        print("-1. exit")
        for i, course in enumerate(courses):
            print(f"{i}. {course['name']}")
        selected = int(input("Choose the index of a course to add marks\n"))

        if selected != -1:
            courses[selected]["marks"] = []

            for student in students:
                marks = {}
                marks["attendance"], marks["midterm"], marks["final"] = map(
                    float,
                    input(
                        f"Add marks of {student['name']} by the order of attendance, midterm score and final : \n"
                    ).split(),
                )
                courses[selected]["marks"].append(marks)
        else:
            break
    print("Finished adding")


def displayCourseAndStudent(courses: list, students: list):
    print("Displaying courses")
    for course in courses:
        print("--------------------------------")
        print(f"- For {course["name"]} :")
        for i, student in enumerate(students):
            if "marks" in course:
                print(
                    f"{student['ID']} {student['name']} {student['DoB']} : {course['marks'][i]['attendance']} {course['marks'][i]['midterm']} {course['marks'][i]['final']}"
                )
            else:
                print(f"{student['ID']} {student['name']} {student['DoB']} : No info")


def main():
    students = setStudents()
    courses = setCourses()
    setMarks(courses=courses, students=students)
    displayCourseAndStudent(courses=courses, students=students)


if __name__ == "__main__":
    main()
