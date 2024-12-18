from domains.Course import *
from domains.Student import *
import gzip


def studentsToFile(students):
    try:
        print("Saving students info into 'student.txt'")
        f = open("students.txt", "w")
        for student in students:
            f.write(student.getID() + "\n")
            f.write(student.getName() + "\n")
            f.write(student.getDob() + "\n")
        print("         ...Done")
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
        print("         ...Done")
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
        print("         ...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()


def getStudentsFromFile(file_name):
    try:
        print(f"Reading students info from '{file_name}'")
        f = open(file_name)
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
        print("         ...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()
        return students


def getCoursesFromFile(file_name):
    try:
        print(f"Reading courses info from '{file_name}'")
        f = open(file_name)
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
        print("         ...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()
        return courses


def getMarksFromFile(courses, file_name):
    try:
        print(f"Reading marks from '{file_name}'")
        f = open(file_name, "r")
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
        print("         ...Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()


def compress(filenames, compressed_name):
    print(f"Compressing into {compressed_name}")
    with gzip.open(compressed_name, "wb") as f_out:
        for name in filenames:
            f_out.write(len(name).to_bytes(4, byteorder="big"))
            f_out.write(name.encode("utf-8"))
            with open(name, "rb") as f_in:
                content = f_in.read()
                f_out.write(len(content).to_bytes(4, byteorder="big"))
                f_out.write(content)
    print(f"            ...Done")


def decompress(compressed_name):
    print(f"Decompressing {compressed_name}")
    with gzip.open("students.dat", "rb") as f_in:
        while True:
            # Read name of a file
            name_length_bytes = f_in.read(4)
            if not name_length_bytes:
                break

            name_length = int.from_bytes(name_length_bytes, byteorder="big")
            file_name = f_in.read(name_length).decode("utf-8")

            # Read the data in a file
            content_length_bytes = f_in.read(4)
            content_length = int.from_bytes(content_length_bytes, byteorder="big")
            file_data = f_in.read(content_length)

            with open(file_name, "wb") as out_file:
                out_file.write(file_data)
            print(f"Extracted: {file_name} ({content_length} bytes)")
    print("         ...Done")
