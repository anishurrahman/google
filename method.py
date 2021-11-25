class Doctor:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("I am doctor " + self.name)
        print("My age is " + str(self.age))
        print("I make per year " + str(self.salary)+" USD")
doctor1 = Doctor("Mohammad Anishur Rahman", 21, 1000000)
doctor1.salary=150000 #modify object properties
doctor1.name="MA Rahman"
doctor2 = Doctor("Hima Ritchil", 20, 1100000)
doctor2.salary=1250000
doctor3 = Doctor("Rina Gomes", 19, 1200000)
doctor1.display()
doctor2.display()
doctor3.display()
