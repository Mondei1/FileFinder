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
from lib.var import texts_size


def scan(searchFor, path, MD5scan, dirScan, lowerCase, readFiles):

    # Remove the "/" If it start's with it.
    if str(path).endswith("/"):
        path = path[:1]

    # Phase 1 - To calculate the scan progress I must have the total amount of files to calculate the percent number.
    if not readFiles:
        for root, dirs, files in os.walk(path):
            for file in files:
                sys.stdout.write("\rCalculate how many files are exists (" + str(var.all_files) + ")...")
                var.all_files += 1
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                for line in codecs.open(root + "/" + file, "r", encoding='utf-8', errors='ignore').readlines():
                    sys.stdout.write("\rCalculate how many lines are exists (" + str(var.all_files) + ")...")
                    var.texts_total += 1
    print("")

    # Phase 2 - Finally, here I scan all files
    for root, dirs, files in os.walk(path):
        # File read scan
        if readFiles:
            for file in files:
                for line in codecs.open(root + "/" + file, "r", encoding='utf-8', errors='ignore').readlines():
                    splited = line.split(" ")
                    line_cnt = 0
                    for word in splited:
                        line_cnt += 1
                        if word.lower() == searchFor.lower():
                            var.texts += root + "/" + file + " (in line " + str(line_cnt) + "), "
                            var.texts_size += 1
                    line_cnt = 0
        # Dir scan
        if dirScan:
            for dir in dirs:
                if dir == searchFor:
                    var.dirs += root + "/" + dir + ", "
                    var.dirs_size += 1
        # Normal scan
        if not dirScan:
            for filee in files:
                try:
                    # If the MD5 scan is enabled, the program will calculate the MD5 hash of every file and check if it the same
                    # MD5 scan
                    if MD5scan:
                        sys.stdout.write("\rProgress: " + str(func.getPercent()) + "% (" + str(var.scanned_files) + " / " + str(var.all_files) +")")
                        md5sum = ""
                        for blacklist in var.blacklist:
                            if blacklist == filee:
                                md5sum = "UNKOWN (file is in blacklist)"
                        if md5sum == "":
                            if func.md5sum(root + "/" + filee) == searchFor:
                                var.founded += ", " + root + "/" + filee
                                print("\nFound target file: " + root + "/" + filee)
                                sys.exit(0)
                    else:
                        if lowerCase:
                            if str(filee).lower() == searchFor.lower():
                                var.founded += ", " + root + "/" + filee
                                var.founded_size += 1
                        else:
                            if str(filee) == searchFor:
                                var.founded += ", " + root + "/" + filee
                                var.founded_size += 1
                        sys.stdout.write("\rProgress: " + str(func.getPercent()) + "% (" + str(var.scanned_files) + " / " + str(var.all_files) + ") - Founded: " + str(var.founded_size))
                    var.scanned_files += 1
                except FileNotFoundError:
                    pass
                except OSError:
                    pass

    # Phase 3 - Print all founded files
    if not dirScan or not readFiles:
        founded_array = var.founded.split(", ")
        print("\nFiles (" + str(var.founded_size) + "):")
        founded_array.remove("")
        for ffile in founded_array:
            sys.stdout.write("- " + ffile + "\n")

    if dirScan:
        dir_array = var.dirs.split(", ")
        dir_array.remove("")
        print("Dir's (" + str(var.dirs_size) + "):")
        for dir in dir_array:
            sys.stdout.write("- " + dir + "\n")

    if readFiles:
        texts_array = var.texts.split(", ")
        print("Text (" + str(var.texts_size) + "):")
        for text in texts_array:
            print("- " + text)