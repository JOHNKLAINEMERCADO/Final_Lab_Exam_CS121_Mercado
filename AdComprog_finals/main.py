from utils.user_manager import UserManager, clear_screen, mainMenu

def hello():
	clear_screen()
	print("┏┓┏┳━┳┓┏┓┏━┓┏┓")
	print("┃┗┛┃┳┫┃┃┃┃┃┃┃┃")
	print("┃┏┓┃┻┫┗┫┗┫┃┃┃┃")
	print("┗┛┗┻━┻━┻━┻━┛┣┫")
	print("╋╋╋╋╋╋╋╋╋╋╋╋┗┛")

def thankYou():
	clear_screen()
	print("╭━━━━┳╮╱╱╱╱╱╱╱╭╮")
	print("┃╭╮╭╮┃┃╱╱╱╱╱╱╱┃┃")
	print("╰╯┃┃╰┫╰━┳━━┳━╮┃┃╭╮")
	print("╱╱┃┃╱┃╭╮┃╭╮┃╭╮┫╰╯╯")
	print("╱╱┃┃╱┃┃┃┃╭╮┃┃┃┃╭╮╮")
	print("╱╱╰╯╱╰╯╰┻╯╰┻╯╰┻╯╰╯")
	print("╭╮╱╭┳━━┳╮╭╮")
	print("┃┃╱┃┃╭╮┃┃┃┃")
	print("┃╰━╯┃╰╯┃╰╯┃")
	print("╰━╮╭┻━━┻━━╯")
	print("╭━╯┃")
	print("╰━━╯")

def main():
	hello()
	UserManager.load_users()
	while True:
		mainMenu()
		choice = input("Enter your choice (1-3): ")
		if choice == '1':
			UserManager.register()
		elif choice == '2':
			UserManager.login()
		elif choice == '3':
			thankYou()
			break
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
		
	