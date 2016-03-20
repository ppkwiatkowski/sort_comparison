import sys
import os

pypyPath = "/Users/pk/Downloads/pypy-4.0.1-src/"
sys.path.append(os.path.normpath(pypyPath))
sys.path.append(os.path.normpath(pypyPath + "/rpython/rlib"))

from listsort import TimSort as TS


def sort(inSeq):
    TS(inSeq).sort()
    return inSeq
