courses = []

with open("dados/courses.csv", "r") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)


def get_language(course):
    return course["language"]

def get_category(course):
    return course["category"]

for course in sorted(courses, key=lambda course: course["language"] ):
    print(f"{course['language']} - {course['category']}")



