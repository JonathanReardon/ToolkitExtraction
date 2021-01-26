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


def get_outcome_label():
    global OUTCOMETITLE
    OUTCOMETITLE = []
    for section in range(len(data["References"])):
        outcomelabel_holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomelabel_holder.append(
                        data["References"][section]["Outcomes"][subsection]["Title"])
                else:
                    outcomelabel_holder.append(exclude)
            OUTCOMETITLE.append(outcomelabel_holder)
        else:
            for i in range(max(x)):
                outcomelabel_holder.append(exclude)
            OUTCOMETITLE.append(outcomelabel_holder)


get_outcome_label()

outcome_title_df = pd.DataFrame(OUTCOMETITLE)

outcome_title_df.columns = [
    "out_tit_"+'{}'.format(column+1) for column in outcome_title_df.columns]

""" outcome_label_text_df.fillna("NA", inplace=True) """
outcome_title_df = outcome_title_df.replace(r'^\s*$', "NA", regex=True)

print(outcome_title_df)

outcome_title_df.to_csv("out_tit.csv", index=False)
