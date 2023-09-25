class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage
students = [
    Student("Alice", "S001", 3.8),
    Student("Bob", "S002", 3.5),
    Student("Charlie", "S003", 3.9),
    Student("David", "S004", 3.7)
]

sorted_students = sort_students(students)

# Print sorted students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"