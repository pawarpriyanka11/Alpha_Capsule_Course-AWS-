# Advanced Caterpillar Flag Game

A Python game built with Pygame where you control a caterpillar to collect flags.

## Features

- Caterpillar that grows as you collect flags
- Six colored flags to collect
- Obstacles to navigate around
- Particle effects when collecting flags
- Trail showing the caterpillar's path
- Menu system with start/quit options
- High score tracking
- Sound effects (optional)

## Controls

- Arrow keys: Move the caterpillar
- R: Restart the game
- ESC: Toggle menu

## Setup

1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the game:
   ```
   python game.py
   ```

## Optional Sound Files

For sound effects, add these files to the game directory:
- `collect.wav` - Played when collecting a flag
- `gameover.wav` - Played when the game ends

The game will work without these files, but will be silent.

## Game Mechanics

- Control the caterpillar to collect all six flags
- Each flag is worth 50 points
- The caterpillar grows longer with each flag collected
- Navigate around blue obstacles
- Game ends when all flags are collected
- Try to beat your high score!
