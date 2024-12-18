import pygame
import random
import math
import os

from modules.world.world import *
from modules.player.player import Player
from modules.projectile.projectiles import Projectiles
from modules.enemy.enemy import Enemy

FONT_PATH = 'game_assets/font/arcadeclassic/ARCADECLASSIC.TTF'

def show_menu():
    """
    Initializes the menu screen, plays background music, and waits for user input 
    to start the game or quit.
    """
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("game_assets/music/start_sound.mp3")
    pygame.mixer.music.play(-1)

    root = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu")

    background_image = pygame.image.load('game_assets/images/background.jpg')
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

    pygame.mixer.music.stop()


def show_game_over_screen(score):
    """
    Displays the game over screen, showing the final score and providing options 
    to restart or quit.
    """
    pygame.init()

    root = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Over")

    background_image = pygame.image.load('game_assets/images/background.jpg')
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
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        root.blit(background_image, (0, 0))
        root.blit(game_over_text, game_over_rect)
        root.blit(score_text, score_rect)
        root.blit(prompt_text, prompt_rect)
        pygame.display.update()


def main():
    """
    The main game loop that initializes the game, handles player movement, projectile 
    firing, enemy spawning, collision detection, and updates the score and health.
    """
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("game_assets/music/battle_music.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)

    shoot_sound = pygame.mixer.Sound("game_assets/music/shoot_sound.wav")

    projectile_list = []
    enemy_list = []

    root = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")

    player = Player()

    shoot = False

    run_game = True
    clock = pygame.time.Clock()
    score = 0

    while run_game:
        clock.tick(FPS)

        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not shoot:
                    projectile = Projectiles(player.get_center(), mouse_position)
                    projectile_list.append(projectile)
                    shoot = True
                    shoot_sound.play()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and shoot:
                    shoot = False

        if random.randint(1, 100) <= 5:
            enemy = Enemy(player.get_center(), WIDTH, HEIGHT)
            enemy_list.append(enemy)

        player.calculate_angle(player.rect.center, mouse_position)

        root.fill(BLACK)

        keys = pygame.key.get_pressed()
        player.handle_movement(keys)

        for projectile in projectile_list[:]:
            projectile.move_projectile()
            if projectile.check_projectile_off_screen(WIDTH, HEIGHT):
                projectile_list.remove(projectile)
            else:
                projectile.draw(root)

        for enemy in enemy_list[:]:
            enemy.move_enemy()
            if enemy.check_enemy_off_screen(WIDTH, HEIGHT):
                enemy_list.remove(enemy)
            else:
                enemy.draw(root)

        for enemy in enemy_list[:]:
            for projectile in projectile_list[:]:
                if enemy.check_collision(projectile):
                    enemy_list.remove(enemy)
                    projectile_list.remove(projectile)
                    score += 1
                    break

        for enemy in enemy_list[:]:
            if player.check_collision_with_enemy(enemy):
                player.health -= 1
                enemy_list.remove(enemy)
                if not player.is_alive():
                    run_game = False
                    break

        player.put_image(root)

        font = pygame.font.Font(FONT_PATH, 36)
        health_text = font.render(f'Health   {player.health}', True, (255, 255, 255))
        root.blit(health_text, (10, 10))

        score_text = font.render(f'Score   {score}', True, (255, 255, 255))
        root.blit(score_text, (WIDTH - 150, 10))

        pygame.display.update()

    pygame.mixer.music.stop()
    show_game_over_screen(score)
    pygame.quit()


if __name__ == '__main__':
    show_menu()
    main()
