import xml.etree.ElementTree as ET
import locale
import sys

from lib.var import *

"""
Example: getByID("Enter_Path") --> Return the english text If the sys-language is English.
                                   It can also return the german text If the sys-language is german. And so on...
"""

# Store the sys-language and split it.
language = locale.getdefaultlocale().__getitem__(0).split("_")

# NOTE:
# In fall that no IF or ELSE always the case, return the english text.
def getByID(id):
    try:
        en_tree = ET.parse('lib/lang/en.xml')
        de_tree = ET.parse('lib/lang/de.xml')
    except FileNotFoundError:
        print(BOLD + RED + "ERROR: Didn't find en.xml or de.xml in lib/lang/\n" +
              "       Please clone this project again from GitHub!" + ENDC)
        sys.exit(0)

    string = '''.//*[@id='%ID%']'''
    string = str(string).replace("%ID%", id)

    if language.__contains__("de"):
        return de_tree.findall(string)[0].text
    else:
        return en_tree.findall(string)[0].text