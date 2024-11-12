import pygame
import random
import math

class Enemy:
    def __init__(self, player_pos, screen_width, screen_height):
        # Load the enemy sprite
        self.image = pygame.image.load('game_assets/images/enemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))  # Adjust the size as needed
        self.rect = self.image.get_rect()

        # Randomly spawn enemy off-screen
        self.rect.x, self.rect.y = self.random_spawn_position(screen_width, screen_height)
        
        # Calculate angle to the player
        dx = player_pos[0] - self.rect.x
        dy = player_pos[1] - self.rect.y
        self.angle = math.degrees(math.atan2(dy, dx))
        self.speed = 5
        self.velocity_x = self.speed * math.cos(math.radians(self.angle))
        self.velocity_y = self.speed * math.sin(math.radians(self.angle))

    def random_spawn_position(self, screen_width, screen_height):
        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            return (random.randint(0, screen_width), -self.rect.height)
        elif edge == 'bottom':
            return (random.randint(0, screen_width), screen_height + self.rect.height)
        elif edge == 'left':
            return (-self.rect.width, random.randint(0, screen_height))
        elif edge == 'right':
            return (screen_width + self.rect.width, random.randint(0, screen_height))

    def move_enemy(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def draw(self, root):
        root.blit(self.image, self.rect)

    def check_enemy_off_screen(self, screen_width, screen_height):
        return self.rect.x < -self.rect.width or self.rect.x > screen_width + self.rect.width or self.rect.y < -self.rect.height or self.rect.y > screen_height + self.rect.height

    def check_collision(self, projectile):
        distance = math.sqrt((self.rect.centerx - projectile.x)**2 + (self.rect.centery - projectile.y)**2)
        return distance < self.rect.width / 2 + projectile.RADIUS