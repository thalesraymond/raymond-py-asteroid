# Asteroids Clone

A classic Asteroids game clone built with Python and Pygame.

## Overview

This project is a modern implementation of the classic arcade game *Asteroids*. The player controls a triangular ship in a field of floating asteroids. The goal is to survive as long as possible by shooting asteroids and avoiding collisions.

## Features

- **Smooth Ship Movement:** Rotate and accelerate your ship with precision.
- **Dynamic Asteroid Field:** Asteroids spawn and move at varying speeds.
- **Combat System:** Shoot projectiles that split larger asteroids into smaller ones.
- **Collision Detection:** Realistic interactions between the player, asteroids, and shots.
- **Performance Logging:** Integrated logging for game events and state tracking.

## Controls

| Key | Action |
|-----|--------|
| `W` | Move Forward |
| `S` | Move Backward |
| `A` | Rotate Left |
| `D` | Rotate Right |
| `SPACE` | Shoot |

## Requirements

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for package management)
- Pygame 2.6.1

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/raymond-py-asteroid.git
   cd raymond-py-asteroid
   ```

2. **Sync dependencies using `uv`:**
   ```bash
   uv sync
   ```

## Running the Game

To start the game, run the following command:

```bash
uv run main.py
```

## Project Structure

- `main.py`: Entry point and main game loop.
- `player.py`: Ship movement, rendering, and shooting logic.
- `asteroid.py`: Asteroid behavior and splitting mechanics.
- `asteroidfield.py`: Logic for spawning asteroids.
- `shot.py`: Projectile handling.
- `circleshape.py`: Base class for circular collision detection.
- `constants.py`: Global game constants and configuration.
- `logger.py`: Event and state logging utility.
