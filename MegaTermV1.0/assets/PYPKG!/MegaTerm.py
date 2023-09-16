import os
import time
import sys
import subprocess
import platform
from tabulate import tabulate
import readline
import curses

def display_commands():
    max_command_length = max(len(command[0]) for command in commands)

    for command in commands:
        command_name = command[0]
        description = command[1]
        padding = " " * (max_command_length - len(command_name))
        print(f"{command_name}:{padding} {description}")

def install_tabulate():
    subprocess.run(["pip", "install", "tabulate"], stdout=subprocess.DEVNULL)

def colorize_text(text, color):
    color_codes = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    colored_text = color_codes[color.lower()] + text + color_codes['reset']
    return colored_text

def print_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

def print_slowly(text, delay=0.15):
    for char in text:
        print(char,end='', flush=True)
        time.sleep(delay)
def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Listing files in directory: {directory}")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Directory not found.")

def create_file(file_name):
    try:
        with open(file_name, 'w'):
            print(f"File '{file_name}' created.")
    except IOError:
        print("Unable to create file.")


def change_directory_relative(relative_path):
    try:
        current_directory = os.getcwd()
        new_directory = os.path.abspath(os.path.join(current_directory, relative_path))
        os.chdir(new_directory)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found.")

# for read a file on black window
def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    stdscr.clear()
    stdscr.addstr(content)
    stdscr.addstr(curses.LINES - 1, 0, "Enter 'q' to quit.")
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

aliases = {
    "ls": "list_files('.')",
    "cd": "change_directory_command",        # Alias is not working for now
    "touch": "create_empty_file",
    "mkdir": "create_directory",
    "rmdir": "remove_directory",
    "rmfile": "remove_file",
}

commands = [
    ["htuse", "How To Use The 'Move The pen' game!"],
    ["clear", "To Clear The Terminal Console"],
    ["cmd or --help", "To Display All Commands !"],
    ["src", "To Display All Code src"],
    ["--version", "Get The Programme Version"],
    ["about", "About The 'MYP' Programme"],
    ["about -dev", "About The Devloper 'Wassim_Bolles'"],
    ["more", "For get more important! commands"],
    ["exit", "For Exiting the terminal"]
]

more_commands = [
    ["ls", "Display list of files and directories"],
    ["cat", "Display the files content"],
    ["cd", "Change directory"],
    ["touch", "For make a file"],
    ["mkdir", "Make directory"],
    ["rmdir", "Remove directory"],
    ["rmdfile", "Remove file"]
]

all_commands = [
    ["about", "About The 'MTP' Game!"],
    ["about -dev", "About The Devloper 'Wassim_Bolles'"],
    ["cat", "Display the files content"],
    ["cd", "Change directory"],
    ["clear", "To Clear The Terminal Console"],
    ["cmd or --help", "To Display All Commands !"],
    ["exit", "For Exiting the terminal..."],
    ["htuse", "How To Use The 'Move The pen' game.c"],
    ["ls", "Display list of files and directories"],
    ["more", "For get more important commands"],
    ["mkdir", "Make directory"],
    ["src", "To Display All Code src"],
    ["rmdir", "Remove directory"],
    ["rmfile", "Remove file"],
    ["touch", "For make a file"],
    ["--version", "Get The Programme Version"],
]
############################################################ check user ##############################################################
usr = "user"
s = "~"
Helpmsg = "--help"
os.system('cls' if os.name == 'nt' else 'clear');
cmd = input(f"bot : Enter {colorize_text(Helpmsg, 'yellow')} To Get Help\n\n{colorize_text(usr, 'green')}:{colorize_text(s, 'magenta')}$ --");
err00 = "! Command Not Found !"

if cmd != "help":
    print(f"\n\t({cmd})\n\t ^ {colorize_text(err00, 'red')}\n\t\tAbort.\n")
    sys.exit()    

user = input("\033[33mEnter a username : \033[0m")
os.system('cls' if os.name == 'nt' else 'clear');
print_slowly("\033[34mWelecome to MegaTerm V1.0\033[0m\n", 0.04)
print_slowly(f"\nHello ! {colorize_text(user, 'yellow')}\n", 0.05)

