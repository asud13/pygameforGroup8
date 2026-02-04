"""
Main game file - Space Shooter Game
"""
import pygame
import sys
from game import Game
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WINDOW_TITLE

def main():
    """Initialize and run the game"""
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    
    # Create clock for managing frame rate
    clock = pygame.time.Clock()
    
    # Create game instance
    game = Game(screen)
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
        
        # Update game state
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        game.update(dt)
        
        # Draw everything
        game.draw()
        
        # Update display
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
