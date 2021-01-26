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


def get_intervention_text():
    global INTERVENTIONTEXT
    INTERVENTIONTEXT = []
    for section in range(len(data["References"])):
        interventiontext_holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    interventiontext_holder.append(
                        data["References"][section]["Outcomes"][subsection]["InterventionText"])
                else:
                    interventiontext_holder.append(exclude)
            INTERVENTIONTEXT.append(interventiontext_holder)
        else:
            for i in range(max(x)):
                interventiontext_holder.append(exclude)
            INTERVENTIONTEXT.append(interventiontext_holder)


get_intervention_text()

outcome_measure_df = pd.DataFrame(INTERVENTIONTEXT)

outcome_measure_df.columns = [
    "out_measure_"+'{}'.format(column+1) for column in outcome_measure_df.columns]

outcome_measure_df.fillna("NA", inplace=True)
outcome_measure_df = outcome_measure_df.replace(r'^\s*$', "NA", regex=True)

print(outcome_measure_df)

outcome_measure_df.to_csv("outcome_measure.csv", index=False)
