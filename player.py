"""
Player class - handles player character
"""
import pygame
from bullet import Bullet
from config import *

class Player:
    """Player character class"""
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - PLAYER_WIDTH // 2, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.bullets = []
        self.shoot_timer = 0
        
    def update(self, dt, keys):
        """Update player position and bullets"""
        # Movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED * dt
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        
        # Update shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        
        # Update bullets
        for bullet in self.bullets[:]:
            bullet.update(dt)
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
    
    def shoot(self):
        """Create a new bullet if timer allows"""
        if self.shoot_timer <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.append(bullet)
            self.shoot_timer = PLAYER_SHOOT_DELAY
    
    def draw(self, screen):
        """Draw player and bullets"""
        # Draw player as a triangle
        points = [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.right, self.rect.bottom)
        ]
        pygame.draw.polygon(screen, GREEN, points)
        
        # Draw bullets
        for bullet in self.bullets:
            bullet.draw(screen)
