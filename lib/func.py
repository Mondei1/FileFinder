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
from lib import var
from lib.lang.lang import *
import hashlib
from functools import partial

def getPercent():
    if var.skipped:
        return getByID("Word_Unknown")
    else:
        return repr(round((var.files_scanned / var.all_files) * 100, 2))
def getPercent_readScan():
    if var.skipped:
        return getByID("Word_Unknown")
    else:
        return repr(round((var.words_readed / var.words_total) * 100, 2))

def getPercent_dirScan():
    if var.skipped:
        return getByID("Word_Unknown")
    else:
        return repr(round((var.dirs_scanned / var.dirs_total) * 100, 2))

def md5sum(filename):
    BUF_SIZE = 65536
    md5 = hashlib.md5()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def sha1(filename):
    BUF_SIZE = 65536
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def sha256(filename):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def isNormal(MD5scan, dirScan, readFiles, sha1Scan, sha256):
    boolean = True
    if MD5scan:
        boolean = False
    elif dirScan:
        boolean = False
    elif readFiles:
        boolean = False
    elif sha1Scan:
        boolean = False
    elif sha256:
        boolean = False
    return boolean

# This function is called when the program get killed by STRG+C or by sys.exit(0)
def onQuit():
    if var.inScan:
        if var.founded.__len__() > 0:
            print(getByID("Word_Files") + "(%s)" % var.founded.__len__() + ":")
            for found in var.founded:
                print("- " + found)

        if var.dirs.__len__() > 0:
            print("\n" + getByID("Word_Dirs") + " (" + str(len(var.dirs)) + "):")
            for dir in var.dirs:
                sys.stdout.write("- " + dir + "\n")

        if var.skipped_files.__len__() > 0:
            print("\n")
            print(getByID("Word_Skipped_Files") + "(%s)" % var.skipped_files.__len__() + ":")
            for skipped in var.skipped_files:
                print("- " + skipped)
