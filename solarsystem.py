import math
from typing import List
from universalgravity import UniversalGravity

class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets: List[object] = []

    def add_sun(self, sun):
        self.the_sun = sun

    def add_planet(self, planet):
        self.planets.append(planet)

    def show_planets(self):
        for planet in self.planets:
            print(planet)

    def move_planets(self):
        dt = .1  # small time step
        G = UniversalGravity().G    # simplified "gravity constant"

        if self.the_sun is None:
            raise ValueError("No Sun in the SolarSystem!")

        for planet in self.planets:
            dx = self.the_sun.get_x_pos() - planet.get_x_pos()
            dy = self.the_sun.get_y_pos() - planet.get_y_pos()
            distance = math.sqrt(dx**2 + dy**2)
            if distance == 0:
                continue

            # Simple gravity effect (scaled)
            acc_x = G * self.the_sun.get_mass()* dx / distance**3
            acc_y = G * self.the_sun.get_mass()* dy / distance**3

            # Update velocities
            planet.vel_x += acc_x * dt
            planet.vel_y += acc_y * dt

            # Update positions
            planet.x += planet.vel_x * dt
            planet.y += planet.vel_y * dt

            planet.move_to(planet.x, planet.y)


