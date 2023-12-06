# Turtle Crossing Game

This is a simple implementation of the Turtle Crossing game using the Turtle graphics library in Python. In this game, the player (controlled by the user) tries to cross a busy road without getting hit by oncoming cars.

## How to Play

- Use the "w" key to move the player turtle upward.
- Avoid getting hit by the oncoming cars.
- Successfully cross the road to reach the finish line and advance to the next level.

## Dependencies

- Python 3.x
- Turtle graphics library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PrathamVerma999/turtle-crossing-game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd turtle-crossing-game
    ```

3. Run the game:

    ```bash
    python main.py
    ```

## Gameplay

- The game window is set to a size of 600x600 pixels.
- The player starts at the bottom of the screen and moves upwards using the "w" key.
- Cars move horizontally across the screen at varying speeds.
- If the player collides with a car, the game ends.
- Successfully reaching the finish line increases the level, and the pace of cars also increases.

## Code Structure

- `main.py`: The main script that initializes the game and runs the game loop.
- `player.py`: Defines the Player class, representing the user-controlled turtle.
- `car_manager.py`: Manages the generation and movement of cars on the screen.
- `scoreboard.py`: Handles the scoring and level progression.

## Customization

Feel free to customize the game by adjusting parameters such as screen size, player movement controls, and game dynamics in the respective files.

```python
# Example: Change screen size
screen.setup(width=800, height=600)
