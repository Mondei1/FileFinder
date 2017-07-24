from lib import var
import hashlib
from functools import partial

def getPercent():
    return repr(round((var.scanned_files / var.all_files) * 100, 2))

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()