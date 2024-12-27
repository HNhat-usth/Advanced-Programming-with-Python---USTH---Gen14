import os
import subprocess
import re


def exec(command):
    try:
        return os.system(command)
    except Exception as e:
        print(f"An exception occur : {e}")
        return None


def processToFile(command):
    try:
        os.popen(command, "r")
    except Exception as e:
        print(f"An exception occur : {e}")


def fileToProcess(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        command = input("Enter a command : \n>> ")
        if command == "exit":
            break
        elif "<" in command:
            fileToProcess(command)
        elif ">" in command:
            processToFile(command)
        else:
            exec(command)


if __name__ == "__main__":
    main()
