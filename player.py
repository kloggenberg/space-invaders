import world as world

import pygame
import math

class Player:
    def __init__(self):
        self.x = world.WIDTH/2-25
        self.y = world.HEIGHT-50-30
        self.PLAYER_SIZE = 50
        self.PLAYER_SPEED = 8
        self.rect = pygame.Rect(self.x, self.y, self.PLAYER_SIZE, self.PLAYER_SIZE)
        self.health = 10
        self.scaled_image = pygame.transform.scale(pygame.image.load('game_assets/player.png'), (50, 50))
        self.rotated_image = self.scaled_image
        self.angle = 0


    def set_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.PLAYER_SIZE, self.PLAYER_SIZE)


    def handle_movement(self,keys):
        if keys[pygame.K_d]:
            self.move_player_right()
        if keys[pygame.K_a]:
            self.move_player_left()
        if keys[pygame.K_w]:
            self.move_player_up()
        if keys[pygame.K_s]:
            self.move_player_down()
        self.set_rect()


    def get_center(self):
        return self.rect.center
        
        
    def move_player_right(self):
        if self.x + self.PLAYER_SPEED < world.WIDTH - self.PLAYER_SIZE:
            self.x = self.x + self.PLAYER_SPEED
    

    def move_player_left(self):
        if self.x - self.PLAYER_SPEED > 0:
            self.x = self.x- self.PLAYER_SPEED
    

    def move_player_up(self):
        if self.y - self.PLAYER_SPEED > 0:
            self.y = self.y - self.PLAYER_SPEED

    
    def move_player_down(self):
        if self.y + self.PLAYER_SPEED < world.HEIGHT - self.PLAYER_SIZE:
            self.y = self.y + self.PLAYER_SPEED

    
    def draw_player(self,root):
        pygame.draw.rect(root, world.RED, self.rect)


    def is_alive(self):
        if self.health > 0:
            return True
        return False

    
    def put_image(self,root):
        root.blit(self.rotated_image, (self.x, self.y))
        
        
    def rotate_image(self,angle):
        self.rotated_image = pygame.transform.rotate(self.scaled_image, angle-90)
    
    
    def calculate_angle(self,point1, point2):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        self.rotate_image(math.degrees(math.atan2(-dy, dx)))
    
    
    def check_collision_with_enemy(self, enemy):
            distance = math.sqrt((self.rect.centerx - enemy.rect.centerx) ** 2 + (self.rect.centery - enemy.rect.centery) ** 2)
            return distance < self.PLAYER_SIZE / 2 + enemy.rect.width / 2