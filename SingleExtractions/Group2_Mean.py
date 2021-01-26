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

def get_group2mean():
    global GROUP2MEAN
    GROUP2MEAN = []
    for section in range(len(data["References"])):
        group2meanholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    group2meanholder.append(
                        data["References"][section]["Outcomes"][subsection]["Data4"])
                else:
                    group2meanholder.append(exclude)
            GROUP2MEAN.append(group2meanholder)
        else:
            for i in range(max(x)):
                group2meanholder.append(exclude)
            GROUP2MEAN.append(group2meanholder)

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

get_group2mean()

group2mean_df = pd.DataFrame(GROUP2MEAN)

group2mean_df.columns = [
    "out_g2_mean_"+'{}'.format(column+1) for column in group2mean_df.columns]

group2mean_df.fillna("NA", inplace=True)
group2mean_df = group2mean_df.replace(r'^\s*$', "NA", regex=True)

print(group2mean_df)
# get outcometypeId data (to check)
get_outcometypeID()
outcometypeid_df = pd.DataFrame(OUTCOMETYPEID)

outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns=["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group2mean_df.columns:
    group2mean_df[col][mask] = "NA"
print(group2mean_df)

group2mean_df.to_csv("Group2Mean.csv", index=False)