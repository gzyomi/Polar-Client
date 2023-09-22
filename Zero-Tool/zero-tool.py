import sys,os
from colorama import Fore

print(Fore.CYAN+"""

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
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
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Polar
""")

def display_menu():
    print(Fore.BLUE + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    1. Localizza IP                 | 7. Scanner Dominio      
    2. Discord-Nuker                | 8. DDOS
    3. Web Scanner                  | 9. Discord-Token-Grabber
    4. Email-Nuker                  | 10. Keylogger 
    5. Localizza Telefono           | 11. Web-Crawler
    6. Scanner Porte                | 12. Reverse-Shell 
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/ip-lookup.py"' if os.name == 'nt' else 'python Zero-Tool/ip-lookup.py')
    elif command == '2':
        os.system('cmd /k "python Zero-Tool/nuke-bot/main.py"' if os.name == 'nt' else 'python Zero-Tool/nuke-bot/main.py')
    elif command == '3':
        os.system('cmd /k "python Zero-Tool/Subdirectory-scanner/main.py"' if os.name == 'nt' else 'python Zero-Tool/Subdirectory-scanner/main.py')
    elif command == '4':
        os.system('cmd /k "python Zero-Tool/email-bomber.py"' if os.name == 'nt' else 'python Zero-Tool/email-bomber.py')
    elif command == '5':
        os.system('cmd /k "python Zero-Tool/phone-locator.py"' if os.name == 'nt' else 'python Zero-Tool/phone-locator.py')
    elif command == '6':
        os.system('cmd /k "python Zero-Tool/port-scanner.py"' if os.name == 'nt' else 'python Zero-Tool/port-scanner.py"')
    elif command == '7':
        os.system('cmd /k "python Zero-Tool/subdomain/main.py"' if os.name == 'nt' else 'python Zero-Tool/subdomain/main.py')
    elif command == '8':
        os.system('cmd /k "python Zero-Tool/ddos.py"' if os.name == 'nt' else 'python Zero-Tool/ddos.py')
    elif command == '9':
        os.system('cmd /k "python Zero-Tool/discord-token-grabber.py"' if os.name == 'nt' else 'python Zero-Tool/discord-token-grabber.py')
    elif command == '10':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Keylogger.py"')
    elif command == '11':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Web-Crawler.py"')
    elif command == '12':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Reverse-Shell.py"')
    else:
        print(Fore.RED + 'Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
