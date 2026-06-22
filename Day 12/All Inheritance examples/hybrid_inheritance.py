class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old."


class Student(Person):
    def __init__(self, name, age, roll_no):

        Person.__init__(self, name, age)
        self.roll_no = roll_no

    def study(self):
        return f"{self.name} (Roll No: {self.roll_no}) is studying for exams."


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}."


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_no, subject, working_hours):
        Student.__init__(self, name, age, roll_no)
        Teacher.__init__(self, name, age, subject)
        self.working_hours = working_hours

    def assist(self):
        return f"{self.name} assists students for {self.working_hours} hours a week."

    def display_ta_info(self):
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Roll No       : {self.roll_no}")
        print(f"Subject       : {self.subject}")
        print(f"Working Hours : {self.working_hours} hrs/week")


def run_demo():
    ta = TeachingAssistant(name="Ananya", age=23, roll_no="CS2025", subject="Python", working_hours=10)

    print("Output:")
    ta.display_ta_info()
    print(ta.introduce())  
    print(ta.study())      
    print(ta.teach())      
    print(ta.assist())     
