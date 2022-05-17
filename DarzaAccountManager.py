import os
import shutil

from click import option

def QueryMain():
    CheckFolder()
    PrintTitle()
    option = QueryOption(["Change Account", "Launch Darza's Dominion", "Exit"])
    if option == 0:
        ChangeAccount()
    elif option == 2:
        return
    elif option == 3:
        exit()
    
def CheckFolder():
    try:
        os.mkdir('Accounts')
    except FileExistsError:
        return
    
def PrintTitle():
    os.system('cls')
    print(''' ██████╗██████╗  █████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║     ██║  ██║███████║██████╔╝
██║     ██║  ██║██╔══██║██╔══██╗
╚██████╗██████╔╝██║  ██║██║  ██║
 ╚═════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
 ''')
    
def QueryOption(options):
    PrintTitle()
    for i, option in enumerate(options):
        print(f'[{i}] {option}')
        
    print()
    
    option = input('Select an option: ')
    return int(option)
    
def ChangeAccount():
    accounts = os.listdir('Accounts')
    option = QueryOption(accounts)
    CopyAccount(accounts[option])

def CopyAccount(account):
    path = f'C:/Users/{os.getlogin()}/Appdata/Local/RippleStudio/Darza/settings.dat'
    
    shutil.copy(f'Accounts/{account}', path)
    
if __name__ == "__main__":
    QueryMain()