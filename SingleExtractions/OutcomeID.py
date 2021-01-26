import os
import json
import pandas as pd

from CODES import *
from DATAFILE import file

exclude = "NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data = json.load(f)

x = []
for study in range(len(data["References"])):
    if "Outcomes" in data["References"][study]:
        x.append(len(data["References"][study]["Outcomes"]))


def get_outcomeID():
    global OUTCOMEID
    OUTCOMEID = []
    for section in range(len(data["References"])):
        outcomeIDholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomeIDholder.append(
                        data["References"][section]["Outcomes"][subsection]["OutcomeId"])
                else:
                    outcomeIDholder.append(exclude)
            OUTCOMEID.append(outcomeIDholder)
        else:
            for i in range(max(x)):
                outcomeIDholder.append(exclude)
            OUTCOMEID.append(outcomeIDholder)


get_outcomeID()

outcome_ID_df = pd.DataFrame(OUTCOMEID)

outcome_ID_df.columns = [
    "Outcome_ID_"+'{}'.format(column+1) for column in outcome_ID_df.columns]

outcome_ID_df.fillna("NA", inplace=True)
outcome_ID_df = outcome_ID_df.replace(r'^\s*$', "NA", regex=True)

print(outcome_ID_df)

outcome_ID_df.to_csv("outcomeID.csv", index=False)
