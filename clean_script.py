#!/usr/bin/env python3
import os, shutil

FOLDER_TO_DELETE = 'C:\WinCache'

def remove_file():
    for filename in os.listdir(FOLDER_TO_DELETE):
        file_path = os.path.join(FOLDER_TO_DELETE, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def main():
    remove_file()
    os.system("shutdown /r")