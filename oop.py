# Create a class Named softwareEngineer
class SoftwareEngineer: #Head of the class
    def __init__(self, name, age, id, salary): #init function
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
    def displayDetails(self):
        print("I am " + self.name + " I am " + str(self.age) + " My Id is " + "" + str(self.id) + " My Salary is " + str(
                self.salary))
rina = SoftwareEngineer("Rina Gomes", 22, 101, 1500000)
hima = SoftwareEngineer("Hima Ritchil",23, 102, 155000)
anishur = SoftwareEngineer("Anishur Rahman", 24, 103,1600000)

rina.displayDetails()
hima.displayDetails()
anishur.displayDetails()



