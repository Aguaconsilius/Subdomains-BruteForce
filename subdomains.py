import requests
import sys
import colorama 
from colorama import Fore,Style

print( ' ')    
print(Fore.BLUE + ">")
print("GitHub: https://github.com/Aguaconsilius" + Style.RESET_ALL)
    
print( ' ')
print('⠄⠄⠄⠄⠄⠄⠪⡳⣶⣾⣿⣿⣶⠦⠤⠒⣶⣶⣤⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠉⠪⡻⣿⣀⣶⣶⣶⡤⠬⠙⠛⠃⢤⣭⠖⣢⡀⢄⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢚⢿⣿⣿⣯⠴⢛⣭⣽⣽⣕⡉⢜⣵⠾⢿⣿⣄⠄.')
print('⠄⠄⠄⠄⠄⠄⠄⠄⢀⢔⣦⣾⣿⣿⣟⢿⣿⡟⠄⠘⣿⣿⡞⣿⡀⢠⡽⣿⣷⡀')
print('⠄⠄⠄⠄⠄⣠⣤⣮⣷⣿⣿⣿⣿⣿⡟⡏⣿⠁ ⭕ ⣡⣿⣿⡿⠿ ⭕ ⠅')
print('⠄⠄⠄⣴⣽⣿⣿⠟⠫⠽⣿⣿⡿⢻⣧⠱⣙⠿⢿⠿⢿⢛⣥⡙⠥⠬⠅⣂⣤⡤')
print('⠄⢌⣾⣿⣿⡿⣱⠚⠻⣷⣝⢿⣿⣦⣭⣑⣂⣉⣭⣥⣶⣿⣿⣷⣄⣾⣿⠿⠋⢹')
print('⣜⣿⣿⣿⣿⢱⣿⠄⠸⣦⣭⠓⠪⠭⣛⣛⡿⠿⠿⠿⠿⣟⣛⣛⠭⢝⣢⠄⢧⢸')
print('⢻⣿⣿⣿⣿⢸⣿⠄⠄⠻⠃⠄⢿⣷⡶⠄⣭⣭⡍⠩⣭⣭⡤⠄⠄⠻⣿⠄⠄⢸')
print('⣿⣿⣿⣿⣿⡸⣿⡀⠄⠄⠄⠄⠈⠁⠄⠄⠹⠋⠄⠄⠙⠟⠁⠄⠄⠄⠄⢠⡠⠎')
print('⢡⢿⣿⣿⣿⣧⢻⣧⠄⢠⣶⡀⠄⠄⡄⠄⠄⠄⣀⠄⠄⠄⢀⣄⠄⠄⢠⡿⠝⠄')
print('⠄⠩⢿⣿⣿⣿⣧⠻⣧⡙⢿⣿⠄⢰⣿⡄⠄⢀⣿⡄⠄⢀⣾⣿⡷⠄⡩⠊⠄⠄')
print('⠄⠄⠑⢝⢿⣿⣿⣷⣬⣛⠳⢦⣤⣍⣙⣛⣀⣛⣛⣃⣀⡉⢍⠠⠔⠊⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠑⠫⢿⣿⣿⣿⣿⣷⣶⣬⣭⣭⣭⠭⠭⠙⠂⠉⠄⠄⠄⠄⠄⠄⠄⠄')

print("")
print('-' * 50)
print("This script bruteforces subdomains for a given domain")
print('-' * 50)
list = input(Fore.BLUE + "Enter filename or Path to subdomain list: " + Style.RESET_ALL)
domain = input(Fore.BLUE + "Enter a domain to bruteforce: " + Style.RESET_ALL)

sub_list = open(list).read()
subs = sub_list.splitlines()
print("\nBruteforcing " + domain + ":\n")

for sub in subs:
    url_to_check = f"https://{sub}.{domain}"

    try:
        requests.get(url_to_check)

    except requests.ConnectionError:
        pass

    else:
        print(Fore.YELLOW + '%-12s %s' % (sub," \033[mis a valid domain -> ") + Fore.YELLOW + url_to_check + Style.RESET_ALL)

print("\nBruteforcing " + domain + " is complete\n")