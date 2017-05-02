class Sample:
    name = None
    __privateAttr = "attr"

    def __init__(self):
        self.name = "shinil.kim"

    def hello(self):
        print('hello world! '+self.name)
        self.__privateMethod()

    def __privateMethod(self):
        print('this is a private method: '+self.__privateAttr)

class MyData:
    __name = None
    __age = None
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.head = self.Head()
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age
    def sayHello(self, name=None):
        if name is not None:
            print('Hello '+name)
        else:
            print('Hello')
    class Head: # Inner class example
        def talk(self): print('talking...')

if __name__ == "__main__":
    a = Sample()
    a.hello()

    b = MyData('shinil.kim', 40)
    print('My name is ',b.getName()," : ",b.getAge())
    b.sayHello()
    b.sayHello('shinil.kim')
    b.head.talk()
