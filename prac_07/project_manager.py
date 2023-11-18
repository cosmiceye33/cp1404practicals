"""
estimate: 3 hrs
actual: 4hrs
"""

from project import Project
import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date \n- (A)dd new project " \
       "\n- (U)pdate project \n- (Q)uit"

def main():
    """Program to load and update projects."""
    projects = []
    load_projects()
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            load_new_projects(projects)
        elif choice == "d":
            display_projects()
        elif choice == "a":
            add_new_project(projects)
        elif choice == "s":
            save_projects(projects)
        elif choice == "f":
            display_projects_by_date(projects)
        elif choice == "u":
            update_project_details(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")
    save_ending_projects()


def save_ending_projects(projects):
    """Saves the projects"""
    with open(FILENAME, 'w') as out_file:
        for project in projects:
            print(project, file=out_file, end="\n")


def update_project_details(projects):
    """Updates a projects completion and priority"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    percentage = int(input("New percentage: "))
    priority = int(input("Priority: "))
    projects[project_choice] = Project(projects[project_choice].name, projects[project_choice].start_date, priority,
                                       projects[project_choice].cost_estimate, percentage)


def display_projects_by_date(projects):
    """Displays the projects after a entered date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")  # e.g., "30/9/2022"
    date_object = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if date > date_object:
            print(project)


def save_projects(projects):
    """Save the current projects to a file"""
    filename = input("Filename: ")
    with open(filename, 'w') as out_file:
        for project in projects:
            print(project, file=out_file, end="\n")
    print(f"Projects saved to {out_file}")


def add_new_project(projects):
    """Adds new projects to the list"""
    project_name = get_project_details("Name: ")
    date_string = get_project_details("Start Date (d/m/yyyy): ")
    priority = int(get_project_details("Priority: "))
    cost = float(get_project_details("Cost estimate: $"))
    completion = int(get_project_details("Completion rate: "))
    projects.append(Project(project_name, date_string, priority, cost, completion))


def display_projects():
    """Displays complete and Incomplete projects"""
    complete_projects, incomplete_projects = determine_if_complete()
    print("Complete Project:")
    for project in complete_projects:
        print(f" {project}")
    print("Incomplete Project:")
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(f" {project}")


def determine_if_complete(projects):
    """Sorts complete and incomplete projects into lists"""
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    complete_projects.sort()
    return complete_projects, incomplete_projects


def load_new_projects(projects):
    """Loads a new file of projects"""
    projects
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


def load_projects(projects):
    """Loads a file of projects"""
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))


def get_project_details(display_string):
    detail = input(f"{display_string}")
    while detail == "":
        print("Input cannot be blank.")
        detail = input(f"{display_string}: ")
    return detail


main()
