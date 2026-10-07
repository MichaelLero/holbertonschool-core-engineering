class Fish:
    """Represents a basic fish with swimming capabilities."""

    def swim(self):
        print("The fish is swimming")
        
    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Represents a basic bird with flying capabilities."""

    def fly(self):
        print("The bird is flying")
        
    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Instantiate an object of the FlyingFish class
my_fish = FlyingFish()

# Call the methods in the requested sequential order
# my_fish.fly()
# my_fish.swim()
# my_fish.habitat()

# Display the Method Resolution Order (MRO)
print("\n--- Method Resolution Order ---")
print(FlyingFish.mro())
