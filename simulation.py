from typing import List
from universalgravity import UniversalGravity
from sun import Sun
from planet import Planet
from solarsystem import SolarSystem
import turtle
import time

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        self._t = turtle.Turtle()
        self._t.hideturtle()
        self._screen = turtle.Screen()
        self._screen.setup(width=width, height=height)
        self._screen.bgcolor("black")
        self._t.clear()



    def freeze(self):
        self._screen.exitonclick()   # correct method name

    def run(self):
        for period in range(self.num_periods):
            print(f"Period {period + 1}:")
            self.solar_system.show_planets()
            self.solar_system.move_planets()
            print("---")

        print("Simulation complete")
        self.freeze()


