class People :
    def __init__(self, age=0, name=None) :
        self.__age = age
        self.__name = name
    
    def getAge(self) :
        return self.__age

    def setAge(self, age) :
        self.__age = age

    def getName(self) :
        return self.__name
    
    def setName(self, name) :
        self.__name = name

people = People(50, "kim")
print(people.getAge())
print(people.getName())