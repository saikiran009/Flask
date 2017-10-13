# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:41:45 2016

@author: Sai Kiran
"""

from flask import Flask,make_response
from werkzeug.exceptions import ServiceUnavailable
import requests
import json
app = Flask(__name__)

'''To get the proper json'''
def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response
new_dict = {} 


'''Get the numbers from service 8081 and do the bakend analysis what you wanna do with those(in this case it's simple judging type of numbers: even or odd'''
@app.route('/display',methods= ['GET'])
def display():
    try:
        numbers= requests.get("http://127.0.0.1:8081/number")        
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("No link")    
    numbers = numbers.json()
    string = json.dumps(numbers)
    numbers = json.loads(string)
    data =[]
    for k in numbers['number']:
        data.append(int(k))
    numbers_list = data   
    even_number = []
    odd_number =[]
    for k in numbers_list :
        if k %2 == 0:
            even_number.append(k)
        else:
            odd_number.append(k)
    numbers1 = {'even_numbers': even_number,'odd_numbers': odd_number}   
    return json.dumps(numbers1)

'''Return the computed result to the port 8081'''
def t_input():
    answer = display()
    r = requests.post("http://127.0.0.1:8081/return",data = json.dumps(answer))
    return r.json()
t_input()
  
if __name__ == '__main__' :
    app.run(port = 8080,debug = True)
