from math import floor
from numpy import average
import curses


class NameID:
    def setID(self, ID: str):
        if isinstance(ID, str) and ID != "":
            self._ID = ID
            return 1
        else:
            print("ID must be an non-empty string\n")
            return 0

    def setName(self, name: str):
        if isinstance(name, str) and name != "":
            self._name = name
            return 1
        else:
            print("Name must be an non-empty string\n")
            return 0

    def getName(self):
        return self._name

    def getID(self):
        return self._ID


class Student(NameID):
    def __init__(self) -> None:
        self._ID = ""
        self._name = ""
        self._Dob = ""
        self._GPA = None

    def __str__(self) -> str:
        return f"{self._ID} {self._name} {self._Dob}"

    def setDob(self, Dob: str):
        if isinstance(Dob, str) and Dob != "":
            self._Dob = Dob
            return 1
        else:
            print("Date of birth must be an non-empty string\n")
            return 0

    def setID(self, ID: str):
        if isinstance(ID, str) and ID != "":
            self._ID = ID
            return 1
        else:
            print("Student ID must be an non-empty string\n")
            return 0

    def getDob(self):
        return self._Dob

    def setGPA(self, num):
        self._GPA = num

    def getGPA(self):
        return self._GPA

    def haveGPA(self):
        return self._GPA is not None

    @staticmethod
    def createStudent():
        print("- Creating a new student : \n")
        student = Student()
        while True:
            if student.setID(input("Enter an ID : ")):
                break
        while True:
            if student.setName(input("Enter a name : ")):
                break
        while True:
            if student.setDob(input("Enter a Date of Birth : ")):
                break

        return student

    def calculateGPA(self, courses):
        """Calculate GPA and return 1 if student is graded in all course, return -1 otherwise"""
        overalls = []
        ects = []
        for course in courses:
            overall, message = course.get1StudentOverall(self)
            if overall != None:
                overalls.append(overall)
                ects.append(course.getECT())
            else:
                return -1, f"{message}, cant calculate GPA"
        self.setGPA(average(overalls, weights=ects))
        return 1, ""


class Course(NameID):
    def __init__(self) -> None:
        self._ID = ""
        self._name = ""
        self._ECT = 0
        self._marks = {}  # {student : int}

    def __str__(self) -> str:
        return f"{self._ID} {self._name} {self._ECT} ECTS"

    def setETC(self, num=3):
        self._ECT = num

    def getECT(self):
        return self._ECT

    def getMarks(self):
        return self._marks

    def get1StudentOverall(self, student):
        if str(student) in self._marks.keys():
            return average(self._marks[str(student)], weights=[0.1, 0.4, 0.5]), ""
        else:
            return (
                None,
                f"{student.getName()} hasnt been graded in the course {self.getName()}",
            )

    def displayMarks(self):
        """Display marks of all students in this course"""
        print("---------------------------------------")
        if self._marks == {}:
            print(f"Havent add marks of any student of the course {str(self)}")
            return
        else:
            print(f"Displaying all marks of the course {str(self)} :")
            for key, scores in self._marks.items():
                print(
                    f"{key} : {scores[0]}, {scores[1]}, {scores[2]} -> overall : {average(scores,weights=[0.1, 0.4, 0.5]):.2f}"
                )

    def addMarks(self, student):
        """Add/overwrite marks of a student in the course"""
        if str(student) in self._marks.keys():
            print(
                f"- Already have {student.getName()} {student.getID()}, changing marks"
            )
        else:
            print(f"- Adding marks for {student.getName()} {student.getID()}")

        self._marks[str(student)] = [
            floor(inputNum(float, "Enter a attendance score : ", "attendance score")),
            floor(inputNum(float, "Enter a midterm score : ", "midterm score")),
            floor(inputNum(float, "Enter a final score : ", "final score")),
        ]

    @staticmethod
    def createCourse():
        print("- Creating a new course : \n")
        course = Course()
        while True:
            if course.setID(input("Enter an ID : ")):
                break
        while True:
            if course.setName(input("Enter a name : ")):
                break
        course.setETC(
            inputNum(
                int,
                "Enter the number of credits for this course : ",
                "Number of Credits",
                0,
                10,
            )
        )
        return course


