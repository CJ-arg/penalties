import pygame


class Goal:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.width = 150
        self.height = 350

    def draw(self, interface):
        pygame.draw.rect(
            interface, "white", pygame.Rect(self.x, self.y, 25, self.height)
        )
        pygame.draw.rect(
            interface,
            "white",
            pygame.Rect(self.x + self.width + 400, self.y, 25, self.height),
        )
        pygame.draw.rect(
            interface, "white", pygame.Rect(self.x, self.y, self.width + 400, 25)
        )

        pygame.draw.line(
            interface,
            "white",
            (0, self.y + self.height - 3),
            (800, self.y + self.height),
            6,
        )

        pygame.draw.line(
            interface,
            "white",
            (self.x, self.y + 50),
            (self.x + self.width + 400, self.y + 50),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x, self.y + 100),
            (self.x + self.width + 400, self.y + 100),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x, self.y + 150),
            (self.x + self.width + 400, self.y + 150),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x, self.y + 200),
            (self.x + self.width + 400, self.y + 200),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x, self.y + 250),
            (self.x + self.width + 400, self.y + 250),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x, self.y + 300),
            (self.x + self.width + 400, self.y + 300),
            2,
        )

        pygame.draw.line(
            interface,
            "white",
            (self.x + 50, self.y),
            (self.x + 50, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 100, self.y),
            (self.x + 100, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 150, self.y),
            (self.x + 150, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 200, self.y),
            (self.x + 200, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 250, self.y),
            (self.x + 250, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 300, self.y),
            (self.x + 300, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 350, self.y),
            (self.x + 350, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 400, self.y),
            (self.x + 400, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 450, self.y),
            (self.x + 450, self.y + self.height),
            2,
        )
        pygame.draw.line(
            interface,
            "white",
            (self.x + 500, self.y),
            (self.x + 500, self.y + self.height),
            2,
        )


class Goalst:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.width = 150
        self.height = 350

    def draw(self, interface):
        pygame.draw.rect(
            interface, "white", pygame.Rect(self.x, self.y, 25, self.height)
        )
        pygame.draw.rect(
            interface,
            "white",
            pygame.Rect(self.x + self.width + 400, self.y, 25, self.height),
        )
        pygame.draw.rect(
            interface, "white", pygame.Rect(self.x, self.y, self.width + 400, 25)
        )
