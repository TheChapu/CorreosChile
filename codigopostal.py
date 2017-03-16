# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import urllib
import httplib
import json
#RH352992401CN
#ALS00359081
# Pagina
link       = "http://seguimientoweb.correos.cl/ConEnvCorreos.aspx"
host       = "seguimientoweb.correos.cl"
parametros = urllib.urlencode({"obj_key":"Cor398-cc","obj_env":"RH352992401CN"})
headers    = {
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
"Content-type": "application/x-www-form-urlencoded",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://www.correos.cl/SitePages/seguimiento/seguimiento.aspx?",
"Cookie":"__utma=30439597.1199029372.1476733240.1476733240.1477418931.2; __utmz=30439597.1476733240.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=30439597.2.10.1477418931; __utmc=30439597; __utmt=1"
}

conexion   = httplib.HTTPConnection(host)
conexion.request("POST", link, parametros, headers)
respuesta  = conexion.getresponse()
ver_source = respuesta.read()
data = []


if respuesta.status == 200:
	soup = BeautifulSoup(ver_source, 'html5lib')
	rows = soup.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		data.append([ele for ele in cols if ele])


for x in range(0,len(data)):
	print data[x]
	#Aqui falta un poco de orden
	#for i in range(0,len(data[x])):
		#print data[x][i]
