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
        if dirScan:
            for dir in dirs:
                if dir == searchFor:
                    var.dirs += root + "/" + dir + ", "
                    var.dirs_size += 1
        if not dirScan:
            for filee in files:
                # If the MD5 scan is enabled, the program will calc. the MD5 hash of every file and check if it the same
                if MD5scan:
                    sys.stdout.write("\rProgress: " + str(func.getPercent()) + "% (" + str(var.scanned_files) + " / " + str(var.all_files) + ")")
                    if func.md5sum(root + "/" + filee) == searchFor:
                        var.founded += ", " + root + "/" + filee
                        print("\nFound target file: " + root + "b/" + filee)
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