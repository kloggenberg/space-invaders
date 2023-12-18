import pygame

#Constants
WIDTH, HEIGHT = 600, 900

WHITE, BLACK, RED, BLUE = (255,255,255), (0, 0, 0), (255,0,0), (0,0,255)

PLAYER_SIZE = 50

PLAYER_SPEED = 5 

clock = pygame.time.Clock()
FPS = 60

def draw_player(root,player):
    pygame.draw.rect(root, RED, player)