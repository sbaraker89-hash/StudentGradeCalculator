def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def valid_mark(mark):
    return 0 <= mark <= 100


def is_pass(marks):
    avg = average(marks)
    return avg >= 40


name = input("Enter student name: ")
department = input("Enter department: ")
semester = input("Enter semester: ")
marks = []

for i in range(1, 4):
    while True:
        mark = float(input(f"Enter marks for subject {i}: "))

        if valid_mark(mark):
            marks.append(mark)
            break
        else:
            print("Invalid marks! Enter marks between 0 and 100.")

avg = average(marks)
student_grade = grade(avg)

print("\n------ STUDENT RESULT ------")
print("Name:", name)
print("Department:", department)
print("Semester:", semester)
print("Marks:", marks)
print("Average:", avg)
print("Grade:", student_grade)

if is_pass(marks):
    print("Result: PASS")
else:
    print("Result: FAIL")