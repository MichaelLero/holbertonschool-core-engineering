#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass pulling from Abstract class Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Also a subclass pull from Abstract class Animal"""
    def sound(self):
        return "Meow"
