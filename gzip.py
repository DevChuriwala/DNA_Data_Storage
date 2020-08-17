#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:18:26 2020

@author: neel
"""


import gzip
s_in = b"""\
Here lies the Tengwar inscription in the Black Speech of Mordor Three Rings for 
the Elvenkings under the sky Seven for the Dwarflords in their halls of stone Nine 
for Mortal Men doomed to die One for the Dark Lord on his dark throne In the Land of Mordor 
where the Shadows lie One Ring to rule them all One Ring to find them One Ring to bring them 
all and in the darkness bind them in the Land of Mordor where the Shadows lie"""

s_out = gzip.compress(s_in)
print(len(s_in) / len(s_out))

with gzip.open('/home/neel/Downloads/file.txt.gz', 'wb') as f:
    f.write(s_in)
    
with gzip.open('/home/neel/Downloads/file.txt.gz', 'rb') as f:
    file_content = f.read()
print(file_content)