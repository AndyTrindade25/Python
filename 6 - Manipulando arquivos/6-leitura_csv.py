with open("dados/courses.csv", "r") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        print(f"{language} - {category}")
