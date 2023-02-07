from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get sesmd data
sesmd = get_outcome_lvl1("SESMD")
sesmd_df = pd.DataFrame(sesmd)

# round data to 4 decimal places
sesmd_df = sesmd_df.applymap(
    lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

# name each column (number depends on outcome number)
sesmd_df.columns = [
    "se_"+'{}'.format(column+1) for column in sesmd_df.columns]

# fill blanks with NA
sesmd_df.fillna("NA", inplace=True)

# replace problematic text
sesmd_df = sesmd_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
""" sesmd_df.to_csv("sesmd.csv", index=False) """