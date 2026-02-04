# Space Shooter Game

A simple space shooter game built with Python and Pygame.

## Files Structure

- **main.py** - Entry point, initializes Pygame and runs the main game loop
- **config.py** - Game configuration and constants (colors, speeds, dimensions)
- **game.py** - Main Game class that manages game state and logic
- **player.py** - Player class handling movement and shooting
- **bullet.py** - Bullet class for projectiles
- **enemy_manager.py** - Enemy and EnemyManager classes for spawning and managing enemies
- **ui.py** - UI class for drawing score, lives, and game over screens
- **README.md** - This file with instructions

## Requirements

- Python 3.7+
- Pygame

## Installation

Install Pygame using pip:

```bash
pip install pygame
```

## How to Run

```bash
python main.py
```

## Controls

- **Arrow Keys** or **A/D** - Move left/right
- **Spacebar** - Shoot
- **P** - Pause/unpause game
- **R** - Restart game (when game over)

## Gameplay

- Shoot down enemy ships before they reach the bottom
- Avoid colliding with enemies or you'll lose a life
- Earn 10 points for each enemy destroyed
- You start with 3 lives
- Game over when all lives are lost

## Game Features

- Smooth player movement
- Automatic enemy spawning
- Collision detection
- Score tracking
- Lives system
- Pause functionality
- Game over and restart

Enjoy the game!
