class Superhero:
    def __init__(self, name, powers, weakness):
        self.name = name
        self.powers = powers  # Could be a list of powers
        self.weakness = weakness
        
    def use_power(self):
        print(f"{self.name} uses their power: {self.powers[0]}")
        
    def get_weakness(self):
        return f"{self.name} is weak to {self.weakness}."

# Example of creating a Superhero object
spiderman = Superhero("Spiderman", ["webs", "spidey sense"], "radiation")
spiderman.use_power()  # Outputs: Spiderman uses their power: webs

print(spiderman.get_weakness())  # Outputs: Spiderman is weak to radiation.

### Inheritance Layer: Flying Superhero

class FlyingSuperhero(Superhero):
    def __init__(self, name, powers, weakness, can_fly):
        super().__init__(name, powers, weakness)
        self.can_fly = can_fly  # True for flying superheroes

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying high overhead!")
        else:
            print("This superhero cannot fly.")

    # Override use_power to demonstrate inheritance
    def use_power(self):
        super().use_power()
        print(f"And they can also {('fly' if self.can_fly else 'not fly')}!")


# Example of creating a Flying Superhero object
superman = FlyingSuperhero("Superman", ["strength", "flight", "heat vision"], "kryptonite", True)
superman.use_power()  # Outputs: Superman uses their power: strength And they can also fly!
superman.fly()  # Outputs: Superman is flying high overhead!





### Activity 2: Polymorphism Challenge with Vehicles

**Vehicle Base Class:**

```python
class Vehicle:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        raise NotImplementedError("Subclasses must implement abstract method move.")

**Car Class:**

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving: 🚗")

**Plane Class:**

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying: ✈️")

### Example of Polymorphism

# Creating instances of Car and Plane
my_car = Car("My Car")
jet = Plane("My Jet")

# Polymorphic calls
my_car.move()  # Outputs: My Car is driving: 🚗
jet.move()  # Outputs: My Jet is flying: ✈️

# Demonstrating the Use of a List with Different Types
vehicles = [my_car, jet]
for v in vehicles:
    v.move()
    print("A vehicle moved!")
