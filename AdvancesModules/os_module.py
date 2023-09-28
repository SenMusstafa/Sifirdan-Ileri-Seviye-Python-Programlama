import os
import datetime

def main():
    # Getting information about the 'os' module
    # result = dir(os)
    # result = os.name

    # Changing the current directory
    # os.chdir("C:\\")
    # os.chdir("../../../..")

    # Creating a directory
    # os.makedirs("newfile")

    # Getting the current working directory
    # result = os.getcwd()

    # Creating a new directory and renaming it
    # os.makedirs("newdirectory/yeniklasör")
    # os.rename("newdirectory", "yeniklasör")

    # Removing a directory (use with caution)
    # os.rmdir("newdirectory")  # To delete a single directory
    # os.removedirs("yeniklasör/yeniklasör")  # To delete directories and subdirectories

    # Listing files and directories in the current directory
    # result = os.listdir()
    # result = os.listdir("C:\\")

    # Listing Python files in the current directory
    # for dosya in os.listdir():
    #     if dosya.endswith(".py"):
    #         print(dosya)

    # Getting file/directory information using 'os.stat'
    # result = os.stat("_datetime.py")
    # result = datetime.datetime.fromtimestamp(result.st_ctime)  # Creation date
    # result = datetime.datetime.fromtimestamp(result.st_atime)  # Last access date
    # result = datetime.datetime.fromtimestamp(result.st_mtime)  # Modification date

    # Running an external program (e.g., Notepad)
    # os.system("notepad.exe")
    # print(result)

    # Path operations
    result = os.path.abspath("_datetime.py")
    result = os.path.dirname("C:\Etiya Akademi\Python\AdvancesModules")
    result = os.path.dirname(os.path.abspath("_datetime.py"))
    result = os.path.exists("_datetime.py")
    result = os.path.exists("C:\Etiya Akademi\Python\AdvancesModules")
    result = os.path.isdir("C:\Etiya Akademi\Python\AdvancesModules")
    result = os.path.isfile("C:\Etiya Akademi\Python\AdvancesModules")
    result = os.path.join("C:\\", "deneme")
    result = os.path.split("C:\\deneme")
    result = os.path.splitext("_os.py")
    result = result[0]
    print(result)

if __name__ == "__main__":
    main()
