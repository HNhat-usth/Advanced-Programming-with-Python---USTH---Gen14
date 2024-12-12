from .NameID import NameID
from math import floor
from numpy import average
from input import inputNum


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
