import pygame
import random
import math
import os

from world import *
from player import Player
from projectiles import Projectiles
from enemy import Enemy

# Load custom font
FONT_PATH = 'game_assets/font/arcadeclassic/ARCADECLASSIC.TTF'

def show_menu():
    pygame.init()
    
    root = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu")

    # Load the background image
    background_image = pygame.image.load('game_assets/background.jpg')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    font_title = pygame.font.Font(FONT_PATH, 74)
    font_prompt = pygame.font.Font(FONT_PATH, 36)
    
    title_text = font_title.render('Space Invaders', True, (255, 255, 255))
    prompt_text = font_prompt.render('Press SPACE to start', True, (255, 255, 255))

    title_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    prompt_rect = prompt_text.get_rect(center=(WIDTH / 2, HEIGHT - 50))

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False

        root.blit(background_image, (0, 0))
        root.blit(title_text, title_rect)
        root.blit(prompt_text, prompt_rect)
        pygame.display.update()

def show_game_over_screen(score):
    pygame.init()
    
    root = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Over")

    # Load the background image
    background_image = pygame.image.load('game_assets/background.jpg')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    font_game_over = pygame.font.Font(FONT_PATH, 74)
    font_score = pygame.font.Font(FONT_PATH, 36)
    font_prompt = pygame.font.Font(FONT_PATH, 36)
    
    game_over_text = font_game_over.render('Game Over', True, (255, 255, 255))
    score_text = font_score.render(f'Score: {score}', True, (255, 255, 255))
    prompt_text = font_prompt.render('Press R to restart or Q to quit', True, (255, 255, 255))

    game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    score_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20))
    prompt_rect = prompt_text.get_rect(center=(WIDTH / 2, HEIGHT - 50))

    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    main()  # Restart the game
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        root.blit(background_image, (0, 0))
        root.blit(game_over_text, game_over_rect)
        root.blit(score_text, score_rect)
        root.blit(prompt_text, prompt_rect)
        pygame.display.update()

def main():
    pygame.init()
    
    # List for projectiles
    projectile_list = []
    # List for enemies
    enemy_list = []
    
    # Make screen and set window title
    root = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    
    # Make Player
    player = Player()
    
    # Variable to help control shoot
    shoot = False

    run_game = True
    clock = pygame.time.Clock()
    score = 0
    
    while run_game:
        clock.tick(FPS)
        
        # Get the mouse position
        mouse_position = pygame.mouse.get_pos()
        
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not shoot:  # Left mouse button
                    projectile = Projectiles(player.get_center(), mouse_position)
                    projectile_list.append(projectile)
                    shoot = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and shoot:  # Left mouse button
                    shoot = False

        # Randomly spawn enemies
        if random.randint(1, 100) <= 5:  # Adjust the probability as needed
            enemy = Enemy(player.get_center(), WIDTH, HEIGHT)
            enemy_list.append(enemy)
                    
        player.calculate_angle(player.rect.center, mouse_position)
        
        # Make screen color Black
        root.fill(BLACK)
        
        keys = pygame.key.get_pressed()
        player.handle_movement(keys)

        # Move and draw the projectiles
        for projectile in projectile_list[:]:
            projectile.move_projectile()
            if projectile.check_projectile_off_screen(WIDTH, HEIGHT):
                projectile_list.remove(projectile)
            else:
                projectile.draw(root)

        # Move and draw the enemies
        for enemy in enemy_list[:]:
            enemy.move_enemy()
            if enemy.check_enemy_off_screen(WIDTH, HEIGHT):
                enemy_list.remove(enemy)
            else:
                enemy.draw(root)

        # Check for collisions between projectiles and enemies
        for enemy in enemy_list[:]:
            for projectile in projectile_list[:]:
                if enemy.check_collision(projectile):
                    enemy_list.remove(enemy)
                    projectile_list.remove(projectile)
                    score += 1  # Increase the score by 1
                    break  # Exit inner loop to avoid modifying the list while iterating

        # Check for collisions between player and enemies
        for enemy in enemy_list[:]:
            if player.check_collision_with_enemy(enemy):
                player.health -= 1
                enemy_list.remove(enemy)
                if not player.is_alive():
                    run_game = False
                    break  # Exit the game loop if player is not alive

        # Draw the player
        player.put_image(root)
        
        # Display health
        font = pygame.font.Font(FONT_PATH, 36)
        health_text = font.render(f'Health: {player.health}', True, (255, 255, 255))
        root.blit(health_text, (10, 10))
        
        # Display score
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        root.blit(score_text, (WIDTH - 150, 10))
        
        pygame.display.update()
    
    show_game_over_screen(score)  # Show game over screen when the game ends
    pygame.quit()

if __name__ == '__main__':
    show_menu()
    main()
