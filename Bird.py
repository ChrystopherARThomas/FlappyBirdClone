""" Bird class done so users can customize their bird before the game begins
Each bird should have its own unique color and its own unique sound that will be played as the game progreses"""

class Bird:
    # list of available colors for user to choose from
    colors = ['red', 'blue', 'green', 'purple']

    # list of available chirps for user to choose from
    chirps = ['bird chirp', 'cat meow', 'man screaming', 'fart sound']

    # sound effect that plays when bird hits either an object or the ground
    hit = None
    score = 0

    def __init__(self, color, chirp):
        if color not in Bird.colors:
            raise AttributeError
        else:
            self.color = color

        if chirp not in Bird.chirps:
            raise AttributeError
        else:
            self.chirp = chirp

        # pos used to determine whether I have hit an obstacle
        self.xPos = 0
        self.yPos = 0

        # attributes needed to mimic gravity behavior in game
        self.velocity = 0  # how fast bird is moving
        self.gravity = 0.5  # how fast it bring the bird back down
        self.flap_strength = 6  # how much of an upwards boost bird gets





    def move(self, xCor, yCor):
        xCor += 1
        yCor += 1

    def hit(self):
        return None

    def score(self, score):
        return None

class Pipe:
    # allowing users to set the colors of the obstacles
    def __init__(self, color, xPos, yPos):
        self.color = color
        self.xPos = xPos
        self.yPos = yPos

    def have_been_hit(self):
        return None

class Ground:
    def __init__(self):
        None
