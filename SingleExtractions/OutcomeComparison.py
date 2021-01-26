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


def get_control_text():
    global CONTROLTEXT
    CONTROLTEXT = []
    for section in range(len(data["References"])):
        controltext_holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    controltext_holder.append(
                        data["References"][section]["Outcomes"][subsection]["ControlText"])
                else:
                    controltext_holder.append(exclude)
            CONTROLTEXT.append(controltext_holder)
        else:
            for i in range(max(x)):
                controltext_holder.append(exclude)
            CONTROLTEXT.append(controltext_holder)


get_control_text()

out_comp_df = pd.DataFrame(CONTROLTEXT)

out_comp_df.columns = ["out_comp_" +
                       '{}'.format(column+1) for column in out_comp_df.columns]

out_comp_df.fillna("NA", inplace=True)

print(out_comp_df)

out_comp_df.to_csv("out_compe.csv", index=False)
