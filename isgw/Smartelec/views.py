from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from random import randint
import os


# Create your views here.
from sklearn.externals import joblib
from random import randint

import numpy 
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.externals import joblib
import sqlite3
import io
import csv








def datagerator2():
    sunlight = randint(1,5)
    wind = randint(1,12)
    tidal = randint(1,7)
    
    X = [[sunlight , wind , tidal]]
    
    return  X    

def datagerator(request):

    X = datagerator2()

    
    return  HttpResponse(X)

def  realgenerator2():
    ideal_data = datagerator2()
    wind = ideal_data[0][1]
    wind = randint(30,30*wind)
    sunlight = randint(100,220)
    hydro = randint(100,200)
    
    
    
    #daily consumption is 10k
    coal = 10000- (20*sunlight) - (10*wind) - (10*hydro)
    if coal>=6000:
        
    
        nrate  = (coal * 6)/10000
                
        exact_rate = 0.3 + 0.3 + nrate 
        print("hihihihihihihhi" + str(exact_rate))
        
        print("here we return" +str(exact_rate))
        return  str(exact_rate)

        
    else:

        return realgenerator2()


def  realgenerator(request):
	
	Y = realgenerator2()
	print("hihihihihihihihi" + Y)

	return  HttpResponse(Y)






# def saving():
# 	os.chdir(r'/home/vishrut/Desktop/server/isgw/Smartelec')
# 	dataset = pd.read_csv('weather.csv')
# 	X = dataset.iloc[:, :-1].values
# 	y = dataset.iloc[:,3].values

# 	from sklearn.cross_validation import train_test_split
# 	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# 	from sklearn.linear_model import LinearRegression
# 	# print X_train.shape
# 	# print y_train
# 	regressor = LinearRegression()
# 	regressor.fit(X_train, y_train)
# 	joblib.dump(regressor, 'filename.pkl') 

# 	return (X_train, y_train)	






def ideal_surplus2():

	os.chdir(r'/home/vishrut/Desktop/final/server/isgw/Smartelec')
	dataset = pd.read_csv('weather.csv')
	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:,3].values
	print y
	# y = numpy.reshape(y, (19,1))
	# X = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = X , axis = 1)
	# print y.shape
	# y = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = y , axis = 1)

	

	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
	from sklearn.linear_model import LinearRegression
	# print X_train.shape
	# print y_train
	regressor = LinearRegression()
	regressor.fit(X_train, y_train)

	
	# joblib.dump(regressor, 'filename.pkl') 
	# regressor2 = joblib.load('filename.pkl')

	z = datagerator2()
	print z
	f = {}
	m =[]
	q = 0
	
	a = regressor.predict(z[0])
	# X_train = numpy.append(arr = z[0] ,values = X_train )
	# y_train = numpy.append(arr = a , values = y_train)



	return  a

def ideal_surplus(request):

	os.chdir(r'/home/vishrut/Desktop/final/server/isgw/Smartelec')
	dataset = pd.read_csv('weather.csv')
	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:,3].values
	print y
	# y = numpy.reshape(y, (19,1))
	# X = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = X , axis = 1)
	# print y.shape
	# y = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = y , axis = 1)

	

	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
	from sklearn.linear_model import LinearRegression
	# print X_train.shape
	# print y_train
	regressor = LinearRegression()
	regressor.fit(X_train, y_train)

	
	# joblib.dump(regressor, 'filename.pkl') 
	# regressor2 = joblib.load('filename.pkl')

	z = datagerator2()
	print z
	f = {}
	m =[]
	q = 0
	
	a = regressor.predict(z[0])

	
	w = numpy.concatenate((z[0], a.T))
	print w
	for i in w:

		print i
		
		f["%d"%q] = i
		q = q+1
		# m.append(f)
		# print f
	print f	

	b = ['0','1','2','3']
	m.append(f)
	print m	
	csvAdd(m,b)


	return HttpResponse(a)

	


def exact(request):

	os.chdir(r'/home/vishrut/Desktop/final/server/isgw/Smartelec')
	dataset = pd.read_csv('testit.csv')
	X = dataset.iloc[:,:-1].values
	y = dataset.iloc[:,1].values
	# y = numpy.reshape(y, (19,1))
	# X = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = X , axis = 1)

	# y = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = y , axis = 1)

	

	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
	from sklearn.linear_model import LinearRegression
	# print "chal gaya"
	X_train = numpy.reshape(X_train, (len(X_train),1))
	# print X_train.shape
	# print y_train
	regressor = LinearRegression()
	# y = numpy.reshape(y, (19,1))
	regressor.fit(X_train, y_train)

	
	# joblib.dump(regressor, 'filename.pkl') 
	# regressor2 = joblib.load('filename.pkl')

	z = ideal_surplus2()
	print z
	f = {}
	m =[]
	q = 0
	
	a = regressor.predict(z)
	# X_train = numpy.append(arr = z[0] ,values = X_train )
	# y_train = numpy.append(arr = a , values = y_train)
	print(a)

	w = numpy.concatenate((z, a.T))
	print w
	for i in w:

		print i
		
		f["%d"%q] = i
		q = q+1
		# m.append(f)
		# print f
	print f	

	b = ['0','1']
	m.append(f)
	print m	
	csvAdd(m,b)

	return HttpResponse(a)



