#!/usr/bin/python
from os import system, listdir

for file in listdir("."):
    if file.endswith(".ui"):
        name = file[:-3]
        system("pyuic4 -x -o %s.py %s"%(name, file))
    if file.endswith(".qrc"):
        name = file[:-4] + "_rc"
        system("pyrcc4 -o %s.py %s"%(name, file))
