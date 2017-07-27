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


def scan(searchFor, path, MD5scan, dirScan, lowerCase, readFiles, sha1Scan, sha256):
    isNormal = func.isNormal(MD5scan, dirScan, readFiles, sha1Scan, sha256)

    # Remove the "/" If it start's with it.
    if str(path).endswith("/"):
        if not path == "/":
            path = path[:-1]

    # Phase 1 - To calculate the scan progress I must have the total amount of files/words/folders to calculate the percent number.
    try:
        if not dirScan and not readFiles:
            for root, dirs, files in os.walk(path):
                for file in files:
                    sys.stdout.write("\rCalculate how many files are exists (" + str(var.all_files) + ")...")
                    var.all_files += 1
        # Scan based on words
        if readFiles:
            for root, dirs, files in os.walk(path):
                for file in files:
                    for line in codecs.open(root + "/" + file, "r", encoding='utf-8', errors='ignore').readlines():
                        sys.stdout.write("\rCalculate how many words are exists (" + str(var.words_total) + ")...")
                        words = line.split(" ")
                        for words in words:
                            var.words_total += 1
        # Check how many dir's exists
        if dirScan:
            for root, dirs, files in os.walk(path):
                for dir in dirs:
                    sys.stdout.write("\rCalculate how many folders are exists (" + str(var.dirs_total) + ") ...")
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
        print("Text (" + str(len(var.texts)) + "):")
        for found in var.texts:
            print("- " + found)
        sys.exit(0)


    # Dir scan
    if dirScan:
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                sys.stdout.write("\rProgress: " + str(func.getPercent_dirScan()) + "% (" + str(var.dirs_scanned) + " / " + str(
                    var.dirs_total) + ") - Founded: " + str(len(var.dirs)))
                if dir.lower() == searchFor.lower():
                    var.dirs.append(root + "/" + dir)
                var.dirs_scanned += 1

        print("\nDir(s) (" + str(len(var.dirs)) + "):")
        for dir in var.dirs:
            sys.stdout.write("- " + dir + "\n")
        sys.exit(0)

    # MD5 scan
    # If the MD5 scan is enabled, the program will calculate the MD5 hash of every file and check if it the same
    if MD5scan:
        stop = False
        for root, files, dirs in os.walk(path):
            for file in dirs:
                sys.stdout.write("\rProgress: " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(var.all_files) + ")")
                md5sum = ""
                for blacklist in var.blacklist:
                    if blacklist == file:
                        md5sum = "UNKNOWN (file is in blacklist)"
                if md5sum == "":
                    if func.md5sum(root + "/" + file) == searchFor:
                        print(var.BOLD + "\nFound target file: " + root + "/" + file + var.ENDC)
                        stop = True
                var.files_scanned += 1
            if stop:
                break

    # SHA-1 scan
    if sha1Scan:
        stop = False
        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    sys.stdout.write(
                        "\rProgress: " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(
                            var.all_files) + ")")
                    sha1sum = ""
                    for blacklist in var.blacklist:
                        if blacklist == file:
                            sha1sum = "UNKNOWN (file is in blacklist)"
                    if sha1sum == "":
                        if func.sha1(root + "/" + file) == searchFor:
                            print(var.BOLD + "\nFound target file: " + root + "/" + file + var.ENDC)
                            stop = True
                    var.files_scanned += 1
                except FileNotFoundError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file)
                    pass
                except OSError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file)
            if stop:
                break

    # SHA-256 scan
    if sha256:
        stop = False
        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    sys.stdout.write(
                        "\rProgress: " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(
                            var.all_files) + ")")
                    sha256sum = ""
                    for blacklist in var.blacklist:
                        if blacklist == file:
                            var.skipped_files.append(root + "/"+ file + " (File is in blacklist)")
                            sha256sum = "UNKNOWN (file is in blacklist)"
                    if sha256sum == "":
                        if func.sha256(root + "/" + file) == searchFor:
                            print(var.BOLD + "\nFound target file: " + root + "/" + file + var.ENDC)
                            stop = True
                            break
                    var.files_scanned += 1
                except FileNotFoundError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (FileNotFoundError)")
                    pass
                except OSError:
                    var.files_scanned += 1
                    var.skipped_files.append(root + "/" + file + " (OSError --> No permissions)")
            if stop:
                break

    # Normal scan
    if isNormal:
        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    if lowerCase:
                        if str(file).lower() == searchFor.lower():
                            var.founded.append(root + "/" + file)
                    else:
                        if str(file) == searchFor:
                            var.founded.append(root + "/" + file)
                    sys.stdout.write("\rProgress: " + str(func.getPercent()) + "% (" + str(var.files_scanned) + " / " + str(var.all_files) + ") - Founded: " + str(len(var.founded)))
                    var.files_scanned += 1
                except FileNotFoundError:
                    pass
                except OSError:
                    pass
        print("")
        print("Files (%s)" % var.founded.__len__() + ":")
        for found in var.founded:
            print("- " + found)
    # ---------------------------------------------------------------------
    # Phase 3 - Print all skipped files
    print("Skipped files (%s)" % var.skipped_files.__len__())
    for skipped in var.skipped_files:
        print("- "+ skipped)