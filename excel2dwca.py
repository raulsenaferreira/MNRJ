# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:13:17 2015

@author: Raul
"""

from __future__ import absolute_import, division, print_function
import sys
import subprocess
#from util import Util
#from pprint import pprint as pp
import csv # imports the csv module

def main():
    #parametro file contem nome do arquivo original e sua extensao
    file=sys.argv[1]
    files = str(file).split('.')
    #chama o shell e converte planilha para csv
    argument = 'ssconvert {0} {1}.csv'.format(file, files[0])

    command_process = subprocess.call([argument], shell=True)

    outputFile = '{0}-CONVERTIDO.csv'.format(files[0])
    ofile  = open(outputFile, "wb")#open('final.csv', "wb")
    writer = csv.writer(ofile, delimiter=',')

    arg = '{0}.csv'.format(files[0])
    f = open(arg, 'rb')#open("result.csv", 'rb') # opens the csv file

    m={}
    header=True

    try:
        reader = csv.reader(f)  # creates the reader object
        for row in reader:   # iterates the rows of the file in orders
            if header is True:
                header = False
                hasLat = False
                hasLng = False
                hasEventDate = False

                for i in range(0, len(row)):
                    row[i] = mapDWC(row[i])

                    if row[i] == 'decimalLatitude':
                        hasLat = True
                    if row[i] == 'decimalLongitude':
                        hasLng = True
                    if row[i] == 'eventDate':
                        hasEventDate = True

                    #latitude
                    if row[i] == 'graudelatitude':
                        m['grauLat'] = i
                    elif row[i] == 'minutodelatitude':
                        m['minLat'] = i
                    elif row[i] == 'segundodelatitude':
                        m['segLat'] = i
                    elif row[i] == 'latitudenortesul' or 'nous':
                        m['latNS'] = i
                    #longitude
                    elif row[i] == 'graudelongitude':
                        m['grauLong'] = i
                        hasLng = True
                    elif row[i] == 'minutodelongitude':
                        m['minLong'] = i
                    elif row[i] == 'segundodelongitude':
                        m['segLong'] = i
                    elif row[i] == 'longitudelesteoeste' or 'eouw':
                        m['longLO'] = i
                    #data
                    elif row[i] == 'year':
                        m['dateYear'] = i
                    elif row[i] == 'month':
                        m['dateMonth'] = i
                    elif row[i] == 'day':
                        m['dateDay'] = i

                if hasLat == False:
                    row+=['decimalLatitude']
                if hasLng == False:
                    row+=['decimalLongitude']
                if hasEventDate == False:
                    row+=['eventDate']

            else:
                degLatitude=(row[m['grauLat']], row[m['minLat']], row[m['segLat']], row[m['latNS']])
                degLongitude=(row[m['grauLong']], row[m['minLong']], row[m['segLong']], row[m['longLO']])

                row['decimalLatitude'], row['decimalLongitude'] = convertDegreeToLatLong(degLatitude, degLongitude)

                fullDate = '{0}/{1}/{2}'.format(row[m['dateYear']], row[m['dateMonth']], row[m['dateDay']])
                row['eventDate'] = fullDate
            writer.writerow(row)    # prints each row
    finally:
        f.close()
        return True

def mapDWC(term):
        term = str(term).lower().replace(' ','')
        mDWC = dict()

        #mapeamentos por fazer
        '''
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
        mDWC['graudelatitude'] = ''
        mDWC['minutodelatitude'] = ''
        mDWC['segundodelatitude'] = ''
        mDWC['latitudenortesul'] = ''
        mDWC['graudelongitude'] = ''
        mDWC['minutodelongitude'] = ''
        mDWC['segundodelongitude'] = ''
        mDWC['longitudelesteoeste'] = ''
        '''
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
        mDWC['profundidade'] = 'verbatimDepth'
        mDWC['determinador'] = 'identifiedBy'
        mDWC['coletor'] = 'recordedBy'

        try:
            return mDWC[term]
        except KeyError:
            return term

def convertDegreeToLatLong(degLat, degLng):
    #latitude
    lat = int(degLat[0]) + float(degLat[1]) / 60 + float(degLat[2]) / 3600
    if degLat[3]=='S':
        lat*=-1
    #longitude
    lng = int(degLng[0]) + float(degLng[1]) / 60 + float(degLng[2]) / 3600
    if degLng[3]=='W':
        lng*=-1

    return (lat, lng)


main()
