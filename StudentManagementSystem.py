class Student:
    def __init__(self, name, student_id, __email, age, department, *marks):
        self.name = name
        self.student_id = student_id
        self.__email = __email      
        self.age = age
        self.department = department
        self.__marks = marks      
    
    def get_email(self):
        return self.__email

    
    def set_email(self, email):
        self.__email = email

    def student_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Email:", self.__email)
        print("Age:", self.age)
        print("Department:", self.department)

    def calculate_result(self, *marks):
        if len(marks) == 0:
            marks = self.__marks

        if len(marks) == 0:
            return "No marks available."

        total = sum(marks)
        average = total / len(marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return f"Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department,
                 semester, *marks):
        super().__init__(name, student_id, email, age, department, *marks)
        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"

    def student_info(self):
        super().student_info()
        print("Semester:", self.semester)

class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department,
                 research_topic, *marks):
        super().__init__(
            name, student_id, email, age, department, *marks
        )
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def student_info(self):
        super().student_info()
        print("Research Topic:", self.research_topic)

student1 = UndergraduateStudent(
    "Rahim",
    "UG101",
    "rahim@gmail.com",
    21,
    "Computer Science",
    5, 85, 78, 90
)

student2 = GraduateStudent(
    "Karim",
    "GR201",
    "karim@gmail.com",
    25,
    "Computer Science",
    "Artificial Intelligence",
    88, 92, 85
)

print("===== Undergraduate Student =====")
student1.student_info()
print("Student Type:", student1.get_student_type())
print("Result:", student1.calculate_result())

print("\n===== Graduate Student =====")
student2.student_info()
print("Student Type:", student2.get_student_type())
print("Result:", student2.calculate_result())

print("\n===== Method Overloading =====")

print(student1.calculate_result())


print(student1.calculate_result(90, 80))


print(student2.calculate_result(95, 88, 91, 86))