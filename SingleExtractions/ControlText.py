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

def get_control_text():
    global CONTROLTEXT
    CONTROLTEXT = []
    for section in range(len(data["References"])):
        controltext_holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    controltext_holder.append(data["References"][section]["Outcomes"][subsection]["ControlText"])
                else:
                    controltext_holder.append(exclude)
            CONTROLTEXT.append(controltext_holder)
        else:
            for i in range(max(x)):
                controltext_holder.append(exclude)
            CONTROLTEXT.append(controltext_holder)

get_control_text()

control_text_df = pd.DataFrame(CONTROLTEXT)

control_text_df.columns=["Control_Text_Outcome_"+'{}'.format(column+1) for column in control_text_df.columns]

control_text_df.fillna("NA", inplace=True)

control_text_df.to_csv("controltext.csv", index=False)