def csvAdd(dict_data,columns):
    try:
        with open('testit.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=columns)
            for data in dict_data:
                writer.writerow(data)
                





    except  Exception as e:
        #print inspect.stack()
        print e



from Smartelec.models import Device,User,UserTransaction
import json
import requests
from random import randint
import os


# Create your views here.
from sklearn.externals import joblib
from random import randint

import numpy 
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.externals import joblib
import csv



# Create your views here.

def deviceInfo(request):
	deviceId=request.GET.get("deviceId")

	return HttpResponse("We will be up shortly...!")

def userInfo(request):
	username=request.GET.get("name")
	user_object=User.objects.filter(name=username).values()
	print user_object
	output=json.dumps(user_object[0],indent=4)
	return HttpResponse(output,content_type="application/json")



<<<<<<< HEAD


def datagerator2():
    sunlight = randint(1,5)
    wind = randint(1,12)
    tidal = randint(1,7)
    
    X = [[sunlight , wind , tidal]]
    
    return  X    

def datagerator(request):

    X = datagerator2()

    
    return  HttpResponse(X)

def  realgenerator2():
    ideal_data = datagerator2()
    wind = ideal_data[0][1]
    wind = randint(30,30*wind)
    sunlight = randint(100,220)
    hydro = randint(100,200)
    
    
    
    #daily consumption is 10k
    coal = 10000- (20*sunlight) - (10*wind) - (10*hydro)
    if coal>=6000:
        
    
        nrate  = (coal * 6)/10000
                
        exact_rate = 0.3 + 0.3 + nrate 
        print("hihihihihihihhi" + str(exact_rate))
        
        print("here we return" +str(exact_rate))
        return  str(exact_rate)

        
    else:

        return realgenerator2()


def  realgenerator(request):
	
	Y = realgenerator2()
	print("hihihihihihihihi" + Y)

	return  HttpResponse(Y)






# def saving():
# 	os.chdir(r'/home/vishrut/Desktop/server/isgw/Smartelec')
# 	dataset = pd.read_csv('weather.csv')
# 	X = dataset.iloc[:, :-1].values
# 	y = dataset.iloc[:,3].values

# 	from sklearn.cross_validation import train_test_split
# 	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# 	from sklearn.linear_model import LinearRegression
# 	# print X_train.shape
# 	# print y_train
# 	regressor = LinearRegression()
# 	regressor.fit(X_train, y_train)
# 	joblib.dump(regressor, 'filename.pkl') 

# 	return (X_train, y_train)	






def ideal_rate(request):

	os.chdir(r'/usr/desktop/django/isgw/Smartelec')
	dataset = pd.read_csv('weather.csv')
	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:,3].values
	print y.shape
	# y = numpy.reshape(y, (19,1))
	# X = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = X , axis = 1)
	# print y.shape
	# y = numpy.append(arr = numpy.ones((19,1)).astype(int)  , values = y , axis = 1)

	

	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
	from sklearn.linear_model import LinearRegression
	# print X_train.shape
	# print y_train
	regressor = LinearRegression()
	regressor.fit(X_train, y_train)

	
	# joblib.dump(regressor, 'filename.pkl') 
	# regressor2 = joblib.load('filename.pkl')

	z = datagerator2()
	print z
	f = {}
	m =[]
	q = 0
	
	a = regressor.predict(z[0])
	# X_train = numpy.append(arr = z[0] ,values = X_train )
	# y_train = numpy.append(arr = a , values = y_train)
	print(a)
	w = numpy.concatenate((z[0], a.T))
	print w
	for i in w:

		print i
		
		f["%d"%q] = i
		q = q+1
		# m.append(f)
		# print f
	print f	

	b = ['0','1','2','3']
	m.append(f)
	print m	
	csvAdd(m,b)
	return  HttpResponse(a)

	





def csvAdd(dict_data,columns):
    try:
        with open('weather.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=columns)
            for data in dict_data:
                writer.writerow(data)
                print data





    except  Exception as e:
        #print inspect.stack()
        print e




=======
>>>>>>> 372453d2999a244ac536ba8d5ba0e6dca286fb87
