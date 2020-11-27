# SNAKE AND LADDER GAME

import time
import random
import sys

Time_Gap = 1
MAX_VAL = 100
DICE_FACE = [1, 2, 3, 4, 5, 6]

snakes = {
    8: 4,
    18: 10,
    26: 19,
    39: 25,
    51: 46,
    83: 65,
    85: 59,
    92: 45,
    
}

ladders = {
    3: 20,
    6: 24,
    11: 48,
    15: 64,
    17: 74,
    22: 67,
    27: 51,
    32: 81,
    38: 59,
    45: 76,
    49: 98,
    57: 92,
    69: 89,
    73: 93,
    82: 90,
    85: 99
    
}

player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang"
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]


class SnakeAndLadder ():
    global Time_Gap
    global MAX_VAL
    global DICE_FACE
    global snakes
    global ladders
    global player_turn_text
    global snake_bite
    global ladder_jump

    def __init__(self):
        pass

    def welcome_msg(self):
        msg = """
        Welcome to Snake and Ladder Game.

        Rules:
        1. Initally both the players are at s tarting position i.e. 0.
            Take it in turns to roll the dice.
            Move forward the number of spaces shown on the dice.
        2. If you lands at the bottom of a ladder,
                you can move up to the top of the ladder.
        3. If you lands on the head of a snake,
                you must slide down to the bottom of the snake.
        4. The first player to get to the FINAL position is the winner.
        5. Hit enter to roll the dice.
        6. Enter "exit()"(without Quotes) to exit the Game.

        """
        print(msg)

    def get_player_names(self):
        player1_name = None
        while not player1_name:
            player1_name = input(
                "Please enter a valid name for first player: ").strip()
            if player1_name == "exit()":
                sys.exit(1)
        player2_name = None
        while not player2_name:
            player2_name = input(
                "Please enter a valid name for second player: ").strip()
            if player2_name == "exit()":
                sys.exit(1)
        print("\nMatch will be played between " +
              player1_name + " and " + player2_name + "\n")
        return player1_name, player2_name

    def get_dice_value(self):
        time.sleep(Time_Gap)
        dice_value = random.choice(DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value

    def got_snake_bite(self, old_value, current_value, player_name):
        print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
        print("\n" + player_name + " got a snake bite. Down from " +
              str(old_value) + " to " + str(current_value))

    def got_ladder_jump(self, old_value, current_value, player_name):
        print("\n" + random.choice(ladder_jump).upper() + " ########")
        print("\n" + player_name + " climbed the ladder from " +
              str(old_value) + " to " + str(current_value))

    def snake_ladder(self, player_name, current_value, dice_value):
        time.sleep(Time_Gap)
        old_value = current_value
        current_value = current_value + dice_value

        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) +
                  " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " +
              str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            self.got_snake_bite(current_value, final_value, player_name)

        elif current_value in ladders:
            final_value = ladders.get(current_value)
            self.got_ladder_jump(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value

    def check_win(self, player_name, position):
        time.sleep(Time_Gap)
        if MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            print("\nThank you for playing the game.")
            sys.exit(1)

    def select_player_start(self):

        player1_name, player2_name = self.get_player_names()
        time.sleep(Time_Gap)
        player1_current_position = 0
        player2_current_position = 0
        while True:
            time.sleep(Time_Gap)
            player1_input = input("\n" + player1_name + ": " +
                                  random.choice(player_turn_text) +
                                  " Hit the enter to roll dice: ")

            if player1_input == "exit()":
                sys.exit(1)

            print("\nRolling dice...")
            dice_value = self.get_dice_value()
            time.sleep(Time_Gap)
            print(player1_name + " moving....")
            player1_current_position = self.snake_ladder(
                player1_name, player1_current_position, dice_value)

            self.check_win(player1_name, player1_current_position)

            player2_input = input("\n" + player2_name + ": " +
                                  random.choice(player_turn_text) +
                                  " Hit the enter to roll dice: ")

            if player2_input == "exit()":
                sys.exit(1)

            print("\nRolling dice...")
            dice_value = self.get_dice_value()
            time.sleep(Time_Gap)
            print(player2_name + " moving....")
            player2_current_position = self.snake_ladder(
                player2_name, player2_current_position, dice_value)

            self.check_win(player2_name, player2_current_position)

    def get_player_names_computer(self):

        player1_name = None

        while not player1_name:
            player1_name = input(
                "\nPlease Enter a valid name for Player : ").strip()
            if player1_name == "exit()":
                sys.exit(1)

        player2_name = "Computer"

        print("\nMatch will be played between " +
              player1_name + " and " + player2_name + "\n")
        return player1_name, player2_name

    def select_computer_start(self):

        player1_name, player2_name = self.get_player_names_computer()
        time.sleep(1)
        player1_current_position = 0
        player2_current_position = 0
        while True:
            time.sleep(Time_Gap)
            player1_input = input(
                "\n"+player1_name + ":" + random.choice(player_turn_text) +
                "Hit the enter to roll dice : ")

            if player1_input == "exit()":
                sys.exit(1)

            print("\n Rolling Dice.....")

            dice_value = self.get_dice_value()

            time.sleep(Time_Gap)
            print(player1_name + " is Moving...")

            player1_current_position = self.snake_ladder(
                player1_name, player1_current_position, dice_value)

            self.check_win(player1_name, player1_current_position)

            print("\n" + player2_name + "'s Turn ")
            print("\n Rolling Dice....")
            time.sleep(Time_Gap)
            dice_value = random.choice(DICE_FACE)
            print("\nIt's  ", dice_value)
            print(player2_name + " is Moving.... ")
            player2_current_position = self.snake_ladder(
                player2_name, player2_current_position, dice_value)

            self.check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    S = SnakeAndLadder()
    S.welcome_msg()
    time.sleep(Time_Gap)

    option_chances = 5
    while option_chances >= 0:
        selection = input(
            "\nChoose your player option(Enter 1 or 2 )\n" +
            "1) player2 \n 2) computer\n\n >>> ")

        if option_chances == 0:
            print("your playing chances are reached the limit comeback later ")
            break

        if selection == "1":
            print(S.select_player_start())
            break

        elif selection == "2":
            (S.select_computer_start())
            break

        else:
            print("Please Enter Valid Playing Option ")

        option_chances -= 1
