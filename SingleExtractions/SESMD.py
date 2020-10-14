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

def get_SESMD():
    global SESMD
    SESMD = []
    for section in range(len(data["References"])):
        sesmdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    sesmdholder.append(data["References"][section]["Outcomes"][subsection]["SESMD"])
                else:
                    sesmdholder.append(exclude)
            SESMD.append(sesmdholder)
        else:
            for i in range(max(x)):
                sesmdholder.append(exclude)
            SESMD.append(sesmdholder)

get_SESMD()

sesmd_df = pd.DataFrame(SESMD)

sesmd_df = sesmd_df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

sesmd_df.columns=["SESMD_OUTCOME_"+'{}'.format(column+1) for column in sesmd_df.columns]

sesmd_df.fillna("NA", inplace=True)

sesmd_df.to_csv("sesmd.csv", index=False)