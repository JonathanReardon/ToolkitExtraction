import os
import json
import pandas as pd

from AttributeIDList import *
from DATAFILE import file

exclude="NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data=json.load(f)

x=[]
for study in range(len(data["References"])):
    if "Outcomes" in data["References"][study]:
        x.append(len(data["References"][study]["Outcomes"]))

def get_SMD():
    global SMD
    SMD = []
    for section in range(len(data["References"])):
        smdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    smdholder.append(data["References"][section]["Outcomes"][subsection]["SMD"])
                else:
                    smdholder.append(exclude)
            SMD.append(smdholder)
        else:
            for i in range(max(x)):
                smdholder.append(exclude)
            SMD.append(smdholder)

get_SMD()

smd_df = pd.DataFrame(SMD)

smd_df = smd_df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

smd_df.columns=["SMD_Outcome_"+'{}'.format(column+1) for column in smd_df.columns]

smd_df.fillna("NA", inplace=True)

smd_df.fillna("NA", inplace=True)

smd_df.to_csv("smd.csv", index=False)