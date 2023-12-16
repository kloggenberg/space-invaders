import pygame

from game_code_stuff import game_stuff as stuff
from game_code_stuff import check_wins as wins
from game_code_stuff import projectiles as pro

def run_game():
    pygame.init()
    
    #List to store arrays
    projectile_list = []
    
    #Make root screen
    root = pygame.display.set_mode((stuff.WIDTH, stuff.HEIGHT))
    
    #Creating player rects
    player1 = pygame.Rect(20,stuff.HEIGHT/2-25,stuff.PLAYER_SIZE_X,stuff.PLAYER_SIZE_Y)
    player2 = pygame.Rect(stuff.WIDTH-20-stuff.PLAYER_SIZE_X,stuff.HEIGHT/2-25,stuff.PLAYER_SIZE_X,stuff.PLAYER_SIZE_Y)
    
    #Control Shoot
    z_pressed = False
    b_pressed = False
    
    #Main game loop
    run_game = True
    while run_game:
        #Cap the speed of the loop
        stuff.clock.tick(stuff.FPS)
        
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
            elif event.type == pygame.KEYDOWN:
                if not key_pressed:
                    if event.key == pygame.K_z:  # Change this to the key you want to check
                        print("z")
                        key_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z:  # Change this to the key you want to check
                    key_pressed = False
        
        #Rest of the stuff
        root.fill(stuff.WHITE)
        
        #Draw border
        stuff.draw_border(root,stuff.WIDTH, stuff.HEIGHT)
        
        #Draw players
        stuff.draw_player1(root, player1)
        stuff.draw_player2(root,player2)
        
        # Check for key presses
        keys = pygame.key.get_pressed()

        #Movement fo player1
        #Moving on x-axis
        if keys[pygame.K_g]:
            player1.x = stuff.player1_move_x_increase(player1.x)
        if keys[pygame.K_d]:
            player1.x = stuff.player1_move_x_decrease(player1.x)
        #Moving on y-axis
        if keys[pygame.K_r]:
            player1.y = stuff.player_move_y_increase(player1.y)
        if keys[pygame.K_f]:
            player1.y = stuff.player_move_y_decrease(player1.y)
        
        #Movement fo player2
        #Moving on x-axis
        if keys[pygame.K_l]:
            player2.x = stuff.player2_move_x_increase(player2.x)
        if keys[pygame.K_j]:
            player2.x = stuff.player2_move_x_decrease(player2.x)
        #Moving on y-axis
        if keys[pygame.K_i]:
            player2.y = stuff.player_move_y_increase(player2.y)
        if keys[pygame.K_k]:
            player2.y = stuff.player_move_y_decrease(player2.y)
        
        #Check for shooting
        if keys[pygame.K_z] and z_pressed == False:
            z_pressed = True
            projectile = pro.Projectiles(player1.center, "right")
            projectile_list.append(projectile)
            print("z")
        if keys[pygame.K_b] and b_pressed == False:
            b_pressed = True
            projectile = pro.Projectiles(player1.center, "right")
            projectile_list.append(projectile)
            print("b")
            
        #Change var if player shots
        if z_pressed:
            z_pressed = False
        if b_pressed:
            z_pressed = False
        
        #Health checks
        if wins.check_win(wins.player1_health, wins.player2_health):
            run_game = False
            break
        
        #Update screen
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    run_game()