from typing import List

class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float,
                 x: float, y: float, vel_x: float = 0.0, vel_y: float = 0.0):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    # Getters
    def get_mass(self) -> float:
        return self.mass

    def get_distance(self) -> float:
        return self.distance

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def get_x_vel(self) -> float:
        return self.vel_x

    def get_y_vel(self) -> float:
        return self.vel_y

    # Setters
    def set_x_vel(self, new_x_vel: float):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float):
        self.vel_y = new_y_vel

    # Movement
    def move_to(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    def __str__(self) -> str:
        return (f"Planet(name={self.name}, radius={self.radius}, mass={self.mass}, distance={self.distance}, "
                f"x={self.x}, y={self.y}, vel_x={self.vel_x}, vel_y={self.vel_y})")