class UI:
    def __init__(self):
        self.stdscr = None

    def start(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(True)

        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    def close(self):
        if self.stdscr:
            curses.nocbreak()
            curses.echo()
            curses.curs_set(2)
            self.stdscr.keypad(False)
            curses.endwin()

    def display(self, message, title, color_pair=1, emphasis=curses.A_BOLD):
        while True:
            self.stdscr.addstr(0, 0, title, curses.color_pair(2) | curses.A_ITALIC)
            self.stdscr.addstr(
                1, 1, "(Press q to quit)", curses.color_pair(1) | curses.A_ITALIC
            )
            self.stdscr.addstr(2, 0, message, curses.color_pair(color_pair) | emphasis)
            key = self.stdscr.getch()
            if key == ord("q"):
                break


def inputNum(
    converter, message: str, input_name: str, lowerbound: int = 0, upperbound: int = 20
):
    """Repeatedly ask user to input a number in [lowerbound, upperbound]
    until it gets a valid number convertable by 'converter'"""
    user_input = ""
    while True:
        user_input = input(message)
        try:
            user_input = converter(user_input)
            if lowerbound > user_input or user_input > upperbound:
                print(
                    f"{input_name} is supposed to be > {lowerbound} and < {upperbound}"
                )
                continue
            break
        except ValueError:
            print(f"{input_name} is supposed to be a {converter.__name__}")
            continue
    return user_input


def strListToStr(l: list):
    """
    turn a list of str into a str of the format:
    0. value1
    1. value2
    ...
    """
    new_str = ""
    for i, item in enumerate(l):
        new_str += f"{str(i)}. {str(item)} \n"
    return new_str


def pick(my_list, name):
    """Let user pick an index of a list and return it"""
    if my_list == []:
        print(f"There is no {name} registered")
    else:
        while True:
            index = inputNum(
                int,
                f"- Pick a {name} :\n" + strListToStr(my_list),
                "Index",
                0,
                len(my_list) - 1,
            )
            if 0 <= index and index < len(my_list):
                return index
            else:
                print("Invalid number")
    return -1


def sortStudentsByGPA(students, courses):
    """Calculate GPA of all students and return 2 lists of str containing student info sorted by gpa"""
    if students == []:
        print("There is no student registered")
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


def main():
    ui = UI()

    students = []
    courses = []

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
            case 0:  # Add Course
                course = Course.createCourse()
                courses.append(course)
            case 1:  # Add student
                student = Student.createStudent()
                students.append(student)
            case 2:  # Add marks for a student in a course
                index_course = pick(courses, "course")
                index_student = pick(students, "student")
                if index_course != -1 and index_student != -1:
                    courses[index_course].addMarks(students[index_student])
            case 3:  # Display all students
                try:
                    ui.start()
                    sorted_list = sortStudentsByGPA(students=students, courses=courses)
                    ui.display(
                        strListToStr(students),
                        title="- Displaying all students :",
                    )
                except Exception as e:
                    print(f"An error occurred: {e}")
                finally:
                    ui.close()
            case 4:  # Display a course and its students
                index_course = pick(courses, "course")
                if index_course != -1:
                    courses[index_course].displayMarks()
            case 5:  # Calculate GPA of a student
                index_student = pick(students, "students")
                student = students[index_student]
                state, message = student.calculateGPA(courses)
                if state != -1:
                    print(f"{student.getName()}'s GPA is : {student.getGPA():.2f}")
                else:
                    print(message)

            case 6:  # Sort students by GPA
                try:
                    ui.start()
                    sorted_list, students_without_GPA = sortStudentsByGPA(
                        students=students, courses=courses
                    )
                    ui.display(
                        strListToStr(sorted_list)
                        + "\nStudents that havent been fully graded:\n"
                        + strListToStr(students_without_GPA),
                        title="List of students that have been fully graded, ordered by GPA :",
                    )
                except Exception as e:
                    print(f"An error occurred: {e}")
                finally:
                    ui.close()
            case 7:
                break


if __name__ == "__main__":
    main()
