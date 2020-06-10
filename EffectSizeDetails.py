import json
from collections import Counter
from pprint import pprint
import pandas as pd
import numpy as np
import os

# input data file name (.csv) with full path
""" datafile = '/home/jon/json/ToolkitExtraction/Data/May12th_2020.json' """

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, "May12th_2020.json")

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
                    sesmdholder.append(data["References"][section]["Outcomes"][subsection]["SESMD"])
                else:
                    sesmdholder.append(exclude)
            SESMD.append(sesmdholder)
        else:
            for i in range(10):
                sesmdholder.append(exclude)
            SESMD.append(sesmdholder)

# get CIupperSMD info from 'Outcomes' section for all studies and outcomes
def get_CIupperSMD():
    global CIupperSMD
    CIupperSMD = []
    for section in range(len(data["References"])):
        ciupperholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    ciupperholder.append(data["References"][section]["Outcomes"][subsection]["CIUpperSMD"])
                else:
                    ciupperholder.append(exclude)
            CIupperSMD.append(ciupperholder)
        else:
            for i in range(10):
                ciupperholder.append(exclude)
            CIupperSMD.append(ciupperholder)

# get CIlowerSMD info from 'Outcomes' section for all studies and outcomes
def get_CIlowerSMD():
    global CIlowerSMD
    CIlowerSMD = []
    for section in range(len(data["References"])):
        cilowerholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    cilowerholder.append(data["References"][section]["Outcomes"][subsection]["CILowerSMD"])
                else:
                    cilowerholder.append(exclude)
            CIlowerSMD.append(cilowerholder)
        else:
            for i in range(10):
                cilowerholder.append(exclude)
            CIlowerSMD.append(cilowerholder)

# get Outcome (primary/secondary) info from 'Outcomes' section for all studies and outcomes
def get_Outcome():
    global Outcome
    Outcome = []
    for section in range(len(data["References"])):
        outcomeholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomeholder.append(data["References"][section]["Outcomes"][subsection]["OutcomeText"])
                else:
                    outcomeholder.append(exclude)
            Outcome.append(outcomeholder)
        else:
            for i in range(10):
                outcomeholder.append(exclude)
            Outcome.append(outcomeholder)

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
get_CIupperSMD()
get_CIlowerSMD()
get_Outcome()

smd     = pd.DataFrame(SMD)
sesmd   = pd.DataFrame(SESMD)
titles  = pd.DataFrame(titles)
itemids = pd.DataFrame(itemids)
ciupper = pd.DataFrame(CIupperSMD)
cilower = pd.DataFrame(CIlowerSMD)
outcome = pd.DataFrame(Outcome)

df = pd.concat([itemids, titles, smd, sesmd, ciupper, cilower, outcome], axis=1, sort=False)

df.columns = ['ItemID', 'Author', 
              'SMD_1', 'SMD_2', 'SMD_3', 'SMD_4', 'SMD_5', 'SMD_6', 'SMD_7', 'SMD_8', 'SMD_9', 'SMD_10',
              'SESMD_1', 'SESMD_2', 'SESMD_3', 'SESMD_4', 'SESMD_5', 'SESMD_6', 'SESMD_7', 'SESMD_8', 'SESMD_9', 'SESMD_10',
              'CIupperSMD_1', 'CIupperSMD_2', 'CIupperSMD_3', 'CIupperSMD_4', 'CIupperSMD_5', 'CIupperSMD_6', 'CIupperSMD_7', 'CIupperSMD_8', 'CIupperSMD_9', 'CIupperSMD_10',
              'CIlowerSMD_1', 'CIlowerSMD_2', 'CIlowerSMD_3', 'CIlowerSMD_4', 'CIlowerSMD_5', 'CIlowerSMD_6', 'CIlowerSMD_7', 'CIlowerSMD_8', 'CIlowerSMD_9', 'CIlowerSMD_10',
              'Outcome_1', 'Outcome_2', 'Outcome_3', 'Outcome_4', 'Outcome_5', 'Outcome_6', 'Outcome_7', 'Outcome_8', 'Outcome_9', 'Outcome_10']

df = df[['ItemID', 'Author', 
         'Outcome_1', 'SMD_1', 'SESMD_1', 'CIupperSMD_1', 'CIlowerSMD_1', 
         'Outcome_2', 'SMD_2', 'SESMD_2', 'CIupperSMD_2', 'CIlowerSMD_2', 
         'Outcome_3', 'SMD_3', 'SESMD_3', 'CIupperSMD_3', 'CIlowerSMD_3', 
         'Outcome_4', 'SMD_4', 'SESMD_4', 'CIupperSMD_4', 'CIlowerSMD_4', 
         'Outcome_5', 'SMD_5', 'SESMD_5', 'CIupperSMD_5', 'CIlowerSMD_5', 
         'Outcome_6', 'SMD_6', 'SESMD_6', 'CIupperSMD_6', 'CIlowerSMD_6', 
         'Outcome_7', 'SMD_7', 'SESMD_7', 'CIupperSMD_7', 'CIlowerSMD_7', 
         'Outcome_8', 'SMD_8', 'SESMD_8', 'CIupperSMD_8', 'CIlowerSMD_8', 
         'Outcome_9', 'SMD_9', 'SESMD_9', 'CIupperSMD_9', 'CIlowerSMD_9', 
         'Outcome_10', 'SMD_10', 'SESMD_10', 'CIupperSMD_10', 'CIlowerSMD_10']]

df = df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

idx = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_2"] == 'Primary outcome'))

df.loc[idx,['SMD_1', 'SMD_2']] = df.loc[idx,['SMD_2', 'SMD_1']].values
df.loc[idx,['SESMD_1', 'SESMD_2']] = df.loc[idx,['SESMD_2', 'SESMD_1']].values
df.loc[idx,['CIupperSMD_1', 'CIupperSMD_2']] = df.loc[idx,['CIupperSMD_2', 'CIupperSMD_1']].values
df.loc[idx,['CIlowerSMD_1', 'CIlowerSMD_2']] = df.loc[idx,['CIlowerSMD_2', 'CIlowerSMD_1']].values
df.loc[idx,['Outcome_1', 'Outcome_2']] = df.loc[idx,['Outcome_2', 'Outcome_1']].values

df.to_csv("EffectSizeDetails_SWAPPED.csv", index=False)

