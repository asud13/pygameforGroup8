"""
Enemy management - handles enemy spawning and behavior
"""
import pygame
import random
from config import *

class Enemy:
    """Enemy character class"""
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
    
    def update(self, dt):
        """Move enemy downward"""
        self.rect.y += ENEMY_SPEED * dt
    
    def draw(self, screen):
        """Draw enemy as a rectangle"""
        pygame.draw.rect(screen, RED, self.rect)
        # Draw eyes
        eye_size = 4
        left_eye = (self.rect.left + 10, self.rect.top + 10)
        right_eye = (self.rect.right - 10, self.rect.top + 10)
        pygame.draw.circle(screen, WHITE, left_eye, eye_size)
        pygame.draw.circle(screen, WHITE, right_eye, eye_size)


class EnemyManager:
    """Manages enemy spawning and updates"""
    
    def __init__(self):
        self.enemies = []
        self.spawn_timer = ENEMY_SPAWN_DELAY
    
    def update(self, dt):
        """Update all enemies and spawn new ones"""
        # Update spawn timer
        self.spawn_timer -= dt
        if self.spawn_timer <= 0:
            self.spawn_enemy()
            self.spawn_timer = ENEMY_SPAWN_DELAY
        
        # Update all enemies
        for enemy in self.enemies:
            enemy.update(dt)
    
    def spawn_enemy(self):
        """Create a new enemy at random x position"""
        x = random.randint(ENEMY_WIDTH, SCREEN_WIDTH - ENEMY_WIDTH)
        enemy = Enemy(x, -ENEMY_HEIGHT)
        self.enemies.append(enemy)
    
    def draw(self, screen):
        """Draw all enemies"""
        for enemy in self.enemies:
            enemy.draw(screen)
