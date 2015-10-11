# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:17:15 2015

@author: raul
"""


class Util(object):
    
    def mapDWC(term):
        mDWC = dict()
        mDWC['filo'] = 'phylum'
        mDWC['classe'] = 'class'
        mDWC['ordem'] = 'order'
        mDWC['familia'] = 'family'
        mDWC['subfamilia'] = ''
        mDWC['tribo'] = ''
        mDWC['genero'] = 'genus'
        mDWC['epiteto'] = 'specificEpithet'
        mDWC['numerodecampo'] = 'fieldNumber'
        mDWC['ambiente'] = ''
        mDWC['datadedeterminacao'] = 'dateIdentified'
        mDWC['entrada'] = ''
        mDWC['dataentrada'] = ''
        mDWC['tecnicacol'] = 'samplingProtocol'
        mDWC['tipodecolecao'] = 'type'
        mDWC['observacaoreg'] = 'basisOfRecord'
        mDWC['pais'] = 'country'
        mDWC['estado'] = 'stateProvince'
        mDWC['municipio'] = 'municipality'
        mDWC['localidade'] = 'locality'
        mDWC['numerocoletor'] = ''
        mDWC['datacoleta'] = 'eventDate'
        mDWC['observacaocoleta'] = 'eventRemarks'
        mDWC['graudelatitude'] = 'decimalLatitude'
        mDWC['minutodelatitude'] = ''
        mDWC['segundodelatitude'] = ''
        mDWC['latitudenortesul'] = ''
        mDWC['graudelongitude'] = 'decimalLongitude'
        mDWC['minutodelongitude'] = ''
        mDWC['segundodelongitude'] = ''
        mDWC['longitudelesteoeste'] = ''
        mDWC['profundidade'] = 'verbatimDepth'
        mDWC['nºindividuos'] = ''
        mDWC['determinador'] = 'identifiedBy'
        mDWC['coletor'] = 'recordedBy'
        mDWC['projeto'] = ''
        
        try:
            return mDWC[term]
        except KeyError:
            return term
