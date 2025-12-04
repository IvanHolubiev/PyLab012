from typing import List
from universalgravity import UniversalGravity
from sun import Sun
from planet import Planet
from solarsystem import SolarSystem

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods

    def run(self):
        for period in range(self.num_periods):
            print(f"Period {period+1}:")
            self.solar_system.show_planets()
            self.solar_system.move_planets()
            print("---")

