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
    files = str(file).split('.')
    #chama o shell e converte planilha para csv
    args = '{0} {1}.csv'.format(file, files[0])
    argument = 'ssconvert {0}'.format(args)
    command_process = subprocess.call([argument], shell=True)
    outputFile = '{0}-CONVERTIDO.csv'.format(files[0])
    ofile  = open(outputFile, "wb")#open('final.csv', "wb")
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

def mapDWC(term):
        term = str(term).lower().replace(' ','')
        mDWC = dict()

        #mapeamentos por fazer
        mDWC[''] = 'minimumElevationInMeters'
        mDWC[''] = 'maximumElevationInMeters'
        mDWC[''] = 'type'
        mDWC[''] = 'modified'
        mDWC[''] = 'language'
        mDWC[''] = 'license'
        mDWC[''] = 'rightsHolder'
        mDWC[''] = 'institutionID'
        mDWC[''] = 'institutionCode'
        mDWC[''] = 'collectionCode'
        mDWC[''] = 'datasetName'
        mDWC[''] = 'occurrenceID'
        mDWC[''] = 'preparations'
        mDWC[''] = 'countryCode'
        mDWC[''] = 'minimumDepthInMeters'
        mDWC[''] = 'maximumDepthInMeters'
        mDWC[''] = 'locationRemarks'
        mDWC[''] = 'georeferencedBy'
        mDWC[''] = 'georeferencedDate'
        mDWC[''] = 'georeferenceProtocol'
        mDWC[''] = 'typeStatus'
        mDWC[''] = 'scientificName'
        mDWC[''] = 'taxonRank'
        mDWC['idadegeologica'] = ''
        mDWC['minutodelatitude'] = ''
        mDWC['segundodelatitude'] = ''
        mDWC['latitudenortesul'] = ''
        mDWC['minutodelongitude'] = ''
        mDWC['segundodelongitude'] = ''
        mDWC['longitudelesteoeste'] = ''
        #mapeamentos feitos
        mDWC['subfamilia'] = 'dynamicProperties'
        mDWC['tribo'] = 'dynamicProperties'
        mDWC['ambiente'] = 'habitat'
        mDWC['entrada'] = 'dynamicProperties'
        mDWC['dataentrada'] = 'dynamicProperties'
        mDWC['numerocoletor'] = 'dynamicProperties'
        mDWC['nºindividuos'] = 'individualCount'
        mDWC['projeto'] = 'METADADOS'
        mDWC['disponibilidade'] = 'dynamicProperties'
        mDWC['numeroreservado'] = 'dynamicProperties'
        mDWC['subfilo'] = 'dynamicProperties'
        mDWC['superordem'] = 'dynamicProperties'
        mDWC['superfamilia'] = 'dynamicProperties'
        mDWC['sexo'] = 'sex'
        mDWC['tipodecolecao'] = 'dynamicProperties'
        mDWC['hospedeiro'] = 'associatedTaxa'
        mDWC['dna'] = 'associatedSequence'
        mDWC['pecaanatomica'] = 'dynamicProperties'
        mDWC['nous'] = 'dynamicProperties'
        mDWC['eouw'] = 'dynamicProperties'
        mDWC['regiao'] = 'locality'
        mDWC['habito'] = 'habitat'
        mDWC['litologia'] = 'dynamicProperties'
        mDWC['ecossistema'] = 'dynamicProperties'
        mDWC['fenologia'] = 'dynamicProperties'
        mDWC['baciasedimentar'] = 'dynamicProperties'
        mDWC['numerodocoletor'] = 'dynamicProperties'
        mDWC['familiaantiga'] = 'dynamicProperties'
        mDWC['generoantigo'] = 'dynamicProperties'
        mDWC['epitetoantigo'] = 'dynamicProperties'
        mDWC['determinadorantigo'] = 'dynamicProperties'
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
        mDWC['tipodecolecao'] = 'dynamicProperties'
        mDWC['observacaoreg'] = 'basisOfRecord'
        mDWC['continente'] = 'continent'
        mDWC['pais'] = 'country'
        mDWC['estado'] = 'stateProvince'
        mDWC['municipio'] = 'county'
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
