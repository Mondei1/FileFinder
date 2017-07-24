"""COLORS"""
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

all_files = 0
scanned_files = 1

founded = ""
founded_size = 0

dirs = ""
dirs_size = 0

texts = ""
texts_total = 0
texts_size = 0

# This blacklist is for files, where the program can't calculate the MD5 hash!
blacklist = { "steam.pipe" }