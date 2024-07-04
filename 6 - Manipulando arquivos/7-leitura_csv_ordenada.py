courses = []

file_csv = "dados/courses.csv"

with open(file_csv, 'r') as file:
    for line in file:
        language, category = line.rstrip().split(",")
        courses.append(f"{language} - {category}")

for course in sorted(courses, reverse=True):
    print(course)