from universalgravity import UniversalGravity
from sun import Sun
from planet import Planet
from solarsystem import SolarSystem
from simulation import Simulation
import math

def main():
    solar_sys = SolarSystem()
    solar_sys.add_sun(Sun(name="MySun", radius=5, mass=1.989e14, temp=5000, x=0, y=0))
    solar_sys.add_planet(
        Planet(
            name="Earth", radius=20.0, mass=.33, distance=50, x=0, y=50, vel_x=16, vel_y=5, color="blue")
    )
    solar_sys.add_planet(
        Planet(
            name="Mars", radius=22.0, mass=.33, distance=100, x=0, y=50, vel_x=12, vel_y=5, color="red")
    )
    sim = Simulation(solar_sys, 800, 800, 1000)
    sim.run()

if __name__ == '__main__':
    main()
