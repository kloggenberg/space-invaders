import pygame

import game_code_stuff.game_stuff as stuff

def main():
    pygame.init()
    
    root = pygame.display.set_mode((stuff.WIDTH, stuff.HEIGHT))
    pygame.display.set_caption("My Game")
    
    player = pygame.Rect(stuff.WIDTH/2-25, stuff.HEIGHT-50-25, stuff.PLAYER_SIZE, stuff.PLAYER_SIZE)
    
    run_game = True
    while run_game:
        stuff.clock.tick(stuff.FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
        root.fill(stuff.BLACK)
        
        stuff.draw_player(root,player)
        
        pygame.display.update()
    pygame.quit()






if __name__ == '__main__':
    main()