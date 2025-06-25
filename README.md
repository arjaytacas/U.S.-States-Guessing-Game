# 🗺️ U.S. States Guessing Game

An interactive map quiz game built with Python using Turtle graphics and Pandas.

## 🎯 Goal

Guess all 50 U.S. states! Each correct answer is displayed on the map. Exit early and the app will generate a CSV file (`states_to_learn.csv`) with the states you missed.

## 📸 Preview

![Preview Image](./preview.png) <!-- Optional: Add a screenshot if you have one -->

## 💡 Features

- Interactive Turtle-based map
- Real-time state name display on correct guess
- Input handled through simple dialog prompts
- Missed states exported to `states_to_learn.csv`
- Clean separation of logic (via `GameEngine` class)

## 📦 Technologies Used

- Python 3.6+
- Turtle (built-in GUI graphics)
- Pandas (for data handling)

## 🛠️ How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/us-states-guessing-game.git
cd us-states-guessing-game
```

2. Install dependencies:
```
pip install pandas
```
3. Make sure 50_states.csv and blank_states_img.gif are in the same directory.
4. Run the game:
```bash
python main.py
```
📁 Files
main.py: Main logic to run the game

game_engine.py: Class that manages score and state tracking

50_states.csv: Data file with state names and coordinates

blank_states_img.gif: U.S. map image for the game background

states_to_learn.csv: Automatically generated list of missed states

📄 License
This project is for educational use.
