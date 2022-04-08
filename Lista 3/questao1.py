class Student:

    def __init__(self, name, subscription_year, course):
        self.name = name
        self.subscription_year = subscription_year
        self.course = course

    def course_student(self):
        return self.course

    def get_age(self):
        raise NotImplementedError

    def graduate(self): 
        return self.subscription_year + 4

    @classmethod
    def student_per_graduation_year(cls, name, course, graduate):
        return cls(name, course, graduate - 4)

Jose = Student('Peru',2020,'COMP')

print(Jose.course_student())
print(Jose.graduate())

new_student = Student.student_per_graduation_year('Gandhi','COMP',2025)
print(new_student.course)
print(new_student.name)
print(new_student.subscription_year)