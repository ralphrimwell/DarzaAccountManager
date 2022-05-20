from cgi import print_arguments
import os
import shutil
import json
import easygui
import subprocess

#this is the default value, will be overwritten if config.json exists
config = {
  "gameDirectories": {
  }
}


def PrintTitle():
    os.system('cls')
    print(''' ██████╗██████╗  █████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║     ██║  ██║███████║██████╔╝
██║     ██║  ██║██╔══██║██╔══██╗
╚██████╗██████╔╝██║  ██║██║  ██║
 ╚═════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
 ''')
    
    
def QueryMain():
    CheckFolder()
    PrintTitle()
    option = QueryOption('Main menu', ["Launch Darza's Dominion", "Change Account", "Save Account", "Autoloot Accounts", "Exit"])
    if option == 0:
        LaunchGame()
    elif option == 1:
        ChangeAccount()
    elif option == 2:
        SaveAccount()
    elif option == 3:
        CheckAll()
    elif option == 4:
        exit()
      
  


def AddDirectory():
    PrintTitle()
    
    
    print("[0] Select Darza's Dominion.exe")
    path = easygui.fileopenbox("Select Darza's Dominion.exe")
    if path == None:
        return
    name = input('[0] Input name of directory ')
    
    config['gameDirectories'].update({name: path})
    SaveConfig()

def RunProcess(path):
    subprocess.call(path)


def LaunchGame():
    path = QueryGamePath()
    RunProcess(path)
    QueryMain()
    
def QueryGamePath():
    if not bool(config['gameDirectories']):
        AddDirectory()
    
    options = config['gameDirectories'].keys()
    options_list = list(options)
    options_list.append('Add a new game directory')
    
    option = QueryOption('Pick game directory', options_list)
    if option == options_list[-1]:
        AddDirectory()
        
    path = config['gameDirectories'][options_list[option]] #can only use string as key not index dunno
    return path


def CheckAll():
    path = QueryGamePath()
    PrintTitle()
    print(f"[Account Looter - THIS DOESN'T WORK WITH STEAM]\n")

    accounts = os.listdir('Accounts')
    for i, account in enumerate(accounts):
        option = input(f'[{i}] Running game with account: {account} [Y/N] ')
        if option == 'Y' or option == 'y':
            print(option)
            ReplaceFile(account)
            RunProcess(path)
            

    
def CheckFolder():
    try:
        os.mkdir('Accounts')
    except FileExistsError:
        return
    
    
def QueryOption(name, options):
    PrintTitle()
    print(f'[{name}]\n')
    for i, option in enumerate(options):
        print(f'[{i}] {option}')
        
    print()
    
    option = input('Select an option: ')
    return int(option)
    
def ChangeAccount():
    accounts = os.listdir('Accounts')
    option = QueryOption('Change account', accounts)
    ReplaceFile(accounts[option])

def SaveAccount():
    PrintTitle()
    
    path = f'C:/Users/{os.getlogin()}/Appdata/Local/RippleStudio/Darza/settings.dat'
    name = input('What is the name of the account? ')
    
    shutil.copy(path, f'Accounts/{name}.dat')

def ReplaceFile(account):
    path = f'C:/Users/{os.getlogin()}/Appdata/Local/RippleStudio/Darza/settings.dat'
    
    shutil.copy(f'Accounts/{account}', path)

def SaveConfig():
    with open("config.json","w") as f:
        f.write(json.dumps(config, indent=4))
    
if __name__ == "__main__":
    try:
        config = json.load(open('config.json'))
    except FileNotFoundError:
        SaveConfig()
        
    while(True): #instead of calling querymain() to go back to menu
        QueryMain()
