"""
Main Game class - manages game state and game objects
"""
import pygame
from player import Player
from enemy_manager import EnemyManager
from ui import UI
from config import *

class Game:
    """Main game class that handles game logic and state"""
    
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)
        self.enemy_manager = EnemyManager()
        self.ui = UI()
        
        self.score = 0
        self.lives = INITIAL_LIVES
        self.game_over = False
        self.paused = False
        
    def handle_event(self, event):
        """Handle pygame events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.game_over:
                self.player.shoot()
            elif event.key == pygame.K_p:
                self.paused = not self.paused
            elif event.key == pygame.K_r and self.game_over:
                self.reset_game()
    
    def update(self, dt):
        """Update game state"""
        if self.game_over or self.paused:
            return
        
        # Get keyboard state for continuous movement
        keys = pygame.key.get_pressed()
        
        # Update player
        self.player.update(dt, keys)
        
        # Update enemies
        self.enemy_manager.update(dt)
        
        # Check for collisions between bullets and enemies
        for bullet in self.player.bullets[:]:
            for enemy in self.enemy_manager.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.player.bullets.remove(bullet)
                    self.enemy_manager.enemies.remove(enemy)
                    self.score += POINTS_PER_ENEMY
                    break
        
        # Check for collisions between player and enemies
        for enemy in self.enemy_manager.enemies[:]:
            if self.player.rect.colliderect(enemy.rect):
                self.enemy_manager.enemies.remove(enemy)
                self.lives -= 1
                if self.lives <= 0:
                    self.game_over = True
        
        # Remove enemies that went off screen
        for enemy in self.enemy_manager.enemies[:]:
            if enemy.rect.top > SCREEN_HEIGHT:
                self.enemy_manager.enemies.remove(enemy)
    
    def draw(self):
        """Draw everything to the screen"""
        self.screen.fill(BLACK)
        
        if not self.game_over:
            # Draw game objects
            self.player.draw(self.screen)
            self.enemy_manager.draw(self.screen)
            
            # Draw UI
            self.ui.draw_score(self.screen, self.score)
            self.ui.draw_lives(self.screen, self.lives)
            
            if self.paused:
                self.ui.draw_pause_screen(self.screen)
        else:
            self.ui.draw_game_over(self.screen, self.score)
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)
        self.enemy_manager = EnemyManager()
        self.score = 0
        self.lives = INITIAL_LIVES
        self.game_over = False
        self.paused = False
