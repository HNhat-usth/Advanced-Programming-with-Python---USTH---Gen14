from .NameID import NameID
from numpy import average


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
