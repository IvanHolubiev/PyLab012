import turtle

class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: float, y: float):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self._x = x
        self._y = y
        self._t = turtle.Turtle()
        self._t.shape("circle")
        self._t.color("yellow")
        self._t.penup()
        self._t.goto(self._x, self._y)
        self._t.pendown()

    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self._x

    def get_y_pos(self):
        return self._y

    def __str__(self):
        return f"Sun(name={self.name}, x={self._x}, y={self._y})"



