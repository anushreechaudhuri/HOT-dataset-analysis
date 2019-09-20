# so the commands I will be typing are as follows:
# gg - go to top of the file
# Shift-V - go into selection mode (line selection)
# Shift-G - go to bottom of the file
# :retab  # this replaces all tabs with spaces
import pandas as pd
import subprocess
import os

#with open('lsa.txt', 'w') as f:
 #   if f.readLine().contains(
 
remove = ['STNN', 'CAST', 'BTLN', 'CTDRAW', 'CTDPRS', 'QUALT','REVPRS', 'REVTMP', 'CRUISE', 'SAMP']


# should be reading and writing to different files, can't do both simultaneously in one file in python

w = open('filtered_lsa.txt', 'w')

with open('lsa.txt','r') as f:
    new_f = f.readlines()
    for line in new_f:
        if not any(item in line for item in remove):
            w.write(line)
w.close()
f.close()
