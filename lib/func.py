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
import hashlib
from functools import partial

def getPercent():
    if var.skipped:
        return "UNKNOWN"
    else:
        return repr(round((var.files_scanned / var.all_files) * 100, 2))
def getPercent_readScan():
    if var.skipped:
        return "UNKNOWN"
    else:
        return repr(round((var.words_readed / var.words_total) * 100, 2))

def getPercent_dirScan():
    if var.skipped:
        return "UNKNOWN"
    else:
        return repr(round((var.dirs_scanned / var.dirs_total) * 100, 2))

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

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

def isNormal(MD5scan, dirScan, readFiles, sha1Scan):
    boolean = True
    if MD5scan:
        isNormal = False
    elif dirScan:
        isNormal = False
    elif readFiles:
        isNormal = False
    elif sha1Scan:
        isNormal = False
    return boolean