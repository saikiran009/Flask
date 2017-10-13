# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:39:20 2016

@author: Sai Kiran
"""

from flask import Flask
from flask import make_response,request,jsonify
from werkzeug.exceptions import ServiceUnavailable
import json
import requests
'''Used to create a proper Json if user gives input from UI '''
def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response
app = Flask(__name__)
   

'''Takes inpput '''
@app.route('/number',methods = ['GET'])
def get_input():
    numbers = {'number' :['1','2','0','34623','899','80']}
    print numbers
    return nice_json(numbers)


'''Returns the output from other service 8080'''
@app.route('/return',methods = ['POST'])
def resultt():
    input_json = request.get_json(force=True) 
    
    print 'data from client:', input_json
   
    return jsonify(input_json )
    
if __name__ == '__main__' :
    app.run(port = 8081,debug = True)