from Main import load_json, get_outcome_lvl1
import pandas as pd

load_json()

# extract confidence interval upper data
cilowersmd = get_outcome_lvl1("CIUpperSMD")
ciuppersmd_df = pd.DataFrame(cilowersmd)

# round data to 4 decimal places
ciuppersmd_df = ciuppersmd_df.applymap(
    lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

# name each column (number depends on outcome number)
ciuppersmd_df.columns = [
    "ci_upper_"+'{}'.format(column+1) for column in ciuppersmd_df.columns]

# fill blanks with NA
ciuppersmd_df.fillna("NA", inplace=True)

# replace problematic text
ciuppersmd_df = ciuppersmd_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
#ciuppersmd_df.to_csv("ciuppersmd.csv", index=False)

""" print(ciuppersmd_df) """