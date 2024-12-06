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


class Course(NameID):
    def __init__(self) -> None:
        self._ID = ""
        self._name = ""
        self._marks = {}  # {student : int}

    def __str__(self) -> str:
        return f"{self._ID} {self._name}"

    def displayMarks(self):
        print("---------------------------------------")
        if self._marks == {}:
            print(f"Havent add marks of any student of the course {str(self)}")
            return
        else:
            print(f"Displaying all marks of the course {str(self)} :")
            for key, scores in self._marks.items():
                print(f"{key} : {scores[0]}, {scores[1]}, {scores[2]}")

    def addMarks(self, student):
        if str(student) in self._marks.keys():
            print(
                f"- Already have {student.getName()} {student.getID()}, changing marks"
            )
        else:
            print(f"- Adding {student.getName()} {student.getID()}")

        self._marks[str(student)] = [
            inputNum(float, "Enter a attendance score : ", "attendance score"),
            inputNum(float, "Enter a midterm score : ", "midterm score"),
            inputNum(float, "Enter a final score : ", "final score"),
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

        return course

    @staticmethod
    def ifValidScore(score: float):
        if 0 <= score and score <= 20:
            return 1
        return 0


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
            index = int(input(f"- Pick a {name} :\n" + strListToStr(my_list)))
            if 0 <= index and index < len(my_list):
                return index
            else:
                print("Invalid number")
    return -1


def main():
    students = []
    courses = []
    while True:
        option = inputNum(
            int,
            "---------------------------------------\n"
            + "- Pick one options:\n"
            + strListToStr(
                [
                    "Add Course",
                    "Add student",
                    "Add marks for a student in a course",
                    "Display all students",
                    "Display a course and its students",
                    "Exit",
                ]
            ),
            "Option",
            0,
            5,
        )
        print("---------------------------------------")
        match option:
            case 0:
                course = Course.createCourse()
                courses.append(course)
            case 1:
                student = Student.createStudent()
                students.append(student)
            case 2:
                index_course = pick(courses, "course")
                index_student = pick(students, "student")
                if index_course != -1 and index_student != -1:
                    courses[index_course].addMarks(students[index_student])
            case 3:
                print(f"- Displaying all students : \n{strListToStr(students)}")
            case 4:
                index_course = pick(courses, "course")
                if index_course != -1:
                    courses[index_course].displayMarks()
            case 5:
                break


if __name__ == "__main__":
    main()
