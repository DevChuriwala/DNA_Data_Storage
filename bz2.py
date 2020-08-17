#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:50:48 2020

@author: neel
"""


import bz2
data = b"""\
Here lies the Tengwar inscription in the Black Speech of Mordor Three Rings for 
the Elvenkings under the sky Seven for the Dwarflords in their halls of stone Nine 
for Mortal Men doomed to die One for the Dark Lord on his dark throne In the Land of Mordor 
where the Shadows lie One Ring to rule them all One Ring to find them One Ring to bring them 
all and in the darkness bind them in the Land of Mordor where the Shadows lie"""


c = bz2.compress(data)
print(len(data) / len(c))


with bz2.open("myfile.bz2", "wb") as f:
    # Write compressed data to file
    unused = f.write(data)
    
with bz2.open("myfile.bz2", "rb") as f:
    # Decompress data from file
    content = f.read()
print(content)