from Main import get_outcome_lvl1
import pandas as pd

# get group2 mean data
group2mean = get_outcome_lvl1("Data4")
group2mean_df = pd.DataFrame(group2mean)

# name each column (number depends on outcome number)
group2mean_df.columns = [
    "out_g2_mean_"+'{}'.format(column+1) for column in group2mean_df.columns]

# fill blanks with NA
group2mean_df.fillna("NA", inplace=True)

# remove problematic text
group2mean_df = group2mean_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data 
outcomeid = get_outcome_lvl1("OutcomeTypeId")
outcometypeid_df = pd.DataFrame(outcomeid)

# name each column (number depends on outcome number)
outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns=["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group2mean_df.columns:
    group2mean_df[col][mask] = "NA"

# save to disk
group2mean_df.to_csv("Group2Mean.csv", index=False)