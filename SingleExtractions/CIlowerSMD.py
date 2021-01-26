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

def get_CIlowerSMD():
    global CIlowerSMD
    CIlowerSMD = []
    for section in range(len(data["References"])):
        cilowerholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    cilowerholder.append(data["References"][section]["Outcomes"][subsection]["CILowerSMD"])
                else:
                    cilowerholder.append(exclude)
            CIlowerSMD.append(cilowerholder)
        else:
            for i in range(max(x)):
                cilowerholder.append(exclude)
            CIlowerSMD.append(cilowerholder)

get_CIlowerSMD()

cilowersmd_df = pd.DataFrame(CIlowerSMD)

cilowersmd_df = cilowersmd_df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

cilowersmd_df.columns=["ci_lower_"+'{}'.format(column+1) for column in cilowersmd_df.columns]

cilowersmd_df.fillna("NA", inplace=True)
cilowersmd_df = cilowersmd_df.replace(r'^\s*$', "NA", regex=True)

print(cilowersmd_df)

cilowersmd_df.to_csv("cilowersmd.csv", index=False)