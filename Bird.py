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
        self.yPos = 0

        # attributes needed to mimic gravity behavior in game
        self.velocity = 0  # how fast bird is moving
        self.gravity = -0.5  # the force bird gets pulled back down
        self.flap_strength = 6  # how much of an upwards boost bird gets

    def flap(self):
        self.velocity += self.flap_strength
        print("Oooo we movin hoe")

    """ no need for an xCor variable because bird is never actually moving horizontally, only vertically"""
    def move(self, yCor):
        self.velocity += self.gravity
        self.yCor += self.velocity

    def been_hit(self, yCor):
       if yCor != Pipe.yPos:
           self.score += 1
           return False
       else:
           return True

    def score(self):
        return self.score

class Pipe:
    colors = ['green', 'blue', 'purple']
    # allowing users to set the colors of the obstacles
    def __init__(self, color):

        if self.color not in Pipe.colors:
            raise AttributeError
        else:
            self.color = color

        self.xPos = 0
        self.yPos = 0

    def have_been_hit(self):
        return None

class Ground:
    def __init__(self):
        None
