from Main import load_json, get_outcome_lvl1
import pandas as pd

load_json()

# get group1 mean data
group1mean = get_outcome_lvl1("Data3")
group1mean_df = pd.DataFrame(group1mean)

# name each column (number depends on outcome number)
group1mean_df.columns = [
    "out_g1_mean_"+'{}'.format(column+1) for column in group1mean_df.columns
]

# fill blanks with NA   
group1mean_df.fillna("NA", inplace=True)

# remove problematic text
group1mean_df = group1mean_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data (to check)
outcometypeid = get_outcome_lvl1("OutcomeTypeId")
outcometypeid_df = pd.DataFrame(outcometypeid)

# name each column (number depends on outcome number)
outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns=["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group1mean_df.columns:
    group1mean_df[col][mask] = "NA"

# save to disk
#group1mean_df.to_csv("Group1Mean.csv", index=False)

""" print(group1mean_df) """
