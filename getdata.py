#! /usr/bin/env python
# -*- coding: utf-8 -*-


from plotting import *
try:
    import cPickle as pickle
except ImportError:
    import pickle

import urllib
#from gluon.serializers import json
import simplejson as json
import datetime
import os

urlbase='https://www.cloudflare.com/api_json.html'
tkn='323959e52c12fffcde6433413c5e5c0b7e0f2'
email='sistemas-internet@eluniversal.com'
z='eluniversal.com'
a='stats'
interval='120'

params = urllib.urlencode({'a':a,'tkn': tkn, 'email': email, 'z': z, 'interval':interval})
f = urllib.urlopen(urlbase+"/?%s" % params)
f=json.loads(f.read())

#print f, type(f)

#print f['response']['result']
h= f['response']['result']['objs'][0]['currentServerTime']
zoncdate= datetime.datetime.fromtimestamp(h / 1e3)
trafic={}

trafic['uniq']={'Regular':f['response']['result']['objs'][0]['trafficBreakdown']['uniques']['regular'],
						'Threat':f['response']['result']['objs'][0]['trafficBreakdown']['uniques']['threat'],
						'Crawler':f['response']['result']['objs'][0]['trafficBreakdown']['uniques']['crawler'] , 
						'Date':zoncdate
						}

#si existe la leo
if os.path.isfile('data.dat'):
	fichero = file("data.dat")
	data = pickle.load(fichero)
	data['data'].append(trafic['uniq']['Regular'])
	data['label'].append(trafic['uniq']['Date'].time())
	fichero.close()	
	fichero = file("data.dat", "w")	
	pickle.dump(data , fichero, 2)
	fichero.close()
else:
	data={}
	data['data']=[]
	data['label']=[]
	data['data'].append(trafic['uniq']['Regular'])
	#print trafic['uniq']['Date'].time()
	data['label'].append(trafic['uniq']['Date'].time())
	fichero = file("data.dat", "w")	
	pickle.dump(data , fichero, 2)
	fichero.close()

#print data
x=barplot(data['label'],data['data'] )
#x.show()
x.draw()
x.savefig('barhits.jpg')

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
