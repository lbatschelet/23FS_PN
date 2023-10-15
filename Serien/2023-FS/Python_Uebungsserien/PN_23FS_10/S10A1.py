"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 10
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
S10A1_main.py
"""
import statistics


def compute_final_grades(students, grades):
    for i in range(len(students)):
        mean_student = statistics.mean(grades[i])
        students[i][1] = round(mean_student, 2)
    return students

students = [["Joe", "-"],
            ["Kim", "-"],
            ["Sam", "-"]]
grades =   [[5.0, 5.5, 4.5],
            [4.5, 4.0, 5.0],
            [3.5, 5.0, 6.0]]

compute_final_grades(students, grades)
print(students, end=\n)