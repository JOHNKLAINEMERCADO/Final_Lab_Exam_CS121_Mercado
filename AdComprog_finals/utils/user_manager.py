import os
import platform
from utils.input import get_password, get_input
from utils.dice_game import DiceGame
import sys
import termios
import tty

class UserManager:
	user_accounts = {}
	data_folder = "accounts"
	file_name = "users.txt"
	file_path = os.path.join(data_folder, file_name)
	username = ""
		
	def load_users():
		if not os.path.exists(UserManager.file_path):
			return
        
		with open(UserManager.file_path, 'r') as file:
			for line in file:
				line = line.strip()
				if not line:
					continue  # Skip empty lines
				try:
					username, password = line.split(',')
					UserManager.user_accounts[username] = password
				except ValueError:
					print(f"Error reading line: {line}")

			# for line in file:
			# 	username, password = line.strip().split(',')
			# 	UserManager.user_accounts[username] = password
                
		# print(f"Loaded users: {UserManager.user_accounts}")

	def save_user(username, password):
		if not os.path.exists(UserManager.data_folder):
			os.makedirs(UserManager.data_folder)        
        
		with open(UserManager.file_path, 'a') as file:
			file.write(f'{username},{password}\n')
		print(f"User {username} registered successfully.")
						
	def register():
		username = get_input("\nEnter username (at least 4 characters), or leave blank to cancel: ", 4, "Username must be at least 4 characters long.")
		if username is not None:
			if UserManager.find_user(username):
				print(f"Username already exists.")
				return
			password = get_password("\nEnter password (at least 8 characters), or leave blank to cancel: ", 8)
			if password is not None:
				UserManager.save_user(username, password)
			else:
				print("Registration cancelled.")
		else:
			print("Registration cancelled.")

	def find_user(username):
		return UserManager.user_accounts.get(username, None)

	def login():
		print("Login")
		UserManager.load_users()
		UserManager.username = get_input("Enter username, or leave blank to cancel: ")
		if UserManager.username is None:
			print("Login cancelled.")
			return        
		 
		password = get_password("\nEnter password, or leave blank to cancel: ")
		if password is None:
			print("Login cancelled.")
			return
        
		saved_password = UserManager.find_user(UserManager.username)
		if saved_password is None:
			print("Username not found.")
		elif saved_password == password:
			gameMenu()
			# print(f"User {UserManager.username} logged in successfully.")
		else:
			print("Incorrect password.")


def gameMenu():		
    clear_screen()
    # print(" __      __       .__                               ")
    # print("/  \    /  \ ____ |  |   ____  ____   _____   ____  ")
    # print("\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ ")
    # print(" \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ ")
    # print("  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >")
    # print("       \/       \/          \/            \/     \/ ")
    game = DiceGame(UserManager.username)
    while True:
        print("\nMenu:")
        print("1. Start a new game")
        print("2. View top-10 highest scores")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            game.play_game()
        elif choice == '2':
            game.display_top_scores()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def mainMenu():		
	print("===========================")
	print(" Welcome to Dice Roll Game")
	print("===========================")
	print("   [1] Register")
	print("   [2] Login")
	print("   [3] Exit")
	print("===========================")

def pause():
		if platform.system() == "Windows":
			os.system("pause")
		else:
			print("Press any key to continue...", end="", flush=True)
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
			try:
				tty.setraw(fd)
				sys.stdin.read(1)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			print()  # Move to a new line

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
