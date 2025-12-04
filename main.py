from universalgravity import UniversalGravity
from sun import Sun
from planet import Planet
from solarsystem import SolarSystem
from simulation import Simulation
import math

def main():
    solar_sys = SolarSystem()
    solar_sys.add_sun(Sun(name="MySun", radius=5, mass=100, temp=5000, x=0, y=0))
    solar_sys.add_planet(Planet(name="OhNO", radius=22.0, mass=.33, distance=2, x=10, y=0, vel_x=100, vel_y=20))
    sim = Simulation(solar_sys, 500, 500, 100)
    sim.run()

if __name__ == '__main__':
    main()