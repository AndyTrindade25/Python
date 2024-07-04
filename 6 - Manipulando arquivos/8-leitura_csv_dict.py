courses = []

file_csv = "dados/courses.csv"

with open(file_csv, 'r') as file:
    for  line in file:
        language, category = line.rstrip().split(',')
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)


print(courses)

for course in courses:
    print(f"{course['language']} {course['category']}")