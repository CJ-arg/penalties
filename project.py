import pygame
import random
import constants
from goal_keeper import *
from goal import *
from ball import Ball
from gk_action import *


def main():

    player = get_player()
    playervs = get_player_vs()
    goal = get_goal()
    goalstart = Goalst(120, 100)
    action1 = Gk_action1(200, 250)
    action1vs = Gk_action1vs(200, 250)
    action2 = Gk_action2(450, 250)
    action2vs = Gk_action2vs(450, 250)
    action3 = Gk_action3(200, 400)
    action3vs = Gk_action3vs(200, 400)
    action4 = Gk_action4(450, 400)
    action4vs = Gk_action4vs(450, 400)
    action5 = Gk_action5(400, 250)
    action5vs = Gk_action5vs(400, 250)
    ball1 = Ball(200, 200)
    ball2 = Ball(570, 200)
    ball3 = Ball(200, 400)
    ball4 = Ball(570, 400)
    ball5 = Ball(400, 350)

    init_game()
    clock = pygame.time.Clock()

    interface = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    pygame.display.set_caption("⭐⭐⭐ ARGENTINE PENALTIES: THE FINAL  ⭐⭐⭐")

    run = True
    selected_ball = None
    gk_action = None
    score_blue = 0
    score_red = 0
    penalty = 1
    blue_turn = True
    waiting_enter = False

    def random_action():
        action = random.choice([action1, action2, action3, action4, action5])
        return action

    def random_action_vs():
        actionvs = random.choice(
            [action1vs, action2vs, action3vs, action4vs, action5vs]
        )
        return actionvs

    def background_fill(color):
        interface.fill(color)

    goalstart.draw(interface)
    ball1.draw(interface)
    ball2.draw(interface)
    ball3.draw(interface)
    ball4.draw(interface)
    ball5.draw(interface)
    draw_text_init(interface, "PENALTIES THE FINAL", 35, constants.WIDTH // 2, 10)
    draw_text_init(
        interface, "Select an area to shoot the ball", 20, constants.WIDTH // 2, 70
    )
    draw_text_init(
        interface,
        "Press 1 or 2 for the left or right top corners,",
        14,
        constants.WIDTH // 2,
        190,
    )
    draw_text_init(
        interface,
        "3 and 4 left and right bottom corners,",
        15,
        constants.WIDTH // 2,
        400,
    )
    draw_text_init(
        interface,
        "5 to chop it up (a high, soft kick over the goalkeeper).",
        15,
        constants.WIDTH // 2,
        300,
    )
    draw_text_init(interface, " Press ENTER to START", 25, constants.WIDTH // 2, 460)
    pygame.display.update()

    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start = False

    while run and penalty < 11:
        background_fill("green")
        goal.draw(interface)

        if not gk_action and blue_turn:
            player.draw(interface)
        elif not gk_action and not blue_turn:
            playervs.draw(interface)

        if selected_ball and gk_action:

            gk_action.draw(interface)
            selected_ball.draw(interface)

            draw_text(
                interface, "Press ENTER to continue", 25, constants.WIDTH // 2 - 40, 461
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if (
                waiting_enter
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_RETURN
            ):
                waiting_enter = False

            if event.type == pygame.KEYDOWN:
                action = random_action()
                actionvs = random_action_vs()

                if event.key == pygame.K_RETURN:
                    gk_action = None
                    blue_turn = get_turn(blue_turn)
                    if blue_turn:
                        player.draw(interface)
                    elif not blue_turn:
                        playervs.draw(interface)
                if event.key == pygame.K_1:

                    selected_ball = ball1
                    gk_action = action
                    if blue_turn:
                        gk_action = action
                    elif not blue_turn:
                        gk_action = actionvs
                    if blue_turn and gk_action != action1:
                        score_red += 1
                        waiting_enter = True
                    if not blue_turn and gk_action != action1vs:
                        score_blue += 1
                        waiting_enter = True
                    penalty += 1

                if event.key == pygame.K_2:

                    selected_ball = ball2
                    gk_action = action
                    if blue_turn:
                        gk_action = action
                    elif not blue_turn:
                        gk_action = actionvs
                    if blue_turn and gk_action != action2:
                        score_red += 1
                        waiting_enter = True
                    if not blue_turn and gk_action != action2vs:
                        score_blue += 1
                        waiting_enter = True
                    penalty += 1

                if event.key == pygame.K_3:

                    selected_ball = ball3
                    gk_action = action
                    if blue_turn:
                        gk_action = action
                    elif not blue_turn:
                        gk_action = actionvs
                    if blue_turn and gk_action != action3:
                        score_red += 1
                        waiting_enter = True
                    if not blue_turn and gk_action != action3vs:
                        score_blue += 1
                        waiting_enter = True
                    penalty += 1
                if event.key == pygame.K_4:

                    selected_ball = ball4
                    gk_action = action
                    if blue_turn:
                        gk_action = action
                    elif not blue_turn:
                        gk_action = actionvs
                    if blue_turn and gk_action != action4:
                        score_red += 1
                        waiting_enter = True
                    if not blue_turn and gk_action != action4vs:
                        score_blue += 1
                        waiting_enter = True
                    penalty += 1
                if event.key == pygame.K_5:

                    selected_ball = ball5
                    gk_action = action
                    if blue_turn:
                        gk_action = action
                    elif not blue_turn:
                        gk_action = actionvs
                    if blue_turn and gk_action != action5:
                        score_red += 1
                        waiting_enter = True
                    if not blue_turn and gk_action != action5vs:
                        score_blue += 1
                        waiting_enter = True
                    penalty += 1

        draw_text(interface, "SCORE :", 25, constants.WIDTH // 6 - 40, 10)
        draw_text_vs(interface, "SCORE :", 25, constants.WIDTH - 160, 10)
        draw_text_vs(interface, str(score_red), 25, constants.WIDTH - 90, 10)
        draw_text(interface, str(score_blue), 25, constants.WIDTH // 6 + 30, 10)

        pygame.display.update()

        clock.tick(60)

    background_fill("pink")

    if score_blue > score_red:
        text = "BLUE WINS"
    elif score_blue < score_red:
        text = "RED WINS"
    else:
        text = "IT`S A DRAW PLAY AGAIN"
    draw_text(interface, "GAME OVER", 55, constants.WIDTH // 2, 261)
    draw_text(interface, text, 45, constants.WIDTH // 2, 361)
    draw_text(interface, "Press ENTER to EXIT", 25, constants.WIDTH // 2, 461)

    pygame.display.update()

    see_result = True

    while see_result:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                see_result = False

    pygame.quit()


def get_player():
    return Gk(400, 250)


def get_player_vs():
    return Gkvs(400, 250)


def get_goal():
    return Goal(120, 100)


def get_turn(blue_turn):
    return not blue_turn


def init_game():
    pygame.init()
    return


def draw_text_init(interface, text, size, x, y):
    font = pygame.font.SysFont("Georgia", size)
    text_surface = font.render(text, True, ("green"))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    interface.blit(text_surface, text_rect)
    return


def draw_text(interface, text, size, x, y):
    font = pygame.font.SysFont("Georgia", size)
    text_surface = font.render(text, True, ("blue"))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    interface.blit(text_surface, text_rect)
    return


def draw_text_vs(interface, text, size, x, y):
    font = pygame.font.SysFont("Georgia", size)
    text_surface = font.render(text, True, ("red"))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    interface.blit(text_surface, text_rect)
    return


if __name__ == "__main__":
    main()
