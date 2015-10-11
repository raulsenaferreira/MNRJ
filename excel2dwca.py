# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:13:17 2015

@author: Raul
"""

from __future__ import absolute_import, division, print_function
import subprocess
from util import Util
#from pprint import pprint as pp
import csv     # imports the csv module

# deve ser trocado por endereco do arquivo a ser modificado e arquivo destino
file = "TESTE.xlsx result.csv"

#chama o shell e converte planilha para csv
argument = 'ssconvert {0}'.format(file)
command_process = subprocess.call([argument], shell=True)

ofile  = open('final.csv', "wb")
writer = csv.writer(ofile, delimiter=',')

reader=[]
f = open("result.csv", 'rb') # opens the csv file
try:
    reader = csv.reader(f)  # creates the reader object
    for row in reader:   # iterates the rows of the file in orders
        row[0] = row[0]+"Raul"        
        writer.writerow(row)    # prints each row
finally:
    f.close()
    
