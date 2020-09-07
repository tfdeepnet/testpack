class testUser():
    def __init__(self, name="Hello world", age=28):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello world {}".format(self.name))

    def setName(self,yourname):
        self.name = yourname
