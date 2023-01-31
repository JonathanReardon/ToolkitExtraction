from Main import load_json, get_outcome_lvl1
import pandas as pd

load_json()

# get group 1 N data
group2n = get_outcome_lvl1("Data2")
group2N_df = pd.DataFrame(group2n)

# name each column (number depends on outcome number)
group2N_df.columns = [
    "out_g2_n_"+'{}'.format(column+1) for column in group2N_df.columns
]

# fill blanks with NA  
group2N_df.fillna("NA", inplace=True)

# remove problematic text
group2N_df = group2N_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data (to check)
outcomeid = get_outcome_lvl1("OutcomeTypeId")
outcometypeid_df = pd.DataFrame(outcomeid)

# name each column (number depends on outcome number)
outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns = ["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group2N_df.columns:
    group2N_df[col][mask] = "NA"

# save to disk
#group2N_df.to_csv("Group2N.csv", index=False)

""" print(group2N_df) """
