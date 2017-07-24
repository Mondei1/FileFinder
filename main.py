import sys

try:
    from lib.scan import scan
    from lib.var import *
except ImportError:
    print("\033[1mPlease run this script with python3 or higher! (Tested under python3.5 under Linux)\033[0m")
    sys.exit(0)

isMD5 = False
isDirScan = False
isLowerCase = True
isReadFiles = False

# Args check
if sys.argv.__contains__("-help") or sys.argv.__contains__("?"):
    print("Here a an list of arguments:")
    print("Syntax: python3.5 main.py [ARGUMENT]\n")
    print("Arguments:")
    print(" -help OR ?  --> to see this")
    print(" -md5        --> To start the file scan based on one MD5 hash.")
    print(" -dl         --> The program will not lower case your file name.")
    print(" -dir        --> Show's you folders and files with the filename.")
    print(" -r          --> This will read and scan the content of every file")
    sys.exit(0)

if sys.argv.__contains__("-md5"):
    if sys.argv.__contains__("-dl") or sys.argv.__contains__("-dir") or sys.argv.__contains__("-r"):
        print(RED + BOLD + "If you are enable the MD5 scan, you can't enable other scan's!" + ENDC)
        sys.exit(0)

print("")
print(OKBLUE + " /$$$$$$$$ /$$ /$$             " + BOLD + "    /$$$$$$$$ /$$                 /$$                    " + ENDC)
print(OKBLUE + "| $$_____/|__/| $$             " + BOLD + "   | $$_____/|__/                | $$                    " + ENDC)
print(OKBLUE + "| $$       /$$| $$  /$$$$$$    " + BOLD + "   | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ " + ENDC)
print(OKBLUE + "| $$$$$   | $$| $$ /$$__  $$   " + BOLD + "   | $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$" + ENDC)
print(OKBLUE + "| $$__/   | $$| $$| $$$$$$$$   " + BOLD + "   | $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/" + ENDC)
print(OKBLUE + "| $$      | $$| $$| $$_____/   " + BOLD + "   | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      " + ENDC)
print(OKBLUE + "| $$      | $$| $$|  $$$$$$$   " + BOLD + "   | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      " + ENDC)
print(OKBLUE + "|__/      |__/|__/ \_______/   " + BOLD + "   |__/      |__/|__/  |__/ \_______/ \_______/|__/      " + ENDC)
print("                                                                                        ")
print(BOLD + "By Mondei1")
print("Version is DEV_1.1\n" + ENDC)

# Set booleans
if sys.argv.__contains__("-md5"):
    filename = input("Enter MD5 of file your looking for: ")
    if len(filename) < 32 or len(filename) > 32:
        print(RED + "This isn't an MD5 hash! An MD5 hash has a length of 32 characters!" + ENDC)
        sys.exit(0)
    isMD5 = True
elif sys.argv.__contains__("-dir"):
    isDirScan = True
    filename = input("Please enter your folder name: ")
elif sys.argv.__contains__("-r"):
    isReadFiles = True
    filename = input("Enter ONE word that you search: ")
else:
    filename = input("Please enter file name: ")
if sys.argv.__contains__("-dl"):
    isLowerCase = False

print("")
path = input("Please enter path: ")
try:
    scan(filename, path, MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles)
except KeyboardInterrupt:
    print(BOLD + RED + "Exit" + ENDC)