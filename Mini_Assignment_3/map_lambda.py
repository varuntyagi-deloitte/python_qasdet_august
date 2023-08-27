employees = [
    {"name": "test_1", "age": 30, "salary": 50000},
    {"name": "test_2", "age": 25, "salary": 60000},
    {"name": "test_3", "age": 35, "salary": 70000}
]
sal = []
emp_age = []
emp_status = []
for i in employees:
    sal.append(i.get('salary'))
    emp_age.append(i.get('age'))
hr_wage = list(map(lambda value: value / 2080, sal))
cnt = 0
for i in employees:
    i['salary'] = hr_wage[cnt]
    cnt += 1
print(employees)
status = lambda age: age < 30

for i in emp_age:
    if (status(i)) is True:
        emp_status.append("Junior")
    else:
        emp_status.append("Senior")
cnt_1 = 0
for i in employees:
    i['status'] = emp_status[cnt_1]
    cnt_1 += 1

print(employees)
