import xml.etree.ElementTree as ET
import locale

"""
Example: getByID("Enter_Path") --> Return the english text If the sys-language is English.
                                   It can also return the german/... text If the sys-language is german.
"""

# Store the sys-language and split it.
language = locale.getdefaultlocale().__getitem__(0).split("_")

# NOTE:
# In fall that no IF or ELSE always the case, return the english text.
def getByID(id):
    en_tree = ET.parse('lib/lang/en.xml')
    de_tree = ET.parse('lib/lang/de.xml')

    string = '''.//*[@id='%ID%']'''
    string = str(string).replace("%ID%", id)

    if language.__contains__("en"):
        return en_tree.findall(string)[0].text
    elif language.__contains__("de"):
        return de_tree.findall(string)[0].text
    else:
        return en_tree.findall(string)[0].text