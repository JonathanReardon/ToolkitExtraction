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

# get stats info from 'Outcomes' section
def get_SMD():
    global SMD
    SMD = []
    for section in range(len(data["References"])):
        smdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(7):
                if subsection < len(data["References"][section]["Outcomes"]):
                    smdholder.append(data["References"][section]["Outcomes"][subsection]["SMD"])
                else:
                    smdholder.append(exclude)
            SMD.append(smdholder)
        else:
            for i in range(7):
                smdholder.append(exclude)
            SMD.append(smdholder)

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

smd     = pd.DataFrame(SMD)
titles  = pd.DataFrame(titles)
itemids = pd.DataFrame(itemids)

df = pd.concat([itemids, titles, smd], axis=1, sort=False)

df.columns = ['ItemID', 'Title', 'SMD_1', 'SMD_2', 'SMD_3', 'SMD_4', 'SMD_5', 'SMD_6', 'SMD_7']
df.to_csv("test.csv", index=False)

