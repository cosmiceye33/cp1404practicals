from guitar import Guitar

FILENAME = "guitars.csv"

guitars = []
with open(FILENAME, 'r') as in_file:
    for line in in_file:
        line = line.strip()
        parts = line.split(',')
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
guitars.sort()
for guitar in guitars:
    print(f"{guitar.name}, {guitar.year}, {guitar.cost}")
