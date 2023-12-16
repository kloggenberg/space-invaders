import pygame

# from game_code_stuff import game_stuff as stuff

class Projectiles():
    def __init__(self,center,direction):
        self.WIDTH = 2
        self.HEIGHT = 1
        self.x = center[0]
        self.y = center[1]
        self.direction = direction
        self.BULLET_SPEED = 20
        self.GREEN = (0,255,0)
        self.rect = pygame.Rect(self.x,self.y,self.WIDTH, self.HEIGHT)

    def draw(self,root):
        pygame.draw.rect(root, self.GREEN, self.rect)

    
    def move_projectile(self,x):
        if self.direction == "right":
            return x + self.BULLET_SPEED
        elif self.direction == "left":
            return x - self.BULLET_SPEED
    
    
    # def check_projectile_off_screen(self):
    #     if self.direction == "right":
    #         if self.x > stuff.WIDTH:
    #             pass 
    #     elif self.direction == "left":
    #         if self.x < 0:
    #             pass