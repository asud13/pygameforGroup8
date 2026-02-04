"""
UI class - handles all user interface elements
"""
import pygame
from config import *

class UI:
    """User interface class for displaying game info"""
    
    def __init__(self):
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
    
    def draw_score(self, screen, score):
        """Draw the current score"""
        score_text = self.font_small.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
    
    def draw_lives(self, screen, lives):
        """Draw remaining lives"""
        lives_text = self.font_small.render(f"Lives: {lives}", True, WHITE)
        screen.blit(lives_text, (SCREEN_WIDTH - 150, 10))
    
    def draw_game_over(self, screen, final_score):
        """Draw game over screen"""
        # Game over title
        game_over_text = self.font_large.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(game_over_text, game_over_rect)
        
        # Final score
        score_text = self.font_medium.render(f"Final Score: {final_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(score_text, score_rect)
        
        # Restart instruction
        restart_text = self.font_small.render("Press R to Restart", True, CYAN)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        screen.blit(restart_text, restart_rect)
    
    def draw_pause_screen(self, screen):
        """Draw pause overlay"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.font_large.render("PAUSED", True, YELLOW)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(pause_text, pause_rect)
        
        # Resume instruction
        resume_text = self.font_small.render("Press P to Resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        screen.blit(resume_text, resume_rect)
