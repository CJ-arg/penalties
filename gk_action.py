import pygame

class Gk_action1:

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/action1.png")
        self.action1 = pygame.Rect(0, 0, 150, 150)
        self.action1.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.action1)

    def __str__(self):
        return "action1"


class Gk_action1vs:

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/action1vs.png")
        self.action1vs = pygame.Rect(0, 0, 150, 150)
        self.action1vs.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.action1vs)

    def __str__(self):
        return "action1"


class Gk_action2:

    def __init__(self, x, y):

        self.image = pygame.image.load("assets/action2.png")
        self.action2 = pygame.Rect(0, 0, 150, 150)
        self.action2.center = (x, y)

    def __str__(self):
        return "action2"

    def draw(self, interface):
        interface.blit(self.image, self.action2)


class Gk_action2vs:

    def __init__(self, x, y):

        self.image = pygame.image.load("assets/action2vs.png")
        self.action2vs = pygame.Rect(0, 0, 150, 150)
        self.action2vs.center = (x, y)

    def __str__(self):
        return "action2vs"

    def draw(self, interface):
        interface.blit(self.image, self.action2vs)


class Gk_action3:

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/action3.png")
        self.action3 = pygame.Rect(0, 0, 150, 150)
        self.action3.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.action3)

    def __str__(self):
        return "action3"


class Gk_action3vs:

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/action3vs.png")
        self.action3vs = pygame.Rect(0, 0, 150, 150)
        self.action3vs.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.action3vs)

    def __str__(self):
        return "action3vs"


class Gk_action4:

    def __init__(self, x, y):

        self.image = pygame.image.load("assets/action4.png")
        self.action4 = pygame.Rect(0, 0, 150, 150)
        self.action4.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.action4)

    def __str__(self):
        return "action4"


class Gk_action4vs:

    def __init__(self, x, y):

        self.image = pygame.image.load("assets/action4vs.png")
        self.action4vs = pygame.Rect(0, 0, 150, 150)
        self.action4vs.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.action4vs)

    def __str__(self):
        return "action4vs"


class Gk_action5vs:

    def __init__(self, x, y):

        self.image = pygame.image.load("assets/action5vs.png")
        self.action5vs = pygame.Rect(0, 0, 150, 150)
        self.action5vs.center = (x, y)

    def draw(self, interface):
        interface.blit(self.image, self.action5vs)

    def __str__(self):
        return "action5vs"


class Gk_action5:

    def __init__(self, x, y):
        self.hair = pygame.Rect(0, 0, 36, 11)
        self.head = pygame.Rect(0, 0, 50, 50)
        self.eye_l = pygame.Rect(0, 0, 7, 10)
        self.eye_r = pygame.Rect(0, 0, 7, 10)
        self.mouse = pygame.Rect(0, 0, 18, 5)
        self.mouth = pygame.Rect(0, 0, 10, 2)
        self.neck = pygame.Rect(0, 0, 20, 15)
        self.body = pygame.Rect(0, 0, 85, 80)
        self.left_arm = pygame.Rect(0, 0, 16, 70)
        self.right_arm = pygame.Rect(0, 0, 16, 70)
        self.left_hand = pygame.Rect(0, 0, 22, 15)
        self.right_hand = pygame.Rect(0, 0, 22, 15)
        self.pelvis = pygame.Rect(0, 0, 82, 38)
        self.left_leg = pygame.Rect(0, 0, 20, 80)
        self.right_leg = pygame.Rect(0, 0, 20, 80)
        self.left_foot = pygame.Rect(0, 0, 34, 9)
        self.right_foot = pygame.Rect(0, 0, 34, 9)

        self.hair.center = (x, y - 25)
        self.head.center = (x, y)
        self.mouse.center = (x, y + 9)
        self.mouth.center = (x, y + 15)
        self.eye_l.center = (x - 8, y)
        self.eye_r.center = (x + 8, y)
        self.neck.center = (x, y + 30)
        self.body.center = (x, y + 70)
        self.left_arm.center = (x - 50, y + 10)
        self.right_arm.center = (x + 50, y + 10)
        self.left_hand.center = (x - 50, y - 35)
        self.right_hand.center = (x + 50, y - 35)
        self.pelvis.center = (x, y + 110)
        self.left_leg.center = (x - 20, y + 160)
        self.right_leg.center = (x + 20, y + 160)
        self.right_foot.center = (x - 20, y + 200)
        self.left_foot.center = (x + 20, y + 200)

    def __str__(self):
        return "action5"

    def draw(self, interface):
        pygame.draw.circle(interface, ("pink"), self.head.center, self.head.width // 2)
        pygame.draw.circle(
            interface, ("black"), self.eye_r.center, self.eye_r.width // 2
        )
        pygame.draw.circle(
            interface, ("black"), self.eye_l.center, self.eye_l.width // 2
        )
        pygame.draw.rect(interface, ("red"), self.mouth)
        pygame.draw.rect(interface, ("black"), self.mouse)
        pygame.draw.rect(interface, ("black"), self.hair)
        pygame.draw.rect(interface, ("brown"), self.neck)
        pygame.draw.rect(interface, ("blue"), self.body)
        pygame.draw.rect(interface, ("blue"), self.left_arm)
        pygame.draw.rect(interface, ("blue"), self.right_arm)
        pygame.draw.rect(interface, ("white"), self.left_hand)
        pygame.draw.rect(interface, ("white"), self.right_hand)
        pygame.draw.rect(interface, ("pink"), self.left_leg)
        pygame.draw.rect(interface, ("pink"), self.right_leg)
        pygame.draw.rect(interface, ("black"), self.pelvis)
        pygame.draw.rect(interface, ("black"), self.right_foot)
        pygame.draw.rect(interface, ("black"), self.left_foot)
