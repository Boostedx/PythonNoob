class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("Taena mo Janber")
john.talk()
bob = Person("Bob Smith")
bob.talk()