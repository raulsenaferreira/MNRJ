# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:13:17 2015

@author: Raul
"""

from __future__ import absolute_import, division, print_function
from sys import stdin
import subprocess
#from util import Util
#from pprint import pprint as pp
import csv     # imports the csv module

def main(file):
    #parametro file contem nome do arquivo original e sua extensao
    # deve ser trocado por endereco do arquivo a ser modificado e arquivo destino
    #file = "TESTE.xlsx result.csv"
    files = file.split('.')
    #chama o shell e converte planilha para csv
    args = '{0} {1}.csv'.format(file, files[0])
    argument = 'ssconvert {0}'.format(args)
    command_process = subprocess.call([argument], shell=True)
    
    ofile  = open(files[0]+'-CONVERTIDO.csv', "wb")#open('final.csv', "wb")
    writer = csv.writer(ofile, delimiter=',')
    
    header=True
    arg = '{0}.csv'.format(files[0])
    f = open(arg, 'rb')#open("result.csv", 'rb') # opens the csv file
    
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
        return True
    
#DATA ENTRADA aaaa-mm-dd	 = eventDate ?
#COLECAO DE ORIGEM	= institutionCode ?
    
def mapDWC(term):
        term = str(term).lower().replace(' ','')
        mDWC = dict()
        
        #mapeamentos por fazer
        mDWC[''] = 'minimumElevationInMeters'
        mDWC[''] = 'maximumElevationInMeters'
        mDWC[''] = 'type'
        mDWC[''] = 'modified'
        mDWC[''] = 'language'
        mDWC[''] = 'rights'
        mDWC[''] = 'rightsHolder'
        mDWC[''] = 'institutionID'
        mDWC[''] = 'institutionCode'
        mDWC[''] = 'collectionCode'
        mDWC[''] = 'datasetName'
        mDWC[''] = 'occurrenceID'
        mDWC[''] = 'individualCount'
        mDWC[''] = 'preparations'
        mDWC[''] = 'habitat'
        mDWC[''] = 'continent'
        mDWC[''] = 'countryCode'
        mDWC[''] = 'county'
        mDWC[''] = 'minimumDepthInMeters'
        mDWC[''] = 'maximumDepthInMeters'
        mDWC[''] = 'locationRemarks'
        mDWC[''] = 'georeferencedBy'
        mDWC[''] = 'georeferencedDate'
        mDWC[''] = 'georeferenceProtocol'
        mDWC[''] = 'typeStatus'
        mDWC[''] = 'scientificName'
        mDWC[''] = 'Dinamic properties'
        mDWC[''] = 'taxonRank'
        
        mDWC['subfamilia'] = ''
        mDWC['tribo'] = ''
        mDWC['ambiente'] = ''
        mDWC['entrada'] = ''
        mDWC['dataentrada'] = ''
        mDWC['numerocoletor'] = ''
        mDWC['minutodelatitude'] = ''
        mDWC['segundodelatitude'] = ''
        mDWC['latitudenortesul'] = ''
        mDWC['minutodelongitude'] = ''
        mDWC['segundodelongitude'] = ''
        mDWC['longitudelesteoeste'] = ''
        mDWC['nºindividuos'] = ''
        mDWC['projeto'] = ''
        mDWC['disponibilidade'] = ''
        mDWC['numeroreservado'] = ''
        mDWC['subfilo'] = ''
        mDWC['superordem'] = ''
        mDWC['superfamilia'] = ''
        mDWC['subfamilia'] = ''
        mDWC['sexo'] = ''
        mDWC['tipodecolecao'] = ''
        mDWC['hospedeiro'] = ''
        mDWC['dna'] = ''
        mDWC['pecaanatomica'] = ''
        mDWC['nous'] = ''
        mDWC['eouw'] = ''
        mDWC['regiao'] = ''
        mDWC['habito'] = ''
        mDWC['litologia'] = ''
        mDWC['ecossistema'] = ''
        mDWC['fenologia'] = ''
        mDWC['idadegeologica'] = ''
        mDWC['baciasedimentar'] = ''
        mDWC['numerodocoletor'] = ''
        mDWC['familiaantiga'] = ''
        mDWC['generoantigo'] = ''
        mDWC['epitetoantigo'] = ''
        mDWC['determinadorantigo'] = ''
        
        #mapeamentos feitos
        mDWC['filo'] = 'phylum'
        mDWC['classe'] = 'class'
        mDWC['ordem'] = 'order'
        mDWC['familia'] = 'family'
        mDWC['registro'] = 'catalogNumber'
        mDWC['observacaodoregistro'] = 'occurrenceRemarks'
        mDWC['genero'] = 'genus'
        mDWC['epiteto'] = 'specificEpithet'
        mDWC['numerodecampo'] = 'fieldNumber'
        mDWC['reino'] = 'kingdom'
        mDWC['datadedeterminacao'] = 'dateIdentified'
        mDWC['tecnicacol'] = 'samplingProtocol'
        mDWC['tipodecolecao'] = 'type'
        mDWC['observacaoreg'] = 'basisOfRecord'
        mDWC['pais'] = 'country'
        mDWC['estado'] = 'stateProvince'
        mDWC['municipio'] = 'municipality'
        mDWC['localidade'] = 'locality'
        mDWC['datacoleta'] = 'eventDate'
        mDWC['observacaocoleta'] = 'eventRemarks'
        mDWC['graudelatitude'] = 'decimalLatitude'
        mDWC['graudelongitude'] = 'decimalLongitude'
        mDWC['profundidade'] = 'verbatimDepth'
        mDWC['determinador'] = 'identifiedBy'
        mDWC['coletor'] = 'recordedBy'
        
        try:
            return mDWC[term]
        except KeyError:
            return term
            
main(stdin.readline())
