from Main import load_json, get_outcome_lvl1
import pandas as pd

load_json()

# get group1 sd data
group1sd = get_outcome_lvl1("Data5")
group1sd_df = pd.DataFrame(group1sd)

# name each column (number depends on outcome number)
group1sd_df.columns = [
    "out_g1_sd_"+'{}'.format(column+1) for column in group1sd_df.columns
]

# fill blanks with NA  
group1sd_df.fillna("NA", inplace=True)

# remove problematic text
group1sd_df = group1sd_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data (to check)
getoucomeid = get_outcome_lvl1("OutcomeTypeId")
outcometypeid_df = pd.DataFrame(getoucomeid)

# name each column (number depends on outcome number)
outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns=["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group1sd_df.columns:
    group1sd_df[col][mask] = "NA"

# save to disk
#group1sd_df.to_csv("Group1SD.csv", index=False)

print(group1sd_df)
