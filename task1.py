student_marks = {
    "ram": 85,
    "shyam": 78,
    "jay": 92,
    "prakash": 88
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found in the records.")
