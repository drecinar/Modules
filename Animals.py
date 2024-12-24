import stringtools as st

class Animal():
    def __init__(self,name,age):
        self.name = st.upperCase(name)
        self.age = age
        self.position=0
    def Walk(self):
        self.position += 1
    def ShowInfos(self):
        print(vars(self))
        #print(f"Ad : {self.name}\nYaş : {self.age}")


class Cat(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age)
        self.breed = st.lowerCase(breed)
        self.color = color
    def Meow(self):
        print("Meoow")

class Bird(Animal):
    def __init__(self, name, age, colors):
        super().__init__(name, age)
        self.colors = colors
    def Crow(self):
        print("Ciiik")

mandalina = Cat("Mandalina",3,"TeKİr","Turuncu")
mandalina.Walk()
mandalina.ShowInfos()
mandalina.Meow()

print("*******")

cicikus = Bird("Cicikuş",2,["mavi","yeşil","sarı"])
cicikus.ShowInfos()
cicikus.Crow()
