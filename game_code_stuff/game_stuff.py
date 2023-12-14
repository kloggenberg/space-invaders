import pygame

#Constants
WIDTH, HEIGHT = 1500, 900

WHITE, BLACK, RED, BLUE = (255,255,255), (0, 0, 0), (255,0,0), (0,0,255)

players_size_x, players_size_y = 50, 50


clock = pygame.time.Clock()
FPS = 60

def draw_border(root, WIDTH, HEIGHT):
    pygame.draw.rect(root, BLACK ,(WIDTH/2-10, 0, 10, HEIGHT))
    

def draw_players(root,player):
    pygame.draw.rect(root, RED, player)


def player1_move():
    pass

def player1_move():
    pass