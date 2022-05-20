from cgi import print_arguments
import os
import shutil
import json
import easygui

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
    option = QueryOption(["Change Account", "Check All Function", "Save Account", "Launch Darza's Dominion", "Exit"])
    if option == 0:
        ChangeAccount()
    elif option == 1:
        SaveAccount()
    elif option == 2:
        SaveAccount()
    elif option == 3:
        LaunchGame()
    elif option == 4:
        exit()
      
  


def AddDirectory():
    PrintTitle()
    
    
    print("[0] Select Darza's Dominion.exe")
    path = easygui.fileopenbox("Select Darza's Dominion.exe")
    if path == None:
        QueryMain()
    name = input('[0] Input name of directory ')
    
    config['gameDirectories'].update({name: path})
    SaveConfig()
    QueryMain()

def RunProcess(index):
    path = config['gameDirectories'][index]
    os.startfile(path)

def LaunchGame():
    if bool(config['gameDirectories']) == False:
        AddDirectory()
    
    options = config['gameDirectories'].keys()
    options_list = list(options)
    options_list.append('Add a new game directory')
    
    option = QueryOption(options_list)
    if option == options_list[-1]:
        AddDirectory()
        
    RunProcess(options_list[option])
    QueryMain()
    
    
def CheckAll():
    print("test")
    
def CheckFolder():
    try:
        os.mkdir('Accounts')
    except FileExistsError:
        return
    
    
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
    ReplaceFile(accounts[option])
    QueryMain()

def SaveAccount():
    PrintTitle()
    
    path = f'C:/Users/{os.getlogin()}/Appdata/Local/RippleStudio/Darza/settings.dat'
    name = input('What is the name of the account? ')
    
    shutil.copy(path, f'Accounts/{name}.dat')
    QueryMain()

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
        
    QueryMain()