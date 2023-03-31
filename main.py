# A simple Script which updates my SD Card with recent files
# Works suprisingly well

# 1 Day Build, Modified afterwards

import sys
import os
import shutil
from colorama import Fore
from rich.progress import track
import time



# Below: GLobal variables which can be accesed by funtions.
global status
status = "Writing and Updating SD Card..."

global check
check = 'Finding SD Card...'

# Directory is specified here so it can be reused
global get_dir
get_dir = 'Desktop/Projects'

# The SD Card directory, it appears here when inserted 
global SD_Card_dir
SD_Card_dir = '/Volumes/SD_Card/Backup'

# sys.exit() was not working, so i put it ina function and called it, it works flawlessy now

def rerun():
    print(f'{Fore.RED}Running again...')
    os.system('python3 sdcard.py')
    sys.exit()

def quit():
    sys.exit()

# The function below is important as it it will try to create a folder in the sd card
# If it fails, it means that the sd card directory is not present, hence the sd card is not inserted
def perform_check():
    for i in track(range(2), description=check):
        time.sleep(0.5)
    print('-')

    try:
        os.mkdir('/Volumes/SD_Card/test')
        os.rmdir('/Volumes/SD_Card/test')
    except:
        print(f'{Fore.RED}SD Card not found, QUITTING...')
        print(f'Make sure to insert the card as by the SDXC port on the computer ')
        ask_for_rerun = input('Rerun the program? y/n')
        if 'y' in ask_for_rerun:
            rerun()
        elif 'n' in ask_for_rerun:
            quit()
        else:
            rerun()


# Progress bar just for fun
def progressBar():
    for i in track(range(5), description=status):
        time.sleep(0.5)
    print('-')

# Removing the file before adding it again
def format():
    try:
        shutil.rmtree('/Volumes/SD_Card/Backup')
        time.sleep(1)
    except:
        print(f"{Fore.RED}SD Card was removed")
        sys.exit()

def format2():
    try:
        shutil.rmtree('/Volumes/SD_Card/DesktopFiles')
        time.sleep(1)
    except:
        print(f"{Fore.RED}SD Card was removed")
        sys.exit()
    

# The read and write function which is responsible to update the SD Card
def ReadAndWrite():
    path = get_dir
    target_path = SD_Card_dir
    shutil.copytree(path, target_path)

def ReadAndWrite2():
    desktop_path = 'Desktop'
    target_folder = '/Volumes/SD_Card/DesktopFiles'
    shutil.copytree(desktop_path, target_folder)

# Main function which executes all other functions
def ask():
    ask_input0 = input('Copy every directory on /Desktop folder? y/n: ')
    if 'y' in ask_input0:
        format2()
        progressBar()
        print('Please be patient...')
        print('3 - 5 minutes left')
        ReadAndWrite2()
    elif 'y' not in ask_input0:
        pass
    elif 'n' in ask_input0:
        sys.exit()    
    ask_input1 = input('Copy Projects Folder? y/n: ')
    if 'y' in ask_input1:
        format()
        progressBar()
        ReadAndWrite()
    
    
    elif 'y' not in ask_input1:
        pass
    elif 'n' in ask_input1:
        sys.exit()    

        
if __name__ == '__main__':
    perform_check()
    ask()
