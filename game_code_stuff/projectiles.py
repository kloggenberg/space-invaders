import pygame

from game_code_stuff import game_stuff as stuff

class Projectiles():
    def __init__(self,center,direction):
        self.WIDTH = 20
        self.HEIGHT = 10
        self.x = center[0]
        self.y = center[1]
        self.direction = direction
        self.BULLET_SPEED = 20
        self.GREEN = (0,255,0)

    def draw(self,root):
        pygame.draw.rect(root, self.GREEN, (self.x,self.y-self.HEIGHT/2,self.WIDTH,self.HEIGHT))

    
    def move_projectile(self):
        if self.direction == "right":
            return self.x + self.BULLET_SPEED
        elif self.direction == "left":
            return self.x - self.BULLET_SPEED
    
    
    def check_projectile_off_screen(self):
        if self.direction == "right":
            if self.x > stuff.WIDTH:
                return True
        elif self.direction == "left":
            if self.x < 0:
                return True
        else:
            return False