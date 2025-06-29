from turtle import Screen, Turtle
import pandas
from game_engine import GameEngine

screen = Screen()
image = 'blank_states_img.gif'
screen.title('State Name Game')
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
writer = Turtle()
writer.penup()
writer.hideturtle()
game_engine = GameEngine()

while len(game_engine.answered) < 50:
    user_guess = screen.textinput(title=f'{str(len(game_engine.answered))}/50 States Correct', prompt="Type a State name").title()
    if user_guess == 'Exit':
        break
    elif user_guess in game_engine.states and user_guess not in game_engine.answered:
        answer = game_engine.data[game_engine.data.state == user_guess]
        writer.goto(answer.x.item(), answer.y.item())
        writer.color('black')
        writer.write(arg=answer.state.item(), font=('Arial', 8, 'normal'))
        game_engine.scores()
        game_engine.add_to_list(user_guess)

not_guessed = []
for things in game_engine.states:
    if things in game_engine.answered:
        pass
    else:
        not_guessed.append(things)

output = pandas.DataFrame(not_guessed)
output.to_csv('states_to_learn.csv')
