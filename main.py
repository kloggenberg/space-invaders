import pygame

from world import *
from projectiles import Projectiles
from player import Player

def main():
    pygame.init()
    
    #List for projectiles
    projectile_list = []
    
    #Make screen and set window title
    root = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    
    #Make Player
    player = Player()
    
    
    # #Import Image
    # image = pygame.image.load('game_assets/player.png')
    # scaled_width = scaled_height = 50
    # scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))

    
    #Variable to help control shoot
    shoot = False

    run_game = True
    while run_game:
        clock.tick(FPS)
        
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and shoot == False:
                    projectile = Projectiles(player.get_center())
                    projectile_list.append(projectile)
                    shoot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z and shoot == True:
                    shoot = False
                    
                    
        #Make screen color Black
        root.fill(BLACK)
        
        #Draw the player
        # stuff.draw_player(root,player)
        player.put_image(root)
        
        keys = pygame.key.get_pressed()
        player.handle_movement(keys)

        #Draw the projectiles
        for ob in projectile_list:
            ob.draw(root)
            
        #Move the projectiles
        for ob in projectile_list:
            ob.y = ob.move_projectile()
            
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()