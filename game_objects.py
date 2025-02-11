import math

class Puck():
    def __init__(self, angle:float):
        self.angle = angle
        self.size = 10
        self.color = (200,200,200)
        self.x_position = 600
        self.y_position = 600
        self.position = (self.x_position, self.y_position)
        self.x_velocity = math.cos(math.radians(angle))
        self.y_velocity = math.sin(math.radians(angle))

    