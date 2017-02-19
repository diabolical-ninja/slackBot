"""
Title:  metric_runner
Desc:   Contains the functions which calculate the various metrics
Author: Yassin Eltahir
Date:   2017-02-19
"""

import pandas as pd
import yaml
import pyodbc

# Source Config
conf = yaml.load(open('conf.eyaml','r'))

# # Connect to DB
# server = conf['database']['server']
# cnxn = pyodbc.connect("DRIVER={SQL SERVER};SERVER={" + server + "}")



class metricFunctions:
    '''
    Contains all functions which calculate metrics based on user question
    Returns a dictionary with all callable functions
    '''  
        
    def conversion(vertical, datetime):
        '''
        Calculates conversion for the provided verticals & timeframes
        '''
        response = "Sorry, I haven't been taught how to calculate this yet"
        return response
        
    
    def contactRate(vertical, datetime):
        response = "Sorry, I haven't been taught how to calculate this yet"
        return response
    
    def connectRate(vertical, datetime):
        response = "Sorry, I haven't been taught how to calculate this yet"
        return response
    
    def auc(vertical, datetime):
        response = "Sorry, I haven't been taught how to calculate this yet"
        return response
    
    
    funcDict = {
                 "conversion":conversion,
                 "contact rate":contactRate,
                 "connect rate":connectRate,
                 "auc":auc
                 }

