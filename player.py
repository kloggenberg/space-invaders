import world as world

import pygame

class Player:
    def __init__(self):
        self.x = world.WIDTH/2-25
        self.y = world.HEIGHT-50-30
        self.PLAYER_SIZE = 50
        self.PLAYER_SPEED = 8
        self.rect = pygame.Rect(self.x, self.y, self.PLAYER_SIZE, self.PLAYER_SIZE)
        # self.center = self.rect
        self.health = 5
        self.image = pygame.image.load('game_assets/player.png')
        self.scaled_image = pygame.transform.scale(self.image, (50, 50))


    def get_center(self):
        return self.rect.center


    def handle_movement(self,keys):
        if keys[pygame.K_RIGHT]:
            self.move_player_right()
        if keys[pygame.K_LEFT]:
            self.move_player_left()
        if keys[pygame.K_UP]:
            self.move_player_up()
        if keys[pygame.K_DOWN]:
            self.move_player_down()


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
    

    def take_damage(self,ememy_attack):
        self.health = self.health - ememy_attack

    
    def put_image(self,root):
        root.blit(self.scaled_image, (self.x, self.y))