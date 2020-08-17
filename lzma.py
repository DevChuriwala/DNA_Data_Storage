#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:27:25 2020

@author: neel
"""


import lzma
data_in = b"""\
Here lies the Tengwar inscription in the Black Speech of Mordor Three Rings for 
the Elvenkings under the sky Seven for the Dwarflords in their halls of stone Nine 
for Mortal Men doomed to die One for the Dark Lord on his dark throne In the Land of Mordor 
where the Shadows lie One Ring to rule them all One Ring to find them One Ring to bring them 
all and in the darkness bind them in the Land of Mordor where the Shadows lie"""
data_out = lzma.compress(data_in)
print(len(data_in)/len(data_out))

lzc = lzma.LZMACompressor(preset=9)
data_out=lzc.compress(data_in)
print(len(data_in)/len(data_out))
with lzma.open("/home/neel/Downloads/file1.xz", "w", preset=9) as f:
    f.write(data_in)
with lzma.open("/home/neel/Downloads/file1.xz") as f:
    file_content = f.read()
print(file_content)
