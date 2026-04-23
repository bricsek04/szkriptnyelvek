class EmptyClass:
    pass

class MyClass:
    def hello(self):
        return "Hello world!"

class Person:
    pass

class Animal:
    pass

class Dog(Animal): # Zárójelben meg tudjuk adni a szülő osztályt
    pass

class Monster:
    pass

class Teacher(Person):
    pass

class Hello:
    def create_name(self, name):
        self.name = name

    def display_name(self):
        return self.name
    
    def greet(self):
        return f"Hello {self.name}!"

class Hello2:
    def __init__(self, name):  # konstruktor, beállítja az objektum kezdőállapotát
        self.name = name

    def say_hi(self):
        print(f"Hi, {self.name}")

class Bag:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def add_twice(self, value):
        self.add(value)
        self.add(value)

    def __str__(self): 
        return "Bag(" + str(self.data) + ")"


class Proba:
    db = 0
    i = 0 # Ez nem egy példányváltozó, ez egy osztályváltozó, nem kell az osztályt példányosítani, a változó létezik
    def __init__(self):
        Proba.db += 1 

    @staticmethod
    def get_db():
        return Proba.db


def main():
    obj = EmptyClass() # Automatikus a példányosításnl a konstruktort hívja meg, ha nincs akkor is lefut egy alapértelmezett üres konstruktor
    o = MyClass()
    print(o.hello()) # hello(o) valami olyat csinál, hogy meghívja a metódust aminek átadja az objektumot

    o2 = MyClass()
    print(o2.hello()) # o2-vel hívja meg

    h = Hello()
    h.create_name("Alice")
    print(h.display_name())
    print(h.greet())


    b = Bag()
    b.add(5)
    b.add(3)
    b.add_twice(9)
    print(b)

    # print(Proba.i)

    o1 = Proba()
    o2 = Proba()
    print(Proba.db)

    o3 = Proba()
    print(Proba.db)
    print(Proba.get_db())

if __name__ == "__main__":
    main()