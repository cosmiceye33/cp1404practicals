"""

"""

from project import Project

FILENAME = "projects.txt"

projects = []

with open(FILENAME, 'r') as in_file:
    in_file.readline()
    for line in in_file:
        line = line.strip()
        parts = line.split("\t")
        projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
choice = input("Choice: ").lower()
while choice != "s":
    if choice == "l":
        new_projects = input("Filename: ")
        with open(new_projects, 'r') as in_file:
            in_file.readline()
            for line in in_file:
                line = line.strip()
                parts = line.split("\t")
                projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    elif choice == "d":
        complete_projects = []
        incomplete_projects = []
        for project in projects:
            if project.is_complete():
                complete_projects.append(project)
            else:
                incomplete_projects.append(project)
        complete_projects.sort()
        print("Complete Project:")
        for project in complete_projects:
            print(f" {Project(project)}")
        print("Incomplete Project:")
        incomplete_projects.sort()
        for project in incomplete_projects:   #todo find out why it prints a bunch more 0 after the completion
            print(f" {Project(project)}")
    choice = input("Choice: ").lower()

