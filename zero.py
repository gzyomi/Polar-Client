import sys,os
from colorama import Fore

print(Fore.RED+"""
――――――――――――――――――――――――――――――――――――――――――
        _                      _      
  _ __ | |__   ___   ___ _ __ (_)_  __
 | '_ \| '_ \ / _ \ / _ \ '_ \| \ \/ /
 | |_) | | | | (_) |  __/ | | | |>  < 
 | .__/|_| |_|\___/ \___|_| |_|_/_/\_\
 |_|                                  
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Polar
""")

def display_menu():
    print(Fore.MAGENTA + """
    1: Phoenix-Tool (Hack Tools)      | 2: Phoenix-Paid-Tools
    3: Info (informazioni)
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/zero-tool.py"' if os.name == 'nt' else 'python Zero-Tool/zero-tool.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')
    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
