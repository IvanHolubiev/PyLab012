import math
from typing import List
from universalgravity import UniversalGravity

class SolarSystem:
    def __init__(self):
        self.the_sun: "Sun" = None       # forward reference
        self.planets: List["Planet"] = []  # forward reference

    def add_sun(self, the_sun: "Sun"):
        self.the_sun = the_sun

    def add_planet(self, new_planet: "Planet"):
        self.planets.append(new_planet)

    def show_planets(self):
        for planet in self.planets:
            print(planet)

    def move_planets(self):
        dt = 0.001  # Time step for each iteration

        if self.the_sun is None:
            raise ValueError("No Sun in the SolarSystem!")

        for planet in self.planets:
            # Move the planet according to current velocity
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel()
            )

            # Compute distance from Sun
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

            if new_distance == 0:
                continue  # Avoid division by zero

            # Compute acceleration due to Sun's gravity
            acc_x = UniversalGravity.G * self.the_sun.get_mass() * dist_x / new_distance ** 3
            acc_y = UniversalGravity.G * self.the_sun.get_mass() * dist_y / new_distance ** 3

            # Update planet velocities
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)
