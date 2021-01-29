from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get outcome data
outcome = get_outcome_lvl1("OutcomeText")
outcome_df = pd.DataFrame(outcome)

# name each column (number depends on outcome number)
outcome_df.columns = [
    "out_label_" +'{}'.format(column+1) for column in outcome_df.columns]

# fill blanks with NA
outcome_df.fillna("NA", inplace=True)

# save to disk
""" outcome_df.to_csv("outcome.csv", index=False) """