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
# Colors
BLACK = '\033[30m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
RED = '\033[31m'
BLUE = '\033[34m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
STRIKE = '\033[29m'
UNDERLINE = '\033[4m'

# --------------------------
_VERSION = "DEV_1.7"
_AUTHOR = "Mondei1"
# --------------------------

# scan.py will set this value to TRUE when it start's the scan
inScan = False

# If phase 1 is skipped with CTRL+C
skipped = False

# These files cannot be scan because the program hasn't permissions to access the file :c
skipped_files = []

# How many files are founded
all_files = 0
# How many files already scanned
files_scanned = 0
# Founded files
founded = []
# --------------------------
# Founded dir's
dirs = []
# How many dir's already scanned
dirs_scanned = 0
# How many dir's exists
dirs_total = 0
# --------------------------
# Founded text lines (/path/to/file.txt (in line 34), ...)
texts = []
# How many words are readed
words_readed = 0
# How many words exists
words_total = 0
# --------------------------
# This blacklist is for files, where the program can't calculate the MD5 hash!
blacklist = [ "steam.pipe" ]
# --------------------------
# The program will ignore these files/folders
ignore_Files = []
ignore_Folders = []