# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:17:15 2015

@author: raul
"""
def main():
    degLat = ('45', '32', '25', 'N')
    degLng = ('129', '40', '31', 'W')
    lat, lng = converte(degLat, degLng)
    print(lat)
    print(lng)

def converte(degLat, degLng):
    lat = int(degLat[0]) + float(degLat[1]) / 60 + float(degLat[2]) / 3600
    if degLat[3]=='S':
        lat*=-1

    lng = int(degLng[0]) + float(degLng[1]) / 60 + float(degLng[2]) / 3600
    if degLng[3]=='W':
        lng*=-1

    return (lat, lng)

main()
