grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    lines = []
    for i, (name, grade) in enumerate(students.items(), start=1):
        points = 0
        if grade in grades:
            points = grades[grade]
        formatted_line = "{:>4}|{:10s}|{:^5s}|{:^5}".format(i, name, grade, points)
        lines.append(formatted_line)

    return lines

for el in formatted_grades(students):
    print(el)
    