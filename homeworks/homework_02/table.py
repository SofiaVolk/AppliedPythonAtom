import sys
import input
import output
import process
import processtsv
import os
import tempfile
import subprocess
if __name__ == '__main__':
    filename = sys.argv[1]
ms, path = tempfile.mkstemp()
data = input.parser(filename)
if type(data[0]) is dict:
    process.table_proc(data)
else:
    processtsv.table_proc(data)
