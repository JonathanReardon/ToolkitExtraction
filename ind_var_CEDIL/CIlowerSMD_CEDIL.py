from Main import load_json, get_outcome_lvl1
import pandas as pd

load_json()

# extract confidence interval lower data
cilowersmd = get_outcome_lvl1("CILowerSMD")
cilowersmd_df = pd.DataFrame(cilowersmd)

# round data to 4 decimal places
cilowersmd_df = cilowersmd_df.applymap(
    lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

# name each column (number depends on outcome number)
cilowersmd_df.columns=[
    "ci_lower_"+'{}'.format(column+1) for column in cilowersmd_df.columns]

# fill blanks with NA
cilowersmd_df.fillna("NA", inplace=True)

# replace problematic text
cilowersmd_df = cilowersmd_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
#cilowersmd_df.to_csv("cilowersmd.csv", index=False)

print(cilowersmd_df)