import pygame

import game_code_stuff.game_stuff as stuff
import game_code_stuff.projectiles as pro

def main():
    pygame.init()
    
    #List for projectiles
    projectile_list = []
    
    #Make screen and set window title
    root = pygame.display.set_mode((stuff.WIDTH, stuff.HEIGHT))
    pygame.display.set_caption("My Game")
    
    #Player rect
    player = pygame.Rect(stuff.WIDTH/2-25, stuff.HEIGHT-50-30, stuff.PLAYER_SIZE, stuff.PLAYER_SIZE)
    
    #Import Image
    image = pygame.image.load('game_assets/player.png')
    scaled_width = scaled_height = 50
    scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))

    
    #Variable to help control shoot
    shoot = False
    
    run_game = True
    while run_game:
        #Control Loop framerate
        stuff.clock.tick(stuff.FPS)
        
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and shoot == False:
                    projectile = pro.Projectiles(player.center)
                    projectile_list.append(projectile)
                    shoot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z and shoot == True:
                    shoot = False
                    
        #Make screen color Black
        root.fill(stuff.BLACK)
        
        #Draw the player
        # stuff.draw_player(root,player)
        root.blit(scaled_image, (player.x, player.y))
        
        #Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x = stuff.move_player_left(player.x)
        if keys[pygame.K_RIGHT]:
            player.x = stuff.move_player_right(player.x)
        
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