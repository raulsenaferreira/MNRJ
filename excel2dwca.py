# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:13:17 2015

@author: Raul
"""

from __future__ import absolute_import, division, print_function
import subprocess
#from util import Util
#from pprint import pprint as pp
import csv     # imports the csv module

def main():
    # deve ser trocado por endereco do arquivo a ser modificado e arquivo destino
    file = "TESTE.xlsx result.csv"
    
    #chama o shell e converte planilha para csv
    argument = 'ssconvert {0}'.format(file)
    command_process = subprocess.call([argument], shell=True)
    
    ofile  = open('final.csv', "wb")
    writer = csv.writer(ofile, delimiter=',')
    
    header=True
    f = open("result.csv", 'rb') # opens the csv file
    try:
        reader = csv.reader(f)  # creates the reader object
        for row in reader:   # iterates the rows of the file in orders
            if header is True:
                header = False
                for i in range(0, len(row)):
                    row[i] = mapDWC(row[i])
            writer.writerow(row)    # prints each row
    finally:
        f.close()
    
    
    
def mapDWC(term):
        term = str(term).lower().replace(' ','')
        mDWC = dict()
        mDWC['filo'] = 'phylum'
        mDWC['classe'] = 'class'
        mDWC['ordem'] = 'order'
        mDWC['familia'] = 'family'
        #mDWC['subfamilia'] = ''
        #mDWC['tribo'] = ''
        mDWC['genero'] = 'genus'
        mDWC['epiteto'] = 'specificEpithet'
        mDWC['numerodecampo'] = 'fieldNumber'
        #mDWC['ambiente'] = ''
        mDWC['datadedeterminacao'] = 'dateIdentified'
        #mDWC['entrada'] = ''
        #mDWC['dataentrada'] = ''
        mDWC['tecnicacol'] = 'samplingProtocol'
        mDWC['tipodecolecao'] = 'type'
        mDWC['observacaoreg'] = 'basisOfRecord'
        mDWC['pais'] = 'country'
        mDWC['estado'] = 'stateProvince'
        mDWC['municipio'] = 'municipality'
        mDWC['localidade'] = 'locality'
        #mDWC['numerocoletor'] = ''
        mDWC['datacoleta'] = 'eventDate'
        mDWC['observacaocoleta'] = 'eventRemarks'
        mDWC['graudelatitude'] = 'decimalLatitude'
        #mDWC['minutodelatitude'] = ''
        #mDWC['segundodelatitude'] = ''
        #mDWC['latitudenortesul'] = ''
        mDWC['graudelongitude'] = 'decimalLongitude'
        #mDWC['minutodelongitude'] = ''
        #mDWC['segundodelongitude'] = ''
        #mDWC['longitudelesteoeste'] = ''
        mDWC['profundidade'] = 'verbatimDepth'
        #mDWC['nºindividuos'] = ''
        mDWC['determinador'] = 'identifiedBy'
        mDWC['coletor'] = 'recordedBy'
        #mDWC['projeto'] = ''
        
        try:
            return mDWC[term]
        except KeyError:
            return term
            
main()
