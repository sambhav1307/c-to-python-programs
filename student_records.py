from dataclasses import dataclass


@dataclass
class Student:
    roll: int
    name: str
    marks: float


students = []

for _ in range(3):
    roll, name, marks = input("Enter roll, name and marks: ").split()
    students.append(Student(int(roll), name, float(marks)))

print("\nRoll\tName\tMarks")
for s in students:
    print(f"{s.roll}\t{s.name}\t{s.marks:.2f}")
