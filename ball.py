import pygame


class Ball:

    def __init__(self, x, y):

        self.image = pygame.image.load("assets/ball.png")
        self.ball = pygame.Rect(0, 0, 50, 50)
        self.ball.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.ball)
