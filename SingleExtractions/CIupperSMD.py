import os
import json
import pandas as pd

from CODES import *
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

def get_CIupperSMD():
    global CIupperSMD
    CIupperSMD = []
    for section in range(len(data["References"])):
        ciupperholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    ciupperholder.append(data["References"][section]["Outcomes"][subsection]["CIUpperSMD"])
                else:
                    ciupperholder.append(exclude)
            CIupperSMD.append(ciupperholder)
        else:
            for i in range(max(x)):
                ciupperholder.append(exclude)
            CIupperSMD.append(ciupperholder)

get_CIupperSMD()

ciuppersmd_df = pd.DataFrame(CIupperSMD)

ciuppersmd_df = ciuppersmd_df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

ciuppersmd_df.columns=["CI_upper_Outcome_"+'{}'.format(column+1) for column in ciuppersmd_df.columns]

ciuppersmd_df.fillna("NA", inplace=True)

""" print(ciuppersmd_df) """

""" ciuppersmd_df.to_csv("ciuppersmd.csv", index=False) """