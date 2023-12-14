import pygame

from game_code_stuff import game_stuff as stuff

def run_game():
    pygame.init()
    
    #Make root screen
    root = pygame.display.set_mode((stuff.WIDTH, stuff.HEIGHT))
    
    #Each Player's health at start of game
    player1_health = 5
    player2_health = 5
    
    player1 = pygame.Rect(20,stuff.HEIGHT/2-25,stuff.players_size_x,stuff.players_size_y)
    
    run_game = True
    while run_game:
        stuff.clock.tick(stuff.FPS)
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
            
        #Rest of the stuff
        root.fill(stuff.WHITE)
        #Drawing reacts
        stuff.draw_border(root,stuff.WIDTH, stuff.HEIGHT)
        stuff.draw_players(root, player1)    
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    run_game()