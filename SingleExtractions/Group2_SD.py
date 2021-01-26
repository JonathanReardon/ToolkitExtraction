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

def get_group2sd():
    global GROUP2SD
    GROUP2SD = []
    for section in range(len(data["References"])):
        group2sdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(x)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    group2sdholder.append(
                        data["References"][section]["Outcomes"][subsection]["Data6"])
                else:
                    group2sdholder.append(exclude)
            GROUP2SD.append(group2sdholder)
        else:
            for i in range(max(x)):
                group2sdholder.append(exclude)
            GROUP2SD.append(group2sdholder)

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

get_group2sd()

group2sd_df = pd.DataFrame(GROUP2SD)

group2sd_df.columns = [
    "out_g2_sd_"+'{}'.format(column+1) for column in group2sd_df.columns]

group2sd_df.fillna("NA", inplace=True)
group2sd_df = group2sd_df.replace(r'^\s*$', "NA", regex=True)

print(group2sd_df)
# get outcometypeId data (to check)
get_outcometypeID()
outcometypeid_df = pd.DataFrame(OUTCOMETYPEID)

outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns=["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group2sd_df.columns:
    group2sd_df[col][mask] = "NA"
print(group2sd_df)

group2sd_df.to_csv("Group2SD.csv", index=False)