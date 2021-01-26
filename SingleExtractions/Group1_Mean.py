import os
import json
import pandas as pd

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

def get_group1mean():
    global GROUP1MEAN
    GROUP1MEAN = []
    for section in range(len(data["References"])):
        group1meanholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    group1meanholder.append(
                        data["References"][section]["Outcomes"][subsection]["Data3"])
                else:
                    group1meanholder.append(exclude)
            GROUP1MEAN.append(group1meanholder)
        else:
            for i in range(max(x)):
                group1meanholder.append(exclude)
            GROUP1MEAN.append(group1meanholder)

def get_outcometypeID():
    global OUTCOMETYPEID
    OUTCOMETYPEID = []
    for section in range(len(data["References"])):
        outcometypeidholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcometypeidholder.append(
                        data["References"][section]["Outcomes"][subsection]["OutcomeTypeId"])
                else:
                    outcometypeidholder.append(exclude)
            OUTCOMETYPEID.append(outcometypeidholder)
        else:
            for i in range(max(x)):
                outcometypeidholder.append(exclude)
            OUTCOMETYPEID.append(outcometypeidholder)

get_group1mean()

group1mean_df = pd.DataFrame(GROUP1MEAN)

group1mean_df.columns = [
    "out_g1_mean_"+'{}'.format(column+1) for column in group1mean_df.columns]

group1mean_df.fillna("NA", inplace=True)
group1mean_df = group1mean_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data (to check)
get_outcometypeID()
outcometypeid_df = pd.DataFrame(OUTCOMETYPEID)

outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns=["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group1mean_df.columns:
    group1mean_df[col][mask] = "NA"

group1mean_df.to_csv("Group1Mean.csv", index=False)