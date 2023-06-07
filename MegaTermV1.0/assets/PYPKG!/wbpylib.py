import os
import time
import sys
import subprocess
import platform

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
