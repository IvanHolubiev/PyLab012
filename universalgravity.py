class UniversalGravity:
    def __init__(self, G: float = 6.67430e-11):
        self.G = G

    def force(self, m1: float, m2: float, distance: float) -> float:
        if distance == 0:
            return 0
        return self.G * m1 * m2 / (distance ** 2)

