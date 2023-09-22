import sys,os
from colorama import Fore

print(Fore.CYAN+"""
――――――――――――――――――――――――――――――――――――――――――
                                                  
                        88                        
                        88                        
                        88                        
8b,dPPYba,   ,adPPYba,  88 ,adPPYYba, 8b,dPPYba,  
88P'    "8a a8"     "8a 88 ""     `Y8 88P'   "Y8  
88       d8 8b       d8 88 ,adPPPPP88 88          
88b,   ,a8" "8a,   ,a8" 88 88,    ,88 88          
88`YbbdP"'   `"YbbdP"'  88 `"8bbdP"Y8 88          
88                                                
88                                                
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Polar
""")

def display_menu():
    print(Fore.BLUE + """
    1: Polar-Tool (Hack Tools)      | 2: Polar-Paid-Tools
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
