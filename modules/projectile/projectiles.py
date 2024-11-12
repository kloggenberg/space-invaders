import pygame
import math

class Projectiles:
    """
    Represents a projectile fired from the player towards a target. Handles movement, 
    drawing, and off-screen detection of the projectile.
    """
    def __init__(self, center, target):
        """
        Initializes the projectile with a starting position and a target.
        
        :param center: The (x, y) coordinates for the starting position of the projectile.
        :param target: The (x, y) coordinates of the target, usually the mouse position.
        """
        self.RADIUS = 5  # Radius of the projectile
        self.x = center[0]
        self.y = center[1]
        self.BULLET_SPEED = 10
        self.GREEN = (0, 255, 0)

        # Calculate angle to target (mouse position)
        dx = target[0] - center[0]
        dy = target[1] - center[1]
        self.angle = math.degrees(math.atan2(dy, dx))
        self.velocity_x = self.BULLET_SPEED * math.cos(math.radians(self.angle))
        self.velocity_y = self.BULLET_SPEED * math.sin(math.radians(self.angle))

    def draw(self, root):
        """
        Draws the projectile as a circle on the screen.

        :param root: The pygame surface on which to draw the projectile.
        """
        pygame.draw.circle(root, self.GREEN, (int(self.x), int(self.y)), self.RADIUS)

    # def draw_glow(self, root):
    #     """
    #     (Optional) Draws a glow effect around the projectile. 
    #     This effect is currently commented out.
    #
    #     :param root: The pygame surface on which to draw the glow.
    #     """
    #     for i in range(1, 8):
    #         alpha = max(0, 255 - 32 * i)
    #         glow_surface = pygame.Surface((self.RADIUS * 8, self.RADIUS * 8), pygame.SRCALPHA)
    #         pygame.draw.circle(glow_surface, (*self.GREEN, alpha), (self.RADIUS * 4, self.RADIUS * 4), self.RADIUS * i)
    #         root.blit(glow_surface, (self.x - self.RADIUS * 4, self.y - self.RADIUS * 4), special_flags=pygame.BLEND_RGBA_ADD)

    def move_projectile(self):
        """
        Updates the position of the projectile based on its velocity.
        """
        self.x += self.velocity_x
        self.y += self.velocity_y

    def check_projectile_off_screen(self, screen_width, screen_height):
        """
        Checks if the projectile is off the screen.

        :param screen_width: The width of the screen.
        :param screen_height: The height of the screen.
        :return: Boolean indicating whether the projectile is off-screen.
        """
        return self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height
