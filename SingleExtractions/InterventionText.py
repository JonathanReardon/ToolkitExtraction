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

def get_intervention_text():
    global INTERVENTIONTEXT
    INTERVENTIONTEXT = []
    for section in range(len(data["References"])):
        interventiontext_holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    interventiontext_holder.append(data["References"][section]["Outcomes"][subsection]["InterventionText"])
                else:
                    interventiontext_holder.append(exclude)
            INTERVENTIONTEXT.append(interventiontext_holder)
        else:
            for i in range(max(x)):
                interventiontext_holder.append(exclude)
            INTERVENTIONTEXT.append(interventiontext_holder)

get_intervention_text()

intervention_text_df = pd.DataFrame(INTERVENTIONTEXT)

intervention_text_df.columns=["Intervention_Text_Outcome_"+'{}'.format(column+1) for column in intervention_text_df.columns]

intervention_text_df.fillna("NA", inplace=True)

intervention_text_df.to_csv("interventiontext.csv", index=False)