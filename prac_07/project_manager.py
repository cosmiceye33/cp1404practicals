"""

"""

from project import Project
import datetime

FILENAME = "projects.txt"

projects = []


def main():
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    choice = input("Choice: ").lower()
    while choice != "q":
        if choice == "l":
            projects.clear()
            new_projects = input("Filename: ")
            with open(new_projects, 'r') as in_file:
                in_file.readline()
                for line in in_file:
                    line = line.strip()
                    parts = line.split("\t")
                    parts[2] = int(parts[2])
                    parts[3] = float(parts[3])
                    parts[4] = int(parts[4])
                    projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
            print(projects)
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
                print(f" {project}")
            print("Incomplete Project:")  # 2 save function 2 load function
            incomplete_projects.sort()
            for project in incomplete_projects:
                print(f" {project}")

        elif choice == "a":
            project_name = get_project_details("Name: ")
            date_string = get_project_details("Start Date (d/m/yyyy): ")
            priority = int(get_project_details("Priority: "))
            cost = float(get_project_details("Cost estimate: $"))
            completion = int(get_project_details("Completion rate: "))
            projects.append(Project(project_name, date_string, priority, cost, completion))
        choice = input("Choice: ").lower()


def get_project_details(display_string):
    detail = input(f"{display_string}")
    while detail == "":
        print("Input cannot be blank.")
        detail = input(f"{display_string}: ")
    return detail


main()
# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
#         print(f"That day is/was {date.strftime('%A')}")
#         print(date.strftime("%d/%m/%Y")
