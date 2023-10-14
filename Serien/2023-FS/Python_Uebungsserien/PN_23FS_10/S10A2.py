"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 10
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
S10A2.py
"""

student_lectures = {
    "Sarah": {"V1", "V2", "V3"},
    "Jasmine": {"V1", "V2"},
    "Dominique": {"V2", "V3"},
    "Stefan": {"V3"},
    "Uda": {"V1", "V3"},
    "Nina": {"V1", "V3"},
    "Berfin": {"V1", "V2"},
    "Marius": {"V1", "V3"},
    }

def get_lectures(name):
    return student_lectures.get(name, set())

def get_students_lectures(V1, V2):
    students = set()
    for name, lectures in student_lectures.items():
        if V1 in lectures and V2 in lectures:
            students.add(name)
    return students

print("Studierende die V1 und V2 besuchen:", get_students_lectures("V1", "V2"))


another = "y"

while another == "y":
    name = input("Gebgen Sie den Namen einer Studierenden Person ein: ")
    print(get_lectures(name))
    another = input("Wollen Sie einen weiteren Namen eingeben? (y/n)")
    