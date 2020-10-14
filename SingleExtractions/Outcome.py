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

def get_outcome():
    global OUTCOME
    OUTCOME = []
    for section in range(len(data["References"])):
        outcomeholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomeholder.append(data["References"][section]["Outcomes"][subsection]["OutcomeText"])
                else:
                    outcomeholder.append(exclude)
            OUTCOME.append(outcomeholder)
        else:
            for i in range(max(x)):
                outcomeholder.append(exclude)
            OUTCOME.append(outcomeholder)

get_outcome()

outcome_df = pd.DataFrame(OUTCOME)

outcome_df.columns=["Outcome_"+'{}'.format(column+1) for column in outcome_df.columns]

outcome_df.fillna("NA", inplace=True)

outcome_df.to_csv("outcome.csv", index=False)