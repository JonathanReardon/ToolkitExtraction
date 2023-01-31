from Main import load_json, get_outcome_lvl1
import pandas as pd

load_json()

# get group2sd data
groupd2sd = get_outcome_lvl1("Data6")
group2sd_df = pd.DataFrame(groupd2sd)

# name each column (number depends on outcome number)
group2sd_df.columns = [
    "out_g2_sd_"+'{}'.format(column+1) for column in group2sd_df.columns
]

# fill blanks with NA  
group2sd_df.fillna("NA", inplace=True)

# remove problematic text
group2sd_df = group2sd_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data (to check)
outcomeid = get_outcome_lvl1("OutcomeTypeId")
outcometypeid_df = pd.DataFrame(outcomeid)

# name each column (number depends on outcome number)
outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns=["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group2sd_df.columns:
    group2sd_df[col][mask] = "NA"

# save to disk
#group2sd_df.to_csv("Group2SD.csv", index=False)

""" print(group2sd_df) """
