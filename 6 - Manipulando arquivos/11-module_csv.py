import csv

courses = []

with open("dados/courses.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        courses.append({"language": row["language"], "category": row["category"]})

for course in courses:
    print(f"{course['language']} - {course['category']}")