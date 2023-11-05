from BuyGamepass import buy_gamepass
from GetAccountInfo import get_roblox_data
import os

print('\033[31mRobux Stealer CLI   \033[0m')
print('\033[34m [+]Buy Gamepass (1) \033[0m')
print('\033[34m [+]Get Account Info (2) \033[0m')

choice=input('\033[31m> \033[0m')

options=['1','2']
while True:
    if choice in options:
        choice=choice
        break
    else:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('\033[31mRobux Stealer CLI   \033[0m')
        print('\033[34m [+]Buy Gamepass (1) \033[0m')
        print('\033[34m [+]Get Account Info (2) \033[0m')
        choice=input('\033[31m> \033[0m')

if choice=='1':
    print('\033[31mBuy Gamepass Selected\033[0m')
    
    print('\033[34m Gamepass URL: \033[0m')
    url=input('\033[31m> \033[0m')
    
    print('\033[34m ROBLOSECURITY: \033[0m')
    cookie=input('\033[31m> \033[0m')
    
    buy_gamepass(url,cookie)
elif choice=='2':
    print('\033[31mGet Account info Selected\033[0m')  
    
    print('\033[34m ROBLOSECURITY: \033[0m')
    cookie=input('\033[31m> \033[0m')
    print('')
    get_roblox_data(cookie)
    
