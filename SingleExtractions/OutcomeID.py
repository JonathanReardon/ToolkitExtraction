from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get outcome ID data
outcome_ID = get_outcome_lvl1("OutcomeId")
outcome_ID_df = pd.DataFrame(outcome_ID)

# name each column (number depends on outcome number)
outcome_ID_df.columns = [
    "Outcome_ID_"+'{}'.format(column+1) for column in outcome_ID_df.columns]

# fill blanks with NA
outcome_ID_df.fillna("NA", inplace=True)

# replace problematic text
outcome_ID_df = outcome_ID_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
""" outcome_ID_df.to_csv("outcomeID.csv", index=False) """