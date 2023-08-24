from Mini_Assignment_1.data import *
from math import *

Alice = []
Bob = []
Charlie = []
David = []

for i in alice_marks().values():
    Alice.append(i)
for i in bob_marks().values():
    Bob.append(i)
for i in charlie_marks().values():
    Charlie.append(i)
for i in david_marks().values():
    David.append(i)

grades = {
    'Alice': Alice,
    'Bob': Bob,
    'Charlie': Charlie,
    'David': David
}
max_avg = {
    'Alice': sum(Alice) / len(Alice),
    'Bob': sum(Bob) / len(Bob),
    'Charlie': sum(Charlie) / len(Charlie),
    'David': sum(David) / len(David)
}
for j, i in grades.items():
    print("Student:", j)
    print("Average Grade:", sum(i) / len(i))
    print()

print("Student with Highest average Grade:")
print("Student:", max(max_avg, key=max_avg.get))
print("Average Grade:", max(max_avg.values()))
