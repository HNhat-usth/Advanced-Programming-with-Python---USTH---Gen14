from domains.Course import *
from domains.Student import *
import gzip
import pickle


def pickleAndCompress(students, courses, file_name):
    try:
        print(f"Saving data to '{file_name}'..")
        with gzip.open(f"{file_name}", "wb") as f:
            pickle.dump((students, courses), f)
        print("     ... Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()


def decompressAndUnpickle(file_name):
    students, courses = [], []
    print(f"Reading data from '{file_name}'..")
    try:
        with gzip.open(f"{file_name}", "rb") as f:
            students, courses = pickle.load(f)
        print("     ... Done")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        f.close()
        return students, courses
