import sys
import os
import termios

def clear_input_buffer():
    if os.name == 'nt':
        # For Windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        # For Unix-based systems
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        
def get_password(prompt="Enter your password: ", min_length=8):
    while True:
        clear_input_buffer()
        input_text = ""
        if os.name == 'nt':  # Check if the OS is Windows
            import msvcrt
            print(prompt, end='', flush=True)
            while True:
                ch = msvcrt.getch()
                if ch in {b'\r', b'\n'}:  # Enter key
                    break
                elif ch == b'\x08':  # Backspace key
                    if len(input_text) > 0:
                        input_text = input_text[:-1]
                        sys.stdout.write('\b \b')
                else:
                    input_text += ch.decode('utf-8')
                    sys.stdout.write('*')
                sys.stdout.flush()
            print()  # Move to the next line
        else:  # Assume the OS is Unix-based
            import tty
            import termios
            print(prompt, end='', flush=True)
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                while True:
                    ch = sys.stdin.read(1)
                    if ch in {'\n', '\r'}:  # Enter key
                        break
                    elif ch == '\x7f':  # Backspace key
                        if len(input_text) > 0:
                            input_text = input_text[:-1]
                            sys.stdout.write('\b \b')
                    else:
                        input_text += ch
                        sys.stdout.write('*')
                    sys.stdout.flush()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            print()  # Move to the next line
        
        if input_text == "":
            print("Input cancelled.")
            return None
        
        if len(input_text) >= min_length :
            return input_text
        else:
            print(f"Password must be at least {min_length} characters long. Please try again.")

def get_input(label="Enter input: ", min_length=4, error_message=None):
    if error_message is None:
        error_message = f"Input must be at least {min_length} characters long. Please try again."

    while True:
        clear_input_buffer()
        input_text = input(label)
        
        if input_text == "":
            print("Input cancelled.")
            return None
        
        if len(input_text) >= min_length:
            return input_text
        else:
            print(error_message)						