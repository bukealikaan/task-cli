import sys

def main():
    folderPath = "C:/tasks/task.txt"
    task = " ".join(sys.argv[2:])
    command = sys.argv[1]

    if command == "add":
        if task == "":
            return
        else:
            appendTask(task, folderPath)

    if command == "del":
        if task == "":
            return
        else:
            deleteTask(task, folderPath)

    if command == "list":
        listTasks(folderPath)

def appendTask(text, filename):
    with open(filename, "a", encoding="utf-8") as f:
        print(text, file=f)

def deleteTask(text, filename):
    with open(filename, "r") as f:
            lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip("\n") != text:
                f.write(line)

def listTasks(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        print("---Task List---")
        for line in lines:
            print(line.strip())
        print("---------------")


if __name__ == "__main__":
    main()