import turtle

class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float,
                 x: float, y: float, vel_x: float = 0.0, vel_y: float = 0.0,
                 color: str = None):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color

        self._t = turtle.Turtle()
        self._t.shape("circle")
        self._t.color(self.color)
        self._t.penup()
        self._t.goto(self.x, self.y)
        self._t.pendown()

    # Getters
    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def get_x_vel(self):
        return self.vel_x

    def get_y_vel(self):
        return self.vel_y

    # Setters
    def set_x_vel(self, new_x_vel):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel):
        self.vel_y = new_y_vel

    # Move turtle
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self._t.goto(new_x, new_y)

    def __str__(self):
        return f"Planet(name={self.name}, x={self.x}, y={self.y}, vel_x={self.vel_x}, vel_y={self.vel_y})"
