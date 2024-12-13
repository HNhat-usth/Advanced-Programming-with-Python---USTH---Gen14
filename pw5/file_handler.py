from domains.Course import *
from domains.Student import *


def studentsToFile(students):
    try:
        print("Saving students info into 'student.txt'")
        f = open("students.txt", "w")
        for student in students:
            f.write(student.getID() + "\n")
            f.write(student.getName() + "\n")
            f.write(student.getDob() + "\n")
        print("...Done")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close()


def coursesToFile(courses):
    try:
        print("Saving courses info into 'courses.txt'")
        f = open("courses.txt", "w")
        for course in courses:
            f.write(course.getID() + "\n")
            f.write(course.getName() + "\n")
            f.write(str(course.getECT()) + "\n")
        print("...Done")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close()


def marksToFile(courses):
    try:
        print("Saving marks into 'marks.txt'")
        f = open("marks.txt", "w")
        for course in courses:
            all_marks = course.getMarks()
            for studentinfo in all_marks.keys():
                f.write(studentinfo + "\n")
                for component in all_marks[studentinfo]:
                    f.write(str(component) + "\n")
            f.write("\n")
        print("...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()


def getStudentsFromFile():
    try:
        print("Reading students info from 'students.txt'")
        f = open("students.txt")
        students = []
        while True:
            id, name, dob = (
                f.readline().rstrip("\n"),
                f.readline().rstrip("\n"),
                f.readline().rstrip("\n"),
            )
            if id == "":
                break
            students.append(Student(id, name, dob))
        print("...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()
        return students


def getCoursesFromFile():
    try:
        print("Reading courses info from 'courses.txt'")
        f = open("courses.txt")
        courses = []
        while True:
            id, name, ect = (
                f.readline().rstrip("\n"),
                f.readline().rstrip("\n"),
                f.readline().rstrip("\n"),
            )
            if id == "":
                break
            courses.append(Course(id, name, int(ect)))
        print("...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()
        return courses


def getMarksFromFile(courses):
    try:
        print("Reading marks from 'marks.txt'")
        f = open("marks.txt", "r")
        for course in courses:
            while True:
                student_info = f.readline().rstrip("\n")
                if student_info == "":
                    break
                attendance, mid, final = (
                    int(f.readline().rstrip("\n")),
                    int(f.readline().rstrip("\n")),
                    int(f.readline().rstrip("\n")),
                )
                course.setMarks(student_info, [attendance, mid, final])
        print("...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()
