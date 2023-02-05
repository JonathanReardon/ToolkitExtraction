from Main import load_json, get_outcome_lvl1
import pandas as pd

load_json()

# get group 1 N data
group1n = get_outcome_lvl1("Data1")
group1N_df = pd.DataFrame(group1n)

# name each column (number depends on outcome number)
group1N_df.columns = [
    "out_g1_n_"+'{}'.format(column+1) for column in group1N_df.columns
]

# fill blanks with NA  
group1N_df.fillna("NA", inplace=True)
group1N_df = group1N_df.replace(r'^\s*$', "NA", regex=True)

# get outcometypeId data (to check)
outcometypeid = get_outcome_lvl1("OutcomeTypeId")
outcometypeid_df = pd.DataFrame(outcometypeid)

# name each column (number depends on outcome number)
outcometypeid_df.columns = [
    "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
]

mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
mask.columns = ["mask"]
mask = mask.iloc[:, 0]

# replace all 0 instances (null data) with "NA"
for col in group1N_df.columns:
    group1N_df.loc[mask, col] = "NA"

# save to disk
#group1N_df.to_csv("Group1N.csv", index=False)

""" print(group1N_df) """
