class Person():
    def __init__(self, name, age):   # This works as constructor of a class, think it as setter and getter
        self.name = name
        self.age = age
    
    def printName(self):
        print("Hello Class and my name is " + self.name)
        
    def setGender(self, gender):
        self.gender = gender
        
    def printGender(self):
        print("Gender: " + self.gender)
        
        
        
        
p1 = Person("Minh", 35)
p1.setGender("Male")
p1.printGender()
p1.printName()


if __name__ == "__main__":
    p = Person("Hieu", 45)
    p.printName()