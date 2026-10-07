#!/usr/bin/env python3

class SwimMixin:
    """Provides swimming functionality to a creature."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying functionality to a creature."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A mythical creature capable of swimming, flying, and roaring."""

    def roar(self):
        print("The dragon roars!")


# my_dragon = Dragon()
# print(Dragon)
