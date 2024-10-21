#!/usr/bin/python2

import sys
import os

class Uniq2FASTAPlugin:
 def input(self, inputfile):
    self.filename = inputfile
 def run(self):
     pass
 def output(self, outputfile):
    file = open(self.filename ,'r')
    outfile = open(outputfile, 'w')
    i=1
    for line in file:
      ls = line.strip().split(" ")
      outfile.write(">" + str(i) + "_" + ls[-2]+"\n")
      outfile.write(ls[-1]+"\n")
      i += 1
    file.close()
    
