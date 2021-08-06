#! /usr/bin/python3
import urllib.request
import json
import sys 
from datetime import datetime

def iss_location():
	url= "http://api.open-notify.org/iss-now.json"
	myReq=urllib.request.Request(url)
	page=urllib.request.urlopen(myReq).read()
	data=json.loads(page.decode('utf-8'))
	return "Current Location of ISS:\n" + "Latitude: " + (data['iss_position']['latitude']) + "\n" + "Longitude: " + (data['iss_position']['longitude'])

print(iss_location())


def people_info():
	url3="http://api.open-notify.org/astros.json"
	infoReq=urllib.request.Request(url3)
	infoPage=urllib.request.urlopen(infoReq).read()
	infoData=json.loads(infoPage.decode('utf-8'))
	names=""
	for naam in range(0 ,len(infoData['people'])):
		names= names + infoData['people'][naam]['name'] + "\n" 
	return  "People currently in space: " + str(len(infoData['people'])) + "\n"+   names

print(people_info())

def pass_time():
    url2="http://api.open-notify.org/iss-pass.json?lat=45.0&lon=-122.3"
    passReq=urllib.request.Request(url2)
    passPage=urllib.request.urlopen(passReq).read()
    passData=json.loads(passPage.decode('utf-8'))
    print ("Enter Details to know when ISS will pass over a location:")
    ltd=float(input("Latitude : "))
    lgd=float(input("Longitude : "))
    if (float(passData['request']['latitude'])==ltd and float(passData['request']['longitude'])==lgd):
         return "Date : " + str(datetime.utcfromtimestamp(passData['request']['datetime']).strftime('%d/%m/%Y')) + "\nTime : " + str(datetime.utcfromtimestamp(passData['request']['datetime']).strftime('%H:%M:%S'))

print(pass_time())    
