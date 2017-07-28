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

import os, sys, codecs
from lib import var, func
from lib.lang.lang import *


def scan(searchFor, path, MD5scan, dirScan, lowerCase, readFiles, sha1Scan, sha256):
    isNormal = func.isNormal(MD5scan, dirScan, readFiles, sha1Scan, sha256)

    # Remove the "/" If it start's with it.
    if str(path).endswith("/"):
        if not path == "/":
            path = path[:-1]

    # Phase 1 - To calculate the scan progress I must have the total amount of files/words/folders to calculate the percent number.
    try:
        if not dirScan and not readFiles:
            message = getByID("Calc_Amount_Of_Files")
            for root, dirs, files in os.walk(path):
                for file in files:
                    sys.stdout.write("\r" + message + " (" + str(var.all_files) + ") ...")
                    var.all_files += 1
        # Scan based on words
        if readFiles:
            message = getByID("Calc_Amount_Of_Words")
            for root, dirs, files in os.walk(path):
                for file in files:
                    for line in codecs.open(root + "/" + file, "r", encoding='utf-8', errors='ignore').readlines():
                        words = line.split(" ")
                        for words in words:
                            var.words_total += 1
                            sys.stdout.write("\r" + message + " (" + str(var.words_total) + ") ...")
        # Check how many dir's exists
        if dirScan:
            message = getByID("Calc_Amount_Of_Dirs")
            for root, dirs, files in os.walk(path):
                for dir in dirs:
                    sys.stdout.write("\r" + message + " (" + str(var.dirs_total) + ") ...")
                    var.dirs_total += 1
    except KeyboardInterrupt:
        var.skipped = True
        var.dirs_total = 0
        var.all_files = 0
        var.words_total = 0
        print(var.BOLD + var.BLUE + "Skipped!" + var.ENDC)
    print("")

    # Phase 2 - Finally, here I scan all files
    # ---------------------------------------------------------------------
    # Read files
    if readFiles:
        for root, dirs, files in os.walk(path):
            # File read scan
            for file in files:
                for line in codecs.open(root + "/" + file, "r", encoding='utf-8', errors='ignore').readlines():
                    splited = line.split(" ")
                    line_cnt = 0
                    for word in splited:
                        line_cnt += 1
                        var.words_readed += 1
                        sys.stdout.write("\rProgress: " + str(func.getPercent_readScan()) + "%(" + str(var.words_readed) + "/" + str(var.words_total) + ")")
                        if word.lower() == searchFor.lower():
                            var.texts.append(root + "/" + file + " (in line " + str(line_cnt - 1) + "), ")
        print("")
        print(getByID("Word_Text") + " (" + str(len(var.texts)) + "):")
        for found in var.texts:
            print("- " + found)
        sys.exit(0)


    # Dir scan
    if dirScan:
        progress = getByID("Word_Progress")
        founded = getByID("Word_Founded")
        passs = False
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                sys.stdout.write("\r" + progress + ": " + str(func.getPercent_dirScan()) + "% (" + str(var.dirs_scanned) + " / " + str(
                    var.dirs_total) + ") - " + founded +": " + str(len(var.dirs)))
                if var.ignore_Folders.__contains__(dir):
                    var.skipped_files.append(root + "/" + dir + " (" + getByID("Folder_Ignored") + ")")
                    passs = True
                if dir.lower() == searchFor.lower() and passs is False:
                    var.dirs.append(root + "/" + dir)
                var.dirs_scanned += 1

        print("\n" + getByID("Word_Dirs") + " (" + str(len(var.dirs)) + "):")
        for dir in var.dirs:
            sys.stdout.write("- " + dir + "\n")

    # MD5 scan
    # If the MD5 scan is enabled, the program will calculate the MD5 hash of every file and check if it the same
    if MD5scan:
        progress = getByID("Word_Progress")
        stop = False
        passs = False
        for root, files, dirs in os.walk(path):
            for file in dirs:
                try:
                    sys.stdout.write("\r" + progress + ": " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(var.all_files) + ")")
                    md5sum = ""
                    # If file is in blacklist
                    for blacklist in var.blacklist:
                        if blacklist == file:
                            var.skipped_files.append(root + "/" + file + " (" + getByID("File_In_Blacklist") + ")")
                            sha256sum = "UNKNOWN (file is in blacklist)"

                    # If file is in '.ignore-files'
                    if var.ignore_Files.__contains__(file):
                        var.skipped_files.append(root + "/" + file + " (" + getByID("File_Ignored") + ")")
                        passs = True
                    if md5sum == "" and passs is False:
                        if func.md5sum(root + "/" + file) == searchFor:
                            print(var.BOLD + "\n" + getByID("Found_Target_File") + root + "/" + file + var.ENDC)
                            stop = True
                    var.files_scanned += 1
                except FileNotFoundError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (FileNotFoundError)")
                    pass
                except OSError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (OSError --> " + getByID("No_Permissions") + ")")
            if stop:
                break

    # SHA-1 scan
    if sha1Scan:
        progress = getByID("Word_Progress")
        stop = False
        passs = False
        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    sys.stdout.write(
                        "\r" + progress + ": " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(
                            var.all_files) + ")")
                    sha1sum = ""
                    # If file is in blacklist
                    for blacklist in var.blacklist:
                        if blacklist == file:
                            var.skipped_files.append(root + "/" + file + " (" + getByID("File_In_Blacklist") + ")")
                            sha256sum = "UNKNOWN (file is in blacklist)"

                    # If file is in '.ignore-files'
                    if var.ignore_Files.__contains__(file):
                        var.skipped_files.append(root + "/" + file + " (" + getByID("File_Ignored") + ")")
                        passs = True
                    if sha1sum == "" and passs is False:
                        if func.sha1(root + "/" + file) == searchFor:
                            print(var.BOLD + "\n" + getByID("Found_Target_File") + root + "/" + file + var.ENDC)
                            stop = True
                    var.files_scanned += 1
                except FileNotFoundError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (FileNotFoundError)")
                    pass
                except OSError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (OSError --> " + getByID("No_Permissions") + ")")
            if stop:
                break

    # SHA-256 scan
    if sha256:
        progress = getByID("Word_Progress")
        stop = False
        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    sys.stdout.write(
                        "\r" + progress + ": " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(
                            var.all_files) + ")")
                    sha256sum = ""

                    # If file is in blacklist
                    for blacklist in var.blacklist:
                        if blacklist == file:
                            var.skipped_files.append(root + "/" + file + " (" + getByID("File_In_Blacklist") + ")")
                            sha256sum = "UNKNOWN (file is in blacklist)"

                    # If file is in '.ignore-files'
                    if var.ignore_Files.__contains__(file):
                        var.skipped_files.append(root + "/" + file + " (" + getByID("File_Ignored") + ")")
                        pass
                    if sha256sum == "":
                        if func.sha256(root + "/" + file) == searchFor:
                            print(var.BOLD + "\n" + getByID("Found_Target_File") + ": " + root + "/" + file + var.ENDC)
                            stop = True
                            break
                    var.files_scanned += 1
                except FileNotFoundError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (FileNotFoundError)")
                    pass
                except OSError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (OSError --> " + getByID("No_Permissions") + ")")
            if stop:
                break

    # Normal scan
    if isNormal:
        progress = getByID("Word_Progress")
        ignored = False
        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    # If file is in '.ignore-files'
                    if var.ignore_Files.__contains__(file):
                        var.skipped_files.append(root + "/" + file + " (" + getByID("File_Ignored") + ")")
                        ignored = True
                    if not ignored:
                        if lowerCase:
                            if str(file).lower() == searchFor.lower():
                                var.founded.append(root + "/" + file)
                        else:
                            if str(file) == searchFor:
                                var.founded.append(root + "/" + file)
                    sys.stdout.write("\r" + progress + ": " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(var.all_files) + ") - Founded: " + str(len(var.founded)))
                    var.files_scanned += 1
                except FileNotFoundError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (FileNotFoundError)")
                    pass
                except OSError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (OSError --> " + getByID("No_Permissions") + ")")
        print("")
        print(getByID("Word_Files") + "(%s)" % var.founded.__len__() + ":")
        for found in var.founded:
            print("- " + found)
    # ---------------------------------------------------------------------
    # Phase 3 - Print all skipped files
    print("")
    print(getByID("Word_Skipped_Files") + "(%s)" % var.skipped_files.__len__() + ":")
    for skipped in var.skipped_files:
        print("- "+ skipped)