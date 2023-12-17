import pygame

#Constants
WIDTH, HEIGHT = 1500, 900

WHITE, BLACK, RED, BLUE = (255,255,255), (0, 0, 0), (255,0,0), (0,0,255)

PLAYER_SIZE_X, PLAYER_SIZE_Y = 50, 50
PLAYER_SPEED = 5 

clock = pygame.time.Clock()
FPS = 60

def draw_border(root, WIDTH, HEIGHT):
    pygame.draw.rect(root, WHITE ,(WIDTH/2-10, 0, 10, HEIGHT))
    

def draw_player1(root,player):
    pygame.draw.rect(root, RED, player)
    
    
def draw_player2(root,player):
    pygame.draw.rect(root, BLUE, player)


#Move functions for player1
def player1_move_x_increase(x):
    if x+PLAYER_SPEED < WIDTH/2-10-PLAYER_SIZE_X:
        return x+PLAYER_SPEED
    return x

def player1_move_x_decrease(x):
    if x-PLAYER_SPEED > 0:
        return x-PLAYER_SPEED
    return x

def player_move_y_increase(y):
    if y-PLAYER_SPEED > 0:
        return y-PLAYER_SPEED
    return y

def player_move_y_decrease(y):
    if y+PLAYER_SPEED < HEIGHT-PLAYER_SIZE_Y:
        return y+PLAYER_SPEED
    return y


#Move functions for player2
def player2_move_x_increase(x):
    if x+PLAYER_SPEED < WIDTH-PLAYER_SIZE_X:
        return x+PLAYER_SPEED
    return x

def player2_move_x_decrease(x):
    if x-PLAYER_SPEED > WIDTH/2:
        return x-PLAYER_SPEED
    return x