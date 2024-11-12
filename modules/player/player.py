import modules.world.world as world
import pygame
import math

class Player:
    """
    Represents the player character in the game. Handles movement, image rotation, 
    and collision detection with enemies.
    """
    def __init__(self):
        """
        Initializes the player at the center-bottom of the screen with a specified size and speed.

        Sets up the player's initial position, health, and rect for collision detection. 
        Also loads and scales the player image for drawing.
        """
        self.x = world.WIDTH/2-25
        self.y = world.HEIGHT-50-30
        self.PLAYER_SIZE = 50
        self.PLAYER_SPEED = 8
        self.rect = pygame.Rect(self.x, self.y, self.PLAYER_SIZE, self.PLAYER_SIZE)
        self.health = 10
        self.scaled_image = pygame.transform.scale(pygame.image.load('game_assets/images/player.png'), (50, 50))
        self.rotated_image = self.scaled_image
        self.angle = 0

    def set_rect(self):
        """
        Updates the player's rect object based on the current position of the player.

        This method is used to keep the player's collision area in sync with their current location.
        """
        self.rect = pygame.Rect(self.x, self.y, self.PLAYER_SIZE, self.PLAYER_SIZE)

    def handle_movement(self, keys):
        """
        Handles the player's movement based on key presses.

        :param keys: The dictionary of key states (from pygame.key.get_pressed()) to check for movement.
        """
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
        """
        Returns the current center position of the player's rectangle.

        :return: Tuple representing the player's center (x, y).
        """
        return self.rect.center

    def move_player_right(self):
        """
        Moves the player to the right, ensuring they do not go beyond the screen width.
        """
        if self.x + self.PLAYER_SPEED < world.WIDTH - self.PLAYER_SIZE:
            self.x = self.x + self.PLAYER_SPEED

    def move_player_left(self):
        """
        Moves the player to the left, ensuring they do not go beyond the screen's left boundary.
        """
        if self.x - self.PLAYER_SPEED > 0:
            self.x = self.x - self.PLAYER_SPEED

    def move_player_up(self):
        """
        Moves the player upward, ensuring they do not go above the screen's top boundary.
        """
        if self.y - self.PLAYER_SPEED > 0:
            self.y = self.y - self.PLAYER_SPEED

    def move_player_down(self):
        """
        Moves the player downward, ensuring they do not go beyond the screen height.
        """
        if self.y + self.PLAYER_SPEED < world.HEIGHT - self.PLAYER_SIZE:
            self.y = self.y + self.PLAYER_SPEED

    def draw_player(self, root):
        """
        Draws the player as a rectangle on the screen.

        :param root: The pygame surface to draw on.
        """
        pygame.draw.rect(root, world.RED, self.rect)

    def is_alive(self):
        """
        Checks if the player is still alive based on their health.

        :return: Boolean indicating whether the player is alive.
        """
        return self.health > 0

    def put_image(self, root):
        """
        Draws the player's image (rotated if necessary) onto the screen.

        :param root: The pygame surface to draw the player image on.
        """
        root.blit(self.rotated_image, (self.x, self.y))

    def rotate_image(self, angle):
        """
        Rotates the player's image to the given angle.

        :param angle: The angle in degrees to rotate the player image.
        """
        self.rotated_image = pygame.transform.rotate(self.scaled_image, angle-90)

    def calculate_angle(self, point1, point2):
        """
        Calculates the angle between two points and rotates the player image accordingly.

        :param point1: The starting point (x, y).
        :param point2: The target point (x, y).
        """
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        self.rotate_image(math.degrees(math.atan2(-dy, dx)))

    def check_collision_with_enemy(self, enemy):
        """
        Checks if the player has collided with an enemy.

        :param enemy: The enemy object to check for collision.
        :return: Boolean indicating whether a collision has occurred.
        """
        distance = math.sqrt((self.rect.centerx - enemy.rect.centerx) ** 2 + (self.rect.centery - enemy.rect.centery) ** 2)
        return distance < self.PLAYER_SIZE / 2 + enemy.rect.width / 2
