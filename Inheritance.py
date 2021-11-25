class Teacher:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def print_name(self):
        print(self.first_name + self.last_name + str(self.age))

teacher1 = Teacher("Hima", " Gomez ", 20)
teacher2 = Teacher("Babul ", " Nokrek ", 23)
teacher1.print_name()
teacher2.print_name()

class Student(Teacher):
    def __init__(self, first_name, last_name, age, salary):
        Teacher. __init__(self,first_name,last_name,age)
        #super().__init__(first_name,last_name,age)
        self.salary = salary

    def print_salary(self):
        print("salary is " + str(self.salary))

student1 = Student("Rina", "Richil", 20, 2000000)
student2 = Student("Hima", "Gomes", 19, 19000000)
student1.print_name()
student2.print_name()
student1.print_salary()
student2.print_salary()