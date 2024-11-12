import pygame
import random
import math

class Enemy:
    """
    Represents an enemy in the game, which moves toward the player and can be hit by projectiles.
    """
    def __init__(self, player_pos, screen_width, screen_height):
        """
        Initializes the enemy with a sprite, a random spawn position, and an initial velocity 
        towards the player.

        :param player_pos: Tuple representing the player's position (x, y).
        :param screen_width: Width of the game screen.
        :param screen_height: Height of the game screen.
        """
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
        """
        Randomly selects a position off-screen for the enemy to spawn from one of the edges.

        :param screen_width: Width of the game screen.
        :param screen_height: Height of the game screen.
        :return: Tuple representing the spawn position (x, y).
        """
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
        """
        Moves the enemy according to its calculated velocity.
        """
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def draw(self, root):
        """
        Draws the enemy on the screen at its current position.

        :param root: The game window surface where the enemy should be drawn.
        """
        root.blit(self.image, self.rect)

    def check_enemy_off_screen(self, screen_width, screen_height):
        """
        Checks if the enemy is off the screen boundaries.

        :param screen_width: Width of the game screen.
        :param screen_height: Height of the game screen.
        :return: Boolean indicating whether the enemy is off-screen.
        """
        return self.rect.x < -self.rect.width or self.rect.x > screen_width + self.rect.width or self.rect.y < -self.rect.height or self.rect.y > screen_height + self.rect.height

    def check_collision(self, projectile):
        """
        Checks if the enemy has collided with a projectile.

        :param projectile: The projectile object to check for collision with the enemy.
        :return: Boolean indicating whether a collision has occurred.
        """
        distance = math.sqrt((self.rect.centerx - projectile.x)**2 + (self.rect.centery - projectile.y)**2)
        return distance < self.rect.width / 2 + projectile.RADIUS
