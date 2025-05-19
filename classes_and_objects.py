class Vehicle:
    def __init__(self, body_style):
        self.body_style = body_style

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, engine_type):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = engine_type

    def drive(self, speed):
        super().drive(speed)
        print(f"Driving my {self.engine} Car at {self.speed}")


class Motorcycle(Vehicle):
    def __init__(self, engine_type, has_sidecar):
        super().__init__("Motorcycle")
        if has_sidecar:
            self.wheels = 3
        else:
            self.wheels = 2

        self.doors = 0
        self.engine = engine_type

    def drive(self, speed):
        super().drive(speed)
        print(f"Driving my {self.engine} Motorcycle at {self.speed}")


car1 = Car("gas")
car2 = Car("electric")
motorcycle1 = Motorcycle("gas", True)

print(motorcycle1.wheels)
print(car1.engine)
print(car2.doors)

car1.drive(30)
car2.drive(40)
motorcycle1.drive(50)
