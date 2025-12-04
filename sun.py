from typing import List

class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: int, y: int):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y

    def get_mass(self) -> float:
        return self.mass

    def get_x_pos(self) -> int:
        return self.x

    def get_y_pos(self) -> int:
        return self.y

    def __str__(self) -> str:
        return f"Sun(name={self.name}, radius={self.radius}, mass={self.mass}, temp={self.temp}, x={self.x}, y={self.y})"

