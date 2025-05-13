# Interactive Molecular Dynamics Game
Learning to Molecular Dynamics while playing.

This project simulates real-time atomic collisions using Python and Pygame.  
Inspired by molecular dynamics and basic Newtonian physics, it allows you to interactively move atoms, observe their collisions, and explore dynamic behavior.

## Features
- Real-time collisions with impulse response
- Mouse interaction and attraction
- Configurable number of particles and initial velocity
- Modular and clean structure using functional design

## Installation

```bash
git clone git@github.com:dajuarez4/interactive_md_game.git
cd interactive_md_game
python -m venv md_game_env
source md_game_env/bin/activate  # or md_game_env\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
