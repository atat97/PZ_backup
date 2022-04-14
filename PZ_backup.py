#Project Zomboid Backup Saves

#TODO:
#1. Remove backup from the "old" folder
#2. Move the recent backup from "new" folder to "old" folder
#3. Copy the save to the "new" backup folder

import glob
import os
import shutil

#Paths TODO: Get user directory automatically; Refactor; Breaks when the folders are empty; 
latest_save_path = max(glob.glob("C:\\Users\\A\\Zomboid\\Saves\\Sandbox\\*"), key=os.path.getctime) 
new_backup_save = max(glob.glob("C:\\Users\\A\\Zomboid\\Saves\\Backup\\new\\*"), key=os.path.getctime)
old_backup_save = max(glob.glob("C:\\Users\\A\\Zomboid\\Saves\\Backup\\old\\*"), key=os.path.getctime)

new_backup_path = "C:\\Users\\A\\Zomboid\\Saves\\Backup\\new"
old_backup_path = "C:\\Users\\A\\Zomboid\\Saves\\Backup\\old"

def backup_PZ():
    #1
    print("Removing old backup...")
    shutil.rmtree(old_backup_save)
    print("Done!")
    #2
    print("Archiving the current backup...")
    shutil.move(new_backup_save, old_backup_path)
    print("Done!")
    #3
    print("Backing up the save...")
    shutil.copytree(latest_save_path, new_backup_path) #TODO: new_backup_path does not exist after it is moved!!!
    print("Done!")

if __name__ == "__main__":
    backup_PZ()
