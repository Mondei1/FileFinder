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
import atexit

try:
    from lib.scan import scan
    from lib.var import *
    from lib.func import *
    from lib.lang.lang import *
except ImportError:
    print("\033[1mPlease run this script with python3 or higher! (Tested with python3.5 under Linux)\033[0m")
    sys.exit(0)

# Auto-Complete
def complete(text, state):
    return (glob.glob(text + '*' + "/") + [None])[state]

# Set atexit
atexit.register(onQuit)

isMD5 = False
isDirScan = False
isLowerCase = True
isReadFiles = False
isSha1 = False
isSHA256 = False
# Args check
if sys.argv.__contains__("-help") or sys.argv.__contains__("?"):
    print(getByID("Help"))
    sys.exit(0)
if sys.argv.__contains__("-md5"):
    if sys.argv.__contains__("-l") or sys.argv.__contains__("-dir") or sys.argv.__contains__("-r"):
        print(RED + BOLD + getByID("Only_One_Scan") + ENDC)
        sys.exit(0)
if sys.argv.__contains__("-sha1"):
    if sys.argv.__contains__("-l") or sys.argv.__contains__("-dir") or sys.argv.__contains__("-r") or sys.argv.__contains__("-md5"):
        print(RED + BOLD + getByID("Only_One_Scan") + ENDC)
        sys.exit(0)
if sys.argv.__contains__("-sha256"):
    if sys.argv.__contains__("-l") or sys.argv.__contains__("-dir") or sys.argv.__contains__("-r") or sys.argv.__contains__("-md5") or sys.argv.__contains__("-sha1"):
        print(RED + BOLD + getByID("Only_One_Scan") + ENDC)
        sys.exit(0)

# Search over command line
if sys.argv.__len__() > 2:
    args = sys.argv
    if str(args[1]).lower() == "-md5":
        isMD5 = True
        if not str(args[2]).lower() == "":
            if len(args[2]) < 32 or len(args[2]) > 32:
                print(RED + getByID("Not_An_MD5_Hash") + ENDC)
                sys.exit(0)
            if str(args[3]) == "":
                args[3] = "/"
            else:
                scan(args[2], args[3], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                     sha1Scan=isSha1, sha256=isSHA256)
                print("")
                sys.exit(0)
    if str(args[1]).lower() == "-sha1":
        isSha1 = True
        if not str(args[2]).lower() == "":
            if len(args[2]) < 40 or len(args[2]) > 40:
                print(RED + getByID("Not_An_SHA1_Hash") + ENDC)
                sys.exit(0)
            else:
                scan(args[2], args[3], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                     sha1Scan=isSha1, sha256=isSHA256)
                print("")
                sys.exit(0)
    if str(args[1]).lower() == "-sha256":
        isSHA256 = True
        if not str(args[2]).lower() == "":
            if len(args[2]) < 64 or len(args[2]) > 64:
                print(RED + getByID("Not_An_SHA256_Hash") + ENDC)
                sys.exit(0)
            else:
                scan(args[2], args[3], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                     sha1Scan=isSha1, sha256=isSHA256)
                print("")
                sys.exit(0)
    if str(args[1]).lower() == "-dir":
        isDirScan = True
        if args[2] == "-l":
            isLowerCase = False
            scan(args[3], args[4], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                 sha1Scan=isSha1, sha256=isSHA256)
        else:
            scan(args[2], args[3], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                 sha1Scan=isSha1, sha256=isSHA256)
        print("")
        sys.exit(0)
    if str(args[1]).lower() == "-r":
        isReadFiles = True
        if args[2] == "-l":
            isLowerCase = False
            scan(args[3], args[4], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                 sha1Scan=isSha1, sha256=isSHA256)
        else:
            scan(args[2], args[3], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                 sha1Scan=isSha1, sha256=isSHA256)
        print("")
        sys.exit(0)
    if str(args[1]).lower() == "-fn":
        if args[2] == "-l":
            isLowerCase = False
            scan(args[3], args[4], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                 sha1Scan=isSha1, sha256=isSHA256)
        else:
            scan(args[2], args[3], MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles,
                 sha1Scan=isSha1, sha256=isSHA256)
        print("")
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
print(BOLD + "By " + var._AUTHOR)
print("Version is " + var._VERSION + "\n" + ENDC)

# Set ignored files/folders
try:
    with open(".ignore-files", 'r') as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            ignore_Files.append(line)
except FileNotFoundError:
    pass
try:
    with open(".ignore-folders", 'r') as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            ignore_Folders.append(line)
except FileNotFoundError:
    pass


# Set Auto-Complete
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

# Set booleans
if sys.argv.__contains__("-md5"):
    filename = input(getByID("Enter_MD5"))
    if len(filename) < 32 or len(filename) > 32:
        print(RED + getByID("Not_An_MD5_Hash") + ENDC)
        sys.exit(0)
    isMD5 = True
elif sys.argv.__contains__("-sha1"):
    filename = input(getByID("Enter_SHA1"))
    if len(filename) < 40 or len(filename) > 40:
        print(RED + getByID("Not_An_SHA1_Hash") + ENDC)
        sys.exit(0)
    isSha1 = True
elif sys.argv.__contains__("-sha256"):
    filename = input(getByID("Enter_SHA256"))
    if len(filename) < 64 or len(filename) > 64:
        print(RED + getByID("Not_An_SHA256_Hash") + ENDC)
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

if ignore_Files.__contains__(filename) or ignore_Folders.__contains__(filename):
    if isNormal(MD5scan=isMD5, dirScan=isDirScan, readFiles=isReadFiles, sha1Scan=isSha1, sha256=isSHA256):
        print(BOLD + RED + getByID("File_Search_Is_Pointless") + ENDC)
    if isDirScan:
        print(BOLD + RED + getByID("Dir_Search_Is_Pointless") + ENDC)

print("")
path = input(getByID("Enter_Path"))
if path == "":
    path = "/"
try:
    scan(filename, path, MD5scan=isMD5, dirScan=isDirScan, lowerCase=isLowerCase, readFiles=isReadFiles, sha1Scan=isSha1, sha256=isSHA256)
except KeyboardInterrupt:
    print(BOLD + RED + "Exit" + ENDC)