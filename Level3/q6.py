"""
Create the custom Python classes which have methods and attributes and implement single inheritance, multiple inheritance,
and multilevel inheritance
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""


# Single Inheritance Example
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        return "Honk! Honk!"

class Car(Vehicle):  # Car inherits from Vehicle
    def honk(self):
        return "Beep! Beep!"

# Multilevel Inheritance Example

class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, brand, battery_size):
        super().__init__(brand)
        self.battery_size = battery_size

    def charge(self):
        return f"Charging the {self.brand} electric car."

# Multiple Inheritance Example
class WaterVehicle:
    def sail(self):
        return "Sailing on water!"

class AmphibiousVehicle(Car, WaterVehicle):  # AmphibiousVehicle inherits from Car and WaterVehicle
    def drive(self):
        return "Driving on land!"

# Main function to run the examples
def main():
    # Single Inheritance
    print("=== Single Inheritance ===")
    my_car = Car("Toyota")
    print(f"{my_car.brand} car says: {my_car.honk()}")  # Output: Beep! Beep!

    # Multilevel Inheritance
    print("\n=== Multilevel Inheritance ===")
    my_electric_car = ElectricCar("Tesla", "75 kWh")
    print(f"{my_electric_car.brand} electric car says: {my_electric_car.honk()}")  # Output: Beep! Beep!
    print(my_electric_car.charge())  # Output: Charging the Tesla electric car.

    # Multiple Inheritance
    print("\n=== Multiple Inheritance ===")
    my_amphibious_vehicle = AmphibiousVehicle("AmphiCar")
    print(f"{my_amphibious_vehicle.brand} vehicle says: {my_amphibious_vehicle.honk()}")  # Output: Beep! Beep!
    print(my_amphibious_vehicle.drive())  # Output: Driving on land!
    print(my_amphibious_vehicle.sail())  # Output: Sailing on water!

if __name__ == "__main__":
    main()
