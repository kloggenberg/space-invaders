import pygame

from game_code_stuff import game_stuff as stuff

class Projectiles():
    def __init__(self,center):
        self.WIDTH = 10
        self.HEIGHT = 20
        self.x = center[0]-5
        self.y = center[1]
        self.BULLET_SPEED = 10
        self.GREEN = (0,255,0)

    def draw(self,root):
        pygame.draw.rect(root, self.GREEN, (self.x,self.y-self.HEIGHT/2,self.WIDTH,self.HEIGHT))

    
    def move_projectile(self):
        return self.y-self.BULLET_SPEED
    
    
    def check_projectile_off_screen(self):
        if self.y < 0:
            return True
        else:
            return False