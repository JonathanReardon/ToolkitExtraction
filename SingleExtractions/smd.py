from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get smd data
smd = get_outcome_lvl1("SMD")
smd_df = pd.DataFrame(smd)

# round data to 4 decimal places
smd_df = smd_df.applymap(
    lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

# name each column (number depends on outcome number)
smd_df.columns = [
    "smd_"+'{}'.format(column+1) for column in smd_df.columns]

# fill blanks with NA
smd_df.fillna("NA", inplace=True)

# replace problematic text
smd_df = smd_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
""" smd_df.to_csv("smd.csv", index=False) """