import pygame

from game_code_stuff import game_stuff as stuff


pygame.init()


def run_game():
    root = pygame.display.set_mode((stuff.WIDTH, stuff.HEIGHT))

    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
    pygame.quit()

if __name__ == "__main__":
    run_game()