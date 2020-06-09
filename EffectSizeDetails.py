import json
from collections import Counter
from pprint import pprint
import numpy as np
import pandas as pd

from questions import *

# input data file name (.csv) with full path
datafile = '/home/jon/json/ToolkitExtraction/Data/May12th_2020.json'

# import dataset (uncomment to select dataset of choice)
with open(datafile) as f:
    data=json.load(f)

# for missing or unavailable data
exclude="NA"

# get SMD info from 'Outcomes' section for all studies and outcomes
def get_SMD():
    global SMD
    SMD = []
    for section in range(len(data["References"])):
        smdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    smdholder.append(data["References"][section]["Outcomes"][subsection]["SMD"])
                else:
                    smdholder.append(exclude)
            SMD.append(smdholder)
        else:
            for i in range(10):
                smdholder.append(exclude)
            SMD.append(smdholder)

# get SESMD info from 'Outcomes' section for all studies and outcomes
def get_SESMD():
    global SESMD
    SESMD = []
    for section in range(len(data["References"])):
        sesmdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    sesmdholder.append(data["References"][section]["Outcomes"][subsection]["SMD"])
                else:
                    sesmdholder.append(exclude)
            SESMD.append(sesmdholder)
        else:
            for i in range(10):
                sesmdholder.append(exclude)
            SESMD.append(sesmdholder)

def get_basic_info():
    global titles, itemids
    titles, itemids = [], []
    for section in range(len(data["References"])):
        if data["References"][section]["ShortTitle"]:
            titles.append(data["References"][section]["ShortTitle"])
        else:
            titles.append(exclude)
        if data["References"][section]["ItemId"]:
            itemids.append(data["References"][section]["ItemId"])
        else:
            itemids.append(exclude)

get_basic_info()
get_SMD()
get_SESMD()

smd     = pd.DataFrame(SMD)
sesmd   = pd.DataFrame(SESMD)
titles  = pd.DataFrame(titles)
itemids = pd.DataFrame(itemids)

df = pd.concat([itemids, titles, smd, sesmd], axis=1, sort=False)

df.columns = ['ItemID', 'Author', 
              'SMD_1', 'SMD_2', 'SMD_3', 'SMD_4', 'SMD_5', 'SMD_6', 'SMD_7', 'SMD_8', 'SMD_9', 'SMD_10',
              'SESMD_1', 'SESMD_2', 'SESMD_3', 'SESMD_4', 'SESMD_5', 'SESMD_6', 'SESMD_7', 'SESMD_8', 'SESMD_9', 'SESMD_10']

df = df[['ItemID', 'Author', 
         'SMD_1', 'SESMD_1', 'SMD_2', 'SESMD_2', 'SMD_3', 'SESMD_3', 'SMD_4','SESMD_4',
         'SMD_5', 'SESMD_5', 'SMD_6', 'SESMD_6', 'SMD_7', 'SESMD_7', 'SMD_8', 'SESMD_8',
         'SMD_9', 'SESMD_9',  'SMD_10', 'SESMD_10']]


df = df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)
""" df.fillna("NA") """
df.to_csv("SMDandSESMD.csv", index=False)

