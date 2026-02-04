"""
Bullet class - handles projectiles
"""
import pygame
from config import *

class Bullet:
    """Bullet projectile class"""
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x - BULLET_WIDTH // 2,
            y - BULLET_HEIGHT,
            BULLET_WIDTH,
            BULLET_HEIGHT
        )
    
    def update(self, dt):
        """Move bullet upward"""
        self.rect.y -= BULLET_SPEED * dt
    
    def draw(self, screen):
        """Draw bullet as a rectangle"""
        pygame.draw.rect(screen, YELLOW, self.rect)
