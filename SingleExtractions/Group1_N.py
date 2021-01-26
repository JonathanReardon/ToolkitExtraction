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


def get_group1N():
    global GROUP1N
    GROUP1N = []
    for section in range(len(data["References"])):
        group1Nholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    group1Nholder.append(
                        data["References"][section]["Outcomes"][subsection]["Data1"])
                else:
                    group1Nholder.append(exclude)
            GROUP1N.append(group1Nholder)
        else:
            for i in range(max(x)):
                group1Nholder.append(exclude)
            GROUP1N.append(group1Nholder)


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


# get group 1 N data
get_group1N()
group1N_df = pd.DataFrame(GROUP1N)

group1N_df.columns = [
    "out_g1_n_"+'{}'.format(column+1) for column in group1N_df.columns]

group1N_df.fillna("NA", inplace=True)
group1N_df = group1N_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data (to check)
get_outcometypeID()
outcometypeid_df = pd.DataFrame(OUTCOMETYPEID)

outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns = ["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group1N_df.columns:
    group1N_df[col][mask] = "NA"

print(group1N_df.dtypes)

group1N_df.to_csv("Group1N.csv", index=False)
