#Importamos las librerias
from bs4 import BeautifulSoup
import requests
import urllib
import httplib
import json

#reemplazar espacio por +
calle = raw_input("Ingrese Calle: ")
calle = calle.replace(" ", "+")
numero= raw_input("Ingrese # : ")
comuna = raw_input("Ingrese Comuna: ")

# Pagina
link       = "http://www.correos.cl/SitePages/codigo_postal/codigo_postal.aspx?calle="+calle+"&numero="+numero+"&comuna="+comuna+'"'
host       = "www.correos.cl"
parametros = urllib.urlencode({"calle":"","numero":"","comuna":""})
headers    = {
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
"Content-type": "application/x-www-form-urlencoded",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://www.correos.cl/SitePages/codigo_postal/codigo_postal.aspx?",
"Cookie":"__utma=30439597.1199029372.1476733240.1477418931.1477504384.3; __utmz=30439597.1476733240.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=30439597; __utmb=30439597.2.10.1477504384; __utmt=1"
}

conexion   = httplib.HTTPConnection(host)
conexion.request("POST", link, parametros, headers)
respuesta  = conexion.getresponse()
ver_source = respuesta.read()
if respuesta.status == 200:
	#Pagina web ver_source
	soup = BeautifulSoup(ver_source, 'lxml')
	e = soup.find_all('span',{'id':'ctl00_PlaceHolderMain_g_78a5f193_c1ad_4599_b57b_b321c2ff5f9f_ctl00_lblDireccionCompleta'})
	f = soup.find_all('span',{"id":"ctl00_PlaceHolderMain_g_78a5f193_c1ad_4599_b57b_b321c2ff5f9f_ctl00_lblCodigoPostal"})
	print "El codigo postal de ", e[0].text,", ","Es : ", f[0].text