############################################################### tabulate #############################################################
msg01 = "These are some commands that you need to use"
print_slowly(f"{colorize_text(msg01, 'blue')}\n", 0.04)
install_tabulate()
table = tabulate(commands, headers=["Command", "Description"], tablefmt="fancy_grid")
table2 = tabulate(more_commands, headers=["Command", "Description"], tablefmt="fancy_grid")
all_table = tabulate(all_commands, headers=["Command", "Description"], tablefmt="fancy_grid")
print(table)
msg00 = "To get more important! commands enter : "
msg01 = "remember to diplay all commands enter : "
print_slowly(f"{colorize_text(msg00, 'blue')}more or cmd\n\n", 0.04);
############################################################### Terminal #############################################################

def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            print("\033[43m" + file + "\033[0m")
        else:
            print("\033[34m" + file + "\033[0m")

def change_directory_command(command):
    command_parts = command.split()
    if len(command_parts) == 2 and command_parts[0] == "cd":
        directory = command_parts[1]
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print("\033[37mDirectory not found.")
    else:
        print("Invalid command.")
import getpass

def print_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"\033[37mFile '{filename}' not found.")
        print_slowly("\033[31mif the file not found !\nThis means that you are changing directory return to Move_The_Pen please.\n", 0.03)

while True:
    sysuser = getpass.getuser()
    cwd = os.getcwd()
    current_folder = os.path.basename(cwd)
    prompt = f"{colorize_text(user, 'yellow')}:/{colorize_text(sysuser, 'cyan')}/{colorize_text(current_folder, 'cyan')}$ "

    bash = input(prompt)
    if bash == "htuse":
        print_file_content("info/htuse")
        print_slowly("\033[34mtry now by enter the command :\033[0m\n./play up[3] down[5] up[2] right[6] up[2] down[5]\n\033[31mif the command does not work please use your terminal or return to Move_The_Pen\n", 0.03)
    elif bash.startswith("cat "):
        filename = bash[4:]
        print_file_content(filename)
    elif bash.startswith("cd "):
        change_directory_command(bash)
    elif bash.startswith("touch "):
        filename = bash[6:]
        try:
            with open(filename, 'w') as file:
                pass
            #print(f"\033[37mFile '{filename}' created.")
        except IOError:
            print(f"\033[37mFailed to create file '{filename}'.")
    elif bash.startswith("mkdir "):
        directory = bash[6:]
        try:
            os.mkdir(directory)
            #print(f"\033[37mDirectory '{directory}' created.")
        except FileExistsError:
            print(f"\033[37mDirectory '{directory}' already exists.")
    elif bash.startswith("rmdir "):
        directory = bash[6:]
        try:
            os.rmdir(directory)
            #print(f"\033[37mDirectory '{directory}' removed.")
        except FileNotFoundError:
            print(f"\033[37mDirectory '{directory}' not found.")
        except OSError:
            print(f"\033[37mFailed to remove directory '{directory}'.")
    elif bash.startswith("./"):
        file_path = bash[2:]
        if os.path.exists(file_path) and os.path.isfile(file_path):
            try:
                subprocess.run(["./" + file_path], shell=True)
            except Exception as e:
                print(f"An error occurred while executing {file_path}: {str(e)}")
            else:
                print(f"File '{file_path}' not found or is not a regular file.")
    elif bash == "cmd" or bash == "--help" or bash == "help":
        print(all_table)
    elif bash == "ls":
        list_files(".")
    elif bash == "src":
        display_file_content('info/src')
    elif bash == "--version":
        display_file_content('info/version')
    elif bash == "about":
        display_file_content('info/version')
    elif bash == "about -dev":
        display_file_content('info/about-developer')
    elif bash == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif bash == "exit":
        print_slowly("\033[34mgoodbye...\033[0m\n", 0.03)
        break
    elif bash == "more":
        print(table2)
        print_slowly(f"{colorize_text(msg01, 'blue')}cmd or --help\n\n", 0.04);
    elif bash.startswith("./"):
        file_path = bash[2:]
        try:
            subprocess.run(["./" + file_path], shell=True)
        except FileNotFoundError:
            print("\033[37mFile not found.\033[0m")
    else:
        print(f"\t\033[35m'{bash}'\n\t ^\033[35m\033[31mInvalid command !\033[0m")
input("\033[34mPress any key")
