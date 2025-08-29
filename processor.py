# 🚀 OOP Assignment Solution

# -------------------------------
# Assignment 1: Design Your Own Class 🏗
# -------------------------------

class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price   # Encapsulation: private attribute

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price (controls access)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    # Method to display phone info
    def phone_info(self):
        return f"{self.brand} {self.model}, Price: ${self.__price}"

    # Method to simulate calling
    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

# Subclass with inheritance
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)  # Inherit from Smartphone
        self.gpu = gpu

    def phone_info(self):
        return f"{self.brand} {self.model} (Gaming Edition, GPU: {self.gpu}), Price: ${self.get_price()}"

# -------------------------------
# Activity 2: Polymorphism Challenge 🎭
# -------------------------------

class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈"

class Boat:
    def move(self):
        return "Sailing 🚤"

# -------------------------------
# Testing Deliverables
# -------------------------------

if __name__ == "__main__":
    # Assignment 1 test
    phone1 = Smartphone("Samsung", "Galaxy S23", 1200)
    phone2 = GamingSmartphone("Asus", "ROG 7", 1500, "Adreno 740")

    print(phone1.phone_info())
    print(phone1.make_call("+123456789"))
    phone1.set_price(1100)   # Update price safely
    print("Updated:", phone1.phone_info())

    print(phone2.phone_info())

    print("\n--- Polymorphism Demo ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
