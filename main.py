"""
This program search for files or folders, based on the filename or MD5 hash
    Copyright (C) 2017  Mondei1 - Nicolas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import glob
import readline
import sys

try:
    from lib.scan import scan
    from lib.var import *
    from lib.lang.lang import *
except ImportError:
    print("\033[1mPlease run this script with python3 or higher! (Tested under python3.5 under Linux)\033[0m")
    sys.exit(0)

# Auto-Complete
def complete(text, state):
    return (glob.glob(text + '*' + "/") + [None])[state]

isMD5 = False
isDirScan = False
isLowerCase = True
isReadFiles = False
isSha1 = False
isSHA256 = False
# Args check
if sys.argv.__contains__("-help") or sys.argv.__contains__("?"):
    print("Here a an list of arguments:")
    print("Syntax: python3.5 main.py [ARGUMENT]\n")
    print("Arguments:")
    print(" -help OR ?  --> to see this")
    print(" -md5        --> To start the file scan based on one MD5 hash.")
    print(" -sha1       --> To start the file scan based on one sha1 hash.")
    print(" -sha256     --> To start the file scan based on one sha256 hash.")
    print(" -l          --> The program will not lower case your file name.")
    print(" -dir        --> Show's you folders and files with the filename.")
    print(" -r          --> This will read and scan the content of every file")
    sys.exit(0)

if sys.argv.__contains__("-md5"):
    if sys.argv.__contains__("-l") or sys.argv.__contains__("-dir") or sys.argv.__contains__("-r"):
        print(RED + BOLD + "You can't enable other scan's! Only one!" + ENDC)
        sys.exit(0)
if sys.argv.__contains__("-sha1"):
    if sys.argv.__contains__("-l") or sys.argv.__contains__("-dir") or sys.argv.__contains__("-r") or sys.argv.__contains__("-md5"):
        print(RED + BOLD + "You can't enable other scan's! Only one!" + ENDC)
        sys.exit(0)
if sys.argv.__contains__("-sha256"):
    if sys.argv.__contains__("-l") or sys.argv.__contains__("-dir") or sys.argv.__contains__("-r") or sys.argv.__contains__("-md5") or sys.argv.__contains__("-sha1"):
        print(RED + BOLD + "You can't enable other scan's! Only one!" + ENDC)
        sys.exit(0)

print("")
print(OKBLUE + "     /$$$$$$$$ /$$ /$$             " + BOLD + "    /$$$$$$$$ /$$                 /$$                    " + ENDC)
print(OKBLUE + "    | $$_____/|__/| $$             " + BOLD + "   | $$_____/|__/                | $$                    " + ENDC)
print(OKBLUE + "    | $$       /$$| $$  /$$$$$$    " + BOLD + "   | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ " + ENDC)
print(OKBLUE + "    | $$$$$   | $$| $$ /$$__  $$   " + BOLD + "   | $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$" + ENDC)
print(OKBLUE + "    | $$__/   | $$| $$| $$$$$$$$   " + BOLD + "   | $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/" + ENDC)
print(OKBLUE + "    | $$      | $$| $$| $$_____/   " + BOLD + "   | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      " + ENDC)
print(OKBLUE + "    | $$      | $$| $$|  $$$$$$$   " + BOLD + "   | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      " + ENDC)
print(OKBLUE + "    |__/      |__/|__/ \_______/   " + BOLD + "   |__/      |__/|__/  |__/ \_______/ \_______/|__/      " + ENDC)
print("                                                                                        ")
print(BOLD + "By Mondei1")
print("Version is DEV_1.5\n" + ENDC)

# Set Auto-Complete
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

# Set booleans
if sys.argv.__contains__("-md5"):
    filename = input(getByID("Enter_MD5"))
    if len(filename) < 32 or len(filename) > 32:
        print(RED + "This isn't an MD5 hash! An MD5 hash has a length of 32 characters!" + ENDC)
        sys.exit(0)
    isMD5 = True
elif sys.argv.__contains__("-sha1"):
    filename = input(getByID("Enter_SHA1"))
    if len(filename) < 40 or len(filename) > 40:
        print(RED + "This isn't an SHA1 hash! An SHA1 hash has a length of 40 characters!" + ENDC)
        sys.exit(0)
    isSha1 = True
elif sys.argv.__contains__("-sha256"):
    filename = input(getByID("Enter_SHA256"))
    if len(filename) < 64 or len(filename) > 64:
        print(RED + "This isn't an SHA256 hash! An SHA256 hash has a length of 64 characters!" + ENDC)
        sys.exit(0)
    isSHA256 = True
elif sys.argv.__contains__("-dir"):
    isDirScan = True
    filename = input(getByID("Enter_Dir_Name"))
elif sys.argv.__contains__("-r"):
    isReadFiles = True
    filename = input(getByID("Enter_One_Word"))
else:
    filename = input(getByID("Enter_File_Name"))
if sys.argv.__contains__("-l"):
    isLowerCase = False

print("")
path = input(getByID("Enter_Path"))
try:
    scan(filename, path, MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles, sha1Scan=isSha1, sha256=isSHA256)
except KeyboardInterrupt:
    print(BOLD + RED + "Exit" + ENDC)