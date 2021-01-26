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


def get_outcome_description():
    global OUTCOMEDESCRIPTION
    OUTCOMEDESCRIPTION = []
    for section in range(len(data["References"])):
        outcomeIDholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomeIDholder.append(
                        data["References"][section]["Outcomes"][subsection]["OutcomeDescription"])
                else:
                    outcomeIDholder.append(exclude)
            OUTCOMEDESCRIPTION.append(outcomeIDholder)
        else:
            for i in range(max(x)):
                outcomeIDholder.append(exclude)
            OUTCOMEDESCRIPTION.append(outcomeIDholder)


get_outcome_description()

outcome_description_df = pd.DataFrame(OUTCOMEDESCRIPTION)

outcome_description_df.columns = [
    "out_desc_"+'{}'.format(column+1) for column in outcome_description_df.columns]

""" outcome_description_df = outcome_description_df.fillna("NA") """
outcome_description_df = outcome_description_df.replace(
    r'^\s*$', "NA", regex=True)

outcome_description_df.replace('\r', ' ', regex=True, inplace=True)
outcome_description_df.replace('\n', ' ', regex=True, inplace=True)
outcome_description_df.replace(':', ' ', regex=True, inplace=True)
outcome_description_df.replace(';', ' ', regex=True, inplace=True)

print(outcome_description_df[20:35])

""" outcome_description_df.to_csv("outcomedescription.csv", index=False) """
