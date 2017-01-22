from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from random import randint
import os
import bs4


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
import random

def exactPrice(request):
    r=requests.get("http://www.vidyutpravah.in/")
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    price=soup.find_all("span",class_="counter")[12].text
    a = random.random()
    b = random.random()
    eprice = a + b + float(price)
    return HttpResponse(json.dumps({"price":eprice},indent=4))














def ideal_surplus2():

    os.chdir(r'/home/vishrut/Desktop/smartgrid/server/isgw/Smartelec')
    dataset = pd.read_csv('weather.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:,3].values
    print y
    
    

    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    from sklearn.linear_model import LinearRegression
    
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    z = [[3,4,5]]
    print z
    f = {}
    m =[]
    q = 0
    
    a = regressor.predict(z)
    


    return  a

def ideal_surplus(request):

    os.chdir(r'/home/vishrut/Desktop/smartgrid/server/isgw/Smartelec')
    # os.chdir(r'/usr/desktop/django/isgw/Smartelec')
    dataset = pd.read_csv('weather.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:,3].values
    print y
  
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    from sklearn.linear_model import LinearRegression

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)


    z = [[3,4,5]]
    print z
    f = {}
    m =[]
    q = 0
    l = regressor.predict(z)

    
    # w = numpy.concatenate((z[0], l.T))
    # print w
    # for i in w:

    #     print i
        
    #     f["%d"%q] = i
    #     q = q+1

    # print f 

    # b = ['0','1','2','3']
    # m.append(f)
    # print m 
    # # csvAdd(m,b)



    return HttpResponse(l+1)

    


def exact(request):

    # os.chdir(r'/usr/desktop/django/isgw/Smartelec')
    os.chdir(r'/home/vishrut/Desktop/smartgrid/server/isgw/Smartelec')
    dataset = pd.read_csv('testit.csv')
    X = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,1].values
   
    

    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    from sklearn.linear_model import LinearRegression

    X_train = numpy.reshape(X_train, (len(X_train),1))

    regressor = LinearRegression()

    regressor.fit(X_train, y_train)

    z = ideal_surplus2()
    print z
    f = {}
    m =[]
    q = 0
    
    a = regressor.predict(z)
    a = a+1

    print(a)

    w = numpy.concatenate((z, a.T))
    print w
    for i in w:

        print i
        
        f["%d"%q] = i
        q = q+1

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
       
        print e



from Smartelec.models import Device,User,UserTransaction
import json
import requests
from random import randint
import os



from sklearn.externals import joblib
from random import randint

import numpy 

import pandas as pd
from sklearn.externals import joblib
import csv




def deviceInfo(request):
    deviceId=request.GET.get("deviceId")

    return HttpResponse("We will be up shortly...!")

def userInfo(request):
    username=request.GET.get("name")
    user_object=User.objects.filter(name=username).values()
    print user_object
    output=json.dumps(user_object[0],indent=4)
    return HttpResponse(output,content_type="application/json")













