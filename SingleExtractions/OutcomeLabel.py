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

def get_outcome_label():
    global OUTCOMELABEL
    OUTCOMELABEL = []
    for section in range(len(data["References"])):
        outcomelabel_holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomelabel_holder.append(data["References"][section]["Outcomes"][subsection]["Title"])
                else:
                    outcomelabel_holder.append(exclude)
            OUTCOMELABEL.append(outcomelabel_holder)
        else:
            for i in range(max(x)):
                outcomelabel_holder.append(exclude)
            OUTCOMELABEL.append(outcomelabel_holder)

get_outcome_label()

outcome_label_text_df = pd.DataFrame(OUTCOMELABEL)

outcome_label_text_df.columns=["Outcome_Label_"+'{}'.format(column+1) for column in outcome_label_text_df.columns]

outcome_label_text_df.fillna("NA", inplace=True)

print(outcome_label_text_df)

outcome_label_text_df.to_csv("outcomelabel_text.csv", index=False)