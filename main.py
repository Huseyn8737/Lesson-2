class Car:
    def __init__(self,brand):
        self.brand=brand

    def drive(self):
        print(f"Brand: {self.brand}")

class Human:
    def __init__(self,name,car):
        self.name=name
        self.car=car

    def go_somewhere(self):
        print(f"Name: {self.name} is going to Edinburgh with his {self.car.brand}")
        self.car.drive()

my_car=Car("BMW")
person=Human("Camal",my_car)

person.go_somewhere()