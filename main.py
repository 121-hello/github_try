# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:33:47 2021

@author: 86188
"""
import os
from fastapi import FastAPI
from flask import jsonify
#from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()

from fastapi import FastAPI
app = FastAPI()



@app.get("/")
def read_root():
    os.system('python insert_sql.py')
    records="{\"result\":true,\"info\":\"Login Success\"}"
    return records

#records="successCallback(" + {'msg': 'ok'} + ")" 
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    




