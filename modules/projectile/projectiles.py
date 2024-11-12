import pygame
import math

class Projectiles:
    def __init__(self, center, target):
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
        # Draw the glow effect
        # self.draw_glow(root)
        # Draw the projectile circle
        pygame.draw.circle(root, self.GREEN, (int(self.x), int(self.y)), self.RADIUS)

    # def draw_glow(self, root):
    #     # Create a gradient glow effect
    #     for i in range(1, 8):
    #         alpha = max(0, 255 - 32 * i)
    #         glow_surface = pygame.Surface((self.RADIUS * 8, self.RADIUS * 8), pygame.SRCALPHA)
    #         pygame.draw.circle(glow_surface, (*self.GREEN, alpha), (self.RADIUS * 4, self.RADIUS * 4), self.RADIUS * i)
    #         root.blit(glow_surface, (self.x - self.RADIUS * 4, self.y - self.RADIUS * 4), special_flags=pygame.BLEND_RGBA_ADD)

    def move_projectile(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def check_projectile_off_screen(self, screen_width, screen_height):
        return self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height