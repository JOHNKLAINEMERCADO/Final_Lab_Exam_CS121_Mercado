import random
import os
import time
import datetime

class DiceGame:
    def __init__(self, user="qwer"):
        self.user = user
        self.scores = self.load_scores()
        self.current_points = 0
        self.wins = 0

    def load_scores(self):
        scores = []
        if os.path.exists("rankings.txt"):
            with open("rankings.txt", "r") as file:
                for line in file:
                    user, points, wins, tym = line.strip().split(",")
                    points = int(points)
                    wins = int(wins)
                    # tym = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    scores.append({"user": user, "points": points, "wins": wins, "time": tym})
        return scores

    def save_scores(self):
        with open("rankings.txt", "w") as file:
            for score in self.scores:
                file.write(f'{score["user"]},{score["points"]},{score["wins"]},{score["time"]}\n')

    def roll_dice(self):
        return random.randint(1, 6)

    def display_dice_animation(self, player_roll, cpu_roll):
        dice_faces = {
            1: (
                "┌─────┐\n"
                "│     │\n"
                "│  ●  │\n"
                "│     │\n"
                "└─────┘\n"
            ),
            2: (
                "┌─────┐\n"
                "│ ●   │\n"
                "│     │\n"
                "│   ● │\n"
                "└─────┘\n"
            ),
            3: (
                "┌─────┐\n"
                "│ ●   │\n"
                "│  ●  │\n"
                "│   ● │\n"
                "└─────┘\n"
            ),
            4: (
                "┌─────┐\n"
                "│ ● ● │\n"
                "│     │\n"
                "│ ● ● │\n"
                "└─────┘\n"
            ),
            5: (
                "┌─────┐\n"
                "│ ● ● │\n"
                "│  ●  │\n"
                "│ ● ● │\n"
                "└─────┘\n"
            ),
            6: (
                "┌─────┐\n"
                "│ ● ● │\n"
                "│ ● ● │\n"
                "│ ● ● │\n"
                "└─────┘\n"
            ),
        }
        for _ in range(5):
            print("Rolling the dice...", end="\r")
            time.sleep(0.2)
        
        player_dice = dice_faces[player_roll].split('\n')
        cpu_dice = dice_faces[cpu_roll].split('\n')
        for i in range(len(player_dice)-1):
            print(f"    {player_dice[i]}     |     {cpu_dice[i]}")

    def play_round(self):
        player_roll = self.roll_dice()
        cpu_roll = self.roll_dice()
        
        print("Player's roll <-|-> CPU's roll:")
        self.display_dice_animation(player_roll, cpu_roll)

        if player_roll > cpu_roll:
          print("    WINNER      |     LOSSER      ")
          print(f"You win this round! {self.user}")
          return "win"
        elif player_roll < cpu_roll:
          print("    LOSSER      |     WINNER      ")
          print("CPU win this round!")
          return "lose"
        else:
          print("               TIE                  ")
          print("It's a tie!")
          return "tie"
        time.sleep(1)

    def play_stage(self):
        player_wins = 0
        cpu_wins = 0
        while player_wins < 2 and cpu_wins < 2:
            result = self.play_round()
            print()  # Move to a new line   
            if result == "win":
                player_wins += 1
                self.current_points += 1
            elif result == "lose":
                cpu_wins += 1
            print(f"Current score - Player: {player_wins}, CPU: {cpu_wins}")

        if player_wins == 2:
            self.current_points += 3
            self.wins += 1
            print(f"You won the stage {self.user}")
            return True
        else:
            print(f"You lost the stage {self.user}")
            return False

    def play_game(self):
        print(f"Starting game as {self.user}")
        self.current_points = 0
        self.wins = 0
        # stages_required_to_win = 3
        while True: #self.wins < stages_required_to_win:
            won_stage = self.play_stage()
            if not won_stage:
                if self.wins == 0:
                    print("Game over. You didn’t win enough stages.")
                    return
                self.record_score()
                print("Game over.")
                return
            print(f"Total points: {self.current_points}, Stages won: {self.wins}")
            while True:
                choice = input("Enter 1 to continue or 0 to stop: ")
                if choice == '1':
                    break
                elif choice == '0':
                    self.record_score()
                    return
                else:
                    print("Invalid choice. Please enter 1 or 0.")

        print("Congratulations! You won the game!")
        self.record_score()

    def record_score(self):
        if self.wins > 0:
            tym = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.scores.append({
                "user": self.user,
                "points": self.current_points,
                "wins": self.wins,
                "time": tym
            })
            self.scores = sorted(self.scores, key=lambda x: x["points"], reverse=True)[:10]
            self.save_scores()

    def display_top_scores(self):
        if not self.scores:
            print("No scores to display yet.")
        else:
            print("Top-10 highest scores:")
            for i, score in enumerate(self.scores, 1):
                print(f"{i}. {score['time']} [{score['user']}]: Points - {score['points']}, Wins - {score['wins']}")
